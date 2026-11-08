"""Write the local docs website (site/): a static page that opens straight from disk, no server.

The data goes in site/data.js as `window.API = {...}` (browsers won't fetch JSON over file://). The page itself
is copied from tools/site_src/.
"""

import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "site_src")


def _p(params):
    """[{Name, Type, Nilable, Default, InnerType, doc}] -> [[name, type, nilable, default, doc]]"""
    out = []
    for a in params or []:
        t = a.get("Type", "?")
        if t == "table" and a.get("InnerType"):
            t = a["InnerType"] + "[]"
        out.append([a.get("Name"), t, bool(a.get("Nilable")), a.get("Default"), a.get("doc") or ""])
    return out


def _call(rec):
    if not rec:
        return None
    out = {k: rec[k] for k in ("n", "returns", "error", "missing", "skipped", "forbidden", "arg") if k in rec}
    return out


def _val(v):
    if isinstance(v, str) and v[:2] == "n:":
        try:
            f = float(v[2:])
            return int(f) if f.is_integer() else f
        except ValueError:
            return v[2:]
    if isinstance(v, str) and v[:2] in ("s:", "b:"):
        return v[2:]
    return v


def compact(model):
    F = {}
    for key, f in model["functions"].items():
        F[key] = {k: v for k, v in {
            "s": f["status"], "sys": f.get("system"), "ns": f.get("namespace"), "g": f.get("game"),
            "a": _p(f.get("args")) if f.get("source") == "client-docs" else None,
            "r": _p(f.get("returns")) if f.get("source") == "client-docs" else None,
            "d": f.get("doc") or None, "fl": f.get("flags") or None,
            "o": _call(f.get("outside")), "c": _call(f.get("combat")),
            "u": f.get("used_by"), "ui": f.get("ui_lua") or (f.get("game") == "fL" or None),
            "file": f.get("file"), "rep": f.get("replaced_by"), "w": f.get("web"),
        }.items() if v not in (None, "", {}, [])}
    E = {}
    for key, e in model["events"].items():
        E[key] = {k: v for k, v in {
            "s": e["status"], "sys": e.get("system"), "p": _p(e.get("payload")) if e.get("source") == "client-docs" else None,
            "d": e.get("doc") or None, "fl": e.get("flags") or None, "chk": (e.get("check") or {}).get("register"),
            "live": e.get("live"), "u": e.get("used_by"), "src": e.get("source"), "file": e.get("file"),
        }.items() if v not in (None, "", {}, [])}
    T = {}
    for key, t in list(model["structures"].items()) + list(model["enums"].items()):
        rec = {"k": t.get("kind"), "s": t.get("status"), "sys": t.get("system"), "d": t.get("doc") or None,
               "f": [[x.get("Name"), x.get("Type"), bool(x.get("Nilable")), x.get("EnumValue", x.get("Value")),
                      x.get("Default"), x.get("doc") or ""] for x in t.get("fields") or []],
               "mm": t.get("mismatches") or None, "file": t.get("file")}
        if t.get("status") == "undocumented" and isinstance(t.get("game"), dict):
            rec["gv"] = sorted(([k, _val(v)] for k, v in t["game"].items()), key=lambda kv: (str(type(kv[1])), kv[1]))
        T[key] = {k: v for k, v in rec.items() if v not in (None, "", {}, [])}
    O = {}
    for sysname, obj in model["objects"].items():
        O[sysname] = {name: {k: v for k, v in {"a": _p(f.get("args")), "r": _p(f.get("returns")), "d": f.get("doc") or None,
                                                "fl": f.get("flags") or None}.items() if v not in (None, "", {}, [])}
                      for name, f in obj["functions"].items()}
    W = {}
    for wt, w in model["widgets"].items():
        methods = {}
        for m, rec in w["methods"].items():
            d = rec.get("doc")
            methods[m] = d["system"] if d else 0
        W[wt] = {k: v for k, v in {"ot": w.get("objectType"), "err": w.get("error"), "sc": w.get("scripts"),
                                   "m": methods}.items() if v not in (None, "", {}, [])}
    C = {}
    for name, c in model["cvars"].items():
        if isinstance(c, dict):
            C[name] = {k: v for k, v in {"d": c.get("default"), "h": c.get("help"), "c": c.get("category"),
                                         "t": c.get("kind")}.items() if v not in (None, "")}
    meta = dict(model.get("meta") or {})
    return {
        "meta": meta, "client": model.get("client_version"), "eventCheck": model.get("event_check_method"),
        "calls": model.get("calls_meta"), "blocked": model.get("blocked"),
        "tainted": {k: len(v) if isinstance(v, (list, dict)) else 0 for k, v in (model.get("tainted") or {}).items()},
        "lua": sorted(k for k, v in (model.get("globals") or {}).items() if isinstance(v, str) and v.startswith("f") and k[:1].islower()),
        "libs": {lib: sorted(map(str, m)) for lib, m in (model.get("tables") or {}).items()
                 if lib in ("string", "table", "math", "bit", "coroutine", "debug", "os") and isinstance(m, dict)},
        "F": F, "E": E, "T": T, "O": O, "W": W, "C": C,
    }


def write(model, out, generated):
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(SRC):
        shutil.copy(os.path.join(SRC, name), os.path.join(out, name))
    data = compact(model)
    data["generated"] = generated
    with open(os.path.join(out, "data.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write("window.API=")
        json.dump(data, f, separators=(",", ":"), sort_keys=True, default=str)
        f.write(";\n")
    return os.path.join(out, "index.html")
