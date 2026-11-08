"""Write the merged model as Markdown pages (docs/) plus api.json."""

import json
import os
import re
import shutil
from collections import defaultdict

BADGE = {"verified": "✅ verified", "undocumented": "🆕 in game, not in Blizzard's docs",
         "not-in-game": "⛔ in Blizzard's docs, not in game", "unverified": "❔ unverified"}
SHORT = {"verified": "✅", "undocumented": "🆕", "not-in-game": "⛔", "unverified": "❔"}
FN_KIND = {"fC": "built-in", "fL": "Lua", "f?": "function"}
# Flags that matter to an add-on author, with plain words.
FLAG_WORDS = {
    "IsProtectedFunction": "protected: only Blizzard's secure code may call it",
    "HasRestrictions": "restricted in some situations",
    "SecretArguments": "secret arguments: {v}",
    "SecretReturns": "always returns secret values",
    "SecretWhenInCombat": "returns secrets in combat",
    "SecretWhenUnitAuraRestricted": "secret while unit auras are restricted",
    "SecretWhenUnitStatsRestricted": "secret while unit stats are restricted",
    "SecretWhenUnitIdentityRestricted": "secret while unit identity is restricted",
    "SecretWhenUnitSpellCastRestricted": "secret while unit spellcasts are restricted",
    "SecretWhenUnitPowerRestricted": "secret while unit power is restricted",
    "SecretWhenCooldownsRestricted": "secret while cooldowns are restricted",
    "SecretWhenEncounterEvent": "secret during encounter events",
    "SecretInChatMessagingLockdown": "secret during chat lockdown",
    "ConditionalSecret": "secret in some conditions",
    "ReturnsNeverSecret": "never returns secrets",
    "SynchronousEvent": "fires synchronously",
    "UniqueEvent": "unique event",
    "MayReturnNothing": "may return nothing",
}


def slug(s):
    return re.sub(r"[^A-Za-z0-9_.-]", "_", str(s))


def _type(p):
    t = p.get("Type", "?")
    if t == "table" and p.get("InnerType"):
        t = p["InnerType"] + "[]"
    return t + ("?" if p.get("Nilable") else "")


def signature(f):
    args = ", ".join("%s: %s" % (a.get("Name"), _type(a)) + (" = %s" % a["Default"] if "Default" in a else "")
                     for a in f.get("args") or [])
    rets = ", ".join("%s: %s" % (r.get("Name"), _type(r)) for r in f.get("returns") or [])
    return "%s(%s)%s" % (f["key"], args, (" → " + rets) if rets else "")


def flags_text(flags):
    out = []
    for k, v in sorted((flags or {}).items()):
        if v is False:
            continue
        w = FLAG_WORDS.get(k)
        if w:
            out.append(w.format(v=v))
        else:
            out.append(k if v is True else "%s: %s" % (k, v))
    return out


def call_text(rec):
    if not rec:
        return None
    if rec.get("skipped"):
        return ("💥 " if "crash" in rec["skipped"] else "") + "not called: %s" % rec["skipped"]
    if rec.get("forbidden"):
        return "⛔ protected: calling it raised ADDON_ACTION_FORBIDDEN"
    if rec.get("missing"):
        return "missing at call time"
    if "error" in rec:
        return "error: `%s`" % rec["error"].replace("`", "'")
    n = rec.get("n", 0)
    vals = rec.get("returns") or []
    return "returned %d value%s%s" % (n, "" if n == 1 else "s", (": " + ", ".join("`%s`" % v for v in vals)) if vals else "")


def write(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def fn_block(f):
    lines = ["### %s" % f["key"], "", "`%s`" % (signature(f) if f.get("source") == "client-docs" else f["key"] + "(...)"), ""]
    lines.append("- Status: %s" % BADGE[f["status"]] + (" (%s)" % FN_KIND.get(f.get("game"), f.get("game"))
                                                         if f.get("game") else ""))
    if f.get("replaced_by"):
        lines.append("- ⚠️ Replaced by the add-on **%s** when dumped." % f["replaced_by"])
    if f.get("doc"):
        lines.append("- Blizzard: %s" % f["doc"])
    for a in (f.get("args") or []) + (f.get("returns") or []):
        if a.get("doc"):
            lines.append("- `%s`: %s" % (a.get("Name"), a["doc"]))
    for t in flags_text(f.get("flags")):
        lines.append("- %s (Blizzard's docs; not checked in game)" % t)
    o, c = call_text(f.get("outside")), call_text(f.get("combat"))
    if o:
        arg = f["outside"].get("arg")
        lines.append("- Called out of combat%s: %s" % ((" with `%s`" % ("player" if arg == "unit" else arg)) if arg else "", o))
    if c:
        lines.append("- Called in combat: %s" % c)
    if f.get("web"):
        w = f["web"]
        lines.append("- Web lead (unverified, [%s](%s)): %s" % (w.get("site", "source"), w.get("url", ""), w.get("text", "")))
    if f.get("used_by"):
        lines.append("- Used by Blizzard's UI in `%s`" % f["used_by"])
    if f.get("source") == "client-docs":
        lines.append("- Source: client docs `%s`" % f.get("file"))
    lines.append("")
    return lines


def render(model, out, generated):
    if os.path.isdir(out):
        for sub in ("systems", "widgets"):
            shutil.rmtree(os.path.join(out, sub), ignore_errors=True)
    os.makedirs(out, exist_ok=True)
    meta = model["meta"]
    fns, events, enums = model["functions"], model["events"], model["enums"]

    # group functions and tables by page
    pages = defaultdict(lambda: {"functions": [], "events": [], "tables": [], "ns": None})
    ns_page = {}
    for f in fns.values():
        if f.get("system"):
            ns_page.setdefault(f.get("namespace"), f["system"]) if f.get("namespace") else None
    for f in fns.values():
        page = f.get("system") or (ns_page.get(f["namespace"]) if f.get("namespace") else None)
        if not page:
            page = f["namespace"] if f.get("namespace") else "_undocumented_globals"
        pages[page]["functions"].append(f)
        pages[page]["ns"] = pages[page]["ns"] or f.get("namespace")
    for e in events.values():
        pages[e.get("system") or "_undocumented_events"]["events"].append(e)
    for name, t in list(enums.items()) + list(model["structures"].items()):
        if t.get("system"):
            pages[t["system"]]["tables"].append(dict(t, key=name))

    def page_path(name):
        return "systems/%s.md" % slug(name)

    for name, p in pages.items():
        if name.startswith("_"):
            continue
        lines = ["# %s" % name, ""]
        if p["ns"]:
            lines += ["Namespace: `%s`" % p["ns"], ""]
        counts = defaultdict(int)
        for f in p["functions"]:
            counts[f["status"]] += 1
        if p["functions"]:
            lines += ["## Functions", "", "| | Function | Out of combat | In combat |", "|---|---|---|---|"]
            for f in sorted(p["functions"], key=lambda f: f["key"]):
                lines.append("| %s | [%s](#%s) | %s | %s |" % (SHORT[f["status"]], f["key"], slug(f["key"]).lower().replace(".", ""),
                                                             _cell(f.get("outside")), _cell(f.get("combat"))))
            lines.append("")
            for f in sorted(p["functions"], key=lambda f: f["key"]):
                lines += fn_block(f)
        if p["events"]:
            lines += ["## Events", ""]
            for e in sorted(p["events"], key=lambda e: e["key"]):
                lines += event_block(e)
        if p["tables"]:
            lines += ["## Types", ""]
            for t in sorted(p["tables"], key=lambda t: t["key"]):
                lines += table_block(t)
        write(os.path.join(out, page_path(name)), lines)

    # undocumented globals
    allund = pages["_undocumented_globals"]["functions"]
    ui = sorted((f for f in allund if f.get("ui_lua") or f.get("game") == "fL"), key=lambda f: f["key"])
    und = sorted((f for f in allund if not (f.get("ui_lua") or f.get("game") == "fL")), key=lambda f: f["key"])
    uil = ["# Blizzard UI functions", "",
           "Global functions written in Lua by Blizzard's own UI code (FrameXML and the Blizzard_ add-ons). They exist "
           "in game, but they're UI helpers that can change with any patch, not client API.", ""]
    for f in ui:
        uil.append("- `%s`%s" % (f["key"], (" (`%s`)" % f["ui_lua"]) if f.get("ui_lua") else ""))
    write(os.path.join(out, "ui-functions.md"), uil)
    lines = ["# Global functions Blizzard's docs don't list", "",
             "In the game (the dump saw them) but in no generated doc file and not written in Blizzard's Lua UI code: "
             "Forever additions or legacy client APIs. Signatures come only from what the probe saw: its no-argument "
             "call often answers with a `Usage:` error. Blizzard's own Lua helpers are in [ui-functions](ui-functions.md).", ""]
    letter = None
    for f in und:
        if f["key"][0].upper() != letter:
            letter = f["key"][0].upper()
            lines += ["## %s" % letter, ""]
        bits = [FN_KIND.get(f.get("game"), "")]
        o = call_text(f.get("outside"))
        if o:
            bits.append(o)
        c = call_text(f.get("combat"))
        if c and c != o:
            bits.append("in combat " + c)
        if f.get("used_by"):
            bits.append("used in `%s`" % f["used_by"])
        lines.append("- `%s`: %s" % (f["key"], "; ".join(b for b in bits if b)))
    write(os.path.join(out, "globals-undocumented.md"), lines)

    # events index
    lines = ["# Events", "", "Checked with %s. Payloads are Blizzard's; \"seen\" counts and argument kinds are what "
             "fired while the probe was on (n number, s string, b boolean, t table, S secret, - nil)." %
             (model.get("event_check_method") or "nothing yet (no dump)"), "",
             "| | Event | Seen | Argument kinds seen | Page |", "|---|---|---|---|---|"]
    for e in sorted(events.values(), key=lambda e: e["key"]):
        live = e.get("live") or {}
        sigs = live.get("sigs") or {}
        lines.append("| %s | `%s`%s | %s | %s | %s |" % (
            SHORT[e["status"]], e["key"], " (protected)" if (e.get("check") or {}).get("register") in ("forbidden", "blocked") else "", live.get("n", ""), " / ".join("`%s`" % s for s in sigs) if sigs else "",
            "[%s](%s)" % (e["system"], page_path(e["system"])) if e.get("system") else (
                "used in `%s`" % e["used_by"] if e.get("used_by") else "")))
    write(os.path.join(out, "events.md"), lines)

    # enums index
    lines = ["# Enums and constants", "", "| | Name | Kind | Values that differ in game | Page |", "|---|---|---|---|---|"]
    for t in sorted(enums.values(), key=lambda t: t["key"]):
        mm = ", ".join("%s: docs %s, game %s" % m for m in t.get("mismatches", [])[:6])
        lines.append("| %s | `%s` | %s | %s | %s |" % (SHORT[t["status"]], t["key"], t.get("kind"), mm,
                                                     "[%s](%s)" % (t["system"], page_path(t["system"])) if t.get("system") else ""))
    und_enums = [t for t in enums.values() if t["status"] == "undocumented"]
    for t in sorted(und_enums, key=lambda t: t["key"]):
        lines += ["", "## %s (game only)" % t["key"], ""]
        for k, v in sorted((t.get("game") or {}).items(), key=lambda kv: str(kv[1])):
            lines.append("- `%s` = %s" % (k, _val(v)))
    write(os.path.join(out, "enums.md"), lines)

    # widgets
    widx = ["# Widgets", "", "One object of each type was created in game and its metatable read.", "",
            "| Type | Methods | Scripts |", "|---|---|---|"]
    for wtype, w in sorted(model["widgets"].items()):
        if w.get("error"):
            widx.append("| %s | not creatable: `%s` | |" % (wtype, w["error"]))
            continue
        widx.append("| [%s](widgets/%s.md) | %d | %d |" % (wtype, slug(wtype), len(w["methods"]), len(w["scripts"])))
        lines = ["# %s" % wtype, "", "Object type reported: `%s`" % w.get("objectType"), "",
                 "Script handlers: " + (", ".join("`%s`" % s for s in w["scripts"]) or "none found"), "", "## Methods", ""]
        for m, rec in sorted(w["methods"].items()):
            d = rec.get("doc")
            if d:
                sig = signature(dict(d, key=m))
                extra = "; ".join(flags_text(d.get("flags")))
                lines.append("- ✅ `%s`%s%s" % (sig, (" — " + d["doc"]) if d.get("doc") else "", (" (" + extra + ")") if extra else ""))
            else:
                lines.append("- 🆕 `%s` (%s, no Blizzard doc)" % (m, FN_KIND.get(rec.get("game"), rec.get("game"))))
        write(os.path.join(out, "widgets", slug(wtype) + ".md"), lines)
    write(os.path.join(out, "widgets.md"), widx)

    # cvars
    lines = ["# CVars and console commands", "", "From `C_Console.GetAllCommands` in game. Defaults only; the probe never reads current values.", "",
             "| Name | Default | Category | Help |", "|---|---|---|---|"]
    for name, c in sorted(model["cvars"].items(), key=lambda kv: str(kv[0]).lower()):
        if not isinstance(c, dict):
            lines.append("| %s | | | %s |" % (name, c))
            continue
        lines.append("| `%s` | %s | %s | %s |" % (name, "`%s`" % c["default"] if c.get("default") not in (None, "") else "",
                                                 c.get("category", ""), str(c.get("help") or "").replace("|", "/")))
    write(os.path.join(out, "cvars.md"), lines)

    # restrictions: what changed in combat, what got blocked
    lines = ["# Restrictions seen in game", ""]
    cm = model["calls_meta"]
    for p in ("outside", "combat"):
        r = cm.get(p) or {}
        lines.append("- %s combat run: %s; restrictions active at start: %s" % (
            "Out of" if p == "outside" else "In", "done" if r.get("done") else ("partial" if r else "not run"),
            _restr(r.get("restrictions"))))
    lines += ["", "## Getters that answered differently in combat", "", "| Function | Out of combat | In combat |", "|---|---|---|"]
    for f in sorted(fns.values(), key=lambda f: f["key"]):
        o, c = f.get("outside"), f.get("combat")
        if o and c and _strip(o) != _strip(c):
            lines.append("| `%s` | %s | %s |" % (f["key"], call_text(o), call_text(c)))
    lines += ["", "## Always secret", "", "Getters whose every return was secret even out of combat.", ""]
    for f in sorted(fns.values(), key=lambda f: f["key"]):
        o = f.get("outside")
        if o and o.get("returns") and all(str(v).startswith("secret") for v in o["returns"]):
            lines.append("- `%s`" % f["key"])
    lines += ["", "## Blocked actions", ""]
    for b in model["blocked"]:
        lines.append("- %s: `%s` during `%s`%s" % (b.get("event"), b.get("fn"), b.get("during"), " (combat)" if b.get("combat") else ""))
    if not model["blocked"]:
        lines.append("None recorded.")
    lines += ["", "## Documented restriction flags", "", "How many documented functions carry each flag (Blizzard's docs, not checked in game).", ""]
    counts = defaultdict(int)
    for f in fns.values():
        for k, v in (f.get("flags") or {}).items():
            if v not in (False, None) and (k.startswith("Secret") or k.startswith("Requires") or k in ("HasRestrictions", "IsProtectedFunction")):
                counts[k] += 1
    for k, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        lines.append("- `%s`: %d" % (k, n))
    write(os.path.join(out, "restrictions.md"), lines)

    # Lua environment
    lines = ["# Lua environment", "", "Lua version: `%s`" % meta.get("lua", "?"), "",
             "How `tostring` shows a built-in function: `%s`; a Lua function: `%s`" % (meta.get("fnPrint", "?"), meta.get("fnPrintLua", "?")), ""]
    lowers = sorted(k for k, v in model["globals"].items() if _is_fn(v) and k[:1].islower())
    lines += ["## Lower-case global functions", "", ", ".join("`%s`" % k for k in lowers) or "none (no dump)", ""]
    for lib in ("string", "table", "math", "bit", "coroutine", "debug", "os"):
        m = model["tables"].get(lib)
        if isinstance(m, dict):
            lines += ["## %s" % lib, "", ", ".join("`%s`" % k for k in sorted(map(str, m))), ""]
    write(os.path.join(out, "lua.md"), lines)

    # index
    def tally(items):
        c = defaultdict(int)
        for i in items:
            c[i["status"]] += 1
        return c
    tf, te, tn = tally(fns.values()), tally(events.values()), tally(enums.values())
    lines = ["# WoW Forever add-on API", "",
             "Generated %s by `tools/apidoc.py build`. Do not edit by hand." % generated, "",
             "- Client docs: Blizzard_APIDocumentationGenerated from client %s" % model.get("client_version"),
             "- Game dump: %s" % ("ApiProbe %s on %s (interface %s), %s" % (meta.get("probe"), meta.get("key"), meta.get("toc"), meta.get("locale"))
                                  if meta else "**none yet: everything below is unverified**"), "",
             "Statuses: " + "; ".join(BADGE.values()), "",
             "| | Functions | Events | Enums and constants |", "|---|---|---|---|"]
    for s in ("verified", "undocumented", "not-in-game", "unverified"):
        lines.append("| %s | %d | %d | %d |" % (BADGE[s], tf[s], te[s], tn[s]))
    lines += ["", "Rule: only ✅ and 🆕 were confirmed in game. Flags such as \"restricted\" or \"secret\" quoted from Blizzard's docs "
              "are leads until a probe call shows them; see [restrictions](restrictions.md) for what the probe saw.", "",
              "## Pages", "", "- [Events](events.md)", "- [Enums and constants](enums.md)", "- [Widgets](widgets.md)",
              "- [Undocumented global functions](globals-undocumented.md)", "- [Restrictions seen in game](restrictions.md)",
              "- [CVars](cvars.md)", "- [Lua environment](lua.md)", "- [Moved from classic](relocated.md)", "- [Reported quirks, checked](checks.md)", "- [Changes between dumps](changes/)", "",
              "## Systems", "", "| System | Namespace | ✅ | 🆕 | ⛔ | ❔ |", "|---|---|---|---|---|---|"]
    for name, p in sorted(pages.items()):
        if name.startswith("_"):
            continue
        c = tally(p["functions"])
        lines.append("| [%s](%s) | %s | %d | %d | %d | %d |" % (name, page_path(name), "`%s`" % p["ns"] if p["ns"] else "",
                                                               c["verified"], c["undocumented"], c["not-in-game"], c["unverified"]))
    if model["tainted"]:
        lines += ["", "## Left out", "", "Globals written by add-ons when the dump ran (not API):", ""]
        for who, names in sorted(model["tainted"].items()):
            n = len(names) if isinstance(names, (list, dict)) else 0
            lines.append("- %s: %d" % (who, n))
    write(os.path.join(out, "index.md"), lines)

    with open(os.path.join(out, "api.json"), "w", encoding="utf-8") as f:
        json.dump({k: v for k, v in model.items() if k not in ("globals", "tables")}, f, indent=0, sort_keys=True, default=str)


def _cell(rec):
    if not rec:
        return ""
    if rec.get("skipped"):
        return "💥 " + rec["skipped"]
    if rec.get("forbidden"):
        return "protected"
    if rec.get("missing"):
        return "missing"
    if "error" in rec:
        return "error"
    n = rec.get("n", 0)
    vals = [str(v) for v in rec.get("returns") or []]
    if vals and all(v.startswith("secret") for v in vals):
        return "secret"
    if any(v.startswith("secret") for v in vals):
        return "partly secret"
    return "%d value%s" % (n, "" if n == 1 else "s")


def _strip(rec):
    return {k: v for k, v in rec.items() if k not in ("from", "arg")}


def _restr(r):
    if not isinstance(r, dict):
        return r or "unknown"
    on = [k for k, v in r.items() if v is True]
    return ", ".join(sorted(on)) or "none"


def _is_fn(v):
    return isinstance(v, str) and v.startswith("f")


def _val(v):
    if isinstance(v, str) and v[:2] in ("n:", "s:", "b:"):
        return v[2:]
    return v


def event_block(e):
    lines = ["### %s" % e["key"], "", "- Status: %s" % BADGE[e["status"]]]
    if e.get("payload"):
        lines.append("- Payload: " + ", ".join("`%s: %s`" % (p.get("Name"), _type(p)) for p in e["payload"]))
    elif e.get("source") == "client-docs":
        lines.append("- Payload: none")
    if e.get("doc"):
        lines.append("- Blizzard: %s" % e["doc"])
    for t in flags_text(e.get("flags")):
        lines.append("- %s (Blizzard's docs)" % t)
    reg = (e.get("check") or {}).get("register")
    if reg in ("forbidden", "blocked"):
        lines.append("- ⛔ Add-ons may not register it: RegisterEvent raised ADDON_ACTION_FORBIDDEN")
    live = e.get("live")
    if live:
        lines.append("- Seen firing %s times (%s in combat); argument kinds: %s" % (
            live.get("n"), live.get("combat"), " / ".join("`%s`" % s for s in (live.get("sigs") or {}))))
    lines.append("")
    return lines


def table_block(t):
    lines = ["### %s" % t["key"], "", "- %s%s" % (t.get("kind"), (" — " + BADGE[t["status"]]) if t.get("status") else "")]
    if t.get("doc"):
        lines.append("- Blizzard: %s" % t["doc"])
    for fld in t.get("fields") or []:
        v = fld.get("EnumValue", fld.get("Value"))
        lines.append("  - `%s`%s%s" % (fld.get("Name"), (": " + _type(fld)) if t.get("kind") in ("Structure", "CallbackType") else "",
                                       (" = %s" % v) if v is not None else ""))
    for name, want, got in t.get("mismatches") or []:
        lines.append("- ⚠️ `%s`: docs say %s, game has %s" % (name, want, _val(got) if got else "nothing"))
    lines.append("")
    return lines
