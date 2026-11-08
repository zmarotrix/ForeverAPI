"""LuaLS definitions for VS Code (the sumneko "Lua" extension), generated from the ForeverAPI model.

Writes luals/library/*.lua (---@meta files: one per API system, plus classes, enums, events, widgets and the classic
names Forever dropped) and luals/.luarc.json. Every function says what the game showed, not only what Blizzard's
docs claim:
  - verified in game, undocumented (in game, not in the docs), or documented but not visible to add-ons
  - always secret / secret in combat / secret in <situation> (Blizzard's flags plus what the probes saw)
  - protected (blocked for add-ons in combat), forbidden (the game refused an add-on call)
  - for a classic name: gone on Forever (---@deprecated, so VS Code strikes it through) and where it went
"""

import json
import os
import re
import shutil

PRIM = {"number": "number", "bool": "boolean", "luaIndex": "integer", "cstring": "string", "string": "string",
        "stringView": "string", "fileID": "integer", "BigUInteger": "number", "BigInteger": "number", "time_t": "integer",
        "WOWGUID": "string", "WOWMONEY": "integer", "uiUnit": "number", "normalizedValue": "number", "Seconds": "number",
        "SingleColorValue": "number", "textureAtlas": "string", "textureKit": "string", "uiAddon": "string|integer",
        "LuaValueVariant": "any", "LuaValueReference": "any", "table": "table", "SimpleTexture": "Texture",
        "SpellIdentifier": "integer|string", "ItemInfo": "integer|string", "ClubId": "string", "ClubStreamId": "string",
        "VoiceChatID": "string", "ClubMemberOpaqueId": "string", "AuraFilters": "string", "function": "function",
        "colorRGB": "ColorMixin", "colorRGBA": "ColorMixin", "vector2": "Vector2DMixin", "vector3": "Vector3DMixin",
        "LuaDurationObject": "table", "kstringClubMessage": "string", "kstringLfgListApplicant": "string",
        "kstringLfgListSearch": "string", "kstringLfgListChat": "string", "SecretUnitToken": "UnitToken"}
CTRL = re.compile(r"[\x00-\x1f]")
NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
KEYWORDS = {"and", "break", "do", "else", "elseif", "end", "false", "for", "function", "if", "in", "local", "nil", "not",
            "or", "repeat", "return", "then", "true", "until", "while"}


def _arg(name, i):
    name = name or "arg%d" % i
    return name + "_" if name in KEYWORDS or not NAME.match(name) else name


class Types:
    def __init__(self, model):
        self.enums = {k for k, t in model["enums"].items() if t.get("kind") == "Enumeration"}
        self.structs = set(model["structures"])
        self.unknown = set()

    def lua(self, p):
        t = p.get("Type") or "any"
        if t == "table" and p.get("InnerType"):
            return self.lua({"Type": p["InnerType"]}) + "[]"
        if t in PRIM:
            return PRIM[t]
        if t.startswith("UnitToken"):
            return "UnitToken"
        if t in self.enums:
            return "Enum." + t
        if t in self.structs:
            return t
        self.unknown.add(t)
        return t


def _secret_seen(model):
    """{function key: set(situation labels)} where the probe or API watch saw a secret return."""
    out = {}
    for key, f in model["functions"].items():
        for phase, label in (("outside", "out of combat"), ("combat", "in combat")):
            rec = f.get(phase) or {}
            if any(isinstance(r, str) and r.startswith("secret") for r in rec.get("returns") or []):
                out.setdefault(key, set()).add(label)
    for sit, s in ((model.get("watch") or {}).get("situations") or {}).items():
        for unit, run in (s.get("runs") or {}).items():
            for key, rec in (run.get("results") or {}).items():
                if any(isinstance(r, str) and r.startswith("secret") for r in (rec or {}).get("returns") or []):
                    out.setdefault(key, set()).add("%s (%s)" % (sit, unit))
    return out


def _forbidden(model):
    out = set()
    for b in model.get("blocked") or []:
        if isinstance(b, dict) and b.get("during"):
            out.add(b["during"])
    for key, f in model["functions"].items():
        for phase in ("outside", "combat"):
            if (f.get(phase) or {}).get("forbidden"):
                out.add(key)
    return out


def _notes(f, seen, forbidden, moved):
    """Plain-words lines about restrictions, for the hover text."""
    key, fl, out = f["key"], f.get("flags") or {}, []
    st = f.get("status")
    if st == "verified":
        out.append("Verified in game.")
    elif st == "undocumented":
        out.append("In game, but not in Blizzard's docs: arguments and returns unknown.")
    elif st == "not-in-game":
        out.append("**Not visible to add-ons on Forever** (in Blizzard's docs only).")
    if fl.get("IsProtectedFunction"):
        out.append("**Protected**: Blizzard code only, or blocked for add-ons in combat.")
    if fl.get("HasRestrictions"):
        out.append("**Restricted**: may be blocked for add-ons.")
    if fl.get("SecretReturns"):
        out.append("**Always secret** return: you can show it (FontString:SetText, StatusBar colours) but not compare or do math on it.")
    whens = sorted(k[len("SecretWhen"):] for k, v in fl.items() if k.startswith("SecretWhen") and v)
    if whens:
        out.append("**Secret when**: " + ", ".join(re.sub(r"(?<!^)([A-Z])", r" \1", w).lower() for w in whens) + ".")
    if fl.get("SecretArguments") == "NotAllowed":
        out.append("Refuses secret arguments.")
    if seen.get(key):
        out.append("Seen secret: " + ", ".join(sorted(seen[key])) + ".")
    if key in forbidden:
        out.append("**Forbidden**: the game refused an add-on call to this.")
    if moved:
        out.append("**Blizzard compatibility shim**, to be removed: use `%s`." % "`, `".join(moved))
    return out


def _fn(lines, types, f, notes, deprecated=None, qual=None):
    name = qual or f["key"]
    if f.get("doc"):
        lines.append("---" + f["doc"].replace("\n", " "))
    for i, n in enumerate(notes):
        if i or f.get("doc"):
            lines.append("---")
        lines.append("---" + n)
    if deprecated:
        lines.append("---@deprecated")
    params = []
    if f.get("source") == "client-docs":
        for i, a in enumerate(f.get("args") or [], 1):
            an = _arg(a.get("Name"), i)
            params.append(an)
            opt = "?" if a.get("Nilable") or "Default" in a else ""
            d = (" Default: %s." % json.dumps(a["Default"])) if "Default" in a else ""
            lines.append("---@param %s%s %s%s" % (an, opt, types.lua(a), (" " + ((a.get("doc") or "") + d).strip()).rstrip()))
        for i, r in enumerate(f.get("returns") or [], 1):
            lines.append("---@return %s%s %s" % (types.lua(r), "?" if r.get("Nilable") else "", _arg(r.get("Name"), i)))
    else:
        params.append("...")
        lines.append("---@param ... any")
        lines.append("---@return any ...")
    lines.append("function %s(%s) end" % (name, ", ".join(params)))
    lines.append("")


def write(model, out):
    lib = os.path.join(out, "library")
    if os.path.isdir(lib):
        shutil.rmtree(lib)
    os.makedirs(lib)
    types = Types(model)
    seen, forbidden = _secret_seen(model), _forbidden(model)
    reloc = {r["old"]: r for r in model.get("relocated") or []}
    head = ["---@meta", "-- Generated by ForeverAPI (tools/apidoc.py luals) from WoW Forever client %s. Do not edit." %
            (model.get("meta") or {}).get("key", model.get("client_version")), ""]
    files = {}

    def file_for(name):
        return files.setdefault(name, list(head))

    namespaces = set()
    for key in sorted(model["functions"]):
        f = model["functions"][key]
        if f.get("status") == "not-in-game" and not f.get("namespace"):
            continue  # a documented global the game doesn't have: leave it undefined, so LuaLS warns
        ns = f.get("namespace")
        if ns and not NAME.match(str(f.get("name"))):
            continue
        if ns and ns not in namespaces:
            namespaces.add(ns)
            file_for(ns).extend(["%s = {}" % ns, ""])
        r = reloc.get(key)
        moved = [n["name"] for n in r["new"] if n["in_game"] == "yes"] if r and r["where"] == "shim" else None
        _fn(file_for(ns or f.get("system") or "Globals"), types, f, _notes(f, seen, forbidden, moved), deprecated=bool(moved))

    # classic names Forever dropped: declared deprecated, so VS Code strikes them through and says where they went
    gone = file_for("ClassicGone")
    for r in model.get("relocated") or []:
        if r["where"] != "missing":
            continue
        new = [n["name"] for n in r["new"] if n["in_game"] == "yes"]
        if "." in r["old"]:
            head_, rest = r["old"].split(".", 1)
            if head_ not in namespaces and head_ not in ("math", "string", "table", "bit", "os", "debug", "coroutine"):
                gone.append("%s = %s or {}" % (head_, head_))
                namespaces.add(head_)
        gone.append("---**Gone on Forever**: calling this errors.%s" % (" Use `%s`." % "` or `".join(new) if new else ""))
        if r.get("change"):
            gone += ["---", "---" + r["change"].replace("\n", " ")]
        if r.get("classic"):
            gone += ["---", "---Classic: `%s`" % r["classic"]]
        gone += ["---@deprecated", "function %s(...) end" % r["old"], ""]

    # structures
    cl = file_for("Structures")
    for name in sorted(model["structures"]):
        t = model["structures"][name]
        if t.get("kind") != "Structure":
            continue
        cl.append("---@class %s" % name)
        for fld in t.get("fields") or []:
            if NAME.match(str(fld.get("Name"))):
                cl.append("---@field %s%s %s" % (fld["Name"], "?" if fld.get("Nilable") else "", types.lua(fld)))
        cl.append("")

    # enums and constants, with the values the game reported
    en = file_for("Enums")
    en += ["Enum = {}", "Constants = {}", ""]
    for name in sorted(model["enums"]):
        t = model["enums"][name]
        if not NAME.match(name) or t.get("status") == "not-in-game":
            continue
        root = "Enum" if t.get("kind") == "Enumeration" else "Constants"
        vals = {}
        for fld in t.get("fields") or []:
            v = fld.get("EnumValue", fld.get("Value"))
            if NAME.match(str(fld.get("Name"))) and isinstance(v, (int, float)):
                vals[fld["Name"]] = v
        for k, v in (t.get("game") or {}).items():
            if NAME.match(str(k)) and isinstance(v, str) and v.startswith("n:") and k not in vals:
                try:
                    vals[k] = float(v[2:]) if "." in v else int(v[2:])
                except ValueError:
                    pass
        if root == "Enum":
            en.append("---@enum Enum.%s" % name)
        en.append("%s.%s = {" % (root, name))
        en += ["  %s = %s," % (k, v) for k, v in sorted(vals.items(), key=lambda kv: kv[1])]
        en += ["}", ""]

    # events: an alias so RegisterEvent completes names, with each event's payload in the hover
    ev = file_for("Events")
    names = sorted(k for k, e in model["events"].items() if e.get("status") in ("verified", "undocumented"))
    ev.append("---@alias ForeverEvent")
    for k in names:
        e = model["events"][k]
        pay = ", ".join("%s: %s" % (p.get("Name"), types.lua(p)) for p in e.get("payload") or [])
        sig = ((e.get("live") or {}).get("sigs") or {})
        secret = any("S" in s.split(",") for s in sig)
        note = (" (secret args seen)" if secret else "") + ("" if e.get("status") == "verified" else " (undocumented)")
        ev.append("---| %s # %s%s" % (json.dumps(k), pay or "no payload", note))
    ev.append("")

    # widgets: each type the probe created, with the documented methods it has
    wd = file_for("Widgets")
    wd += ["---@alias UnitToken string", ""]
    for wt in sorted(model["widgets"]):
        w = model["widgets"][wt]
        if not NAME.match(wt):
            continue
        wd.append("---@class %s" % wt)
        wd.append("local %s = {}" % wt)
        wd.append("")
        for m, rec in sorted(w["methods"].items()):
            d = rec.get("doc")
            if not NAME.match(str(m)):
                continue
            if d:
                fake = dict(d, key=m, source="client-docs", status="verified")
                _fn(wd, types, fake, _notes(fake, {}, set(), None), qual="%s:%s" % (wt, m))
            else:
                wd += ["---@param ... any", "---@return any ...", "function %s:%s(...) end" % (wt, m), ""]

    # Lua differences: math.randomseed is gone
    lua = file_for("LuaEnvironment")
    libs = model.get("tables") or {}
    if isinstance(libs.get("math"), dict) and "randomseed" not in libs["math"]:
        lua += ["---**Gone on Forever**: add-ons can't seed the random generator. `math.random` still works.",
                "---@deprecated", "function math.randomseed(...) end", ""]

    # types Blizzard's docs name but never define: aliases, so hovers show the name
    al = file_for("Aliases")
    for t in sorted(types.unknown):
        if NAME.match(t):
            al.append("---@alias %s any" % t)
    al.append("")

    for name, lines in files.items():
        lines = [CTRL.sub(" ", ln) for ln in lines]
        with open(os.path.join(lib, "%s.lua" % name.replace(".", "_")), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines))
    rc = {"$schema": "https://raw.githubusercontent.com/LuaLS/vscode-lua/master/setting/schema.json",
          "runtime.version": "Lua 5.1", "workspace.library": [os.path.abspath(lib).replace("\\", "/")],
          "diagnostics.globals": ["SLASH_*"], "workspace.checkThirdParty": False}
    with open(os.path.join(out, ".luarc.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(rc, f, indent=2)
    return len(files)
