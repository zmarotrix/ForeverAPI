-- API watch: the same getters ApiProbe calls, but in the situations it can't reach on its own. Background collector
-- for ForeverAPI.
--
-- A situation is where you are and what is happening: "party/boss" is a dungeon boss fight, "none/combat" a fight in
-- the open world, "raid/idle" standing in a raid. The first time the watch sees a situation it calls the no-argument
-- getters once; the first time it sees a kind of unit there (your target as an enemy NPC, a party member, a nameplate,
-- a boss...) it calls the unit getters on it. Only one run at a time; a run stops if the situation changes under it.
-- It also logs every switch of C_RestrictedActions' restriction types with the situation it happened in.
--
-- Stores result shapes (types, secret or not, errors), never a value. Never calls a Cancel*/UnitSet*/Request*/Reward*
-- name, anything that crashed the client, or anything the probe saw refused.

local ADDON = ...
local VERSION = "0.1.0"
local PER_FRAME = 12
local MAX_KEYS = 30
local MAX_TRANSITIONS = 400

ApiWatchDB = ApiWatchDB or {}
local db
local leads = ApiProbeLeads or { calls = {} }
local G = _G
local rawget, pcall, type, select, pairs = rawget, pcall, type, select, pairs
local issecretvalue = rawget(G, "issecretvalue")
local function isSecret(v) return issecretvalue ~= nil and issecretvalue(v) == true end
local function say(msg) print("|cff9ec8ffAPI watch|r " .. msg) end
local function inCombat() return InCombatLockdown and InCombatLockdown() and true or false end
local function buildKey()
  local version, build = GetBuildInfo()
  return tostring(version) .. "." .. tostring(build)
end
local function errText(e)
  if isSecret(e) then return "<secret error>" end
  e = tostring(e):gsub("Interface[\\/]AddOns[\\/]" .. ADDON .. "[\\/][^:]*:%d+: ", "")
  return #e > 200 and e:sub(1, 200) .. "..." or e
end

-------------------------------------------------------------------------------------------
-- What to call
-------------------------------------------------------------------------------------------

local GETTER = { "^Get[%u%d]", "^Is[%u%d]", "^Has[%u%d]", "^Can[%u%d]", "^Should[%u%d]", "^Are[%u%d]",
  "^Does[%u%d]", "^Unit[%u%d]", "^Num[%u%d]" }
local function isGetter(name)
  if name:find("Reward") or name:find("Request") or name:find("Cancel") or name:find("^UnitSet") then return false end
  for _, p in ipairs(GETTER) do if name:find(p) then return true end end
  return false
end

local plainPlan, unitPlan = {}, {}
for _, c in ipairs(leads.calls or {}) do
  local key = c[1] and (c[1] .. "." .. c[2]) or c[2]
  if c[3] == nil then plainPlan[#plainPlan + 1] = { key = key, ns = c[1], fn = c[2] }
  elseif c[3] == "unit" then unitPlan[#unitPlan + 1] = { key = key, ns = c[1], fn = c[2] } end
end
for _, name in ipairs(leads.undocumented or {}) do
  if name:find("^Unit") then unitPlan[#unitPlan + 1] = { key = name, fn = name }
  else plainPlan[#plainPlan + 1] = { key = name, fn = name } end
end

local function skipped(key)
  local crash = leads.crashers or {}
  if crash[key] then return "crashed the client" end
  local ns = key:match("^([%w_]+)%.")
  if ns and crash[ns .. "."] then return "crashed the client (whole namespace skipped)" end
  if leads.refused and leads.refused[key] then return "refused to the probe" end
  if db.skip[key] then return db.skip[key] end
  local fn = key:match("([%w_]+)$")
  if not isGetter(fn) then return "not a getter" end
end

-------------------------------------------------------------------------------------------
-- Situations and units
-------------------------------------------------------------------------------------------

local encounter = false

local function situation()
  local _, zone = IsInInstance()
  local phase = encounter and "boss" or inCombat() and "combat" or "idle"
  return (zone or "none") .. "/" .. phase
end

local function plainBool(f, ...)
  local ok, v = pcall(f, ...)
  if not ok or isSecret(v) then return nil end
  return v and true or false
end

-- the kind of a unit token right now, e.g. "target: enemy npc"; nil when the token is empty
local function unitKind(token)
  if not plainBool(UnitExists, token) then return nil end
  local slot = token:gsub("%d+", "")
  if slot == "player" or slot == "party" or slot == "raid" or slot == "pet" then return slot end
  local isPlayer = plainBool(UnitIsPlayer, token)
  local enemy = plainBool(UnitCanAttack, "player", token)
  local who = (enemy == nil and "unknown") or (enemy and "enemy" or "friendly")
  who = who .. " " .. (isPlayer == nil and "?" or isPlayer and "player" or "npc")
  return slot .. ": " .. who
end

local function candidates()
  local out = { "player", "target", "focus", "pet", "targettarget", "party1", "raid1", "boss1" }
  for i = 1, 40 do
    if plainBool(UnitExists, "nameplate" .. i) then out[#out + 1] = "nameplate" .. i break end
  end
  return out
end

-------------------------------------------------------------------------------------------
-- Restriction transitions
-------------------------------------------------------------------------------------------

local lastRestrictions
local function restrictionsNow()
  local ra = rawget(G, "C_RestrictedActions")
  local E = rawget(G, "Enum") and Enum.AddOnRestrictionType
  if not (ra and ra.IsAddOnRestrictionActive and E) then return "unavailable" end
  local on = {}
  for key, value in pairs(E) do
    local ok, v = pcall(ra.IsAddOnRestrictionActive, value)
    if not ok then on[#on + 1] = key .. "=error"
    elseif isSecret(v) then on[#on + 1] = key .. "=secret"
    elseif v then on[#on + 1] = key end
  end
  table.sort(on)
  return #on > 0 and table.concat(on, ",") or "none"
end

local function noteRestrictions(reason)
  local now = restrictionsNow()
  if now == lastRestrictions then return end
  lastRestrictions = now
  local list = db.transitions
  list[#list + 1] = { at = GetServerTime(), on = now, situation = situation(), reason = reason }
  while #list > MAX_TRANSITIONS do table.remove(list, 1) end
end

-------------------------------------------------------------------------------------------
-- Runs
-------------------------------------------------------------------------------------------

local function shape(v)
  if isSecret(v) then
    local ok, t = pcall(type, v)
    return "secret:" .. (ok and t or "?")
  end
  local t = type(v)
  if t ~= "table" then return t end
  local keys, n = {}, 0
  local ok = pcall(function()
    for k, val in pairs(v) do
      n = n + 1
      if n <= MAX_KEYS then
        keys[#keys + 1] = (isSecret(k) and "<secret key>" or type(k) == "string" and k or "[" .. type(k) .. "]") .. "=" .. (isSecret(val) and "secret" or type(val))
      end
    end
  end)
  if not ok then return "table:unreadable" end
  table.sort(keys)
  if n > MAX_KEYS then keys[#keys + 1] = "...(" .. n .. ")" end
  return "table{" .. table.concat(keys, ",") .. "}"
end

local function capture(ok, ...)
  if not ok then return { error = errText((...)) } end
  local n = select("#", ...)
  local out = { n = n }
  for i = 1, math.min(n, 20) do out[i] = shape((select(i, ...))) end
  return out
end

local job, currentCall, forbiddenHit

local function startRun(sit, label, token, plan)
  local s = db.situations[sit] or { runs = {} }
  db.situations[sit] = s
  local run = { at = GetServerTime(), token = token, results = {} }
  s.runs[label] = run
  job = { situation = sit, label = label, token = token, plan = plan, i = 1, run = run }
end

local function stopRun(why)
  job.run.partial = why
  job = nil
end

local function step()
  if situation() ~= job.situation then stopRun("situation changed") return end
  if job.token and job.token ~= "player" and not plainBool(UnitExists, job.token) then stopRun("unit gone") return end
  local last = math.min(job.i + PER_FRAME - 1, #job.plan)
  for i = job.i, last do
    local c = job.plan[i]
    -- a string local, so a client crash log's Lua stack names the call
    local callKey = c.key
    local why = skipped(callKey)
    local rec
    if why then
      rec = { skipped = why }
    else
      local fn
      if c.ns then
        local t = rawget(G, c.ns)
        fn = type(t) == "table" and rawget(t, c.fn)
      else
        fn = rawget(G, c.fn)
      end
      if type(fn) ~= "function" then
        rec = { missing = true }
      else
        currentCall, forbiddenHit = callKey, nil
        if job.token then rec = capture(pcall(fn, job.token)) else rec = capture(pcall(fn)) end
        currentCall = nil
        if forbiddenHit then rec.forbidden = true end
      end
    end
    job.run.results[callKey] = rec
  end
  job.i = last + 1
  if job.i > #job.plan then
    job.run.done = true
    job = nil
  end
end

-- what to run next in this situation, if anything
local function nextRun()
  local sit = situation()
  local s = db.situations[sit]
  local function done(label) return s and s.runs[label] and s.runs[label].done end
  -- the open world's plain getters are ApiProbe's job; everywhere else, once per situation
  if sit ~= "none/idle" and sit ~= "none/combat" and not done("getters") then
    return sit, "getters", nil, plainPlan
  end
  for _, token in ipairs(candidates()) do
    local kind = unitKind(token)
    if kind and not done(kind) then return sit, kind, token, unitPlan end
  end
end

local idle = 0
local function tick(elapsed)
  if job then step() return end
  idle = idle + elapsed
  if idle < 1 then return end -- look for new work once a second
  idle = 0
  local sit, label, token, plan = nextRun()
  if sit then startRun(sit, label, token, plan) end
end

-------------------------------------------------------------------------------------------
-- Wiring
-------------------------------------------------------------------------------------------

local frame = CreateFrame("Frame")
frame:SetScript("OnUpdate", function(_, elapsed) if db then tick(elapsed) end end)
frame:SetScript("OnEvent", function(_, event, a1, a2)
  if event == "ADDON_LOADED" and a1 == ADDON then
    db = ApiWatchDB
    if db.build ~= buildKey() or db.probe ~= VERSION or db.leads ~= leads.build then
      ApiWatchDB = { build = buildKey(), probe = VERSION, leads = leads.build, situations = {}, transitions = {},
        skip = db.build == buildKey() and db.skip or {} }
      db = ApiWatchDB
    end
    db.skip = db.skip or {}
    return
  end
  if not db then return end
  if event == "ADDON_ACTION_BLOCKED" or event == "ADDON_ACTION_FORBIDDEN" then
    if a1 == ADDON and currentCall then
      forbiddenHit = true
      db.skip[currentCall] = event == "ADDON_ACTION_FORBIDDEN" and "forbidden" or "blocked"
    end
    return
  end
  if event == "ENCOUNTER_START" then encounter = true
  elseif event == "ENCOUNTER_END" then encounter = false
  elseif event == "PLAYER_ENTERING_WORLD" then encounter = false end
  noteRestrictions(event)
end)
for _, e in ipairs({ "ADDON_LOADED", "ADDON_ACTION_BLOCKED", "ADDON_ACTION_FORBIDDEN", "PLAYER_ENTERING_WORLD",
  "ZONE_CHANGED_NEW_AREA", "PLAYER_REGEN_DISABLED", "PLAYER_REGEN_ENABLED", "ENCOUNTER_START", "ENCOUNTER_END",
  "CHALLENGE_MODE_START", "CHALLENGE_MODE_COMPLETED", "PVP_MATCH_ACTIVE", "PVP_MATCH_COMPLETE", "GROUP_ROSTER_UPDATE",
  "ADDON_RESTRICTION_STATE_CHANGED" }) do
  pcall(frame.RegisterEvent, frame, e) -- the last one may not exist on this client
end

SLASH_APIWATCH1 = "/apiwatch"
SlashCmdList.APIWATCH = function()
  local lines = {}
  for sit, s in pairs(db.situations) do
    local n = 0
    for _ in pairs(s.runs) do n = n + 1 end
    lines[#lines + 1] = sit .. " (" .. n .. ")"
  end
  table.sort(lines)
  say(("v%s. Now: %s, restrictions %s%s."):format(VERSION, situation(), restrictionsNow(), job and (", running " .. job.label) or ""))
  say("Seen: " .. (#lines > 0 and table.concat(lines, ", ") or "nothing yet") .. ". Restriction switches logged: " .. #db.transitions .. ".")
end
