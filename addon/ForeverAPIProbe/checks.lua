-- API checks: targeted checks for behaviour testers reported on Forever. Background collector for ForeverAPI.
--
-- Everything here only listens and reads, except /fapi checks chat, which you run yourself.
--   twice     do PLAYER_DEAD, MERCHANT_CLOSED and AUCTION_HOUSE_CLOSED fire twice per death / close?
--   zone      is the zone text stale at PLAYER_ENTERING_WORLD / ZONE_CHANGED_NEW_AREA (after a hearth, taxi, portal)?
--   chat      do "You feel rested.", "Auction created." and AFK on/off reach CHAT_MSG_SYSTEM, or another channel?
--   feed      what UNIT_COMBAT, COMBAT_LOG_MESSAGE, COMBAT_TEXT_UPDATE and C_DamageMeter carry, in and out of combat
--   secrets   UNIT_SPELLCAST_SENT's target by cast context, UnitIsUnit against enemy tokens, the pet's health
--   send      (/fapi checks chat only) can add-on code say / yell / emote, with and without a key press?
-- Stores types, secret flags, counts and Blizzard's own zone names. Never chat text, never player names.

local ADDON = ...
local VERSION = "0.1.0"
local KEEP = 12 -- recent examples kept per list

ApiChecksDB = ApiChecksDB or {}
local db
local G = _G
local issecretvalue = rawget(G, "issecretvalue")
local function isSecret(v) return issecretvalue ~= nil and issecretvalue(v) == true end
local function say(msg) print("|cff9ec8ffFAPI|r checks " .. msg) end
local function inCombat() return InCombatLockdown and InCombatLockdown() and true or false end
local function now() return GetTime and GetTime() or 0 end
local function buildKey()
  local version, build = GetBuildInfo()
  return tostring(version) .. "." .. tostring(build)
end
local function push(list, item)
  list[#list + 1] = item
  while #list > KEEP do table.remove(list, 1) end
end
local function count(t, k) t[k] = (t[k] or 0) + 1 end

-- "s" string, "n" number, "b" boolean, "t" table, "-" nil, upper case when secret
local function kind(v)
  local k = type(v)
  k = (k == "nil" and "-") or (k == "boolean" and "b") or k:sub(1, 1)
  if isSecret(v) then k = k:upper() end
  return k
end
local function sig(...)
  local out = {}
  for i = 1, select("#", ...) do out[i] = kind((select(i, ...))) end
  return table.concat(out, ",")
end
-- a value's shape, two levels deep: secrets and types, no values
local function shape(v, depth)
  if isSecret(v) then return "secret " .. type(v) end
  if type(v) ~= "table" then return type(v) end
  if (depth or 0) >= 2 then return "table" end
  local keys, n = {}, 0
  for k in pairs(v) do
    n = n + 1
    if n <= 12 then keys[#keys + 1] = k end
  end
  table.sort(keys, function(a, b) return tostring(a) < tostring(b) end)
  local parts = {}
  for _, k in ipairs(keys) do
    local key = type(k) == "number" and "[n]" or tostring(k)
    if not (type(k) == "number" and k > 1) then parts[#parts + 1] = key .. "=" .. shape(v[k], (depth or 0) + 1) end
  end
  return "{" .. table.concat(parts, ",") .. (n > 12 and ",..." or "") .. "}" .. (n > 0 and v[1] ~= nil and ("#" .. #v) or "")
end
-- safe equality with a global string: nil when the text is secret. Chat frame lines carry colour codes: contains.
local function sameText(text, globalName, contains)
  if isSecret(text) then return nil end
  local want = rawget(G, globalName)
  if type(text) ~= "string" or type(want) ~= "string" then return false end
  if contains then return text:find(want, 1, true) ~= nil end
  return text == want
end

local currentCall, refused -- for ADDON_ACTION_FORBIDDEN / BLOCKED during a call of ours
local function call(key, fn, ...)
  if db.skip[key] then return false, "skipped: " .. db.skip[key] end
  currentCall, refused = key, nil
  local res = { pcall(fn, ...) }
  currentCall = nil
  if refused then return false, refused end
  return unpack(res, 1, table.maxn(res))
end

-------------------------------------------------------------------------------------------
-- twice: events reported to fire twice
-------------------------------------------------------------------------------------------

local TWICE = { PLAYER_DEAD = true, MERCHANT_CLOSED = true, AUCTION_HOUSE_CLOSED = true,
  MERCHANT_SHOW = true, AUCTION_HOUSE_SHOW = true }
local open = {}
local function twice(event)
  local t = now()
  local o = open[event]
  if o and t - o.last < 1.5 then
    o.fires, o.last = o.fires + 1, t
    o.gap = math.max(o.gap, math.floor((t - o.prev) * 1000))
    o.prev = t
    return
  end
  local rec = db.twice[event] or { episodes = 0, fires = {}, recent = {} }
  db.twice[event] = rec
  o = { fires = 1, first = t, last = t, prev = t, gap = 0, combat = inCombat() }
  open[event] = o
  rec.episodes = rec.episodes + 1
  C_Timer.After(2, function()
    count(rec.fires, tostring(o.fires))
    push(rec.recent, { fires = o.fires, gapMs = o.gap, combat = o.combat, at = GetServerTime() })
    if open[event] == o then open[event] = nil end
  end)
end

-------------------------------------------------------------------------------------------
-- zone: is the zone text stale when the zone events fire?
-------------------------------------------------------------------------------------------

local cause = { spell = nil, spellAt = 0, taxiAt = 0, loading = false, loadingAt = 0 }
local function zoneNow()
  local okm, map = pcall(C_Map.GetBestMapForUnit, "player")
  return { zone = GetZoneText(), real = GetRealZoneText(), sub = GetSubZoneText(), map = okm and map or nil,
    mini = GetMinimapZoneText and GetMinimapZoneText() or nil }
end
local function differs(a, b)
  for _, k in ipairs({ "zone", "real", "sub", "map" }) do
    if a[k] ~= b[k] then return true end
  end
  return false
end
local function howHere()
  local t = now()
  if cause.taxiAt > 0 and t - cause.taxiAt < 20 then return "taxi" end
  if cause.spell and t - cause.spellAt < 60 then return "spell " .. tostring(cause.spell) end
  if cause.loadingAt > 0 and t - cause.loadingAt < 30 then return "loading screen" end
  return "walked"
end
local function zoneEvent(event, a1, a2)
  local first = zoneNow()
  local rec = { event = event, how = howHere(), loading = cause.loading, combat = inCombat(), at = GetServerTime(),
    login = (event == "PLAYER_ENTERING_WORLD") and (a1 and "login" or (a2 and "reload" or "zone")) or nil, t0 = first }
  C_Timer.After(0.5, function() rec.t05 = zoneNow() end)
  C_Timer.After(3, function()
    rec.t3 = zoneNow()
    rec.stale = differs(first, rec.t3)
    rec.staleAt05 = rec.t05 and differs(first, rec.t05) or nil
    local key = event .. " / " .. rec.how:gsub(" %d+$", "")
    local tally = db.zone.tally[key] or { n = 0, stale = 0 }
    db.zone.tally[key] = tally
    tally.n = tally.n + 1
    if rec.stale then tally.stale = tally.stale + 1 end
    push(db.zone.recent, rec)
  end)
end

-------------------------------------------------------------------------------------------
-- chat: system messages reported to skip CHAT_MSG_*
-------------------------------------------------------------------------------------------

-- the message, the global string Blizzard uses for it, and what triggers it
local EXPECT = {
  rested = { "ERR_EXHAUSTION_RESTED" }, wellrested = { "ERR_EXHAUSTION_WELLRESTED" }, normal = { "ERR_EXHAUSTION_NORMAL" },
  auction = { "ERR_AUCTION_STARTED" }, afkOn = { "MARKED_AFK", "MARKED_AFK_MESSAGE" }, afkOff = { "CLEARED_AFK" },
}
local CHANNELS = { "CHAT_MSG_SYSTEM", "UI_INFO_MESSAGE", "UI_ERROR_MESSAGE", "chat frame" }
local function seen(channel, text)
  for name, globals in pairs(EXPECT) do
    for _, g in ipairs(globals) do
      local same = sameText(text, g, channel == "chat frame")
      if same == nil and channel ~= "chat frame" then
        count(db.chat.secretOn, channel) -- can't compare a secret text
        return
      end
      -- MARKED_AFK_MESSAGE is a format string: match its fixed start
      if not same and g == "MARKED_AFK_MESSAGE" and type(text) == "string" and not isSecret(text) and type(rawget(G, g)) == "string" then
        local head = rawget(G, g):match("^(.-)%%") or ""
        same = #head > 3 and text:sub(1, #head) == head
      end
      if same then
        local rec = db.chat.messages[name] or {}
        db.chat.messages[name] = rec
        count(rec, channel)
      end
    end
  end
end
local wasResting, wasAFK
local function trigger(name)
  count(db.chat.triggers, name)
end
local function restingChanged()
  local r = IsResting()
  if wasResting ~= nil and r ~= wasResting then trigger(r and "rested" or "normal") end
  wasResting = r
end
local function afkChanged()
  local ok, a = pcall(UnitIsAFK, "player")
  if not ok or isSecret(a) then return end
  a = a and true or false
  if wasAFK ~= nil and a ~= wasAFK then trigger(a and "afkOn" or "afkOff") end
  wasAFK = a
end

-------------------------------------------------------------------------------------------
-- feed: what add-ons can still see of combat
-------------------------------------------------------------------------------------------

local combatEnd = 0
local function phase()
  if inCombat() then return "combat" end
  if now() - combatEnd < 3 then return "just after combat" end
  return "outside"
end
local function feed(event, ...)
  local f = db.feed[event] or { sigs = {}, phases = {} }
  db.feed[event] = f
  count(f.sigs, sig(...))
  count(f.phases, phase())
  if event == "UNIT_COMBAT" then
    local unit, action, flag = ...
    f.actions = f.actions or {}
    if not isSecret(action) and type(action) == "string" then count(f.actions, action .. ((type(flag) == "string" and not isSecret(flag) and flag ~= "") and ("/" .. flag) or "")) end
    f.units = f.units or {}
    if not isSecret(unit) and type(unit) == "string" then count(f.units, (unit:gsub("%d+$", "N"))) end
  elseif event == "COMBAT_LOG_MESSAGE" then
    local msg = ...
    if not isSecret(msg) and type(msg) == "string" then
      f.wrapped = (f.wrapped or 0) + ((msg:find("|K", 1, true) and 1) or 0)
      f.readable = (f.readable or 0) + 1
    end
  elseif event == "COMBAT_TEXT_UPDATE" then
    local ctype = ...
    f.types = f.types or {}
    if not isSecret(ctype) and type(ctype) == "string" then count(f.types, ctype) end
    local fn = rawget(G, "GetCurrentCombatTextEventInfo")
    if fn then
      local res = { call("GetCurrentCombatTextEventInfo", fn) }
      if res[1] then f.info = f.info or {} count(f.info, sig(unpack(res, 2, table.maxn(res)))) else f.infoError = tostring(res[2]) end
    end
  end
end

-- C_DamageMeter: the shapes it returns, once out of combat, 3 s into each of the first fights, and after
local DM = C_DamageMeter
local function meterSnapshot(label)
  if not DM or (db.meter[label] and db.meter[label].done) then return end
  local out = { at = GetServerTime(), combat = inCombat() }
  local function try(key, fn, ...)
    if type(fn) ~= "function" then out[key] = "no function" return nil end
    local res = { call("C_DamageMeter." .. key, fn, ...) }
    if not res[1] then out[key] = "error: " .. tostring(res[2]) return nil end
    local parts = {}
    for i = 2, math.max(2, table.maxn(res)) do parts[#parts + 1] = shape(res[i]) end
    out[key] = table.concat(parts, ", ")
    return res[2]
  end
  try("IsDamageMeterAvailable", DM.IsDamageMeterAvailable)
  local sessions = try("GetAvailableCombatSessions", DM.GetAvailableCombatSessions)
  try("GetSessionDurationSeconds", DM.GetSessionDurationSeconds, 0)
  local types = (Enum and Enum.DamageMeterType) or {}
  local sessionTypes = (Enum and Enum.DamageMeterSessionType) or {}
  out.types, out.sessionTypes = {}, {}
  for name, v in pairs(types) do out.types[name] = v end
  for name, v in pairs(sessionTypes) do out.sessionTypes[name] = v end
  local session = try("GetCombatSessionFromType", DM.GetCombatSessionFromType, 0, 0)
  -- the first source of that session, by GUID, then its spells
  local src = type(session) == "table" and not isSecret(session) and type(session.combatSources) == "table" and session.combatSources[1]
  if type(src) == "table" then
    out.source = shape(src)
    local guid = src.sourceGUID
    if guid ~= nil then
      try("GetCombatSessionSourceFromType", DM.GetCombatSessionSourceFromType, 0, 0, guid, src.sourceCreatureID)
    end
  end
  if type(sessions) == "table" and not isSecret(sessions) and type(sessions[1]) == "table" then
    local id = sessions[1].sessionID
    if id ~= nil then try("GetCombatSessionFromID", DM.GetCombatSessionFromID, id, 0) end
  end
  out.done = true
  db.meter[label] = out
end

-------------------------------------------------------------------------------------------
-- secrets: the three reported cases
-------------------------------------------------------------------------------------------

local function targetContext()
  if not UnitExists("target") then return "no target" end
  local ok, same = pcall(UnitIsUnit, "target", "player")
  if ok and not isSecret(same) and same then return "target is you" end
  local okc, hostile = pcall(UnitCanAttack, "player", "target")
  if okc and isSecret(hostile) then return "target (hostility secret)" end
  return (okc and hostile) and "enemy target" or "friendly target"
end
local function spellcastSent(unit, target, castGUID, spellID)
  if unit ~= "player" then return end
  local key = targetContext() .. (inCombat() and ", in combat" or ", out of combat")
  local rec = db.secrets.spellcastSent[key] or {}
  db.secrets.spellcastSent[key] = rec
  count(rec, isSecret(target) and "target secret" or (target == nil and "target nil" or (target == "" and "target empty" or "target plain")))
end

-- UnitIsUnit with an enemy unit on either side: does the answer come back secret?
local function unitIsUnitCheck(token, label)
  local function one(a, b)
    local ok, r = call("UnitIsUnit", UnitIsUnit, a, b)
    local k = (not ok) and ("error: " .. tostring(r)) or (isSecret(r) and "secret" or "plain")
    local key = ("%s: UnitIsUnit(%s, %s)%s"):format(label, a:gsub("%d+$", "N"), b, inCombat() and " in combat" or "")
    local rec = db.secrets.unitIsUnit[key] or {}
    db.secrets.unitIsUnit[key] = rec
    count(rec, k)
  end
  one(token, "target")
  one(token, "player")
  one("player", token)
end

local function petHealth(when)
  if not UnitExists("pet") then return end
  for _, fn in ipairs({ "UnitHealth", "UnitHealthMax", "UnitPower", "UnitPowerMax", "UnitIsDead" }) do
    local ok, v = call(fn, G[fn], "pet")
    local key = fn .. '("pet") ' .. when
    local rec = db.secrets.pet[key] or {}
    db.secrets.pet[key] = rec
    count(rec, (not ok) and "error" or (isSecret(v) and "secret" or "plain"))
  end
end

-------------------------------------------------------------------------------------------
-- send: /fapi checks chat (you run it; it speaks in public)
-------------------------------------------------------------------------------------------

local echo -- waiting for our own message to come back
local function sendTest()
  local inInstance, itype = IsInInstance()
  local where = inInstance and (itype or "instance") or "world"
  local run = { at = GetServerTime(), where = where, results = {} }
  db.send[where] = run
  local plan = { { "SAY", "timer" }, { "YELL", "timer" }, { "EMOTE", "timer" }, { "SAY", "keypress" } }
  local i = 0
  local function nextOne()
    i = i + 1
    local p = plan[i]
    if not p then
      say(("chat test done (%s). It saves at your next /reload or logout."):format(where))
      return
    end
    local chatType, how = p[1], p[2]
    local key = chatType .. " from a " .. how
    local function send()
      run.results[key] = {} -- before the call: the echo can arrive inside it
      echo = { chatType = chatType, key = key, at = now() }
      local ok, err = call("SendChatMessage:" .. chatType .. ":" .. how, SendChatMessage, ".", chatType)
      run.results[key].sent = ok and "ok" or tostring(err)
      C_Timer.After(2.5, function()
        if echo and echo.key == key then run.results[key].echo = false echo = nil end
        nextOne()
      end)
    end
    if how == "timer" then
      C_Timer.After(0.2, send) -- no key press behind this call
    else
      run.results[key] = { sent = "type /fapi checks chat again to send this one from a key press" }
      db.sendPending = true
      say("Now type /fapi checks chat once more: that sends the last one from your key press.")
    end
  end
  nextOne()
end
local function sendFromKeypress()
  db.sendPending = nil
  local inInstance, itype = IsInInstance()
  local where = inInstance and (itype or "instance") or "world"
  local run = db.send[where]
  if not run then return end
  local key = "SAY from a keypress"
  run.results[key] = {}
  echo = { chatType = "SAY", key = key, at = now() }
  local ok, err = call("SendChatMessage:SAY:keypress", SendChatMessage, ".", "SAY")
  run.results[key].sent = ok and "ok" or tostring(err)
  C_Timer.After(2.5, function()
    if echo and echo.key == key then run.results[key].echo = false echo = nil end
    say(("chat test done (%s). It saves at your next /reload or logout."):format(where))
  end)
end
local function chatEcho(event, text, _, _, _, _, _, _, _, _, _, _, guid)
  if not echo then return end
  local want = "CHAT_MSG_" .. echo.chatType
  if event ~= want then return end
  local okg, me = pcall(UnitGUID, "player")
  if isSecret(guid) or isSecret(me) then
    db.send.echoSecret = true
    return
  end
  if guid == me then
    for _, run in pairs(db.send) do
      if type(run) == "table" and run.results and run.results[echo.key] then run.results[echo.key].echo = true end
    end
    echo = nil
  end
end

-------------------------------------------------------------------------------------------
-- events
-------------------------------------------------------------------------------------------

local FEED = { "UNIT_COMBAT", "COMBAT_LOG_MESSAGE", "COMBAT_TEXT_UPDATE", "DAMAGE_METER_COMBAT_SESSION_UPDATED",
  "DAMAGE_METER_CURRENT_SESSION_UPDATED", "DAMAGE_METER_RESET" }
local fights = 0
local frame = CreateFrame("Frame")
local function reg(event)
  if db.skip["event:" .. event] then return end
  currentCall, refused = "event:" .. event, nil
  pcall(frame.RegisterEvent, frame, event)
  currentCall = nil
end

frame:SetScript("OnEvent", function(_, event, ...)
  if event == "ADDON_LOADED" then
    if ... ~= ADDON then return end
    if not FAPI.gate("checks", frame) then return end
    db = ApiChecksDB
    if db.build ~= buildKey() or db.probe ~= VERSION then
      local skip = db.build == buildKey() and db.skip or nil
      ApiChecksDB = { build = buildKey(), probe = VERSION, skip = skip }
      db = ApiChecksDB
    end
    for _, k in ipairs({ "skip", "twice", "feed", "meter", "send" }) do db[k] = db[k] or {} end
    db.zone = db.zone or { tally = {}, recent = {} }
    db.chat = db.chat or { triggers = {}, messages = {}, secretOn = {} }
    db.secrets = db.secrets or { spellcastSent = {}, unitIsUnit = {}, pet = {} }
    db.project = { id = rawget(G, "WOW_PROJECT_ID"), mainline = rawget(G, "WOW_PROJECT_MAINLINE"),
      classic = rawget(G, "WOW_PROJECT_CLASSIC"), camelot = rawget(G, "WOW_PROJECT_CAMELOT") }
    for e in pairs(TWICE) do reg(e) end
    for _, e in ipairs(FEED) do reg(e) end
    for _, e in ipairs({ "PLAYER_ENTERING_WORLD", "ZONE_CHANGED_NEW_AREA", "LOADING_SCREEN_ENABLED", "LOADING_SCREEN_DISABLED",
      "UNIT_SPELLCAST_SUCCEEDED", "UNIT_SPELLCAST_SENT", "PLAYER_CONTROL_LOST", "PLAYER_CONTROL_GAINED",
      "PLAYER_UPDATE_RESTING", "PLAYER_FLAGS_CHANGED", "AUCTION_HOUSE_AUCTION_CREATED", "CHAT_MSG_SYSTEM", "UI_INFO_MESSAGE",
      "UI_ERROR_MESSAGE", "PLAYER_REGEN_DISABLED", "PLAYER_REGEN_ENABLED", "PLAYER_TARGET_CHANGED", "NAME_PLATE_UNIT_ADDED",
      "UNIT_PET", "CHAT_MSG_SAY", "CHAT_MSG_YELL", "CHAT_MSG_EMOTE" }) do reg(e) end
    -- chat lines the UI prints without an event
    if DEFAULT_CHAT_FRAME and DEFAULT_CHAT_FRAME.AddMessage then
      hooksecurefunc(DEFAULT_CHAT_FRAME, "AddMessage", function(_, text) seen("chat frame", text) end)
    end
  elseif event == "ADDON_ACTION_FORBIDDEN" or event == "ADDON_ACTION_BLOCKED" then
    if ... == ADDON and currentCall and db then
      refused = event == "ADDON_ACTION_FORBIDDEN" and "forbidden" or "blocked"
      db.skip[currentCall] = refused .. (inCombat() and " in combat" or "")
    end
  elseif TWICE[event] then
    twice(event)
  elseif event == "PLAYER_ENTERING_WORLD" or event == "ZONE_CHANGED_NEW_AREA" then
    zoneEvent(event, ...)
    if event == "PLAYER_ENTERING_WORLD" then
      wasResting = IsResting()
      afkChanged()
      C_Timer.After(5, function() if not inCombat() then meterSnapshot("outside") end end)
    end
  elseif event == "LOADING_SCREEN_ENABLED" then
    cause.loading, cause.loadingAt = true, now()
  elseif event == "LOADING_SCREEN_DISABLED" then
    cause.loading = false
  elseif event == "UNIT_SPELLCAST_SUCCEEDED" then
    local unit, _, spellID = ...
    if unit == "player" and not isSecret(spellID) then cause.spell, cause.spellAt = spellID, now() end
  elseif event == "PLAYER_CONTROL_LOST" or event == "PLAYER_CONTROL_GAINED" then
    local ok, taxi = pcall(UnitOnTaxi, "player")
    if ok and not isSecret(taxi) and taxi then cause.taxiAt = now() end
    if event == "PLAYER_CONTROL_GAINED" and cause.taxiAt > 0 and now() - cause.taxiAt < 5 then cause.taxiAt = now() end
  elseif event == "UNIT_SPELLCAST_SENT" then
    spellcastSent(...)
  elseif event == "PLAYER_UPDATE_RESTING" then
    restingChanged()
  elseif event == "PLAYER_FLAGS_CHANGED" then
    if ... == "player" then afkChanged() end
  elseif event == "AUCTION_HOUSE_AUCTION_CREATED" then
    trigger("auction")
  elseif event == "CHAT_MSG_SYSTEM" then
    seen("CHAT_MSG_SYSTEM", (...))
  elseif event == "UI_INFO_MESSAGE" or event == "UI_ERROR_MESSAGE" then
    local _, text = ...
    seen(event, text)
  elseif event == "CHAT_MSG_SAY" or event == "CHAT_MSG_YELL" or event == "CHAT_MSG_EMOTE" then
    chatEcho(event, ...)
  elseif event == "PLAYER_REGEN_DISABLED" then
    fights = fights + 1
    if fights <= 3 then
      C_Timer.After(3, function()
        if inCombat() then
          meterSnapshot("combat")
          petHealth("in combat")
          if UnitExists("target") then unitIsUnitCheck("target", "target") end
        end
      end)
    end
  elseif event == "PLAYER_REGEN_ENABLED" then
    combatEnd = now()
    C_Timer.After(1, function() if not inCombat() then meterSnapshot("after combat") end end)
    petHealth("out of combat")
  elseif event == "PLAYER_TARGET_CHANGED" then
    if UnitExists("target") then
      local ok, hostile = pcall(UnitCanAttack, "player", "target")
      if ok and not isSecret(hostile) then unitIsUnitCheck("target", hostile and "enemy target" or "friendly target") end
    end
  elseif event == "NAME_PLATE_UNIT_ADDED" then
    local token = ...
    if type(token) == "string" and not isSecret(token) and UnitExists("target") then
      local ok, hostile = pcall(UnitCanAttack, "player", token)
      if ok and not isSecret(hostile) and hostile then unitIsUnitCheck(token, "enemy nameplate") end
    end
  elseif event == "UNIT_PET" then
    if ... == "player" then C_Timer.After(1, function() petHealth(inCombat() and "in combat" or "out of combat") end) end
  end
  for _, e in ipairs(FEED) do
    if e == event then feed(event, ...) break end
  end
end)
frame:RegisterEvent("ADDON_LOADED")
frame:RegisterEvent("ADDON_ACTION_FORBIDDEN")
frame:RegisterEvent("ADDON_ACTION_BLOCKED")

SlashCmdList.APICHECKS = function(msg)
  msg = (msg or ""):lower()
  if msg == "chat" then
    if db.sendPending then return sendFromKeypress() end
    say("This sends \".\" in /say, /yell and /emote, so people near you see it. Run it once in the open world and once in a dungeon. Type |cffffff00/fapi checks chat yes|r to go.")
  elseif msg == "chat yes" then
    sendTest()
  else
    local function n(t) local c = 0 for _ in pairs(t or {}) do c = c + 1 end return c end
    say(("v%s. Seen: %d double-fire episodes, %d zone changes, %d chat triggers, %d combat feeds, %d secret checks. /fapi checks chat tests sending chat."):format(
      VERSION, (db.twice.PLAYER_DEAD and db.twice.PLAYER_DEAD.episodes or 0) + (db.twice.MERCHANT_CLOSED and db.twice.MERCHANT_CLOSED.episodes or 0)
        + (db.twice.AUCTION_HOUSE_CLOSED and db.twice.AUCTION_HOUSE_CLOSED.episodes or 0),
      #db.zone.recent, n(db.chat.triggers), n(db.feed), n(db.secrets.unitIsUnit) + n(db.secrets.spellcastSent) + n(db.secrets.pet)))
  end
end
