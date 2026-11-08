-- API timeline: which events fire, in what order, around everyday moments. Background collector for ForeverAPI.
--
-- Every event goes into a short ring buffer. When a trigger event fires (entering the world, combat, a boss pull,
-- opening loot or a vendor, a quest, death, level-up, joining a group...), the probe keeps the second before it and
-- the next few seconds after it as one trace. It keeps the first few traces of each kind per client build.
-- A trace holds event names, milliseconds from the trigger, argument kinds (n s b t S -) and, when the first
-- argument is a unit token such as "player" or "target", that token. Never any other argument value.

local ADDON = ...
local VERSION = "0.2.0"
local BEFORE = 1.0        -- seconds kept before a trigger
local AFTER = 4.0         -- seconds recorded after it
local MAX_EVENTS = 250    -- per trace
local KEEP = 3            -- traces kept per trigger kind
local RING = 200

ApiTimelineDB = ApiTimelineDB or {}
local db
local issecretvalue = rawget(_G, "issecretvalue")
local function isSecret(v) return issecretvalue ~= nil and issecretvalue(v) == true end
local function say(msg) print("|cff9ec8ffAPI timeline|r " .. msg) end
local function buildKey()
  local version, build = GetBuildInfo()
  return tostring(version) .. "." .. tostring(build)
end

-- trigger event -> kind name (a function picks the kind from the payload)
local TRIGGERS = {
  PLAYER_ENTERING_WORLD = function(login, reload) return login and "login" or reload and "reload" or "zone change" end,
  PLAYER_REGEN_DISABLED = "combat start", PLAYER_REGEN_ENABLED = "combat end",
  ENCOUNTER_START = "boss pull", ENCOUNTER_END = "boss end",
  LOOT_READY = "loot window", MERCHANT_SHOW = "vendor open", MERCHANT_CLOSED = "vendor close",
  MAIL_SHOW = "mailbox open", BANKFRAME_OPENED = "bank open", GOSSIP_SHOW = "npc gossip",
  QUEST_DETAIL = "quest offered", QUEST_ACCEPTED = "quest accepted", QUEST_TURNED_IN = "quest turned in",
  PLAYER_DEAD = "death", PLAYER_UNGHOST = "back from ghost", PLAYER_LEVEL_UP = "level up",
  GROUP_JOINED = "group joined", GROUP_LEFT = "group left", TRADE_SHOW = "trade open",
  AUCTION_HOUSE_SHOW = "auction house open", TAXIMAP_OPENED = "flight master", PLAYER_CONTROL_LOST = "control lost",
  PLAYER_CONTROL_GAINED = "control back", READY_CHECK = "ready check", LFG_PROPOSAL_SHOW = "group finder pop",
  CHALLENGE_MODE_START = "keystone start", PVP_MATCH_ACTIVE = "pvp match start", UPDATE_BATTLEFIELD_STATUS = "battleground queue",
  TRAINER_SHOW = "trainer open", PLAYER_TARGET_CHANGED = "target change", UNIT_SPELLCAST_START = "cast start",
}
local UNIT_PREFIX = { player = true, target = true, focus = true, mouseover = true, pet = true, vehicle = true,
  party = true, raid = true, nameplate = true, boss = true, arena = true, partypet = true, raidpet = true }

local ring, ringNext = {}, 1
local captures = {} -- open traces: { kind, t0, events }, several can overlap
local open = {}     -- kind -> its open trace
local inGroup      -- last known IsInGroup(), for joined/left without relying on GROUP_JOINED

local function kinds(...)
  local n = select("#", ...)
  local parts = {}
  for i = 1, math.min(n, 12) do
    local v = select(i, ...)
    if isSecret(v) then parts[i] = "S"
    else
      local t = type(v)
      parts[i] = t == "nil" and "-" or t == "number" and "n" or t == "string" and "s" or t == "boolean" and "b"
        or t == "table" and "t" or t:sub(1, 1)
    end
  end
  return table.concat(parts, ",")
end

-- "player", "party1", "nameplate7", "party1target", "targettarget" -> the token; anything else -> nil
local function unitOf(a1)
  if type(a1) ~= "string" or isSecret(a1) or #a1 > 24 then return nil end
  local s = a1
  while #s > 6 and s:sub(-6) == "target" do s = s:sub(1, -7) end
  local prefix = s:match("^(%a+)%d*$")
  if prefix and UNIT_PREFIX[prefix] then return a1 end
end

local function now() return GetTimePreciseSec and GetTimePreciseSec() or GetTime() end

local function finish(c)
  open[c.kind] = nil
  local list = db.traces[c.kind] or {}
  db.traces[c.kind] = list
  list[#list + 1] = { at = GetServerTime(), zoneType = c.zoneType, events = c.events, truncated = c.truncated }
end

local function onEvent(event, ...)
  local t = now()
  local entry = { t, event, kinds(...), unitOf((...)) }
  for i = #captures, 1, -1 do
    local c = captures[i]
    if t - c.t0 > AFTER then
      table.remove(captures, i)
      finish(c)
    elseif #c.events < MAX_EVENTS then
      c.events[#c.events + 1] = { math.floor((t - c.t0) * 1000 + 0.5), event, entry[3], entry[4] }
    else
      c.truncated = true
    end
  end
  ring[ringNext] = entry
  ringNext = ringNext % RING + 1

  local trig = TRIGGERS[event]
  -- joining or leaving a group, seen from the roster itself (GROUP_JOINED doesn't fire for every way in)
  if event == "GROUP_ROSTER_UPDATE" or event == "PLAYER_ENTERING_WORLD" then
    local now_in = IsInGroup() and true or false
    if event == "GROUP_ROSTER_UPDATE" and inGroup ~= nil and now_in ~= inGroup then
      trig = now_in and "group joined" or "group left"
    end
    inGroup = now_in
  end
  if trig then
    if event == "UNIT_SPELLCAST_START" and (...) ~= "player" then trig = nil end
    local kind = type(trig) == "function" and trig(...) or trig
    if kind and not open[kind] and #(db.traces[kind] or {}) < KEEP then
      local events = {}
      -- the second before: walk the ring buffer oldest first
      for i = 0, RING - 1 do
        local e = ring[(ringNext + i - 1) % RING + 1]
        if e and t - e[1] <= BEFORE and e ~= entry then
          events[#events + 1] = { math.floor((e[1] - t) * 1000 - 0.5), e[2], e[3], e[4] }
        end
      end
      events[#events + 1] = { 0, event, entry[3], entry[4], trigger = true }
      local _, zoneType = IsInInstance()
      local c = { kind = kind, t0 = t, events = events, zoneType = zoneType }
      captures[#captures + 1] = c
      open[kind] = c
    end
  end
end

local frame = CreateFrame("Frame")
frame:SetScript("OnEvent", function(_, event, ...)
  if event == "ADDON_LOADED" and ... == ADDON then
    db = ApiTimelineDB
    if db.build ~= buildKey() or not db.traces then -- a new add-on version keeps what it recorded
      ApiTimelineDB = { build = buildKey(), probe = VERSION, traces = {} }
      db = ApiTimelineDB
    end
    db.probe = VERSION
  end
  if db then onEvent(event, ...) end
end)
-- an open capture also closes on a quiet timer, so a trace ends even when nothing else fires
frame:SetScript("OnUpdate", function()
  local t = now()
  for i = #captures, 1, -1 do
    if t - captures[i].t0 > AFTER then finish(table.remove(captures, i)) end
  end
end)
frame:RegisterAllEvents()

SLASH_APITIMELINE1 = "/apitimeline"
SlashCmdList.APITIMELINE = function(msg)
  if msg == "reset" then db.traces = {} say("cleared.") return end
  local have = {}
  for kind, list in pairs(db.traces) do have[#have + 1] = kind .. " " .. #list end
  table.sort(have)
  say(("v%s. %d kinds recorded: %s"):format(VERSION, #have, table.concat(have, ", ")))
end
