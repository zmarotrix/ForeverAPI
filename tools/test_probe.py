"""Run ApiProbe in a small stub client, then feed its SavedVariables through import, build and diff.

    python tools/test_probe.py

Proves the probe can't error, never stores a secret, a return value or a string global's text, and that the tools
read what it writes. It says nothing about the real client.
"""

import os
import shutil
import sys
import tempfile

from lupa import lua51

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

STUB = r"""
SECRET = setmetatable({}, { __tostring = function() error("a secret value was turned into text") end,
  __concat = function() error("a secret value was joined to text") end,
  __eq = function() error("a secret value was compared") end,
  __index = function() error("a secret value was indexed") end })
function issecretvalue(v) return rawequal(v, SECRET) end
COMBAT = false
PRINTED = {}
function print(...) local t = {} for i = 1, select("#", ...) do t[i] = tostring((select(i, ...))) end PRINTED[#PRINTED + 1] = table.concat(t, " ") end
function GetBuildInfo() return "1.60.1", "70862", "Nov 1 2026", 16001 end
function GetServerTime() return 1800000000 end
function GetLocale() return "enUS" end
function InCombatLockdown() return COMBAT end
function UnitName() return "Maro" end
function UnitHealth() if COMBAT then return SECRET end return 812 end
function GetPrivateThing() error("Usage: GetPrivateThing(index)") end
function GetQuestReward() error("must never be called") end
function GetUIThing() error("UI helpers must not be called") end
function SendChatMessage() error("must never be called") end
function CancelLogout() error("must never be called") end
function UnitSetRole() error("must never be called") end
function CancelShapeshiftForm() error("must never be called") end
PLAYER_NAME_TEXT = "Maro the Brave"
ADDON_GLOBAL = function() end
TAINTED = { ADDON_GLOBAL = "SomeAddOn" }
function issecurevariable(t, k)
  if t == _G and TAINTED[k] then return false, TAINTED[k] end
  if type(t) == "table" and t ~= _G and k == "GetHooked" then return false, "Hooker" end
  return true
end
C_Timer = { queue = {} }
function C_Timer.After(_, fn) C_Timer.queue[#C_Timer.queue + 1] = fn end
SlashCmdList = {}
Enum = { AddOnRestrictionType = { Combat = 0, Encounter = 1 }, ItemQuality = { Poor = 0, Common = 1, Rare = 3 } }
Constants = { Things = { MAX = 4 } }
C_RestrictedActions = { IsAddOnRestrictionActive = function(t) return COMBAT and t == 0 end }
C_UnitAuras = { GetUnitAuraInstanceIDs = function(unit) return { 1, 2 } end,
  GetAuraDataByIndex = function() if COMBAT then return { name = SECRET, spellId = SECRET } end return { name = "x", spellId = 1 } end,
  GetBuffDataByIndex = function(...) C_UnitAuras_GetBuffDataByIndex_args = select("#", ...) .. ":" .. tostring((...)) .. ":" .. tostring((select(2, ...))) return nil end,
  GetHooked = function() end, GetCrashy = function() error("must never be called") end, GetSecretKeyed = function() return { [SECRET] = 1 } end }
C_Item = { GetItemNameByID = function(id) if id ~= 6948 then error("wrong sample") end return "Hearthstone" end }
C_UnitAuras_GetBuffDataByIndex_args = nil
C_QuestLog = { GetNumQuestLogEntries = function() return 0 end, GetInfo = function() end,
  GetTitleForQuestID = function() error("must never be called without a quest") end }
C_Crashland = { GetAnything = function() error("must never be called") end }
C_ForeverOnly = { GetSomething = function() return 1, "a", nil end }
C_EventUtils = { IsEventValid = function(e) return VALID[e] == true end }
VALID = { PLAYER_LOGIN = true, ADDON_LOADED = true, PLAYER_REGEN_DISABLED = true, ADDON_ACTION_BLOCKED = true,
  ADDON_ACTION_FORBIDDEN = true, UNIT_AURA = true, FOREVER_ONLY_EVENT = true, CHAT_MSG_SAY = true }
C_Console = { GetAllCommands = function() return { { command = "accountName", help = "Saved account name", category = 1, commandType = 0 },
  { command = "reloadui", help = "Reload", category = 2, commandType = 1 } } end }
C_CVar = { GetCVarDefault = function(n) return "" end, GetCVar = function() error("current values must never be read") end }
C_AddOns = { GetNumAddOns = function() return 1 end, GetAddOnInfo = function() return "ApiProbe" end, IsAddOnLoaded = function() return true end }
string.dump = nil

FRAMES = {}
local methods = {}
local mt = { __index = methods }
function methods:GetObjectType() return self.otype end
function methods:SetScript(h, f) self.scripts[h] = f end
function methods:HasScript(h) return h == "OnShow" or h == "OnEvent" or (self.otype == "Button" and h == "OnClick") end
function methods:Hide() end
function methods:RegisterEvent(e)
  if e == "PROTECTED_EVENT" then Fire("ADDON_ACTION_FORBIDDEN", "ApiProbe", "UNKNOWN()") return end
  if not VALID[e] then error("Attempt to register unknown event \"" .. e .. "\"") end self.events[e] = true end
function methods:UnregisterEvent(e) self.events[e] = nil end
function methods:RegisterAllEvents() self.all = true end
function methods:UnregisterAllEvents() self.all = false self.events = {} end
function methods:CreateTexture() return NewObject("Texture") end
function methods:CreateFontString() return NewObject("FontString") end
function methods:CreateAnimationGroup() return NewObject("AnimationGroup") end
function methods:CreateAnimation(t) if t == "FlipBook" then error("unknown animation type") end return NewObject(t) end
function NewObject(t)
  local o = setmetatable({ [0] = newproxy(), otype = t, scripts = {}, events = {} }, mt)
  FRAMES[#FRAMES + 1] = o
  return o
end
local KNOWN = { Frame = true, Button = true, EditBox = true, Cooldown = true, ModelScene = true }
function CreateFrame(t) if not KNOWN[t] then error("CreateFrame: Unknown frame type '" .. tostring(t) .. "'") end return NewObject(t) end
UIParent = NewObject("Frame")
function CreateFont() return NewObject("Font") end

function Fire(event, ...)
  for _, f in ipairs(FRAMES) do
    if (f.all or f.events[event]) and f.scripts.OnEvent then f.scripts.OnEvent(f, event, ...) end
  end
end
function Tick(n) for _ = 1, n do for _, f in ipairs(FRAMES) do if f.scripts.OnUpdate then f.scripts.OnUpdate(f, 0.016) end end end end
function RunTimers() local q = C_Timer.queue C_Timer.queue = {} for _, fn in ipairs(q) do fn() end end

-- WoW-style SavedVariables writer; refuses secrets
function Serialize(v, indent)
  indent = indent or ""
  if rawequal(v, SECRET) then error("a secret value reached the SavedVariables") end
  local t = type(v)
  if t == "string" then return string.format("%q", v) end
  if t == "number" or t == "boolean" then return tostring(v) end
  if t ~= "table" then error("can't save a " .. t) end
  local keys = {}
  for k in pairs(v) do keys[#keys + 1] = k end
  table.sort(keys, function(a, b) if type(a) == type(b) then return a < b end return type(a) == "number" end)
  local out = { "{" }
  for _, k in ipairs(keys) do
    if rawequal(k, SECRET) then error("a secret key reached the SavedVariables") end
    local ks = type(k) == "string" and string.format("[%q]", k) or ("[" .. tostring(k) .. "]")
    out[#out + 1] = indent .. "\t" .. ks .. " = " .. Serialize(v[k], indent .. "\t") .. ","
  end
  out[#out + 1] = indent .. "}"
  return table.concat(out, "\n")
end
"""

LEADS = r"""
ApiProbeLeads = { build = "1.60.1.70862",
  events = { "UNIT_AURA", "NOT_IN_FOREVER_EVENT", "FOREVER_ONLY_EVENT", "PROTECTED_EVENT" },
  crashers = { ["C_UnitAuras.GetCrashy"] = true, ["C_Crashland."] = true },
  calls = { { "C_UnitAuras", "GetUnitAuraInstanceIDs", "unit" }, { "C_UnitAuras", "GetAuraDataByIndex" },
            { "C_UnitAuras", "GetSecretKeyed" }, { "C_UnitAuras", "GetCrashy" }, { "C_Crashland", "GetAnything" }, { nil, "CancelShapeshiftForm" },
            { "C_Item", "GetItemNameByID", { "item" } }, { "C_UnitAuras", "GetBuffDataByIndex", { "unit", "n:1", "nil" } },
            { "C_QuestLog", "GetTitleForQuestID", { "quest" } }, { "C_Missing", "GetNothing" }, { nil, "UnitHealth", "unit" } },
  documented = { UnitHealth = true },
  uiGetters = { GetUIThing = true },
}
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


def run_probe(tweak=""):
    lua = lua51.LuaRuntime(unpack_returned_tuples=True)
    lua.execute(STUB)
    lua.execute(tweak)
    lua.execute(LEADS)
    with open(os.path.join(ROOT, "addon", "ApiProbe", "probe.lua"), encoding="utf-8") as f:
        lua.execute("local f = assert(loadstring(...)); f('ApiProbe')", f.read())
    G = lua.globals()
    G.Fire("ADDON_LOADED", "ApiProbe")
    G.Fire("PLAYER_LOGIN")
    G.RunTimers()
    G.Tick(200)
    G.Fire("CHAT_MSG_SAY", "hello Maro", "Maro-Forever")
    G.Fire("FOREVER_ONLY_EVENT", 5)
    G.SlashCmdList.APIPROBE("calls")
    G.Tick(50)
    lua.execute("COMBAT = true")
    G.Fire("PLAYER_REGEN_DISABLED")
    G.Fire("UNIT_AURA", "player", lua.eval("SECRET"))
    G.Tick(50)
    lua.execute("COMBAT = false")
    G.SlashCmdList.APIPROBE("")
    sv = "ApiProbeDB = " + lua.eval("Serialize(ApiProbeDB)") + "\n"
    return lua, sv


def main():
    import apidoc
    import diff as differ
    from luatable import parse_assignments

    lua, sv = run_probe()
    printed = "\n".join(lua.globals().PRINTED.values())
    check("probe printed its status", "API probe" in printed, printed)
    check("never stores the player's name", "Maro" not in sv)
    check("never stores a string global's text", "Maro the Brave" not in sv)
    check("never reads a CVar's current value", "current values must never" not in sv)
    check("never calls GetQuestReward / SendChatMessage", "must never be called" not in sv)
    db = parse_assignments(sv)["ApiProbeDB"]
    d = db["dump"]
    check("dump finished", "finished" in d["meta"], d["meta"])
    check("built-in vs Lua is unknown without string.dump or 'builtin'", d["globals"].get("UnitName") == "f?", d["globals"].get("UnitName"))
    check("add-on globals left out and counted", "ADDON_GLOBAL" not in d["globals"] and "ADDON_GLOBAL" in d["tainted"]["SomeAddOn"].values())
    check("namespace members recorded", "GetUnitAuraInstanceIDs" in d["tables"]["C_UnitAuras"])
    check("replaced namespace member marked", d["tables"]["C_UnitAuras"]["GetHooked"].endswith("!Hooker"))
    check("enum values kept", d["tables"]["Enum"]["ItemQuality"]["Rare"] == "n:3", d["tables"]["Enum"].get("ItemQuality"))
    check("widgets: Button has OnClick", "OnClick" in d["widgets"]["Button"]["scripts"].values())
    check("widgets: unknown types recorded as errors", "error" in d["widgets"]["Slider"])
    check("events: control name rejected", d["events"]["APIPROBE_NOT_A_REAL_EVENT"]["register"] != "ok")
    check("events: docs-only event rejected", d["events"]["NOT_IN_FOREVER_EVENT"]["register"] != "ok")
    check("events: real event accepted", d["events"]["UNIT_AURA"]["register"] == "ok")
    check("cvars: default kept, help kept", d["cvars"]["accountName"].get("help") == "Saved account name")
    calls = db["calls"]
    out, com = calls["outside"]["results"], calls["combat"]["results"]
    check("outside calls done", calls["outside"]["done"] is True)
    check("combat calls done", calls["combat"]["done"] is True)
    check("unit getter called with player", out["UnitHealth"][1] == "number", out.get("UnitHealth"))
    check("secret return recorded as secret", com["UnitHealth"][1] == "secret:table", com.get("UnitHealth"))
    check("table shape recorded", "name=string" in out["C_UnitAuras.GetAuraDataByIndex"][1], out["C_UnitAuras.GetAuraDataByIndex"])
    check("secret fields inside a table", "name=secret" in com["C_UnitAuras.GetAuraDataByIndex"][1], com["C_UnitAuras.GetAuraDataByIndex"])
    check("secret table key doesn't break it", "C_UnitAuras.GetSecretKeyed" in out)
    check("missing documented function recorded", out["C_Missing.GetNothing"].get("missing") is True)
    check("undocumented getter called when built-in can't be told apart", "Usage: GetPrivateThing" in str(out.get("GetPrivateThing")))
    check("Blizzard UI Lua getters never called", "GetUIThing" not in out)
    live = db["live"]["events"]
    check("live: event counted", live["FOREVER_ONLY_EVENT"]["n"] == 1)
    check("live: secret argument marked S", "s,S" in live["UNIT_AURA"]["sigs"], live["UNIT_AURA"])
    check("Cancel* never called, even if leads list it", "CancelLogout" not in out and "UnitSetRole" not in out and out["CancelShapeshiftForm"].get("skipped") == "not a getter", out.get("CancelShapeshiftForm"))
    check("sample argument passed", out["C_Item.GetItemNameByID"].get(1) == "string" and out["C_Item.GetItemNameByID"].get("arg") == "item", out.get("C_Item.GetItemNameByID"))
    check("sample values never stored", "Hearthstone" not in sv)
    check("trailing nil keeps its place", lua.eval("C_UnitAuras_GetBuffDataByIndex_args") == "3:player:1", lua.eval("C_UnitAuras_GetBuffDataByIndex_args"))
    check("no sample, no call", out["C_QuestLog.GetTitleForQuestID"].get("skipped") == "no sample for quest", out.get("C_QuestLog.GetTitleForQuestID"))
    check("crash-listed namespace skipped", "whole namespace" in str(out["C_Crashland.GetAnything"].get("skipped")), out.get("C_Crashland.GetAnything"))
    check("crash-listed call skipped", out["C_UnitAuras.GetCrashy"].get("skipped") == "crashed the client", out.get("C_UnitAuras.GetCrashy"))
    check("forbidden event recorded", d["events"]["PROTECTED_EVENT"]["register"] == "forbidden", d["events"].get("PROTECTED_EVENT"))
    check("forbidden event remembered", db["skip"]["event:PROTECTED_EVENT"] == "forbidden")
    check("blocked report names the event", any(b.get("during") == "event:PROTECTED_EVENT" for b in db["blocked"].values()))
    check("restrictions recorded in combat", calls["combat"]["restrictions"]["Combat"] is True)

    # with a client that marks built-ins, undocumented getters get called
    _, sv2 = run_probe('local ts = tostring; function tostring(v) if type(v) == "function" and v ~= print and v ~= GetPrivateThing and v ~= UnitName and v ~= UnitHealth then return ts(v) end if type(v) == "function" then return "function: builtin: 0000" end return ts(v) end')
    db2 = parse_assignments(sv2)["ApiProbeDB"]
    o2 = db2["calls"]["outside"]["results"]
    check("built-ins recognised from tostring", db2["dump"]["globals"]["GetPrivateThing"] == "fC")
    check("undocumented getter's usage error kept", "Usage: GetPrivateThing" in str(o2.get("GetPrivateThing")), o2.get("GetPrivateThing"))
    check("unit getter called with player (undocumented)", o2["UnitName"].get(1) == "string")
    check("GetQuestReward never called", "GetQuestReward" not in o2)

    # tools: import, build, diff
    tmp = tempfile.mkdtemp(prefix="apiprobe-test-")
    try:
        for name, value in (("DUMPS", os.path.join(tmp, "dumps")), ("DOCS", os.path.join(tmp, "docs"))):
            setattr(apidoc, name, value)
        p1 = os.path.join(tmp, "a.lua")
        with open(p1, "w", encoding="utf-8") as f:
            f.write(sv)
        dump1 = apidoc.cmd_import(p1)
        check("import wrote a dump", dump1 and os.path.exists(dump1))
        apidoc.cmd_build()
        with open(os.path.join(tmp, "docs", "index.md"), encoding="utf-8") as f:
            index = f.read()
        check("build: index names the dump", "ApiProbe 0.2.2 on 1.60.1.70862" in index)
        with open(os.path.join(tmp, "docs", "systems", "UnitAuras.md"), encoding="utf-8") as f:
            page = f.read()
        check("build: documented function verified", "✅ | [C_UnitAuras.GetUnitAuraInstanceIDs]" in page)
        check("build: documented function missing in game", "⛔ | [C_UnitAuras.AddAuraSound]" in page)
        check("build: hooked member flagged", "Replaced by the add-on **Hooker**" in page or "GetHooked" in page)
        with open(os.path.join(tmp, "docs", "events.md"), encoding="utf-8") as f:
            ev = f.read()
        check("build: Forever-only event", "| 🆕 | `FOREVER_ONLY_EVENT`" in ev, [l for l in ev.splitlines() if "FOREVER_ONLY" in l])
        check("build: candidate event absent in game", "| ⛔ | `NOT_IN_FOREVER_EVENT`" in ev)
        check("build: unchecked docs event stays unverified", "| ❔ | `UNIT_HEALTH`" in ev)
        a = apidoc._load_json(dump1)
        b = dict(a, globals=dict(a["globals"], NewThing="fC"))
        b["globals"].pop("UnitName")
        flat = differ.flatten
        out = os.path.join(tmp, "docs", "changes", "x.md")
        differ.write_report(a, b, "a", "b", out)
        with open(out, encoding="utf-8") as f:
            rep = f.read()
        check("diff: added and removed", "`NewThing`" in rep and "`UnitName`" in rep, rep[:400])
        check("diff: flatten covers calls", any(k.startswith("calls-combat/") for k in flat(a)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("failed: %d" % failed)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
