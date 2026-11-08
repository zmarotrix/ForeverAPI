"""Merge the client's generated docs, the in-game dump and web leads into one model with a status per item.

Statuses:
  verified       the game dump has it (and, for events, RegisterEvent accepted it)
  undocumented   the game has it, Blizzard's docs don't (Forever-only, or a legacy API Blizzard never documented)
  not-in-game    Blizzard's docs list it, the game dump doesn't have it
  unverified     no dump yet, or the dump couldn't check it
"""

import re

UNIT_TYPES = {"UnitToken", "uiUnit", "UnitTokenRestrictedForAddOns", "UnitTokenVariant", "UnitTokenType"}
GETTER = re.compile(r"^(Get|Is|Has|Can|Should|Are|Does|Unit|Num)")
NEVER = re.compile(r"Reward|Request")
CONTROL_EVENT = "APIPROBE_NOT_A_REAL_EVENT"
FLAG_SKIP = {"Name", "Type", "Arguments", "Returns", "Documentation", "Payload", "LiteralName", "Fields", "Values"}


def _list(v):
    if v is None:
        return []
    if isinstance(v, dict):
        return [v[k] for k in sorted(k for k in v if isinstance(k, int))]
    return list(v)


def _docs(v):
    return " ".join(str(x) for x in _list(v) if isinstance(x, str))


def _params(v):
    out = []
    for p in _list(v):
        if isinstance(p, dict):
            out.append({k: (str(x) if not isinstance(x, (bool, int, float, str, type(None))) else x)
                        for k, x in p.items() if k != "Documentation"} | ({"doc": _docs(p.get("Documentation"))}
                                                                         if p.get("Documentation") else {}))
    return out


def _flags(d):
    return {k: (v if isinstance(v, (bool, int, float)) else str(v)) for k, v in d.items() if k not in FLAG_SKIP
            and k != "File"}


def documented(client):
    """Flatten client docs: functions, events, tables (enums/structures/constants), widget API systems."""
    fns, events, tables, objects = {}, {}, {}, {}
    for s in client["systems"]:
        sysname, ns, kind = s.get("Name"), s.get("Namespace"), s.get("Type")
        meta = {"system": sysname, "file": s.get("File")}
        if kind == "ScriptObject":
            objects[sysname] = {"file": s.get("File"), "functions": {}}
        for f in _list(s.get("Functions")):
            item = {"name": f["Name"], "namespace": ns, "args": _params(f.get("Arguments")),
                    "returns": _params(f.get("Returns")), "doc": _docs(f.get("Documentation")),
                    "flags": _flags(f)} | meta
            if kind == "ScriptObject":
                objects[sysname]["functions"][f["Name"]] = item
            else:
                fns[(ns + "." if ns else "") + f["Name"]] = item
        for e in _list(s.get("Events")):
            events[e.get("LiteralName") or e["Name"]] = {"name": e["Name"], "payload": _params(e.get("Payload")),
                                                         "doc": _docs(e.get("Documentation")),
                                                         "flags": _flags(e)} | meta
        for t in _list(s.get("Tables")):
            tables[t["Name"]] = {"kind": t.get("Type"), "fields": _params(t.get("Fields") or t.get("Values")),
                                 "doc": _docs(t.get("Documentation")), "flags": _flags(t)} | meta
    return {"functions": fns, "events": events, "tables": tables, "objects": objects}


def call_plan(docs):
    """Documented getters the probe may call with no arguments, or with "player" as the only argument."""
    plan = []
    for key, f in docs["functions"].items():
        flags = f["flags"]
        if flags.get("IsProtectedFunction") or not GETTER.match(f["name"]) or NEVER.search(f["name"]):
            continue
        required = [a for a in f["args"] if not a.get("Nilable") and "Default" not in a]
        if not required:
            arg = None
        elif len(required) == 1 and (required[0].get("Type") in UNIT_TYPES or required[0].get("Name") == "unit"):
            arg = "unit"
        else:
            continue
        plan.append((f["namespace"], f["name"], arg))
    return sorted(plan, key=lambda c: ((c[0] or ""), c[1]))


def _fn_code(code):
    return isinstance(code, str) and code.startswith("f")


def build(client, dump=None, web=None, framexml=None):
    docs = documented(client)
    web = web or {}
    framexml = framexml or {"events": {}, "globals": {}, "defined": {}}
    g = (dump or {}).get("globals", {})
    tables = (dump or {}).get("tables", {})
    have_dump = bool(dump)
    calls = (dump or {}).get("calls", {})
    outside = (calls.get("outside") or {}).get("results", {})
    combat = (calls.get("combat") or {}).get("results", {})

    def game_code(key):
        if "." in key:
            ns, name = key.split(".", 1)
            members = tables.get(ns)
            return members.get(name) if isinstance(members, dict) else None
        return g.get(key)

    functions = {}
    for key, f in docs["functions"].items():
        code = game_code(key)
        status = ("verified" if _fn_code(code) else "not-in-game") if have_dump else "unverified"
        functions[key] = dict(f, key=key, status=status, game=code, source="client-docs")
    # functions the game has and the docs don't
    if have_dump:
        for name, code in g.items():
            if _fn_code(code) and name not in functions:
                functions[name] = {"key": name, "name": name, "namespace": None, "status": "undocumented",
                                   "game": code, "source": "game", "system": None,
                                   "used_by": framexml["globals"].get(name),
                                   "ui_lua": (framexml.get("defined") or {}).get(name)}
        for ns, members in tables.items():
            if not (ns.startswith("C_") and isinstance(members, dict)):
                continue
            for name, code in members.items():
                key = ns + "." + str(name)
                if _fn_code(code) and key not in functions:
                    functions[key] = {"key": key, "name": name, "namespace": ns, "status": "undocumented",
                                      "game": code, "source": "game", "system": None}
    for key, f in functions.items():
        if key in outside:
            f["outside"] = outside[key]
        if key in combat:
            f["combat"] = combat[key]
        if key in web:
            f["web"] = web[key]
        if isinstance(f.get("game"), str) and "!" in f["game"]:
            f["replaced_by"] = f["game"].split("!", 1)[1]

    # events
    checked = (dump or {}).get("events", {})
    live = ((dump or {}).get("live") or {}).get("events", {})
    control = checked.get(CONTROL_EVENT, {})
    register_works = control.get("register") not in (None, "ok")
    events = {}
    names = set(docs["events"]) | set(checked) | set(live) | set(framexml["events"])
    names.discard(CONTROL_EVENT)
    for name in names:
        d = docs["events"].get(name)
        c = checked.get(name)
        if c is not None and register_works:
            exists = c.get("register") == "ok"
        elif c is not None and c.get("valid") is not None:
            exists = bool(c.get("valid"))
        else:
            exists = None
        if name in live:
            exists = True
        if not have_dump or exists is None:
            status = "unverified"
        elif exists:
            status = "verified" if d else "undocumented"
        else:
            status = "not-in-game"
        events[name] = dict(d or {}, key=name, status=status, check=c, live=live.get(name),
                            source="client-docs" if d else ("game" if name in live else "framexml"),
                            used_by=framexml["events"].get(name))

    # enums and constants
    enums = {}
    game_enum = tables.get("Enum") or {}
    game_const = tables.get("Constants") or {}
    for name, t in docs["tables"].items():
        if t["kind"] not in ("Enumeration", "Constants"):
            continue
        game_vals = (game_enum if t["kind"] == "Enumeration" else game_const).get(name)
        if not have_dump:
            status = "unverified"
        elif not isinstance(game_vals, dict):
            status = "not-in-game"
        else:
            status = "verified"
        mismatches = []
        if isinstance(game_vals, dict):
            for fld in t["fields"]:
                want = fld.get("EnumValue", fld.get("Value"))
                got = game_vals.get(fld.get("Name"))
                if got is None:
                    mismatches.append((fld.get("Name"), want, None))
                elif isinstance(want, (int, float)) and got != "n:%s" % _num(want):
                    mismatches.append((fld.get("Name"), want, got))
        enums[name] = dict(t, key=name, status=status, game=game_vals, mismatches=mismatches, source="client-docs")
    if have_dump:
        for kind, src in (("Enumeration", game_enum), ("Constants", game_const)):
            for name, vals in src.items():
                if name not in enums and isinstance(vals, dict):
                    enums[name] = {"key": name, "kind": kind, "status": "undocumented", "game": vals,
                                   "fields": [], "mismatches": [], "source": "game"}

    widgets = {}
    for wtype, rec in ((dump or {}).get("widgets") or {}).items():
        methods = rec.get("methods") or {}
        docs_for = {}
        for sysname, obj in docs["objects"].items():
            fnames = set(obj["functions"])
            if fnames and fnames <= set(methods):
                for m in fnames:
                    docs_for.setdefault(m, obj["functions"][m])
        widgets[wtype] = {"key": wtype, "error": rec.get("error"), "objectType": rec.get("objectType"),
                          "methods": {m: {"game": c, "doc": docs_for.get(m)} for m, c in methods.items()},
                          "scripts": _list(rec.get("scripts"))}

    return {
        "meta": (dump or {}).get("meta", {}), "client_version": client.get("version"),
        "functions": functions, "events": events, "enums": enums, "widgets": widgets,
        "objects": docs["objects"], "structures": {k: v for k, v in docs["tables"].items()
                                                   if v["kind"] in ("Structure", "CallbackType")},
        "cvars": (dump or {}).get("cvars", {}), "tables": tables, "globals": g,
        "tainted": (dump or {}).get("tainted", {}), "blocked": _list((dump or {}).get("blocked")),
        "calls_meta": {p: {k: v for k, v in (calls.get(p) or {}).items() if k != "results"} for p in ("outside", "combat")},
        "live_since": ((dump or {}).get("live") or {}).get("since"),
        "event_check_method": "RegisterEvent" if register_works else ("C_EventUtils.IsEventValid" if checked else None),
    }


def _num(v):
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v)
