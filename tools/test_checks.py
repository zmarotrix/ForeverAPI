"""Run ApiChecks in the stub client from test_probe.py, then import its SavedVariables and build from them.

    python tools/test_checks.py

Proves it can't error, never stores chat text or a player's name, never calls ResetAllCombatSessions, sends chat only
from /apichecks chat yes, and that the tools read what it writes. It says nothing about the real client.
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
for _, e in ipairs({ "PLAYER_DEAD", "MERCHANT_CLOSED", "MERCHANT_SHOW", "AUCTION_HOUSE_CLOSED", "AUCTION_HOUSE_SHOW",
  "UNIT_COMBAT", "COMBAT_LOG_MESSAGE", "COMBAT_TEXT_UPDATE", "DAMAGE_METER_COMBAT_SESSION_UPDATED",
  "PLAYER_ENTERING_WORLD", "ZONE_CHANGED_NEW_AREA", "LOADING_SCREEN_ENABLED", "LOADING_SCREEN_DISABLED",
  "UNIT_SPELLCAST_SUCCEEDED", "UNIT_SPELLCAST_SENT", "PLAYER_CONTROL_LOST", "PLAYER_CONTROL_GAINED",
  "PLAYER_UPDATE_RESTING", "PLAYER_FLAGS_CHANGED", "AUCTION_HOUSE_AUCTION_CREATED", "CHAT_MSG_SYSTEM", "UI_INFO_MESSAGE",
  "UI_ERROR_MESSAGE", "PLAYER_REGEN_DISABLED", "PLAYER_REGEN_ENABLED", "PLAYER_TARGET_CHANGED", "NAME_PLATE_UNIT_ADDED",
  "UNIT_PET", "CHAT_MSG_SAY", "CHAT_MSG_YELL", "CHAT_MSG_EMOTE" }) do VALID[e] = true end
-- DAMAGE_METER_RESET and DAMAGE_METER_CURRENT_SESSION_UPDATED left unknown: registering them must not break anything
NOW = 100
function GetTime() return NOW end
ZONE, SUB, MAP = "Elwynn Forest", "Goldshire", 1429
function GetZoneText() return ZONE end
function GetRealZoneText() return ZONE end
function GetSubZoneText() return SUB end
function GetMinimapZoneText() return SUB end
C_Map = { GetBestMapForUnit = function() return MAP end }
RESTING, AFK, TAXI, PET = false, false, false, true
function IsResting() return RESTING end
function UnitIsAFK() return AFK end
function UnitOnTaxi() return TAXI end
function UnitGUID(u) return u == "player" and "Player-1-0001" or "Creature-0-1" end
TARGET = "enemy"
function UnitExists(u) return u == "player" or (u == "pet" and PET) or (u == "target" and TARGET ~= nil) or u == "nameplate3" end
function UnitCanAttack(_, u) return (u == "target" and TARGET == "enemy") or u == "nameplate3" end
function UnitIsUnit(a, b)
  if a == "nameplate3" or b == "nameplate3" or ((a == "target" or b == "target") and TARGET == "enemy") then return SECRET end
  return a == b
end
function UnitHealth() return SECRET end
function UnitHealthMax(u) return u == "pet" and SECRET or 100 end
function UnitPower() return 50 end
function UnitPowerMax() return 100 end
function UnitIsDead() return false end
function IsInInstance() return INSTANCE ~= nil, INSTANCE end
ERR_EXHAUSTION_RESTED = "You feel rested."
ERR_EXHAUSTION_NORMAL = "You feel normal."
ERR_AUCTION_STARTED = "Auction created."
CLEARED_AFK = "You are no longer AFK."
MARKED_AFK = "You are now AFK."
MARKED_AFK_MESSAGE = "You are now AFK: %s"
WOW_PROJECT_ID, WOW_PROJECT_MAINLINE, WOW_PROJECT_CLASSIC, WOW_PROJECT_CAMELOT = 18, 1, 2, 18
CHATLINES = {}
DEFAULT_CHAT_FRAME = NewObject("Frame")
function DEFAULT_CHAT_FRAME:AddMessage(t) CHATLINES[#CHATLINES + 1] = t end
function hooksecurefunc(t, name, post)
  local orig = t[name]
  t[name] = function(...) local r = { orig(...) } post(...) return unpack(r) end
end
Enum.DamageMeterType = { DamageDone = 0, HealingDone = 2 }
Enum.DamageMeterSessionType = { Overall = 0, Current = 1 }
METER_RESET = false
C_DamageMeter = {
  IsDamageMeterAvailable = function() return true, "" end,
  GetAvailableCombatSessions = function() return { { sessionID = 7, name = "Fight" } } end,
  GetSessionDurationSeconds = function() return COMBAT and SECRET or 12 end,
  GetCombatSessionFromType = function() return { combatSources = { { sourceGUID = "Player-1-0001", totalAmount = COMBAT and SECRET or 100 } },
    maxAmount = COMBAT and SECRET or 100, totalAmount = COMBAT and SECRET or 100 } end,
  GetCombatSessionSourceFromType = function() return { combatSpells = {}, maxAmount = 1, totalAmount = 1 } end,
  GetCombatSessionFromID = function() return { combatSources = {} } end,
  ResetAllCombatSessions = function() METER_RESET = true end,
}
function GetCurrentCombatTextEventInfo() return SECRET, "Fire" end
SENT = {}
function SendChatMessage(text, chatType)
  if not HARDWARE and (chatType == "SAY" or chatType == "YELL") and INSTANCE == nil then
    Fire("ADDON_ACTION_BLOCKED", "ApiChecks", "SendChatMessage()")
    return
  end
  SENT[#SENT + 1] = chatType
  Fire("CHAT_MSG_" .. chatType, text, "Maro", "", "", "Maro", "", 0, 0, "", 0, 1, "Player-1-0001")
end
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


def main():
    lua = lua51.LuaRuntime(unpack_returned_tuples=True)
    lua.execute(test_probe.STUB)
    lua.execute(EXTRA)
    with open(os.path.join(ROOT, "addon", "ApiChecks", "checks.lua"), encoding="utf-8") as h:
        lua.execute("local f = assert(loadstring(...)); f(select(2, ...))", h.read(), "ApiChecks")
    G = lua.globals()
    run = G.RunTimers
    G.Fire("ADDON_LOADED", "ApiChecks")
    G.Fire("PLAYER_LOGIN")
    G.Fire("PLAYER_ENTERING_WORLD", True, False)
    run()

    # twice: a death that fires twice, a merchant close that fires once
    G.Fire("PLAYER_DEAD")
    lua.execute("NOW = NOW + 0.1")
    G.Fire("PLAYER_DEAD")
    G.Fire("MERCHANT_CLOSED")
    run()
    lua.execute("NOW = NOW + 10")

    # zone: hearth, loading screen, zone event while the text is still the old zone
    G.Fire("UNIT_SPELLCAST_SUCCEEDED", "player", "Cast-1", 8690)
    G.Fire("LOADING_SCREEN_ENABLED")
    G.Fire("ZONE_CHANGED_NEW_AREA")
    lua.execute('ZONE, SUB, MAP = "Stormwind City", "Trade District", 1453')
    G.Fire("LOADING_SCREEN_DISABLED")
    run()
    run()

    # chat: rested arrives as CHAT_MSG_SYSTEM; AFK off only in the chat frame; the auction message nowhere
    lua.execute("RESTING = true")
    G.Fire("PLAYER_UPDATE_RESTING")
    G.Fire("CHAT_MSG_SYSTEM", "You feel rested.", "")
    lua.execute("AFK = true")
    G.Fire("PLAYER_FLAGS_CHANGED", "player")
    lua.execute("AFK = false")
    G.Fire("PLAYER_FLAGS_CHANGED", "player")
    lua.execute('DEFAULT_CHAT_FRAME:AddMessage("|cffffff00You are no longer AFK.|r")')
    G.Fire("AUCTION_HOUSE_AUCTION_CREATED", 5)
    G.Fire("CHAT_MSG_SYSTEM", lua.eval("SECRET"), "")
    G.Fire("CHAT_MSG_SYSTEM", "Maro has come online.", "")

    # secrets and feed
    G.Fire("UNIT_SPELLCAST_SENT", "player", lua.eval("SECRET"), "Cast-2", 133)
    lua.execute("TARGET = nil")
    G.Fire("UNIT_SPELLCAST_SENT", "player", "", "Cast-3", 2061)
    lua.execute('TARGET = "enemy"')
    G.Fire("PLAYER_TARGET_CHANGED")
    G.Fire("NAME_PLATE_UNIT_ADDED", "nameplate3")
    G.Fire("UNIT_COMBAT", "player", "WOUND", "CRITICAL", lua.eval("SECRET"), 1)
    G.Fire("COMBAT_LOG_MESSAGE", "|Kq1|k hits you for 12.", 1, 1, 1, 1)
    lua.execute("COMBAT = true")
    G.Fire("PLAYER_REGEN_DISABLED")
    G.Fire("UNIT_COMBAT", "party1", "HEAL", "", lua.eval("SECRET"), 1)
    G.Fire("COMBAT_TEXT_UPDATE", "DAMAGE")
    run()
    lua.execute("COMBAT = false")
    G.Fire("PLAYER_REGEN_ENABLED")
    run()

    # send: nothing until "chat yes"; the timer path is blocked in the open world, the key press goes through
    G.SlashCmdList.APICHECKS("chat")
    check("chat test asks first", lua.eval("#SENT") == 0)
    G.SlashCmdList.APICHECKS("chat yes")
    for _ in range(12):
        run()
    lua.execute("HARDWARE = true")
    G.SlashCmdList.APICHECKS("chat")
    lua.execute("HARDWARE = false")
    run()
    G.SlashCmdList.APICHECKS("")

    sv = "ApiChecksDB = %s\n" % lua.eval("Serialize(ApiChecksDB)")
    check("never stores a player's name or chat text", "Maro" not in sv and "hits you" not in sv and "come online" not in sv)
    check("never resets the damage meter", lua.eval("METER_RESET") is False)
    from luatable import parse_assignments
    db = parse_assignments(sv)["ApiChecksDB"]
    tw = db["twice"]
    check("twice: double death counted", tw.get("PLAYER_DEAD", {}).get("fires", {}).get("2") == 1, tw.get("PLAYER_DEAD"))
    check("twice: single merchant close counted", tw.get("MERCHANT_CLOSED", {}).get("fires", {}).get("1") == 1, tw.get("MERCHANT_CLOSED"))
    z = db["zone"]
    stale = [k for k, v in z["tally"].items() if v.get("stale")]
    check("zone: stale text after a hearth seen", any("ZONE_CHANGED_NEW_AREA / spell" in k for k in stale), z["tally"])
    check("zone: login not stale", z["tally"].get("PLAYER_ENTERING_WORLD / walked", {}).get("stale") == 0, z["tally"])
    ch = db["chat"]
    check("chat: triggers counted", ch["triggers"].get("rested") == 1 and ch["triggers"].get("afkOff") == 1 and ch["triggers"].get("auction") == 1, ch["triggers"])
    check("chat: rested reached CHAT_MSG_SYSTEM", ch["messages"].get("rested", {}).get("CHAT_MSG_SYSTEM") == 1, ch["messages"])
    check("chat: AFK off seen only in the chat frame", ch["messages"].get("afkOff") == {"chat frame": 1}, ch["messages"])
    check("chat: secret system text counted, not compared", ch["secretOn"].get("CHAT_MSG_SYSTEM") == 1, ch["secretOn"])
    fd = db["feed"]
    uc = fd.get("UNIT_COMBAT", {})
    check("feed: UNIT_COMBAT amount secret in the signature", "s,s,s,T,n" in uc.get("sigs", {}), uc)
    check("feed: actions kept, units folded", uc.get("actions", {}).get("WOUND/CRITICAL") == 1 and uc.get("units", {}).get("partyN") == 1, uc)
    check("feed: combat text info shape", "T,s" in (fd.get("COMBAT_TEXT_UPDATE", {}).get("info") or {}), fd.get("COMBAT_TEXT_UPDATE"))
    check("feed: combat log line read, not stored", fd.get("COMBAT_LOG_MESSAGE", {}).get("wrapped") == 1)
    m = db["meter"]
    check("meter: out-of-combat snapshot", "maxAmount=number" in str(m.get("outside", {}).get("GetCombatSessionFromType")), m.get("outside"))
    check("meter: in-combat amounts secret", "maxAmount=secret table" in str(m.get("combat", {}).get("GetCombatSessionFromType")), m.get("combat"))
    s = db["secrets"]
    check("secrets: spellcast target by context", any("secret" in str(v) for v in s["spellcastSent"].values())
          and any(k.startswith("no target") for k in s["spellcastSent"]), s["spellcastSent"])
    check("secrets: UnitIsUnit on an enemy nameplate", s["unitIsUnit"].get("enemy nameplate: UnitIsUnit(nameplateN, target)", {}).get("secret") == 1, s["unitIsUnit"])
    check("secrets: pet health secret", s["pet"].get('UnitHealth("pet") out of combat', {}).get("secret") == 1, s["pet"])
    world = db["send"].get("world", {}).get("results", {})
    check("send: timer path blocked and learned", "blocked" in str(world.get("SAY from a timer", {}).get("sent")) and "SendChatMessage:SAY:timer" in db["skip"], world)
    check("send: emote from a timer goes through and echoes", world.get("EMOTE from a timer", {}).get("echo") is True, world)
    check("send: key press path works", world.get("SAY from a keypress", {}).get("sent") == "ok" and world.get("SAY from a keypress", {}).get("echo") is True, world)
    check("project ID recorded", db["project"]["id"] == 18)

    import apidoc
    tmp = tempfile.mkdtemp(prefix="checks-test-")
    try:
        sv_dir = os.path.join(tmp, "game", "WTF", "Account", "1", "SavedVariables")
        os.makedirs(sv_dir)
        with open(os.path.join(sv_dir, "ApiChecks.lua"), "w", encoding="utf-8") as f:
            f.write(sv)
        apidoc.GAME = os.path.join(tmp, "game")
        apidoc.DUMPS = os.path.join(tmp, "dumps")
        apidoc.DOCS = os.path.join(tmp, "docs")
        apidoc.SITE = os.path.join(tmp, "site")
        apidoc.LUALS = os.path.join(tmp, "luals")
        apidoc.import_collectors()
        check("import: checks file written", apidoc.latest_dump("checks") is not None)
        apidoc.cmd_build()
        with open(os.path.join(tmp, "site", "data.js"), encoding="utf-8") as f:
            data = f.read()
        check("site data carries the checks", '"checks":{' in data)
        check("docs page written", os.path.exists(os.path.join(tmp, "docs", "checks.md")))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("failed: %d" % failed)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
