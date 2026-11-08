-- API widgets: what add-on code can do with a secret value on this client. Background collector for ForeverAPI.
--
-- Runs by itself once per client build: 10 seconds after login (out of combat), and again in your first fight.
-- A secret comes from a getter the probe found always secret (UnitHealth("player"), UnitInRange("player")).
--   ops      Lua operations on the secret: type, tostring, arithmetic, comparison, concatenation, as a table key...
--   setters  every widget setter in plan.lua (generated from Blizzard's docs): first with plain values as a control,
--            then with the secret in its first number or true/false slot, on hidden frames of our own.
-- Stores ok or the error text for each, never a value.

local ADDON = ...
local VERSION = "0.1.1"
local PER_FRAME = 15

ApiWidgetsDB = ApiWidgetsDB or {}
local db
local plan = ApiWidgetsPlan or { build = "none", setters = {} }
local G = _G
local issecretvalue = rawget(G, "issecretvalue")

local function isSecret(v) return issecretvalue ~= nil and issecretvalue(v) == true end
local function say(msg) print("|cff9ec8ffAPI widgets|r " .. msg) end
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
local function result(ok, err) if ok then return "ok" end return errText(err) end

-- secrets to test with: { number = s, boolean = b } (whichever this client hands out)
local function secrets()
  local out = {}
  local ok, n = pcall(UnitHealth, "player")
  if ok and isSecret(n) then out.number = n end
  local ok2, b = pcall(UnitInRange, "player")
  if ok2 and isSecret(b) then out.boolean = b end
  return out
end

-------------------------------------------------------------------------------------------
-- Lua operations on a secret
-------------------------------------------------------------------------------------------

local OPS = {
  { "type(s)", function(s) return type(s) end, "number" },
  { "issecretvalue(s)", function(s) return issecretvalue(s) end, "number" },
  { "tostring(s)", function(s) return tostring(s) end, "number" },
  { "tonumber(s)", function(s) return tonumber(s) end, "number" },
  { "s + 1", function(s) return s + 1 end, "number" },
  { "s * 2", function(s) return s * 2 end, "number" },
  { "-s", function(s) return -s end, "number" },
  { "s == s", function(s) return s == s end, "number" },
  { "s == 1", function(s) return s == 1 end, "number" },
  { "s < 1", function(s) return s < 1 end, "number" },
  { "s .. \"\"", function(s) return s .. "" end, "number" },
  { "string.format(\"%d\", s)", function(s) return string.format("%d", s) end, "number" },
  { "math.floor(s)", function(s) return math.floor(s) end, "number" },
  { "math.max(s, 1)", function(s) return math.max(s, 1) end, "number" },
  { "t[s] = 1 (as a key)", function(s) local t = {} t[s] = 1 return true end, "number" },
  { "t[1] = s (as a value)", function(s) local t = {} t[1] = s return true end, "number" },
  { "select(\"#\", s)", function(s) return select("#", s) end, "number" },
  { "if b then", function(b) if b then return 1 end return 2 end, "boolean" },
  { "not b", function(b) return not b end, "boolean" },
  { "b == true", function(b) return b == true end, "boolean" },
  { "b and 1 or 2", function(b) return b and 1 or 2 end, "boolean" },
}

local function runOps(sec)
  local out = {}
  for _, op in ipairs(OPS) do
    local s = sec[op[3]]
    if s == nil then
      out[op[1]] = "no secret " .. op[3] .. " available"
    else
      local ok, v = pcall(op[2], s)
      if not ok then
        out[op[1]] = errText(v)
      elseif op[1] == "type(s)" and not isSecret(v) then
        out[op[1]] = "ok: " .. tostring(v) -- the type name is not a value of yours
      else
        out[op[1]] = isSecret(v) and "ok (result secret)" or "ok"
      end
    end
  end
  return out
end

-------------------------------------------------------------------------------------------
-- Widget setters
-------------------------------------------------------------------------------------------

local ANIMATIONS = { Animation = true, Alpha = true, Translation = true, Scale = true, LineScale = true,
  LineTranslation = true, Rotation = true, Path = true, FlipBook = true, TextureCoordTranslation = true, VertexColor = true }
local holder, objects = nil, {}
local function object(kind)
  if objects[kind] ~= nil then return objects[kind] or nil end
  holder = holder or CreateFrame("Frame", nil, UIParent)
  holder:Hide()
  local ok, obj = pcall(function()
    if kind == "Texture" then return holder:CreateTexture() end
    if kind == "MaskTexture" then return holder:CreateMaskTexture() end
    if kind == "Line" then return holder:CreateLine() end
    if kind == "FontString" then local fs = holder:CreateFontString() fs:SetFontObject(GameFontNormal) return fs end
    if kind == "AnimationGroup" then return holder:CreateAnimationGroup() end
    if kind == "Font" then return CreateFont("ApiWidgetsFont") end
    if ANIMATIONS[kind] then
      holder.group = holder.group or holder:CreateAnimationGroup()
      return holder.group:CreateAnimation(kind)
    end
    return CreateFrame(kind, nil, holder) -- plan.lua only names frame types the probe created in game
  end)
  objects[kind] = ok and obj or false
  return ok and obj or nil
end

-- argument kinds: "S" the secret (number or boolean, by slot type), "n:<num>", "b:false", "s:<text>"
local function args(kinds, sec, plainRun)
  local vals = {}
  for i, k in ipairs(kinds) do
    -- (not "plainRun and false or secret": false would fall through to the secret)
    if k == "Sn" then
      if plainRun then vals[i] = 1 else vals[i] = sec.number end
    elseif k == "Sb" then
      if plainRun then vals[i] = false else vals[i] = sec.boolean end
    elseif k == "nil" then vals[i] = nil
    elseif k:sub(1, 2) == "n:" then vals[i] = tonumber(k:sub(3))
    elseif k == "b:false" then vals[i] = false
    elseif k:sub(1, 2) == "s:" then vals[i] = k:sub(3)
    end
  end
  return vals, #kinds
end

-------------------------------------------------------------------------------------------
-- Runs
-------------------------------------------------------------------------------------------

local job

local function start(phase)
  if job then return end
  local sec = secrets()
  local run = { at = GetServerTime(), combat = inCombat(), probe = VERSION, plan = plan.build,
    hasNumber = sec.number ~= nil, hasBoolean = sec.boolean ~= nil, ops = runOps(sec), setters = {} }
  db.runs[phase] = run
  job = { phase = phase, run = run, sec = sec, i = 1 }
end

local function step()
  local run, sec = job.run, job.sec
  if job.phase == "combat" and not inCombat() then
    run.partial = true
    job = nil
    return
  end
  local last = math.min(job.i + PER_FRAME - 1, #plan.setters)
  for i = job.i, last do
    local entry = plan.setters[i]
    -- a string local, so a client crash log's Lua stack names the call
    local callKey = entry[1] .. ":" .. entry[2]
    local obj = object(entry[1])
    local rec
    if not obj then
      rec = { plain = "no " .. entry[1] .. " object" }
    elseif type(obj[entry[2]]) ~= "function" then
      rec = { plain = "no such method" }
    else
      local fn = obj[entry[2]]
      local pv, pn = args(entry[3], sec, true)
      rec = { plain = result(pcall(fn, obj, unpack(pv, 1, pn))) }
      local needs = false
      for _, k in ipairs(entry[3]) do
        if (k == "Sn" and sec.number == nil) or (k == "Sb" and sec.boolean == nil) then needs = true end
      end
      if needs then
        rec.secret = "no secret of that kind available"
      else
        local sv, sn = args(entry[3], sec, false)
        rec.secret = result(pcall(fn, obj, unpack(sv, 1, sn)))
      end
    end
    run.setters[callKey] = rec
  end
  job.i = last + 1
  if job.i > #plan.setters then
    run.done = true
    job = nil
    say(("%s run done (%d setters). It saves at your next /reload or logout."):format(run.combat and "combat" or "out-of-combat", #plan.setters))
  end
end

local frame = CreateFrame("Frame")
frame:SetScript("OnUpdate", function() if job then step() end end)
frame:SetScript("OnEvent", function(_, event, a1)
  if event == "ADDON_LOADED" and a1 == ADDON then
    db = ApiWidgetsDB
    if db.build ~= buildKey() or db.probe ~= VERSION or db.plan ~= plan.build then
      ApiWidgetsDB = { build = buildKey(), probe = VERSION, plan = plan.build, runs = {} }
      db = ApiWidgetsDB
    end
  elseif event == "PLAYER_LOGIN" then
    if not (db.runs.outside and db.runs.outside.done) then
      C_Timer.After(10, function() if not inCombat() then start("outside") end end)
    end
  elseif event == "PLAYER_REGEN_DISABLED" then
    if db.runs.outside and db.runs.outside.done and not (db.runs.combat and db.runs.combat.done) then
      db.runs.combat = nil
      start("combat")
    end
  end
end)
frame:RegisterEvent("ADDON_LOADED")
frame:RegisterEvent("PLAYER_LOGIN")
frame:RegisterEvent("PLAYER_REGEN_DISABLED")

SLASH_APIWIDGETS1 = "/apiwidgets"
SlashCmdList.APIWIDGETS = function(msg)
  if msg == "rerun" then
    db.runs = {}
    if not inCombat() then start("outside") end
    return
  end
  local o, c = db.runs.outside, db.runs.combat
  say(("v%s, %d setters planned. Out of combat: %s. In combat: %s. /apiwidgets rerun to test again."):format(VERSION, #plan.setters,
    o and (o.done and "done" or "partial") or "not yet", c and (c.done and "done" or "partial") or "waits for your next fight"))
end
