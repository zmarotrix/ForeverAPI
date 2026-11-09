"""ForeverAPI: document the WoW Forever add-on API from what the game itself confirms.

    python tools/apidoc.py extract     read Blizzard's docs and UI code out of the client, write leads.lua for the probe
    python tools/apidoc.py deploy      copy addon/ForeverAPIProbe into the game's AddOns folder
    python tools/apidoc.py import      read the probe's SavedVariables into dumps/<build>/<time>.json
    python tools/apidoc.py build       merge client docs + latest dump + web leads into docs/ and the website site/
    python tools/apidoc.py diff A B    compare two dumps (or two client-doc extracts), write docs/changes/
    python tools/apidoc.py release     zip the add-on and the VS Code definitions into dist/
    python tools/apidoc.py release --publish [--yes]   post them as GitHub release v<TOC version> (dry run without --yes)
    python tools/apidoc.py status [--json]             repo, site, release, open submissions (for Norgannon Desk)
    (--json on status, contrib and release --publish: the log goes to stderr, one JSON object to stdout)
    python tools/apidoc.py contrib --github [--dry-run]   file other people's /fapi export submissions
    python tools/apidoc.py contrib <file> --as <name>     file one from a file on disk
    python tools/apidoc.py classic-scan [folders]   list the globals classic add-ons call (for the relocated-API table)
    python tools/apidoc.py luals       same as build (build also writes the VS Code definitions in luals/)
    python tools/apidoc.py all         extract, import (if there's a dump), build

Nothing here downloads anything. Web leads are files you add under sources/web/ (format in README.md).
"""

import datetime
import glob
import gzip
import json
import os
import re
import shutil
import subprocess
import sys

NL = chr(10)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import clientdocs  # noqa: E402
import diff as differ  # noqa: E402
import model  # noqa: E402
import render  # noqa: E402
import website  # noqa: E402
import relocated  # noqa: E402
import luals  # noqa: E402
import checkspage  # noqa: E402
import contrib  # noqa: E402

from luatable import parse_assignments  # noqa: E402

ROOT = os.path.dirname(HERE)
# the game folder (override with the FOREVER_GAME environment variable)
GAME = os.environ.get("FOREVER_GAME", r"G:\Games\World of Warcraft\_forever_")
ADDON = "ForeverAPIProbe"
ADDON_SRC = os.path.join(ROOT, "addon", ADDON)
ADDON_DST = os.path.join(GAME, "Interface", "AddOns", ADDON)
# the five add-ons it replaced: deploy removes them from the game so nothing runs twice
OLD_ADDONS = ["ApiProbe", "ApiWatch", "ApiTimeline", "ApiWidgets", "ApiChecks"]
CLIENT_DIR = os.path.join(ROOT, "sources", "client-docs")
WEB_DIR = os.path.join(ROOT, "sources", "web")
DUMPS = os.path.join(ROOT, "dumps")
DOCS = os.path.join(ROOT, "docs")
SITE = os.path.join(ROOT, "site")
LUALS = os.path.join(ROOT, "luals")


def _rel(p):
    try:
        return os.path.relpath(p, ROOT)
    except ValueError:
        return p


def _save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "wt", encoding="utf-8") as f:
        json.dump(data, f, sort_keys=True, default=str)


def _load_json(path):
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def normalize(v):
    """SavedVariables tables -> JSON-safe: pure arrays become lists, other keys become strings."""
    if isinstance(v, dict):
        if v and all(isinstance(k, int) for k in v):
            return [normalize(v[k]) for k in sorted(v)]
        return {str(k): normalize(x) for k, x in v.items()}
    if isinstance(v, list):
        return [normalize(x) for x in v]
    return v


def _call_record(rec):
    """{n=2, [1]="number", [2]="secret:string", from=...} -> {"n": 2, "returns": [...], ...}"""
    if not isinstance(rec, dict):
        return rec
    out = {str(k): v for k, v in rec.items() if not isinstance(k, int)}
    if "n" in rec:
        out["returns"] = [rec.get(i + 1, "nil") for i in range(min(int(rec["n"]), 30))]
    return out


def _lua_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def cmd_extract():
    client = clientdocs.extract()
    leads = clientdocs.framexml_leads()
    version = client["version"]
    _save_json(os.path.join(CLIENT_DIR, version + ".json.gz"), client)
    _save_json(os.path.join(CLIENT_DIR, version + ".framexml.json.gz"), leads)
    _save_json(os.path.join(CLIENT_DIR, version + ".deprecated.json.gz"), clientdocs.deprecations())
    docs = model.documented(client)
    web_events = set()
    for w in _web():
        web_events.update(w.get("events", []))
    events = sorted(set(docs["events"]) | set(leads["events"]) | web_events)
    plan = model.call_plan(docs)
    documented = sorted(k for k, f in docs["functions"].items() if not f["namespace"])
    lines = ["-- Generated by tools/apidoc.py extract from client %s. Do not edit." % version,
             "-- Candidate names for the probe to check; nothing here is trusted until the game confirms it.",
             "ApiProbeLeads = {", "  build = %s," % _lua_str(version), "  events = {"]
    lines += ["    %s," % _lua_str(e) for e in events]
    lines += ["  },", "  calls = {"]
    for ns, name, arg in plan:
        if isinstance(arg, list):
            extra = ", { %s }" % ", ".join(_lua_str(x) for x in arg)
        else:
            extra = ", \"unit\"" if arg else ""
        lines.append("    { %s, %s%s }," % (_lua_str(ns) if ns else "nil", _lua_str(name), extra))
    lines += ["  },", "  documented = {"]
    lines += ["    [%s] = true," % _lua_str(n) for n in documented]
    lines += ["  },", "  -- calls that crashed the client (sources/crashers.json, from the game's crash logs): never called again",
              "  crashers = {"]
    lines += ["    [%s] = true," % _lua_str(k) for k in sorted(cmd_crashes())]
    # for API watch: calls the probe saw refused (each one costs a popup), and undocumented built-in getters
    dump_path = latest_dump()
    dump = _load_json(dump_path) if dump_path else {}
    refused = sorted({b.get("during") for b in dump.get("blocked") or [] if b.get("during")})
    undocumented = sorted(n for n, c in (dump.get("globals") or {}).items()
                          if c in ("fC", "f?") and model.GETTER.match(n) and not model.NEVER.search(n)
                          and n not in docs["functions"] and n not in leads.get("defined", {}))
    lines += ["  },", "  -- calls the probe saw refused (ADDON_ACTION_FORBIDDEN / BLOCKED): API watch never makes them",
              "  refused = {"]
    lines += ["    [%s] = true," % _lua_str(k) for k in refused]
    lines += ["  },", "  -- built-in getters the game has and Blizzard's docs don't (from the latest dump)", "  undocumented = {"]
    lines += ["    %s," % _lua_str(n) for n in undocumented]
    lines += ["  },", "  -- getter-named globals Blizzard's own Lua UI code defines: UI helpers, not client API, so not called",
              "  uiGetters = {"]
    lines += ["    [%s] = true," % _lua_str(n) for n in sorted(leads.get("defined", {})) if model.GETTER.match(n)]
    lines += ["  },", "}", ""]
    with open(os.path.join(ADDON_SRC, "leads.lua"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    # API watch calls the same getters in other situations, so it gets the same leads
    write_widget_plan(docs, version)
    print("client %s: %d systems, %d documented functions, %d candidate events (%d from UI code only), %d getters to call"
          % (version, len(client["systems"]), len(docs["functions"]), len(events),
             len(set(leads["events"]) - set(docs["events"])), len(plan)))
    return client


CRASHERS = os.path.join(ROOT, "sources", "crashers.json")
_CRASH_KEY = re.compile(r'callKey\s*=\s*"([^"]+)"')


def cmd_crashes():
    """Read the client's crash logs; any crash inside ApiProbe's call loop names its call in the local `callKey`.
    Those names go to sources/crashers.json, and extract puts them in leads.lua so the probe never calls them again."""
    known = _load_json(CRASHERS) if os.path.exists(CRASHERS) else {}
    for path in sorted(glob.glob(os.path.join(GAME, "Errors", "*.txt"))):
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
        if not any("%s/" % name in text for name in COLLECTORS):
            continue
        for key in _CRASH_KEY.findall(text):
            if key not in known:
                known[key] = {"log": os.path.basename(path)}
                print("crasher:", key, "from", os.path.basename(path))
    with open(CRASHERS, "w", encoding="utf-8") as f:
        json.dump(known, f, indent=1, sort_keys=True)
    return known


def write_widget_plan(docs, version):
    """ApiWidgets/plan.lua: the setters to try a secret on, from Blizzard's docs and the widgets the probe created.
    Setters named in a crash log ("Texture:SetWidth") are left out."""
    dump_path = latest_dump()
    widgets = _load_json(dump_path).get("widgets") if dump_path else None
    crashers = _load_json(CRASHERS) if os.path.exists(CRASHERS) else {}
    plan = [p for p in model.widget_plan(docs, widgets) if "%s:%s" % (p[0], p[1]) not in crashers]
    lines = ["-- Generated by tools/apidoc.py extract from client %s and the latest dump. Do not edit." % version,
             "ApiWidgetsPlan = {", "  build = %s," % _lua_str(version), "  setters = {"]
    for wtype, name, kinds, protected in plan:
        lines.append("    { %s, %s, { %s }%s }," % (_lua_str(wtype), _lua_str(name), ", ".join(_lua_str(k) for k in kinds),
                                                  ', "protected"' if protected else ""))
    lines += ["  },", "}", ""]
    with open(os.path.join(ADDON_SRC, "plan.lua"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    print("widget setters to test with a secret: %d" % len(plan))


COLLECTORS = [ADDON]


def cmd_deploy():
    for name in OLD_ADDONS:
        old = os.path.join(GAME, "Interface", "AddOns", name)
        if os.path.isdir(old):
            shutil.rmtree(old)
            print("removed the old", old)
    for name in COLLECTORS:
        src = os.path.join(ROOT, "addon", name)
        if not os.path.isdir(src):
            continue
        dst = os.path.join(GAME, "Interface", "AddOns", name)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print("deployed", dst)


def _sv_files(old="ApiProbe"):
    """SavedVariables files that may hold a module's data: ForeverAPIProbe.lua, or the old separate add-on's file."""
    out = []
    for name in (ADDON, old):
        out += glob.glob(os.path.join(GAME, "WTF", "Account", "*", "SavedVariables", name + ".lua"))
    return out


def _newest_with(var, old):
    """(path, table) of the newest SavedVariables file holding `var`, or (None, None)."""
    for path in sorted(_sv_files(old), key=os.path.getmtime, reverse=True):
        with open(path, encoding="utf-8", errors="replace") as f:
            db = parse_assignments(f.read()).get(var)
        if db:
            return path, db
    return None, None


def cmd_import(path=None):
    if not path:
        import_collectors()
    if path:
        with open(path, encoding="utf-8", errors="replace") as f:
            db = parse_assignments(f.read()).get("ApiProbeDB") or {}
        files = [path]
    else:
        found, db = _newest_with("ApiProbeDB", "ApiProbe")
        if not found:
            print("no probe data yet: switch the probe module on in game (/fapi on probe), then /reload or log out")
            return None
        files = [found]
    dump = db.get("dump")
    if not dump:
        print("the SavedVariables have no dump yet (%s)" % files[0])
        return None
    calls = db.get("calls") or {}
    for phase in calls.values():
        if isinstance(phase, dict) and isinstance(phase.get("results"), dict):
            phase["results"] = {k: _call_record(r) for k, r in phase["results"].items()}
    dump = normalize(dict(dump, calls=calls, live=db.get("live") or {}, blocked=db.get("blocked") or []))
    key = dump["meta"].get("key", "unknown")
    stamp = datetime.datetime.fromtimestamp(os.path.getmtime(files[0])).strftime("%Y%m%d-%H%M%S")
    out = os.path.join(DUMPS, key, stamp + ".json.gz")
    _save_json(out, dump)
    print("imported %s -> %s (%d globals)" % (files[0], _rel(out), len(dump.get("globals", {}))))
    return out


def _others(path):
    """True for a dump made from someone else's data (Collector players, GitHub submissions)."""
    b = os.path.basename(path)
    return "_player-" in b or "_gh-" in b


def latest_dump(prefix=None):
    """Newest ApiProbe dump, or with a prefix ("watch", "timeline", "widgets") the newest collector import."""
    files = glob.glob(os.path.join(DUMPS, "*", "*.json.gz"))
    if prefix:
        files = [f for f in files if os.path.basename(f).startswith(prefix + "_") and not _others(f)]
    else:
        files = [f for f in files if os.path.basename(f)[:1].isdigit()]
    files.sort(key=os.path.getmtime)
    return files[-1] if files else None


# collector add-on -> (SavedVariables global, import prefix)
COLLECTOR_SV = {"ApiWatch": ("ApiWatchDB", "watch"), "ApiTimeline": ("ApiTimelineDB", "timeline"),
                "ApiWidgets": ("ApiWidgetsDB", "widgets"), "ApiChecks": ("ApiChecksDB", "checks")}


CONTRIB_DIR = os.path.join(ROOT, "contrib")
# players' API watch data, passed on by the Norgannon Collector's import (one file per player, ApiWatchDB format)
CONTRIB_WATCH = os.path.join(ROOT, "contrib", "watch")


def _watch_results(db):
    for sit in (db.get("situations") or {}).values():
        for run in (sit.get("runs") or {}).values():
            run["results"] = {k: _call_record(r) for k, r in (run.get("results") or {}).items()}


def import_contrib():
    """contrib/watch/<player>.lua -> dumps/<build>/watch_player-<player>.json.gz, replaced when the file changes."""
    for path in sorted(glob.glob(os.path.join(CONTRIB_WATCH, "*.lua"))):
        with open(path, encoding="utf-8", errors="replace") as f:
            db = parse_assignments(f.read()).get("ApiWatchDB") or {}
        if not db.get("build") or not db.get("situations"):
            continue
        _watch_results(db)
        name = os.path.splitext(os.path.basename(path))[0]
        out = os.path.join(DUMPS, db["build"], "watch_player-%s.json.gz" % name)
        if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(path):
            continue
        _save_json(out, normalize(db))
        print("imported player watch %s -> %s" % (name, _rel(out)))


def merged_watch():
    """Every watch dump of the newest watch build as one. Maro's own runs are verified; runs only other people
    sent (Collector players, GitHub submissions) come in as reported, with how many accounts agree."""
    newest = latest_dump("watch")
    if not newest:
        return None
    build_dir = os.path.dirname(newest)
    build = os.path.basename(build_dir)
    files = sorted(glob.glob(os.path.join(build_dir, "watch_*.json.gz")), key=os.path.getmtime)
    maro = [_load_json(p) for p in files if not _others(p)]
    reports = [(os.path.basename(p).split("_", 1)[1].split(".json")[0], _load_json(p)) for p in files if _others(p)]
    for rec in contrib.stored(build, CONTRIB_DIR):
        if (rec.get("data") or {}).get("watch"):
            reports.append((rec["who"], prepare_collector("watch", rec["data"]["watch"])))
    return contrib.merge_watch(maro, reports)


def _reports(build, module):
    """[(who, data)] for one module from every filed GitHub submission of a build."""
    return [(rec["who"], rec["data"][module]) for rec in contrib.stored(build, CONTRIB_DIR)
            if isinstance((rec.get("data") or {}).get(module), dict)]


def prepare_collector(prefix, db):
    """A module's saved table in the shape the build reads (lists for timeline events, call records for watch)."""
    if prefix == "timeline":
        # each event is { ms, name, kinds, unit, trigger = true }: keep it as a plain list
        for traces in (db.get("traces") or {}).values():
            for trace in (traces.values() if isinstance(traces, dict) else traces):
                evs = trace.get("events") or {}
                evs = [evs[k] for k in sorted(evs)] if isinstance(evs, dict) else evs
                trace["events"] = [[e.get(1), e.get(2), e.get(3), e.get(4), bool(e.get("trigger"))] if isinstance(e, dict)
                                   else list(e) + [None] * (4 - len(e)) + [False] for e in evs]
    if prefix == "watch":
        _watch_results(db)
    return normalize(db)


def import_collectors():
    """Each module's SavedVariables -> dumps/<build>/<prefix>_<time>.json.gz (when it has data)."""
    import_contrib()
    for old, (var, prefix) in COLLECTOR_SV.items():
        path, db = _newest_with(var, old)
        if not path or not db.get("build"):
            continue
        stamp = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y%m%d-%H%M%S")
        out = os.path.join(DUMPS, db["build"], "%s_%s.json.gz" % (prefix, stamp))
        _save_json(out, prepare_collector(prefix, db))
        print("imported %s -> %s" % (prefix, _rel(out)))


def latest_client(version=None):
    if version:
        p = os.path.join(CLIENT_DIR, version + ".json.gz")
        return p if os.path.exists(p) else None
    files = sorted((p for p in glob.glob(os.path.join(CLIENT_DIR, "*.json.gz")) if ".framexml." not in p and ".deprecated." not in p),
                   key=os.path.getmtime)
    return files[-1] if files else None


def _web():
    out = []
    for p in sorted(glob.glob(os.path.join(WEB_DIR, "*.json"))):
        out.append(_load_json(p))
    return out


def cmd_build():
    dump_path = latest_dump()
    dump = _load_json(dump_path) if dump_path else None
    version = (dump or {}).get("meta", {}).get("version")
    client_path = None
    if dump:
        # the docs extract for the build the dump came from, when we have it
        client_path = latest_client("%s.%s" % (version, dump["meta"].get("build")))
    client_path = client_path or latest_client()
    if not client_path:
        client_path = None
        client = cmd_extract()
    else:
        client = _load_json(client_path)
    fx_path = os.path.join(CLIENT_DIR, client["version"] + ".framexml.json.gz")
    framexml = _load_json(fx_path) if os.path.exists(fx_path) else None
    web = {}
    for w in _web():
        for key, item in (w.get("items") or {}).items():
            web[key] = dict(item, site=w.get("site"), url=item.get("url") or w.get("url"))
    m = model.build(client, dump, web, framexml)
    for prefix, field in (("timeline", "timeline"), ("widgets", "secret_tests"), ("checks", "checks")):
        p = latest_dump(prefix)
        m[field] = _load_json(p) if p else None
    build_key = (m.get("meta") or {}).get("key") or client["version"]
    if m.get("secret_tests") is not None or _reports(build_key, "widgets"):
        m["secret_tests"] = contrib.merge_widgets(m.get("secret_tests"), _reports(build_key, "widgets"))
    live_reports = [(who, (p or {}).get("live") or {}) for who, p in _reports(build_key, "probe")]
    m["reported_events"] = contrib.reported_events(live_reports, ((dump or {}).get("live") or {}).get("events") or {})
    for name, n in m["reported_events"].items():
        e = m["events"].get(name)
        if e is None:
            m["events"][name] = {"key": name, "status": "reported", "source": "contributors", "reported": n}
        elif e.get("status") not in ("verified", "undocumented") or not e.get("live"):
            e["reported"] = n
    m["contributors"] = sorted({rec["who"] for rec in contrib.stored(build_key, CONTRIB_DIR)})
    m["watch"] = merged_watch()   # yours and every player's who shares through the Collector
    dep_path = os.path.join(CLIENT_DIR, client["version"] + ".deprecated.json.gz")
    dep = _load_json(dep_path) if os.path.exists(dep_path) else {}
    usage = relocated.load(os.path.join(ROOT, "sources", "classic-usage.json"))
    m["relocated"] = relocated.build(m, dep, usage, relocated.load(os.path.join(ROOT, "sources", "relocated.json")))
    covered = {r["old"] for r in m["relocated"]}
    m["relocated_unmapped"] = [u for u in relocated.missing_unmapped(m, usage) if u[0] not in covered]
    m["meta"]["project_id"] = (m.get("globals") or {}).get("WOW_PROJECT_ID", "n:?")[2:]
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    render.render(m, DOCS, stamp)
    relocated.render_md(m["relocated"], m["relocated_unmapped"], m["meta"], os.path.join(DOCS, "relocated.md"))
    with open(os.path.join(DOCS, "compat.json"), "w", encoding="utf-8", newline=NL) as f:
        json.dump(relocated.compat_json(m["relocated"], m["meta"].get("key")), f, indent=1, sort_keys=True)
    checkspage.render_md(m.get("checks"), os.path.join(DOCS, "checks.md"))
    n = luals.write(m, LUALS)
    print("VS Code definitions: %d files in luals/library" % n)
    page = website.write(m, SITE, stamp)
    print("website: %s" % page)
    print("docs written to %s (client %s, dump %s)" % (_rel(DOCS), client["version"],
                                                       _rel(dump_path) if dump_path else "none"))


DEFAULT_CLASSIC = [r"G:\Projects\pfQuest\Questie", r"G:\Projects\pfQuest\AlexAtlasLoot"]


def cmd_classic_scan(folders):
    """Which globals classic add-ons call: sources/classic-usage.json, for the relocated-API table."""
    folders = folders or [f for f in DEFAULT_CLASSIC if os.path.isdir(f)]
    usage = relocated.scan(folders)
    out = os.path.join(ROOT, "sources", "classic-usage.json")
    with open(out, "w", encoding="utf-8", newline=NL) as f:
        json.dump({k: usage[k] for k in sorted(usage)}, f, indent=0, sort_keys=True)
    print("scanned %d add-on folders: %d global calls -> %s" % (len(folders), len(usage), _rel(out)))


def known_for_build(build):
    """contrib.Known for a client build we have Blizzard's docs for, else None."""
    cp = os.path.join(CLIENT_DIR, build + ".json.gz")
    if not os.path.exists(cp):
        return None
    fx = os.path.join(CLIENT_DIR, build + ".framexml.json.gz")
    dumps = sorted((p for p in glob.glob(os.path.join(DUMPS, build, "*.json.gz")) if os.path.basename(p)[:1].isdigit()),
                   key=os.path.getmtime)
    plan_setters = []
    plan = os.path.join(ADDON_SRC, "plan.lua")
    if os.path.exists(plan):
        with open(plan, encoding="utf-8") as f:
            p = parse_assignments(f.read()).get("ApiWidgetsPlan") or {}
        sets = p.get("setters") or {}
        for e in (sets.values() if isinstance(sets, dict) else sets):
            e = list(e.values()) if isinstance(e, dict) else e
            plan_setters.append("%s:%s" % (e[0], e[1]))
    return contrib.Known(_load_json(cp), _load_json(fx) if os.path.exists(fx) else None,
                         _load_json(dumps[-1]) if dumps else None, plan_setters)


def cmd_contrib(argv):
    """contrib --github [--dry-run]: file open "API data" issues. contrib <file> --as <name>: file a file."""
    dry = "--dry-run" in argv
    cache = {}

    def known(build):
        if build not in cache:
            cache[build] = known_for_build(build)
        return cache[build]
    texts = []
    if "--github" in argv:
        for issue, text in contrib.open_issues():
            login = (issue.get("author") or {}).get("login")
            texts.append((contrib.person(login), "#%d" % issue["number"], text, issue["number"]))
        print("%d open API data issue(s) on %s" % (len(texts), contrib.REPO))
    else:
        files = [a for a in argv if not a.startswith("--") and a != (argv[argv.index("--as") + 1] if "--as" in argv else None)]
        who = argv[argv.index("--as") + 1] if "--as" in argv else None
        if not files or not who:
            print("usage: apidoc.py contrib --github [--dry-run]  |  apidoc.py contrib <file> --as <name>")
            return 0
        for path in files:
            with open(path, encoding="utf-8", errors="replace") as f:
                texts.append(("local-" + re.sub(r"[^A-Za-z0-9_-]", "", who), path, f.read(), None))
    report = []
    n = contrib.run(texts, known, dry, CONTRIB_DIR, report)
    print("%d submission(s) filed under contrib/%s" % (n, " (dry run: nothing written)" if dry else ""))
    if "--json" in argv:
        _json_out({"dry_run": dry, "filed": n, "submissions": report})
    return n


def _json_out(obj):
    """--json: the machine-readable answer goes to the real stdout (the human log went to stderr)."""
    sys.__stdout__.write(json.dumps(obj, indent=1, default=str) + NL)
    sys.__stdout__.flush()


def _gh_json(*args):
    try:
        out = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8", timeout=60)
        return json.loads(out.stdout) if out.returncode == 0 and out.stdout.strip() else None
    except Exception:  # no gh, no network: the status just says unknown
        return None


def _probe_version():
    with open(os.path.join(ADDON_SRC, ADDON + ".toc"), encoding="utf-8") as f:
        return re.search(r"^## Version:\s*(\S+)", f.read(), re.M).group(1)


def cmd_status(argv=()):
    """apidoc.py status [--json]: one look at ForeverAPI, for Norgannon Desk."""
    def git(*a):
        r = subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else ""
    dump = latest_dump()
    client = latest_client()
    issues = _gh_json("issue", "list", "-R", contrib.REPO, "--state", "open", "--label", contrib.LABEL,
                      "--limit", "200", "--json", "number,title,author,createdAt")
    rel = _gh_json("release", "view", "-R", contrib.REPO, "--json", "tagName,publishedAt,url")
    version = _probe_version()
    filed = contrib.stored(None, CONTRIB_DIR)
    state = os.path.join(ROOT, ".last-import")
    st = {
        "repo": "https://github.com/" + contrib.REPO,
        "site": "https://zmarotrix.github.io/ForeverAPI/",
        "client_docs": os.path.basename(client).split(".json")[0] if client else None,
        "last_dump": os.path.basename(os.path.dirname(dump)) + "/" + os.path.basename(dump) if dump else None,
        "last_import": datetime.datetime.fromtimestamp(os.path.getmtime(state)).isoformat(timespec="seconds")
        if os.path.exists(state) else None,
        "probe_version": version,
        "released": (rel or {}).get("tagName"),
        "release_url": (rel or {}).get("url"),
        "release_needed": bool(rel) and (rel or {}).get("tagName") != "v" + version,
        "submissions_open": None if issues is None else [
            {"issue": i["number"], "who": (i.get("author") or {}).get("login"), "opened": i.get("createdAt"),
             "url": "https://github.com/%s/issues/%d" % (contrib.REPO, i["number"])} for i in issues],
        "filed": len(filed),
        "contributors": sorted({rec["who"] for rec in filed}),
        "git": {"branch": git("branch", "--show-current"), "dirty": bool(git("status", "--porcelain")),
                "ahead": git("rev-list", "--count", "@{u}..HEAD") or None},
    }
    if "--json" in argv:
        _json_out(st)
    else:
        for k, v in st.items():
            if k == "submissions_open" and isinstance(v, list):
                v = len(v)
            elif isinstance(v, list):
                v = ", ".join(map(str, v)) or "none"
            print("%-17s %s" % (k, v))
    return st


LUALS_README = """WoW Forever API definitions for VS Code (the Lua extension by sumneko, LuaLS).

Unzip this folder into your add-on workspace, then copy ForeverAPI-LuaLS/.luarc.json to the workspace root
(or add "ForeverAPI-LuaLS/library" to Lua.workspace.library in your VS Code settings). Lua 5.1.

Every function says what the game showed: verified, always secret, secret in combat, protected, forbidden.
Classic names that are gone on Forever are struck through, with where they went.
Reference: https://zmarotrix.github.io/ForeverAPI/
"""


def cmd_publish_release(argv):
    """release --publish [--yes]: make the zips and post them as GitHub release v<version> (from the TOC).

    Without --yes it only says what it would do. With --yes: refuses if the tag exists or a test fails, else
    tags, pushes and runs gh release create with both zips. Bump ## Version in the TOC first."""
    version, outs = cmd_release()
    tag = "v" + version
    exists = _gh_json("release", "view", tag, "-R", contrib.REPO, "--json", "tagName") is not None
    plan = {"tag": tag, "files": [os.path.basename(o) for o in outs], "exists": exists, "published": False}
    if exists:
        print("%s is already released: bump ## Version in %s.toc first." % (tag, ADDON))
    elif "--yes" not in argv:
        print("dry run: would test, tag %s, push and post %s. Add --yes to do it." % (tag, ", ".join(plan["files"])))
    else:
        for t in ("test_probe.py", "test_collectors.py", "test_checks.py"):
            r = subprocess.run([sys.executable, os.path.join(HERE, t)], capture_output=True, text=True)
            if r.returncode:
                print(r.stdout[-2000:])
                sys.exit("tests failed (%s): nothing released" % t)
        subprocess.run(["git", "tag", tag], cwd=ROOT, check=True)
        subprocess.run(["git", "push", "-q", "origin", "HEAD", tag], cwd=ROOT, check=True)
        build = plan["files"][-1].split("-")[-1][:-4] if len(plan["files"]) > 1 else "?"
        notes = ("ForeverAPI Probe %s for WoW Forever client %s. Unzip ForeverAPIProbe into _forever_/Interface/AddOns, "
                 "restart the game, then type /fapi. VS Code definitions: the ForeverAPI-LuaLS zip." + NL + NL +
                 "Reference: https://zmarotrix.github.io/ForeverAPI/") % (version, build)
        subprocess.run(["gh", "release", "create", tag, *outs, "-R", contrib.REPO, "--title", "ForeverAPI Probe " + version,
                        "--notes", notes], check=True)
        plan["published"] = True
        print("released", tag)
    if "--json" in argv:
        _json_out(plan)
    return plan


def cmd_release():
    """dist/ForeverAPIProbe-<version>.zip (the add-on) and dist/ForeverAPI-LuaLS-<build>.zip (VS Code definitions)."""
    import zipfile
    with open(os.path.join(ADDON_SRC, ADDON + ".toc"), encoding="utf-8") as f:
        version = re.search(r"^## Version:\s*(\S+)", f.read(), re.M).group(1)
    dist = os.path.join(ROOT, "dist")
    os.makedirs(dist, exist_ok=True)
    out = os.path.join(dist, "%s-%s.zip" % (ADDON, version))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for name in sorted(os.listdir(ADDON_SRC)):
            z.write(os.path.join(ADDON_SRC, name), "%s/%s" % (ADDON, name))
    print("add-on:", _rel(out))
    outs = [out]
    if os.path.isdir(LUALS):
        client = latest_client()
        build = os.path.basename(client).split(".json")[0] if client else "unknown"
        lz = os.path.join(dist, "ForeverAPI-LuaLS-%s.zip" % build)
        with zipfile.ZipFile(lz, "w", zipfile.ZIP_DEFLATED) as z:
            for root, _, files in os.walk(LUALS):
                for name in sorted(files):
                    p = os.path.join(root, name)
                    z.write(p, "ForeverAPI-LuaLS/" + os.path.relpath(p, LUALS).replace(os.sep, "/"))
            z.writestr("ForeverAPI-LuaLS/README.txt", LUALS_README)
        print("VS Code definitions:", _rel(lz))
        outs.append(lz)
    return version, outs


def cmd_diff(a, b):
    da, db_ = _load_json(a), _load_json(b)
    name = "%s__%s.md" % (os.path.basename(a).split(".json")[0], os.path.basename(b).split(".json")[0])
    out = os.path.join(DOCS, "changes", name)
    differ.write_report(da, db_, a, b, out)
    print("diff written to", _rel(out))


def main(argv):
    if "--json" in argv:
        sys.stdout = sys.stderr  # the log; _json_out writes the answer to the real stdout
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__)
        return
    cmd = argv[0]
    if cmd == "extract":
        cmd_extract()
    elif cmd == "deploy":
        cmd_deploy()
    elif cmd == "import":
        cmd_import(argv[1] if len(argv) > 1 else None)
    elif cmd == "build":
        cmd_build()
    elif cmd == "diff":
        if len(argv) == 1:
            dumps = sorted(glob.glob(os.path.join(DUMPS, "*", "*.json.gz")), key=os.path.getmtime)
            if len(dumps) < 2:
                print("need two dumps (or pass two files)")
                return
            cmd_diff(dumps[-2], dumps[-1])
        else:
            cmd_diff(argv[1], argv[2])
    elif cmd == "release":
        if "--publish" in argv:
            cmd_publish_release(argv[1:])
        else:
            cmd_release()
    elif cmd == "status":
        cmd_status(argv[1:])
    elif cmd == "contrib":
        cmd_contrib(argv[1:])
    elif cmd == "classic-scan":
        cmd_classic_scan(argv[1:])
    elif cmd == "luals":
        cmd_build()
    elif cmd == "all":
        cmd_extract()
        cmd_import()
        cmd_build()
    else:
        print("unknown command", cmd)
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
