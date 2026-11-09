-- ForeverAPI Probe: a developer add-on that records what WoW Forever's add-on API really does, for the ForeverAPI
-- reference (https://zmarotrix.github.io/ForeverAPI/). Nothing records until you switch a module on with /fapi.
--
-- Modules (each its own file, each off until you turn it on):
--   probe     once per client build: every global, namespace member, enum, widget method and event name; getters
--             called out of and in combat; a live count of every event and its argument types
--   watch     getters again in each situation (dungeon, raid, boss fight, PvP) and on each kind of unit
--   timeline  which events fire, in what order, around login, zoning, combat, loot, vendors, flights...
--   widgets   which widget setters and Lua operations accept a secret value
--   checks    behaviour testers reported: events firing twice, stale zone text, the combat feed, secret cases
--
-- What it stores: names, types, "secret or not", error text and event order. Never a value, a chat line, or a
-- player's name. /fapi export turns it into one text block to submit on GitHub.

local ADDON = ...
ForeverAPIProbeDB = ForeverAPIProbeDB or {}

FAPI = {
  version = "1.0.0",
  order = { "probe", "watch", "timeline", "widgets", "checks" },
  about = {
    probe = "the API itself, once per client build; getters in and out of combat; every event that fires",
    watch = "getters in dungeons, raids, boss fights and PvP, and on each kind of unit",
    timeline = "the order events fire in around everyday moments",
    widgets = "which widget setters accept a secret value (a few seconds, once per build)",
    checks = "reported quirks: events firing twice, stale zone text, the combat feed, secret cases",
  },
  -- the slash handler each module registers (kept from when they were separate add-ons)
  slash = { probe = "APIPROBE", watch = "APIWATCH", timeline = "APITIMELINE", widgets = "APIWIDGETS", checks = "APICHECKS" },
  running = {},
}

local function say(msg) print("|cff9ec8ffForeverAPI Probe|r " .. msg) end
FAPI.say = say

local function settings()
  local db = ForeverAPIProbeDB
  db.modules = db.modules or {}
  return db
end

function FAPI.on(name)
  return settings().modules[name] == true
end

-- Called from each module's ADDON_LOADED. A module that's off stops listening for good (until a /reload).
function FAPI.gate(name, ...)
  if FAPI.on(name) then
    FAPI.running[name] = true
    return true
  end
  for i = 1, select("#", ...) do
    local f = select(i, ...)
    f:UnregisterAllEvents()
    f:SetScript("OnUpdate", nil)
  end
  return false
end

local function list(names)
  return #names > 0 and table.concat(names, ", ") or "none"
end

local function status()
  say("v" .. FAPI.version .. ". Modules (|cff80ff80on|r / off):")
  for _, name in ipairs(FAPI.order) do
    local on, running = FAPI.on(name), FAPI.running[name]
    local state = on and (running and "|cff80ff80on|r" or "|cffffff00on after /reload|r") or (running and "|cffffff00off after /reload|r" or "off")
    print(("  %s: %s - %s"):format(name, state, FAPI.about[name]))
  end
  say("/fapi on <module|all>, /fapi off <module|all>, /fapi <module> for its own commands, /fapi export to share.")
end

local function switch(on, what)
  local names = {}
  if what == "all" then names = FAPI.order
  elseif FAPI.about[what] then names = { what }
  else say("no module called '" .. tostring(what) .. "'. Modules: " .. table.concat(FAPI.order, ", ")) return end
  for _, n in ipairs(names) do settings().modules[n] = on or nil end
  local changed = {}
  for _, n in ipairs(names) do
    if (FAPI.running[n] == true) ~= on then changed[#changed + 1] = n end
  end
  if #changed > 0 then
    say(("%s %s after your next /reload. Type |cffffff00/reload|r now to start."):format(list(changed), on and "starts" or "stops"))
  else
    say(("%s already %s."):format(list(names), on and "on" or "off"))
  end
end

local loginFrame = CreateFrame("Frame")
loginFrame:RegisterEvent("PLAYER_LOGIN")
loginFrame:SetScript("OnEvent", function()
  local any = false
  for _, n in ipairs(FAPI.order) do any = any or FAPI.on(n) end
  if not any then
    say("is installed but records nothing until you choose what to record: type |cffffff00/fapi|r.")
  end
end)

SLASH_FOREVERAPIPROBE1 = "/fapi"
SlashCmdList.FOREVERAPIPROBE = function(msg)
  msg = (msg or ""):match("^%s*(.-)%s*$")
  local cmd, rest = msg:match("^(%S+)%s*(.*)$")
  cmd = cmd and cmd:lower()
  if not cmd or cmd == "help" or cmd == "status" then
    status()
  elseif cmd == "on" or cmd == "off" then
    switch(cmd == "on", (rest or ""):lower())
  elseif cmd == "export" then
    if FAPI.ShowExport then FAPI.ShowExport() end
  elseif FAPI.about[cmd] then
    if not FAPI.running[cmd] then
      say(cmd .. " is off. /fapi on " .. cmd .. ", then /reload.")
      return
    end
    local handler = SlashCmdList[FAPI.slash[cmd]]
    if handler then handler(rest or "") end
  else
    say("unknown command '" .. cmd .. "'.")
    status()
  end
end
