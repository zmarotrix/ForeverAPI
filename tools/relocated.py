"""Relocated API: classic globals that are missing (or only shimmed) on Forever, where each one went, and how the call
changed.

Sources, most trusted first:
  guide     Blizzard's own 11.0 spell book transition guide, shipped in the client (Blizzard_Deprecated).
  shim      Blizzard's deprecation add-ons in the client: each old name is rewritten on top of its replacement.
            A shim gated to the "classic" game type does not load on Forever; one that loads keeps the old name
            working for now ("Blizzard: will be removed at the next expansion").
  curated   sources/relocated.json, for what Blizzard's files don't cover.
  same-name a C_ namespace function with the same name (a lead only).
Every old and new name is checked against the in-game dump, so a wrong mapping shows up as not-in-game.

Which classic names to look at: everything the sources above name, plus every global the classic add-ons on disk
call (sources/classic-usage.json, written by `apidoc.py classic-scan <add-on folders>`).
"""

import json
import os
import re

LIBS = ("string", "table", "math", "bit", "coroutine", "os", "debug")

# ---------------------------------------------------------------------------------------------------------------
# classic add-on usage
# ---------------------------------------------------------------------------------------------------------------

_CALL = re.compile(r"(?<![\w.:])([A-Z][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?)\s*\(")
_LIBCALL = re.compile(r"(?<![\w.:])((?:%s)\.[a-z][a-z0-9_]*)\s*\(" % "|".join(LIBS))
_DEFS = re.compile(r"^\s*(?:local\s+)?function\s+([A-Za-z_][\w.:]*)|^\s*(?:local\s+)?([A-Za-z_][\w.]*)\s*=", re.M)
_COMMENT = re.compile(r"--\[(=*)\[.*?\]\1\]|--[^\n]*", re.S)
_STRING = re.compile(r"\"(?:\\.|[^\"\\\n])*\"|'(?:\\.|[^'\\\n])*'")


def scan(folders):
    """{name: {"n": calls, "addons": [...]}} for globals the add-ons under `folders` call and never define."""
    calls, defined = {}, set()
    for folder in folders:
        addon = os.path.basename(os.path.normpath(folder))
        for root, _, files in os.walk(folder):
            for name in files:
                if not name.endswith(".lua"):
                    continue
                with open(os.path.join(root, name), encoding="utf-8", errors="replace") as f:
                    text = _STRING.sub('""', _COMMENT.sub("", f.read()))
                for a, b in _DEFS.findall(text):
                    defined.add((a or b).split(":")[0])
                for m in _CALL.findall(text) + _LIBCALL.findall(text):
                    rec = calls.setdefault(m, {"n": 0, "addons": set()})
                    rec["n"] += 1
                    rec["addons"].add(addon)
    out = {}
    for name, rec in calls.items():
        head = name.split(".")[0]
        if name in defined or (head in defined and head not in LIBS):
            continue  # the add-on's own function or table
        if "." in name and not (head.startswith("C_") or head in LIBS):
            continue  # a method on some table: not a global API
        out[name] = {"n": rec["n"], "addons": sorted(rec["addons"])}
    return out


# ---------------------------------------------------------------------------------------------------------------
# Blizzard's files
# ---------------------------------------------------------------------------------------------------------------

_DEF_FN = re.compile(r"^[ \t]*(?:function\s+([A-Za-z_][\w.]*)\s*\(([^)]*)\)|([A-Za-z_][\w.]*)\s*=\s*function\s*\(([^)]*)\))", re.M)
_ALIAS = re.compile(r"^[ \t]*([A-Za-z_][\w.]*)\s*=\s*([A-Z][\w]*(?:\.[\w]+)+|[A-Z]\w+)\s*;?\s*$", re.M)
_TARGET = re.compile(r"(?<![\w.:])((?:C_\w+|[A-Z]\w*Util|Get\w+|Unit\w+|Is\w+|Player\w+)(?:\.\w+)?)\s*\(")


def parse_shims(dep):
    """[{old, args, new, file, gate}] from the deprecation add-ons."""
    out = []
    for path, rec in sorted(dep.items()):
        if "TransitionGuide" in path:
            continue
        text = _COMMENT.sub("", rec["text"])
        defs = list(_DEF_FN.finditer(text))
        for i, m in enumerate(defs):
            old = m.group(1) or m.group(3)
            args = (m.group(2) if m.group(1) else m.group(4)) or ""
            body = text[m.end(): defs[i + 1].start() if i + 1 < len(defs) else len(text)]
            targets = [t for t in _TARGET.findall(body) if t != old and t not in ("GetCVarBool",)]
            out.append({"old": old, "args": args.strip(), "new": _uniq(targets)[:3], "file": path, "gate": rec.get("gate")})
        for m in _ALIAS.finditer(text):
            old, new = m.group(1), m.group(2)
            if old.isupper() or old.split(".")[-1].isupper() or new.split(".")[-1].isupper():
                continue  # constants
            out.append({"old": old, "args": None, "new": [new], "file": path, "gate": rec.get("gate"), "alias": True})
    return out


_GUIDE = re.compile(r"^\s*([A-Za-z_][\w./]*)\s*\(([^)]*)\)\s*=?\s*([A-Za-z_][\w.]*)\s*\(([^)]*)\)", re.M)
_GUIDE_MOVED = re.compile(r"^\s*(C_\w+\.\w+)\s*=\s*(C_\w+\.\w+)", re.M)


def parse_guide(dep):
    """[{old, args, new, new_args, note}] from Blizzard's spell book transition guide."""
    out = []
    for path, rec in dep.items():
        if "TransitionGuide" not in path:
            continue
        note = None
        for line in rec["text"].splitlines():
            if line.strip().startswith("--") and not line.strip().startswith("---"):
                note = line.strip().lstrip("-").strip()
                continue
            m = _GUIDE.match(line)
            if m:
                for old in m.group(1).split("/"):
                    if "." in old:
                        continue  # GameTooltip:SetSpellBookItem style lines
                    out.append({"old": old, "args": m.group(2).strip(), "new": [m.group(3)],
                                "new_args": m.group(4).strip(), "note": note, "file": path})
                continue
            m = _GUIDE_MOVED.match(line)
            if m:
                out.append({"old": m.group(1), "args": None, "new": [m.group(2)], "note": note, "file": path})
            if not line.strip():
                note = None
    return out


def _guide_change(g):
    if g.get("new_args") is None:
        out = "Moved as is."
    else:
        out = "Now `%s(%s)`." % (g["new"][0], g["new_args"])
        if "spellBank" in g["new_args"]:
            out += " spellBank is Enum.SpellBookSpellBank.Player or .Pet instead of the \"spell\" / \"pet\" book type."
    if g.get("note"):
        out += " Blizzard: " + g["note"].rstrip(".") + "."
    return out


def _uniq(xs):
    seen, out = set(), []
    for x in xs:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


# ---------------------------------------------------------------------------------------------------------------
# the table
# ---------------------------------------------------------------------------------------------------------------

def _in_game(model, name):
    """"yes" / "no" / None (no dump to tell)."""
    if not model.get("globals"):
        return None
    if "." in name:
        head, rest = name.split(".", 1)
        if head in LIBS or head.startswith("C_"):
            t = (model.get("tables") or {}).get(head)
            return "yes" if isinstance(t, dict) and rest in t else "no"
        return "yes" if isinstance((model.get("tables") or {}).get(head), dict) else "no"  # e.g. AuraUtil.X: a UI table
    f = model["functions"].get(name)
    if f and f.get("status") in ("verified", "undocumented"):
        return "yes"
    code = model["globals"].get(name)
    return "yes" if isinstance(code, str) and code.startswith("f") else "no"


def _sig(model, name):
    f = model["functions"].get(name) or {}
    if f.get("source") != "client-docs":
        return None

    def p(params):
        return ", ".join(("%s%s" % (a.get("Name"), "?" if a.get("Nilable") or "Default" in a else "")) for a in params or [])
    return "%s = %s(%s)" % (p(f.get("returns")) or "nothing", name, p(f.get("args")))


def _flags(model, name):
    """Restriction words for a replacement: what a developer must know before switching to it."""
    f = model["functions"].get(name) or {}
    fl = f.get("flags") or {}
    out = []
    if fl.get("IsProtectedFunction"):
        out.append("protected")
    if fl.get("SecretReturns"):
        out.append("always secret")
    elif fl.get("SecretWhenInCombat") or any(k.startswith("SecretWhen") for k in fl):
        out.append("secret in combat")
    for phase in ("outside", "combat"):
        rec = f.get(phase) or {}
        if rec.get("forbidden"):
            out.append("forbidden")
        if any(isinstance(r, str) and r.startswith("secret") for r in rec.get("returns") or []):
            out.append("secret %s" % ("in combat" if phase == "combat" else "out of combat"))
    return _uniq(out)


def build(model, dep, usage, curated):
    """[{old, where, new: [{name, in_game, sig, flags}], classic, change, source, file, callers}] sorted by old."""
    usage = usage or {}
    rows = {}

    def add(old, source, new, **kw):
        row = rows.get(old)
        if row is None:
            row = rows[old] = {"old": old, "sources": [], "new": [], "classic": None, "change": None, "file": None}
        if source not in row["sources"]:
            row["sources"].append(source)
        for n in new:
            if n not in row["new"]:
                row["new"].append(n)
        for k, v in kw.items():
            if v and not row.get(k):
                row[k] = v

    for c in (curated or {}).get("entries", []):
        add(c["old"], "curated", c.get("new") or [], classic=c.get("classic"), change=c.get("change"),
            confidence=c.get("confidence"))
    for g in parse_guide(dep):
        add(g["old"], "guide", g["new"], classic="%s(%s)" % (g["old"], g["args"]) if g.get("args") is not None else None,
            change=_guide_change(g), file=g["file"])
    for s in parse_shims(dep):
        src = "shim" if s.get("gate") in (None, "mainline") or "mainline" in (s.get("gate") or "") else "classic shim"
        add(s["old"], src, s["new"], classic="%s(%s)" % (s["old"], s["args"]) if s.get("args") is not None else None,
            file=s["file"], gate=s.get("gate"))
    # classic add-on calls that aren't in the game: look for a same-named C_ function
    by_name = {}
    for key, f in model["functions"].items():
        if f.get("namespace") and f.get("status") in ("verified", "undocumented"):
            by_name.setdefault(f["name"], []).append(key)
    for name in usage:
        if name in rows or "." in name:
            continue
        if _in_game(model, name) == "no" and by_name.get(name):
            add(name, "same-name", sorted(by_name[name]))

    out = []
    for old, row in rows.items():
        present = _in_game(model, old)
        if present is None:
            where = "unverified"
        elif present == "yes":
            where = "shim" if row.get("file") and ("shim" in row["sources"]) else "present"
        else:
            where = "missing"
        if where == "present" and "curated" not in row["sources"] and "guide" not in row["sources"]:
            continue  # still there and nobody says it moved
        new = [{"name": n, "in_game": _in_game(model, n), "sig": _sig(model, n), "flags": _flags(model, n)}
               for n in row["new"]]
        u = usage.get(old)
        out.append({"old": old, "where": where, "new": new, "classic": row.get("classic"), "change": row.get("change"),
                    "sources": row["sources"], "file": row.get("file"), "gate": row.get("gate"),
                    "confidence": row.get("confidence") or ("lead" if row["sources"] == ["same-name"] else None),
                    "callers": u and {"n": u["n"], "addons": u["addons"]}})
    out.sort(key=lambda r: (r["where"] != "missing", -((r["callers"] or {}).get("n") or 0), r["old"].lower()))
    return out


def missing_unmapped(model, usage):
    """Classic add-on calls not in the game and not in the table: candidates for sources/relocated.json."""
    return sorted(((n, u["n"], u["addons"]) for n, u in (usage or {}).items() if _in_game(model, n) == "no"),
                  key=lambda x: -x[1])


def compat_json(rows, version):
    """The table for Norgannon Core's Core.Compat: only mappings whose replacement exists in game."""
    out = {"build": version, "about": "Generated by ForeverAPI tools/apidoc.py build. old -> replacement, verified "
           "against an in-game dump. 'change' says how the call differs; 'where': missing (old name gone), shim (old "
           "name works through Blizzard's deprecation add-on, to be removed), present.", "entries": []}
    for r in rows:
        live = [n for n in r["new"] if n["in_game"] == "yes"]
        out["entries"].append({"old": r["old"], "where": r["where"], "new": [n["name"] for n in live],
                               "new_not_in_game": [n["name"] for n in r["new"] if n["in_game"] == "no"],
                               "signatures": {n["name"]: n["sig"] for n in live if n["sig"]},
                               "flags": {n["name"]: n["flags"] for n in live if n["flags"]},
                               "classic": r["classic"], "change": r["change"], "confidence": r["confidence"],
                               "sources": r["sources"]})
    return out


def load(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


WHERE = {"missing": "Gone on Forever", "shim": "Still works through Blizzard's deprecation add-ons (to be removed)",
         "present": "Still there", "unverified": "Not checked (no in-game dump)"}


def render_md(rows, unmapped, meta, path):
    lines = ["# Relocated API", "",
             "Classic (1.15) globals that Forever dropped or moved, where each one went and how the call changed. "
             "Every name in this table was checked against an in-game dump of client %s." % meta.get("key", "?"), "",
             "- **gone**: the old name doesn't exist on Forever. Calling it errors.",
             "- **shim**: the old name still works, through Blizzard's own deprecation add-ons "
             "(Blizzard_Deprecated*). Blizzard says these will be removed, so switch.",
             "- Sources: *guide* is Blizzard's spell book transition guide in the client; *shim* a Blizzard deprecation "
             "add-on; *classic shim* one Blizzard ships for classic only, which Forever doesn't load; *curated* our own "
             "sources/relocated.json; *same-name* only a function of the same name in a C_ namespace (a lead).", "",
             "Note: Forever reports `WOW_PROJECT_ID` = %s (`WOW_PROJECT_CAMELOT`), not `WOW_PROJECT_MAINLINE` (1) or "
             "`WOW_PROJECT_CLASSIC` (2), but it loads Blizzard's *mainline* deprecation shims, not the classic ones. "
             "Add-ons that branch on the project ID take neither branch." % meta.get("project_id", "18"), ""]
    for where in ("missing", "shim", "present", "unverified"):
        sub = [r for r in rows if r["where"] == where]
        if not sub:
            continue
        lines += ["## %s (%d)" % (WHERE[where], len(sub)), "",
                  "| Classic | Forever | How it changed | Source |", "|---|---|---|---|"]
        for r in sub:
            new = "<br>".join("`%s`%s%s" % (n["name"], "" if n["in_game"] != "no" else " (not visible to add-ons)",
                                            (" *" + ", ".join(n["flags"]) + "*") if n["flags"] else "") for n in r["new"]) or "none"
            change = (r["change"] or "") + ((" Classic: `%s`." % r["classic"]) if r["classic"] and r["classic"] not in (r["change"] or "") else "")
            if r["confidence"]:
                change = "**%s.** %s" % (r["confidence"].capitalize(), change)
            used = (" Called %d× by %s." % (r["callers"]["n"], ", ".join(r["callers"]["addons"]))) if r["callers"] else ""
            lines.append("| `%s` | %s | %s%s | %s |" % (r["old"], new, change.replace("|", "\\|").strip(), used, ", ".join(r["sources"])))
        lines.append("")
    if unmapped:
        lines += ["## Classic add-on calls with no known home yet", "",
                  "Globals the scanned classic add-ons call that aren't in the game, and nothing above maps. Some are "
                  "the add-ons' own helpers that the scan couldn't tell apart; the rest need an entry in "
                  "sources/relocated.json.", ""]
        lines += ["- `%s` (%d× by %s)" % (n, c, ", ".join(a)) for n, c, a in unmapped]
        lines.append("")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
