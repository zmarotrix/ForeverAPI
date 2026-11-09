"""Stub-client checks for LibForever-1.0 on its own (no NorgannonDB Core): loading, two copies, events, combat queue,
secrets, Compat, Names and SavedVars.

    python tools/test_libforever.py

NorgannonDB's harnesses test the same code through Core (tools/deploy.py runs them); this one covers what only
matters to a library that several add-ons ship: copies of different versions, in either load order.
Needs lupa (pip install lupa).
"""

import os
import re
import sys

from lupa import lua51

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LIB = os.path.join(ROOT, "lib", "LibForever-1.0")
LIBSTUB = os.path.join(ROOT, "lib", "LibStub", "LibStub.lua")

STUB = r"""
T = { events = {}, timers = {}, combat = false, chat = {}, secret = {} }
local frames = {}
function CreateFrame()
  local f = { scripts = {}, registered = {} }
  function f:RegisterEvent(e)
    if e:find("^NOT_") then error("unknown event " .. e) end
    self.registered[e] = true
  end
  function f:UnregisterEvent(e) self.registered[e] = nil end
  function f:SetScript(k, fn) self.scripts[k] = fn end
  frames[#frames + 1] = f
  return f
end
function T.Fire(event, ...)
  for _, f in ipairs(frames) do
    if f.registered[event] and f.scripts.OnEvent then f.scripts.OnEvent(f, event, ...) end
  end
end
function T.FrameCount() return #frames end
function T.Tick()
  local due = T.timers
  T.timers = {}
  for _, fn in ipairs(due) do fn() end
end
C_Timer = { After = function(_, fn) table.insert(T.timers, fn) end }
function GetBuildInfo() return "1.60.1", "70862", "Nov 1 2026", 16001 end
function GetLocale() return "enUS" end
function InCombatLockdown() return T.combat end
function GetServerTime() return 1000 end
function issecretvalue(v) return T.secret[v] == true end
function strtrim(s) return (s:gsub("^%s+", ""):gsub("%s+$", "")) end
function Ambiguate(name) return (name:gsub("%-.*$", "")) end
DEFAULT_CHAT_FRAME = { AddMessage = function(_, m) table.insert(T.chat, m) end }
C_Spell = {
  GetSpellInfo = function(id) return { name = "Spell " .. id, iconID = 136243, castTime = 1500, minRange = 0,
    maxRange = 40, spellID = id, originalIconID = 136243 } end,
  GetSpellSubtext = function() return "Rank 3" end,
}
C_QuestLog = { IsQuestFlaggedCompleted = function(id) return id == 783 end }
UnitExists = function(u) return u == "party1" end
UnitGUID = function() return "Player-1-0001" end
GetUnitName = function(u) if u == "player" then return "Tyrant Kuma" end return "Elowen" end
UnitName = function() return "Elowen" end
"""


def main():
    lua = lua51.LuaRuntime(encoding="utf-8")
    lua.execute(STUB)
    load = lua.eval("function(path) local chunk = assert(loadfile(path)) chunk('Test', {}) end")
    files = re.findall(r'<Script file="([^"]+)"', open(os.path.join(LIB, "LibForever-1.0.xml"), encoding="utf-8").read())
    with open(os.path.join(LIB, "Base.lua"), encoding="utf-8") as handle:
        minor = int(re.search(r'local MAJOR, MINOR = "LibForever-1.0", (\d+)', handle.read()).group(1))

    def load_copy(as_minor):
        """Loads the library's files as if its MINOR were as_minor (another add-on's older or newer copy)."""
        for name in files:
            path = os.path.join(LIB, name)
            if name == "Base.lua" and as_minor != minor:
                with open(path, encoding="utf-8") as handle:
                    text = handle.read().replace('"LibForever-1.0", %d' % minor, '"LibForever-1.0", %d' % as_minor, 1)
                lua.execute(text)
            else:
                load(path)

    failed = 0

    def check(label, ok, detail=None):
        nonlocal failed
        print(("PASS " if ok else "FAIL ") + label + ("" if ok or detail is None else "  -- %s" % detail))
        failed += 0 if ok else 1

    load(LIBSTUB)
    load_copy(minor)
    LF = lua.eval('(LibStub("LibForever-1.0"))')
    check("loads, and says its version", LF.MINOR == minor and LF._loading is None)
    check("every file filled its part", all(LF[k] is not None for k in ("Compat", "Secret", "Names", "SavedVars", "Client")))

    # events: owners, and an event the client doesn't have
    lua.execute("""
      LF = LibStub("LibForever-1.0")
      heard = {}
      LF:On("PLAYER_LOGIN", "a", function(e, x) heard.a = x end)
      LF:On("PLAYER_LOGIN", "b", function() error("b breaks") end)
      LF:On("PLAYER_LOGIN", "c", function(e, x) heard.c = x end)
      securecallfunction = function(fn, ...) local ok = pcall(fn, ...) end
      T.Fire("PLAYER_LOGIN", 7)
    """)
    check("an event reaches every owner, past one that errors", lua.eval("heard.a == 7 and heard.c == 7"))
    check("an event the client lacks is refused", lua.eval('LF:On("NOT_AN_EVENT", "a", print)') is False)
    lua.execute('LF:Off("PLAYER_LOGIN", "a"); heard = {}; T.Fire("PLAYER_LOGIN", 8)')
    check("Off removes only that owner", lua.eval("heard.a == nil and heard.c == 8"))
    lua.execute('got = nil; LF:Listen("MSG", "me", function(m, v) got = v end); LF:Send("MSG", 3)')
    check("messages reach listeners", lua.eval("got == 3"))

    # combat queue, next frame, restrictions
    lua.execute("""
      T.combat = true
      ran = 0
      LF:AfterCombat(function() ran = ran + 1 end, "k")
      LF:AfterCombat(function() ran = ran + 10 end, "k")
      changed = 0
      LF:Listen(LF.RESTRICTIONS_CHANGED, "t", function() changed = changed + 1 end)
    """)
    check("AfterCombat holds work in combat", lua.eval("ran == 0") and lua.eval('LF:Restricted("combat") == "combat"'))
    lua.execute('T.combat = false; T.Fire("PLAYER_REGEN_ENABLED"); T.Tick()')
    check("and runs it once combat ends, a key only once", lua.eval("ran == 10"), lua.eval("ran"))
    check("the restrictions message comes on the next frame", lua.eval("changed == 1"))
    check("Restricted is nil out of combat", lua.eval("LF:Restricted() == nil"))

    # secrets and Plain
    lua.execute('S = setmetatable({}, {}); T.secret[S] = true; function Pair() return S, 5 end')
    check("Plain turns secrets into nil", lua.eval("select(2, LF.Plain(Pair)) == 5 and LF.Plain(Pair) == nil"))
    check("Safe falls back on a secret", lua.eval("LF.Safe(S, 0) == 0 and LF.Safe(4, 0) == 4"))
    check("Global and Now", lua.eval('LF.Global("GetServerTime") == 1000 and LF.Now() == 1000'))
    check("Client says Forever", lua.eval('LF.Client.IsForever() and LF.Client.Flavor() == "forever"'))

    # Compat
    check("Compat.GetSpellInfo answers in classic's shape, with the rank",
          lua.eval('select(2, LF.Compat.GetSpellInfo(8936)) == "Rank 3" and LF.Compat.GetSpellInfo(8936) == "Spell 8936"'))
    check("a generated one passes straight through", lua.eval("LF.Compat.IsQuestFlaggedCompleted(783) == true"))
    check("nothing is written into the globals", lua.eval("rawget(_G, 'GetSpellInfo') == nil"))

    # Names
    lua.execute('T.Fire("CHAT_MSG_SAY", "hi", "Elowen Brightwater-Realm", "", "", "", "", 0, 0, "", 0, 1, "Player-1-0002")')
    check("Names learns full names from chat", lua.eval('LF.Names:Address("Elowen") == "Elowen Brightwater"'))
    check("Names.First and Key", lua.eval('LF.Names.First("Tyrant Kuma") == "Tyrant" and LF.Names.Key("Tyrant-Realm") == "tyrant"'))
    check("Names.IsMe", lua.eval('LF.Names.IsMe("Tyrant") and not LF.Names.IsMe("Elowen")'))

    # SavedVars and the debug sink
    lua.execute("""
      lines = {}
      LF:SetDebugSink(function(source, text) table.insert(lines, source .. ": " .. text) end)
      OldDB = { size = 2 }
      sv = LF:SavedVars("OldDB", { version = 3, defaults = { size = 1, shown = true, deep = { a = 1 } },
        migrate = { [2] = function(s) s.scale = s.size end, [3] = function() error("boom") end } })
      fresh = LF:SavedVars("NewDB", { version = 3, defaults = { size = 1 } })
    """)
    check("SavedVars runs migrations in order and fills defaults",
          lua.eval("sv.scale == 2 and sv.shown == true and sv.deep.a == 1 and sv._v == 3 and OldDB == sv"))
    check("a failed migration goes to the debug sink", lua.eval("#lines == 1 and lines[1]:find('migration to 3 failed') ~= nil"))
    check("a fresh save starts at its version", lua.eval("fresh._v == 3 and fresh.size == 1"))
    lua.execute("LF:SetDebugSink(nil); LF:Debug('x', '%d', 1)")
    check("Debug with no sink does nothing", lua.eval("#lines == 1"))

    # Another add-on's older copy loads after this one: it steps aside, and nothing is reset
    frames = lua.eval("T.FrameCount()")
    load_copy(minor - 1 if minor > 1 else 0)
    check("an older copy steps aside", lua.eval('(LibStub("LibForever-1.0")).MINOR') == minor and lua.eval("LF._loading") is None)
    lua.execute('heard = {}; T.Fire("PLAYER_LOGIN", 9)')
    check("and the handlers stay", lua.eval("heard.c == 9"))
    check("Compat is the same table", lua.eval('LibStub("LibForever-1.0").Compat == LF.Compat'))

    # A newer copy loads after: it takes over the same frame, handlers, queue and names
    lua.execute("T.combat = true; LF:AfterCombat(function() ran = 99 end)")
    lua.execute("oldNames, oldCompat = LF.Names, LF.Compat")
    load_copy(minor + 1)
    check("a newer copy takes over", lua.eval('(LibStub("LibForever-1.0")).MINOR') == minor + 1 and lua.eval("LF._loading") is None)
    check("on the same event frame", lua.eval("T.FrameCount()") == frames, (frames, lua.eval("T.FrameCount()")))
    lua.execute('heard = {}; T.Fire("PLAYER_LOGIN", 10)')
    check("the older copy's handlers still fire", lua.eval("heard.c == 10"))
    lua.execute('T.combat = false; T.Fire("PLAYER_REGEN_ENABLED")')
    check("work queued before the upgrade runs after it", lua.eval("ran == 99"))
    check("names learned before the upgrade are kept", lua.eval('LF.Names:Address("Elowen") == "Elowen Brightwater"')
          and lua.eval("LF.Names == oldNames"))
    check("Compat is filled again", lua.eval("LF.Compat == oldCompat and LF.Compat.GetSpellInfo ~= nil"))

    print("failed: %d" % failed)
    print("errors: 0")
    return failed


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
