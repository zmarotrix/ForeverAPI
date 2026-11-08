"""Run the three background collectors (ApiWatch, ApiTimeline, ApiWidgets) in the stub client from test_probe.py,
then import their SavedVariables and build the site from them.

    python tools/test_collectors.py

Proves they can't error, never store a value (a player name, a secret, an event argument), skip what they must, and
that the tools read what they write. It says nothing about the real client.
"""

import os
import shutil
import sys
import tempfile

from lupa import lua51

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import test_probe  # noqa: E402

EXTRA = r"""
INSTANCE = "none"
for _, e in ipairs({ "ENCOUNTER_START", "ENCOUNTER_END", "PLAYER_ENTERING_WORLD", "ZONE_CHANGED_NEW_AREA",
  "PLAYER_REGEN_ENABLED", "GROUP_ROSTER_UPDATE", "CHALLENGE_MODE_START", "CHALLENGE_MODE_COMPLETED",
  "PVP_MATCH_ACTIVE", "PVP_MATCH_COMPLETE", "UNIT_HEALTH" }) do VALID[e] = true end
function IsInInstance() return INSTANCE ~= "none", INSTANCE end
TARGET = true
function UnitExists(u) return u == "player" or (u == "target" and TARGET) or u == "nameplate3" end
function UnitIsPlayer(u) return u == "player" end
function UnitCanAttack(_, u) return u == "target" or u == "nameplate3" end
function UnitInRange() return SECRET end
function UnitHealth() return SECRET end -- like the real client: secret even out of combat
function UnitTargetLevel(u) if COMBAT and u ~= "player" then return SECRET end return 60 end
function GetFancyCrash() error("must never be called: crasher") end
function GetRefusedThing() error("must never be called: refused") end
function SetEverything() error("must never be called: not a getter") end
NOW = 100
function GetTime() return NOW end
function GetTimePreciseSec() return NOW end
GameFontNormal = {}
local m = getmetatable(CreateFrame("Frame")).__index
function m:SetFontObject() end
function m:SetValue(v) if issecretvalue(v) then error("SetValue: secret values are not allowed") end end
function m:SetAlphaFromBoolean(b) end
function m:SetShown(b) if issecretvalue(b) then error("SetShown: no secrets") end end
function m:SetText(t) if issecretvalue(t) then error("SetText: can't take a secret") end end
function m:SetWidth(w) end
C_RestrictedActions.IsAddOnRestrictionActive = function(t) return (COMBAT and t == 0) or (INSTANCE ~= "none" and t == 1) end
"""

LEADS = r"""
ApiProbeLeads = { build = "1.60.1.70862", events = {},
  calls = { { nil, "UnitHealth", "unit" }, { nil, "UnitTargetLevel", "unit" }, { nil, "GetFancyCrash" },
            { nil, "GetRefusedThing" }, { nil, "GetBuildInfo" }, { "C_Missing", "GetNothing" } },
  crashers = { GetFancyCrash = true }, refused = { GetRefusedThing = true },
  undocumented = { "SetEverything", "UnitName" }, documented = {}, uiGetters = {},
}
ApiWidgetsPlan = { build = "1.60.1.70862", setters = {
  { "StatusBar", "SetValue", { "Sn" } }, { "Texture", "SetAlphaFromBoolean", { "Sb" } },
  { "FontString", "SetText", { "Sn" } }, { "Frame", "SetWidth", { "Sn" } }, { "Frame", "SetShown", { "Sb" } } } }
"""

passed = failed = 0


def check(name, ok, detail=""):
    global passed, failed
    if ok:
        passed += 1
        print("PASS", name)
    else:
        failed += 1
        print("FAIL", name, detail)


def load(lua, addon, files):
    for f in files:
        with open(os.path.join(ROOT, "addon", addon, f), encoding="utf-8") as h:
            lua.execute("local f = assert(loadstring(...)); f(select(2, ...))", h.read(), addon)


def main():
    lua = lua51.LuaRuntime(unpack_returned_tuples=True)
    stub = test_probe.STUB.replace('KNOWN = { Frame = true, Button = true, EditBox = true, Cooldown = true, ModelScene = true }',
                                   'KNOWN = { Frame = true, Button = true, EditBox = true, Cooldown = true, ModelScene = true, StatusBar = true }')
    lua.execute(stub)
    lua.execute(EXTRA)
    lua.execute(LEADS)
    load(lua, "ApiWatch", ["watch.lua"])
    load(lua, "ApiTimeline", ["timeline.lua"])
    load(lua, "ApiWidgets", ["widgets.lua"])
    G = lua.globals()
    for addon in ("ApiWatch", "ApiTimeline", "ApiWidgets"):
        G.Fire("ADDON_LOADED", addon)
    G.Fire("PLAYER_LOGIN")
    G.Fire("PLAYER_ENTERING_WORLD", True, False)
    G.RunTimers()

    def tick(n, step=0.2):
        for _ in range(n):
            lua.execute("NOW = NOW + %s" % step)
            lua.execute("for _, f in ipairs(FRAMES) do if f.scripts.OnUpdate then f.scripts.OnUpdate(f, %s) end end" % step)

    tick(60)
    G.Fire("CHAT_MSG_SAY", "hello Maro", "Maro-Forever")
    G.Fire("UNIT_AURA", "party1target", lua.eval("SECRET"))
    lua.execute("COMBAT = true")
    G.Fire("PLAYER_REGEN_DISABLED")
    G.Fire("UNIT_HEALTH", "target")
    tick(60)
    lua.execute("COMBAT = false")
    G.Fire("PLAYER_REGEN_ENABLED")
    lua.execute('INSTANCE = "party"')
    G.Fire("PLAYER_ENTERING_WORLD", False, False)
    G.Fire("ENCOUNTER_START", 1, "Boss", 1, 5)
    lua.execute("COMBAT = true")
    tick(80)
    lua.execute("COMBAT = false")
    G.Fire("ENCOUNTER_END", 1, "Boss", 1, 5, 1)
    tick(40)
    for cmd in ("APIWATCH", "APITIMELINE", "APIWIDGETS"):
        G.SlashCmdList[cmd]("")
    svs = {name: "%s = %s\n" % (name, lua.eval("Serialize(%s)" % name)) for name in ("ApiWatchDB", "ApiTimelineDB", "ApiWidgetsDB")}
    allsv = "".join(svs.values())
    printed = "\n".join(G.PRINTED.values())
    check("all three printed a status", all(s in printed for s in ("API watch", "API timeline", "API widgets")), printed)
    check("never stores the player's name", "Maro" not in allsv)
    check("never calls a crasher, a refused call or a non-getter", "must never be called" not in allsv)

    from luatable import parse_assignments
    w = parse_assignments(svs["ApiWatchDB"])["ApiWatchDB"]
    sits = w["situations"]
    check("watch: open-world target run", "target: enemy npc" in sits.get("none/idle", {}).get("runs", {}), list(sits))
    check("watch: open-world plain getters left to the probe", "getters" not in sits.get("none/idle", {}).get("runs", {}))
    check("watch: dungeon boss situation seen", "party/boss" in sits, list(sits))
    boss = sits.get("party/boss", {}).get("runs", {})
    check("watch: getters run in the boss fight", "getters" in boss, list(boss))
    g = boss.get("getters", {}).get("results", {})
    check("watch: crasher skipped", g.get("GetFancyCrash", {}).get("skipped") == "crashed the client", g.get("GetFancyCrash"))
    check("watch: refused skipped", g.get("GetRefusedThing", {}).get("skipped") == "refused to the probe")
    check("watch: non-getter skipped", "SetEverything" not in g or g["SetEverything"].get("skipped") == "not a getter")
    t = boss.get("target: enemy npc", {}).get("results", {})
    check("watch: target secret in the boss fight", t.get("UnitTargetLevel", {}).get(1) == "secret:table", t.get("UnitTargetLevel"))
    check("watch: nameplate kind recorded", any(k.startswith("nameplate") for s in sits.values() for k in s["runs"]))
    tr = w["transitions"]
    tr = list(tr.values()) if isinstance(tr, dict) else tr
    check("watch: restriction switches logged", any("Combat" in str(x.get("on")) for x in tr) and any(str(x.get("situation")).startswith("party/") and "Encounter" in str(x.get("on")) for x in tr), tr[:3])

    tl = parse_assignments(svs["ApiTimelineDB"])["ApiTimelineDB"]["traces"]
    check("timeline: login traced", "login" in tl, list(tl))
    check("timeline: combat start traced", "combat start" in tl, list(tl))
    cs = tl.get("combat start", {})
    cs = list(cs.values()) if isinstance(cs, dict) else cs
    evs = cs[0]["events"] if cs else {}
    evs = list(evs.values()) if isinstance(evs, dict) else evs
    names = [e[2] if isinstance(e, dict) else e[1] for e in evs]
    check("timeline: the second before is kept", "UNIT_AURA" in names, names)
    check("timeline: unit tokens kept, other args not", "party1target" in str(evs) and "hello" not in allsv)

    wd = parse_assignments(svs["ApiWidgetsDB"])["ApiWidgetsDB"]["runs"]
    o, c = wd.get("outside", {}), wd.get("combat", {})
    check("widgets: out-of-combat run done", o.get("done") is True, o)
    check("widgets: combat run done", c.get("done") is True, c)
    check("widgets: secret refused by SetValue", "not allowed" in str(o["setters"]["StatusBar:SetValue"].get("secret")), o["setters"]["StatusBar:SetValue"])
    check("widgets: plain control ok", o["setters"]["StatusBar:SetValue"].get("plain") == "ok")
    check("widgets: true/false control call is plain", o["setters"]["Frame:SetShown"].get("plain") == "ok" and "no secrets" in str(o["setters"]["Frame:SetShown"].get("secret")), o["setters"].get("Frame:SetShown"))
    check("widgets: secret boolean accepted", o["setters"]["Texture:SetAlphaFromBoolean"].get("secret") == "ok")
    check("widgets: arithmetic on a secret errors in the stub", o["ops"]["s + 1"] != "ok")

    # tools: import and build from these SavedVariables
    import apidoc
    tmp = tempfile.mkdtemp(prefix="collectors-test-")
    try:
        sv_dir = os.path.join(tmp, "game", "WTF", "Account", "1", "SavedVariables")
        os.makedirs(sv_dir)
        for name, text in (("ApiWatch", svs["ApiWatchDB"]), ("ApiTimeline", svs["ApiTimelineDB"]), ("ApiWidgets", svs["ApiWidgetsDB"])):
            with open(os.path.join(sv_dir, name + ".lua"), "w", encoding="utf-8") as f:
                f.write(text)
        apidoc.GAME = os.path.join(tmp, "game")
        apidoc.DUMPS = os.path.join(tmp, "dumps")
        apidoc.DOCS = os.path.join(tmp, "docs")
        apidoc.SITE = os.path.join(tmp, "site")
        apidoc.import_collectors()
        check("import: three collector files", all(apidoc.latest_dump(p) for p in ("watch", "timeline", "widgets")))
        tlj = apidoc._load_json(apidoc.latest_dump("timeline"))
        first = next(iter(tlj["traces"].values()))[0]["events"][0]
        check("import: timeline events are plain lists", isinstance(first, list) and len(first) == 5, first)
        apidoc.cmd_build()
        with open(os.path.join(tmp, "site", "data.js"), encoding="utf-8") as f:
            data = f.read()
        check("site data carries all three", '"watch":{' in data and '"timeline":{' in data and '"secrets":{' in data)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("failed: %d" % failed)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
