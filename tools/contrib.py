"""Other people's ForeverAPI Probe data: read, check, file and count it.

Developers run `/fapi export` in game and attach the text block to an "API data" issue on zmarotrix/ForeverAPI.
`apidoc.py contrib --github` downloads every open one, checks it, files it under contrib/<build>/gh-<account>.json.gz,
thanks the sender and closes the issue. `apidoc.py contrib <file> --as <name>` does the same for a file on disk.

Checks, before anything is kept:
  - it decodes, and its client build is one we have Blizzard's docs for (sources/client-docs/<build>.json.gz);
  - each module's data has the shape the add-on writes, and stays under sane sizes;
  - every function, event and widget method it names exists in the client's own docs, UI code or our dump of
    that build. Names that don't are dropped and listed in the reply; if more than a few are made up, the
    whole file is turned away.

Trust (used by the build): Maro's own runs are what "verified" means. Data from anyone else is "reported", with
the number of independent GitHub accounts behind it, until Maro's run confirms it or two accounts agree.
"""

import base64
import datetime
import glob
import gzip
import json
import os
import re
import subprocess
import urllib.request
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CONTRIB = os.path.join(ROOT, "contrib")
REPO = "zmarotrix/ForeverAPI"
LABEL = "api-data"
FAPI_RE = re.compile(r"FAPI:(\d+):(\{[^}\n]*\}):([A-Za-z0-9+/=\s]+)")
MODULES = ("probe", "watch", "timeline", "widgets", "checks")
MAX_RAW = 8 * 1024 * 1024            # decompressed bytes
MAX_UNKNOWN = 10                     # made-up names before the whole file is turned away
NAME_OK = re.compile(r"^[A-Za-z_][A-Za-z0-9_.:]{0,120}$")


# ---------------------------------------------------------------------------------------------------------------
# decoding
# ---------------------------------------------------------------------------------------------------------------

def _inflate(data):
    for wbits in (zlib.MAX_WBITS, -zlib.MAX_WBITS, zlib.MAX_WBITS | 16):
        try:
            d = zlib.decompressobj(wbits)
            out = d.decompress(data, MAX_RAW + 1)
            if len(out) > MAX_RAW:
                raise ValueError("too large once unpacked")
            return out
        except zlib.error:
            continue
    raise ValueError("not compressed data")


def _lua_literal(text):
    from luatable import parse_assignments
    return parse_assignments("X = " + text).get("X")


def _cbor(raw):
    import cbor2
    return cbor2.loads(raw)


def decode(text):
    """Yields (header, data) for every FAPI export string in text, and for a pasted ForeverAPIProbe.lua."""
    found = False
    for m in FAPI_RE.finditer(text):
        found = True
        if int(m.group(1)) != 1:
            raise ValueError("export format %s is newer than this tool" % m.group(1))
        header = json.loads(m.group(2))
        body = base64.b64decode(re.sub(r"\s+", "", m.group(3)))
        if header.get("enc") == "cbor":
            data = _cbor(_inflate(body))
        elif header.get("enc") == "lua":
            if len(body) > MAX_RAW:
                raise ValueError("too large")
            data = _lua_literal(body.decode("utf-8", "replace"))
        else:
            raise ValueError("unknown encoding %r" % header.get("enc"))
        yield header, data
    if not found and any(v in text for v in ("ApiWatchDB", "ApiChecksDB", "ApiWidgetsDB", "ApiProbeDB", "ApiTimelineDB")):
        # a SavedVariables file attached as it is
        from luatable import parse_assignments
        sv = parse_assignments(text)
        data, mods = {}, []
        for mod, var in (("watch", "ApiWatchDB"), ("timeline", "ApiTimelineDB"), ("widgets", "ApiWidgetsDB"), ("checks", "ApiChecksDB")):
            if isinstance(sv.get(var), dict) and sv[var].get("build"):
                data[mod] = sv[var]
                mods.append(mod)
        p = sv.get("ApiProbeDB")
        if isinstance(p, dict) and p.get("live"):
            data["probe"] = {"calls": p.get("calls"), "live": p.get("live"), "blocked": p.get("blocked"),
                             "meta": (p.get("dump") or {}).get("meta")}
            mods.append("probe")
        if mods:
            build = next((data[m].get("build") for m in mods if m != "probe"), None) or \
                ((data.get("probe") or {}).get("live") or {}).get("build")
            fp = (sv.get("ForeverAPIProbeDB") or {}).get("contributor")
            yield {"build": build, "enc": "savedvariables", "modules": ",".join(mods), "contributor": fp}, data


# ---------------------------------------------------------------------------------------------------------------
# checking
# ---------------------------------------------------------------------------------------------------------------

class Known:
    """Every name the client's own docs, UI code and our dump of a build know about."""

    def __init__(self, client, framexml, dump, plan_setters):
        import model
        docs = model.documented(client)
        self.functions = set(docs["functions"])
        fx = framexml or {}
        self.functions |= set(fx.get("globals") or {}) | set(fx.get("defined") or {})
        g = (dump or {}).get("globals") or {}
        self.functions |= {k for k, v in g.items() if isinstance(v, str) and v.startswith("f")}
        for ns, members in ((dump or {}).get("tables") or {}).items():
            if isinstance(members, dict):
                self.functions |= {"%s.%s" % (ns, k) for k in members}
        self.events = set(docs["events"]) | set(fx.get("events") or {}) | set(((dump or {}).get("live") or {}).get("events") or {})
        self.events |= set((dump or {}).get("events") or {})
        self.setters = set(plan_setters or [])

    def fn(self, key):
        return key in self.functions

    def event(self, name):
        return name in self.events


def _dict(x):
    if isinstance(x, list):
        return {i + 1: v for i, v in enumerate(x)}
    return x if isinstance(x, dict) else None


def check(header, data, known_for_build):
    """(clean data, problems, dropped names). problems non-empty means the file is turned away."""
    problems, dropped = [], []
    build = str(header.get("build") or "")
    known = known_for_build(build)
    if known is None:
        return None, ["it's from client build %s, which this reference doesn't cover yet" % (build or "unknown")], []
    data = _dict(data)
    if not data or not any(m in data for m in MODULES):
        return None, ["it holds no ForeverAPI Probe data"], []
    clean = {}

    def name_ok(kind, name):
        ok = isinstance(name, str) and NAME_OK.match(name) and (known.fn(name) if kind == "fn" else known.event(name))
        if not ok:
            dropped.append("%s %s" % ("function" if kind == "fn" else "event", str(name)[:60]))
        return ok

    w = _dict(data.get("watch"))
    if w is not None:
        if str(w.get("build")) != build:
            problems.append("its watch data is from a different build")
        sits = {}
        for sit, s in (_dict(w.get("situations")) or {}).items():
            if not isinstance(sit, str) or not re.match(r"^[a-z]+/(idle|combat|boss)$", sit):
                problems.append("a situation name the add-on never writes (%s)" % str(sit)[:40])
                continue
            runs = {}
            for label, run in (_dict((_dict(s) or {}).get("runs")) or {}).items():
                run = _dict(run) or {}
                res = {k: r for k, r in (_dict(run.get("results")) or {}).items() if name_ok("fn", k)}
                if res:
                    runs[str(label)[:60]] = dict(run, results=res)
            if runs:
                sits[sit] = {"runs": runs}
        clean["watch"] = dict(w, situations=sits)

    p = _dict(data.get("probe"))
    if p is not None:
        live = _dict(p.get("live")) or {}
        evs = {k: v for k, v in (_dict(live.get("events")) or {}).items() if name_ok("event", k)}
        calls = {}
        for phase, c in (_dict(p.get("calls")) or {}).items():
            if phase in ("outside", "combat"):
                c = _dict(c) or {}
                calls[phase] = dict(c, results={k: r for k, r in (_dict(c.get("results")) or {}).items() if name_ok("fn", k)})
        clean["probe"] = {"live": dict(live, events=evs), "calls": calls, "meta": p.get("meta")}

    wd = _dict(data.get("widgets"))
    if wd is not None:
        runs = {}
        for phase, run in (_dict(wd.get("runs")) or {}).items():
            run = _dict(run) or {}
            st = {}
            for k, r in (_dict(run.get("setters")) or {}).items():
                if k in known.setters:
                    st[k] = r
                else:
                    dropped.append("widget method %s" % str(k)[:60])
            runs[phase] = dict(run, setters=st)
        clean["widgets"] = dict(wd, runs=runs)

    for mod in ("timeline", "checks"):
        if _dict(data.get(mod)) is not None:
            clean[mod] = data[mod]
            if mod == "timeline":
                for traces in (_dict(data[mod].get("traces")) or {}).values():
                    for trace in (_dict(traces) or {}).values():
                        for e in (_dict((_dict(trace) or {}).get("events")) or {}).values():
                            e = _dict(e) or {}
                            if e.get(2) is not None and not known.event(e.get(2)):
                                dropped.append("event %s" % str(e.get(2))[:60])

    if len(set(dropped)) > MAX_UNKNOWN:
        problems.append("it names %d functions or events this client doesn't have" % len(set(dropped)))
    return clean, problems, sorted(set(dropped))


# ---------------------------------------------------------------------------------------------------------------
# storing
# ---------------------------------------------------------------------------------------------------------------

def person(login):
    return "gh-" + re.sub(r"[^A-Za-z0-9_-]", "", login or "unknown")[:39]


def _plain(v):
    """Lua tables mix number and string keys: make every key a string so it stores as JSON."""
    if isinstance(v, dict):
        return {str(k): _plain(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_plain(x) for x in v]
    return v


def store(header, data, who, origin, contrib=CONTRIB):
    """contrib/<build>/<who>.json.gz; a newer file from the same person replaces the older one."""
    build = str(header.get("build"))
    out = os.path.join(contrib, build, who + ".json.gz")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rec = {"who": who, "origin": origin, "received": datetime.datetime.now().isoformat(timespec="seconds"),
           "header": _plain(header), "data": _plain(data)}
    with gzip.open(out, "wt", encoding="utf-8") as f:
        json.dump(rec, f, sort_keys=True, default=str)
    return out


def stored(build=None, contrib=CONTRIB):
    """[record] for every filed submission (of one build, or all)."""
    out = []
    for path in sorted(glob.glob(os.path.join(contrib, build or "*", "*.json.gz"))):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            out.append(json.load(f))
    return out


# ---------------------------------------------------------------------------------------------------------------
# GitHub
# ---------------------------------------------------------------------------------------------------------------

def gh(*args):
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True, encoding="utf-8").stdout


def open_issues():
    issues = json.loads(gh("issue", "list", "-R", REPO, "--state", "open", "--label", LABEL, "--limit", "200",
                           "--json", "number,author,body,title"))
    for issue in issues:
        body = issue.get("body") or ""
        texts = [body]
        for url in re.findall(r"https://github\.com/user-attachments/files/\d+/[^\s)\]]+", body):
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    texts.append(r.read(MAX_RAW).decode("utf-8", "replace"))
            except Exception as exc:  # one dead link must not stop the rest
                print("  #%d: cannot download %s (%s)" % (issue["number"], url, exc))
        yield issue, "\n".join(texts)


def reply(number, text, close, dry_run, reason=None):
    if dry_run:
        print("  #%s: would %s: %s" % (number, "close" if close else "comment", text[:160]))
        return
    gh("issue", "comment", str(number), "-R", REPO, "--body", text)
    if close:
        args = ["issue", "close", str(number), "-R", REPO]
        if reason:
            args += ["--reason", reason]
        gh(*args)


def thanks(build, mods, dropped):
    t = ("Thank you! Your ForeverAPI Probe data for client %s is in (%s). It shows on the reference as "
         "\"reported\" until Maro's own run or a second contributor confirms it. Export again any time: a newer "
         "file from you replaces this one, so nothing counts twice." % (build, ", ".join(mods)))
    if dropped:
        t += ("\n\nA few names in it don't exist in this client's docs, UI code or our dump, so they were left out: "
              + ", ".join("`%s`" % d for d in dropped[:20]) + (" and more" if len(dropped) > 20 else "") + ".")
    return t


def run(texts, known_for_build, dry_run=False, contrib=CONTRIB):
    """texts: [(who, origin, text, issue number or None)]. Returns how many files were stored."""
    n = 0
    for who, origin, text, number in texts:
        got, problems_all, saved = False, [], []
        try:
            items = list(decode(text))
        except Exception as exc:
            items, problems_all = [], ["the export couldn't be read (%s)" % exc]
        for header, data in items:
            got = True
            clean, problems, dropped = check(header, data, known_for_build)
            if problems:
                problems_all += problems
                print("  %s: turned away: %s" % (origin, "; ".join(problems)))
                continue
            if not dry_run:
                store(header, clean, who, origin, contrib)
            saved.append((header, clean, dropped))
            n += 1
            print("  %s: stored %s for %s (%s)%s" % (origin, ", ".join(clean), header.get("build"), who,
                                                    ", dropped %d unknown names" % len(dropped) if dropped else ""))
        if number is None:
            continue
        if saved:
            header, clean, dropped = saved[-1]
            reply(number, thanks(header.get("build"), list(clean), dropped), True, dry_run)
        elif got or problems_all:
            reply(number, "Thanks for sharing! This export couldn't be used, because " + "; and ".join(problems_all)
                  + ". If you think that's wrong, reply here and Maro will look.", True, dry_run, "not planned")
        else:
            reply(number, "Thanks! There's no export in this post yet. In game, type `/fapi export`, copy the box "
                  "(Ctrl+C), and paste it in a comment here (or save it as a .txt file and drag that in).", False, dry_run)
    return n


# ---------------------------------------------------------------------------------------------------------------
# trust
# ---------------------------------------------------------------------------------------------------------------

def _sig(rec):
    """What a call result says, for comparing two reports (types and secrets, not counts)."""
    rec = rec or {}
    return json.dumps({k: rec.get(k) for k in ("returns", "error", "forbidden", "missing")}, sort_keys=True, default=str)


def merge_watch(maro_dbs, reports):
    """One watch table. maro_dbs: Maro's own imports; reports: [(who, watch db)] from everyone else.

    Maro's runs are taken as they are (by = "maro"). A run only others reported gets, per function, the result
    most of them agree on and "rep": how many independent accounts gave exactly that result; by = "reported".
    """
    merged = None
    for db in maro_dbs:
        if merged is None:
            merged = dict(db, situations={}, transitions=[], sources=0, reporters=[])
        merged["sources"] += 1
        for sit, s in (db.get("situations") or {}).items():
            target = merged["situations"].setdefault(sit, {"runs": {}})
            for label, run in (s.get("runs") or {}).items():
                have = target["runs"].get(label)
                if have is None or (run.get("done") and not have.get("done")):
                    target["runs"][label] = dict(run, by="maro")
        merged["transitions"] += list(db.get("transitions") or [])
    pool = {}
    for who, db in reports:
        if merged is None:
            merged = dict(db, situations={}, transitions=[], sources=0, reporters=[])
        if who not in merged["reporters"]:
            merged["reporters"].append(who)
        for sit, s in (db.get("situations") or {}).items():
            for label, run in (s.get("runs") or {}).items():
                if label in ((merged["situations"].get(sit) or {}).get("runs") or {}):
                    continue  # Maro has this one
                for key, rec in (run.get("results") or {}).items():
                    pool.setdefault((sit, label), {}).setdefault(key, {}).setdefault(_sig(rec), {})[who] = rec
    for (sit, label), fns in pool.items():
        results = {}
        for key, by_sig in fns.items():
            sig, whos = max(by_sig.items(), key=lambda kv: len(kv[1]))
            results[key] = dict(next(iter(whos.values())), rep=len(whos))
        merged["situations"].setdefault(sit, {"runs": {}})["runs"][label] = {"results": results, "by": "reported", "done": True}
    if merged:
        merged["transitions"] = sorted(merged["transitions"], key=lambda t: t.get("at") or 0)[-2000:]
    return merged


def reported_events(reports, maro_live):
    """{event: number of accounts that saw it fire} for events Maro's own live counter hasn't seen."""
    out = {}
    for who, live in reports:
        for name in (live.get("events") or {}):
            if name not in (maro_live or {}):
                out.setdefault(name, set()).add(who)
    return {k: len(v) for k, v in out.items()}


def merge_widgets(maro, reports):
    """Maro's widget runs, plus setters only others tested (each with "rep")."""
    runs = {k: dict(v) for k, v in ((maro or {}).get("runs") or {}).items()}
    for phase in ("outside", "combat"):
        have = (runs.get(phase) or {}).get("setters") or {}
        pool = {}
        for who, db in reports:
            for k, r in ((((db.get("runs") or {}).get(phase)) or {}).get("setters") or {}).items():
                if k not in have:
                    pool.setdefault(k, {}).setdefault(json.dumps(r, sort_keys=True), set()).add(who)
        if pool:
            run = runs.setdefault(phase, {"setters": {}, "ops": {}, "by": "reported"})
            st = dict(run.get("setters") or {})
            for k, sigs in pool.items():
                sig, whos = max(sigs.items(), key=lambda kv: len(kv[1]))
                st[k] = dict(json.loads(sig), rep=len(whos))
            run["setters"] = st
    out = dict(maro or {}, runs=runs)
    return out if runs else maro


def trusted(rep):
    """A report is as good as verified once two independent accounts agree."""
    return (rep or 0) >= 2
