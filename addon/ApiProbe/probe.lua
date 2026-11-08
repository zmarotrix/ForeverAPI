-- API probe: records what this client's add-on API really is, so the docs built from it (G:\Projects\ForeverAPI)
-- say only what the game confirmed.
--
--   dump    every global, every secure table's members (C_* namespaces, Enum, Constants, mixins), one object of every
--           widget type with its methods and script handlers, every candidate event checked with RegisterEvent, CVars
--           with their help text and defaults, and the add-on list. Runs by itself once per client build.
--   calls   calls the getters in leads.lua (from Blizzard's own docs) plus the client's undocumented built-in getters,
--           out of combat at once and again in your next combat, and records the shape of what came back.
--   live    counts every event that fires and the argument types it carried.
--
-- What it stores: names, kinds and types. Never a return value, an event argument or a CVar's current value, so
-- nothing about your character, chat or account lands in the file. Secret values are only ever passed to issecretvalue.
-- It never casts, targets, sends or changes a setting; the only calls it makes are getters (Get/Is/Has/Can/...).

local ADDON = ...
local VERSION = "0.2.0"
local CHUNK = 1500          -- globals examined per frame while dumping
local CALLS_PER_FRAME = 20  -- getters called per frame
local MAX_MEMBERS = 10000   -- members recorded per table (Enum alone has thousands)
local MAX_SIGS = 4          -- distinct argument signatures kept per event
local MAX_KEYS = 40         -- keys described per returned table

ApiProbeDB = ApiProbeDB or {}
local db
local leads = ApiProbeLeads or { events = {}, calls = {} }

local G = _G
local rawget, pcall, type, tostring, select, pairs, next = rawget, pcall, type, tostring, select, pairs, next
local issecretvalue = rawget(G, "issecretvalue")
local issecurevariable = rawget(G, "issecurevariable")

local function isSecret(v)
  return issecretvalue ~= nil and issecretvalue(v) == true
end

local function say(text)
  print("|cff9ec8ffAPI probe|r " .. text)
end

local function now()
  local f = rawget(G, "GetServerTime") or rawget(G, "time")
  return f and f() or 0
end

local function inCombat()
  local f = rawget(G, "InCombatLockdown")
  return f and f() and true or false
end

local function buildKey()
  local f = rawget(G, "GetBuildInfo")
  if not f then return "unknown" end
  local version, build = f()
  return tostring(version) .. "." .. tostring(build)
end

-- Error text without our own file path, cut short.
local function errText(e)
  if isSecret(e) then return "<secret error>" end
  e = tostring(e)
  e = e:gsub("Interface[\\/]AddOns[\\/]" .. ADDON .. "[\\/][^:]*:%d+: ", "")
  return #e > 240 and e:sub(1, 240) .. "..." or e
end

-------------------------------------------------------------------------------------------
-- What a value is
-------------------------------------------------------------------------------------------

-- Function kind: "fC" built into the client, "fL" written in Lua, "f?" when this client gives no way to tell.
local function fnKind(f)
  local ok, s = pcall(tostring, f)
  if ok and type(s) == "string" and s:find("builtin", 1, true) then return "fC" end
  local dump = rawget(string, "dump")
  if dump then return pcall(dump, f) and "fL" or "fC" end
  return "f?"
end

local function isWidget(v)
  return type(v) == "table" and type(rawget(v, 0)) == "userdata"
end

local function objectType(v)
  local ok, t = pcall(function() return v:GetObjectType() end)
  if ok and type(t) == "string" then return t end
  return "forbidden"
end

-- Compact code for one value. Numbers and booleans keep their value; strings don't (most are localized UI text).
local function code(v, keepStrings)
  if isSecret(v) then return "secret" end
  local t = type(v)
  if t == "function" then return fnKind(v) end
  if t == "table" then return isWidget(v) and ("o:" .. objectType(v)) or "t" end
  if t == "number" then return "n:" .. tostring(v) end
  if t == "boolean" then return v and "b:true" or "b:false" end
  if t == "string" then return keepStrings and ("s:" .. (#v > 200 and v:sub(1, 200) or v)) or "s" end
  if t == "userdata" then return "u" end
  if t == "thread" then return "x" end
  return t
end

-- Whether name is still Blizzard's (secure) and, if not, which add-on last wrote it.
local function taint(tbl, key)
  if not issecurevariable then return true end
  local ok, secure, by = pcall(issecurevariable, tbl, key)
  if not ok then return true end
  return secure and true or false, by
end

-- Members of a table: name -> code, nested one level for Enum / Constants style tables.
local function members(t, nested, keepStrings)
  local out, n = {}, 0
  local ok = pcall(function()
    for k, v in pairs(t) do
      if type(k) == "string" or type(k) == "number" then
        n = n + 1
        if n > MAX_MEMBERS then out["(more)"] = "truncated"; break end
        if nested and type(v) == "table" and not isWidget(v) then
          out[k] = members(v, false, true)
        else
          out[k] = code(v, keepStrings)
        end
      end
    end
  end)
  if not ok then out["(error)"] = "pairs failed" end
  return out
end

-------------------------------------------------------------------------------------------
-- Widgets: one of each type, its methods and script handlers
-------------------------------------------------------------------------------------------

local FRAME_TYPES = { "Frame", "Button", "CheckButton", "EditBox", "ScrollFrame", "Slider", "StatusBar", "Cooldown",
  "ColorSelect", "GameTooltip", "MessageFrame", "ScrollingMessageFrame", "SimpleHTML", "Model", "PlayerModel",
  "DressUpModel", "CinematicModel", "TabardModel", "ModelScene", "MovieFrame", "Browser", "FogOfWarFrame",
  "UnitPositionFrame", "OffScreenFrame", "ArchaeologyDigSiteFrame", "QuestPOIFrame", "ScenarioPOIFrame", "Checkout",
  "EventFrame", "EventButton", "EventEditBox", "ItemButton", "DropdownButton" }
-- Only real creatable types: the client prints a LUA_WARNING for an unknown type even inside pcall.

local SCRIPTS = { "OnLoad", "OnShow", "OnHide", "OnEvent", "OnUpdate", "OnSizeChanged", "OnEnter", "OnLeave",
  "OnMouseDown", "OnMouseUp", "OnMouseWheel", "OnClick", "PreClick", "PostClick", "OnDoubleClick", "OnDragStart",
  "OnDragStop", "OnReceiveDrag", "OnKeyDown", "OnKeyUp", "OnChar", "OnAttributeChanged", "OnEnable", "OnDisable",
  "OnValueChanged", "OnMinMaxChanged", "OnTextChanged", "OnTextSet", "OnEnterPressed", "OnEscapePressed",
  "OnTabPressed", "OnSpacePressed", "OnEditFocusGained", "OnEditFocusLost", "OnCursorChanged",
  "OnInputLanguageChanged", "OnArrowPressed", "OnHorizontalScroll", "OnVerticalScroll", "OnScrollRangeChanged",
  "OnTooltipSetDefaultAnchor", "OnTooltipCleared", "OnTooltipAddMoney", "OnTooltipSetItem", "OnTooltipSetUnit",
  "OnTooltipSetSpell", "OnHyperlinkClick", "OnHyperlinkEnter", "OnHyperlinkLeave", "OnMessageScrollChanged",
  "OnColorSelect", "OnCooldownDone", "OnModelLoaded", "OnModelCleared", "OnAnimFinished", "OnAnimStarted",
  "OnDressModel", "OnMovieFinished", "OnMovieShowSubtitle", "OnMovieHideSubtitle", "OnGamePadButtonDown",
  "OnGamePadButtonUp", "OnGamePadStick", "OnPlay", "OnPause", "OnStop", "OnFinished", "OnLoop", "OnExternalLink",
  "OnButtonUpdate", "OnError", "OnRequestNewSize", "OnUpdateModel", "OnPanFinished", "OnMouseWheelChanged" }

local ANIMATIONS = { "Animation", "Alpha", "Translation", "Scale", "LineScale", "LineTranslation", "Rotation", "Path",
  "FlipBook", "TextureCoordTranslation", "VertexColor" }

local function describeObject(obj)
  local rec = { objectType = objectType(obj), methods = {}, scripts = {} }
  local mt = getmetatable(obj)
  local index = type(mt) == "table" and rawget(mt, "__index")
  if type(index) == "table" then
    for k, v in pairs(index) do
      if type(k) == "string" then rec.methods[k] = code(v) end
    end
  else
    rec.methods["(no __index table)"] = type(index)
  end
  if type(obj.HasScript) == "function" then
    for _, h in ipairs(SCRIPTS) do
      local ok, has = pcall(obj.HasScript, obj, h)
      if ok and has then rec.scripts[#rec.scripts + 1] = h end
    end
  end
  return rec
end

local function dumpWidgets()
  local out = {}
  local CreateFrame = rawget(G, "CreateFrame")
  local parent = rawget(G, "UIParent")
  local holder
  if CreateFrame then
    holder = CreateFrame("Frame", nil, parent)
    holder:Hide()
  end
  local made = {}
  local function try(label, make)
    local ok, obj = pcall(make)
    if ok and obj then
      made[label] = obj
      local described, rec = pcall(describeObject, obj)
      out[label] = described and rec or { error = errText(rec) }
      if described and type(obj.Hide) == "function" then pcall(obj.Hide, obj) end
      return obj
    end
    out[label] = { error = ok and "nothing created" or errText(obj) }
  end
  if CreateFrame then
    for _, t in ipairs(FRAME_TYPES) do
      try(t, function() return CreateFrame(t, nil, holder) end)
    end
  end
  if holder then
    try("Texture", function() return holder:CreateTexture() end)
    try("MaskTexture", function() return holder:CreateMaskTexture() end)
    try("Line", function() return holder:CreateLine() end)
    try("FontString", function() return holder:CreateFontString() end)
    local group = try("AnimationGroup", function() return holder:CreateAnimationGroup() end)
    if group then
      for _, a in ipairs(ANIMATIONS) do
        local anim = try(a, function() return group:CreateAnimation(a) end)
        if a == "Path" and anim then
          try("ControlPoint", function() return anim:CreateControlPoint() end)
        end
      end
    end
  end
  local CreateFont = rawget(G, "CreateFont")
  if CreateFont then try("Font", function() return CreateFont("ApiProbeFont") end) end
  local scene = made.ModelScene
  if scene and scene.CreateActor then try("ModelSceneActor", function() return scene:CreateActor() end) end
  return out
end

-------------------------------------------------------------------------------------------
-- Events: is each candidate name real?
-------------------------------------------------------------------------------------------

local CONTROL_EVENT = "APIPROBE_NOT_A_REAL_EVENT"

-- What the probe is doing right now, so ADDON_ACTION_FORBIDDEN (which fires inside the call) can name it.
local currentCall, forbiddenHit

-- Names that must never be touched again: learned in game (db.skip, kept across sessions) or from crash logs
-- (leads.crashers, written by tools/apidoc.py extract).
local function skipped(key)
  if leads.crashers and leads.crashers[key] then return "crashed the client" end
  if db.skip and db.skip[key] then return db.skip[key] end
end

local function checkEvents(names)
  local out = {}
  local CreateFrame = rawget(G, "CreateFrame")
  if not CreateFrame then return out end
  local f = CreateFrame("Frame")
  local utils = rawget(G, "C_EventUtils")
  local isValid = utils and utils.IsEventValid
  local function one(name)
    local rec = {}
    local why = skipped("event:" .. name)
    if why then
      out[name] = { register = why }
      return
    end
    currentCall, forbiddenHit = "event:" .. name, nil
    local ok, err = pcall(f.RegisterEvent, f, name)
    currentCall = nil
    rec.register = forbiddenHit and "forbidden" or ok and "ok" or errText(err)
    if ok then pcall(f.UnregisterEvent, f, name) end
    if isValid then
      local vok, v = pcall(isValid, name)
      rec.valid = vok and not isSecret(v) and (v and true or false) or nil
    end
    out[name] = rec
  end
  one(CONTROL_EVENT)
  for _, name in ipairs(names) do
    if type(name) == "string" and out[name] == nil then one(name) end
  end
  return out
end

-------------------------------------------------------------------------------------------
-- CVars, add-ons, Lua
-------------------------------------------------------------------------------------------

local function dumpCVars()
  local out = {}
  local console = rawget(G, "C_Console")
  local all = console and console.GetAllCommands or rawget(G, "ConsoleGetAllCommands")
  if not all then return { ["(missing)"] = "no C_Console.GetAllCommands" } end
  local ok, list = pcall(all)
  if not ok or type(list) ~= "table" then return { ["(error)"] = errText(list) } end
  local cvar = rawget(G, "C_CVar")
  local getDefault = cvar and cvar.GetCVarDefault
  for _, c in ipairs(list) do
    if type(c) == "table" and type(c.command) == "string" then
      local rec = { help = type(c.help) == "string" and c.help or nil, category = c.category, kind = c.commandType }
      -- the default, never the current value (some CVars hold account details)
      if getDefault and c.commandType == 0 then
        local dok, d = pcall(getDefault, c.command)
        if dok and type(d) == "string" and not isSecret(d) then rec.default = d end
      end
      out[c.command] = rec
    end
  end
  return out
end

local function dumpAddOns()
  local out = {}
  local A = rawget(G, "C_AddOns")
  local count = A and A.GetNumAddOns or rawget(G, "GetNumAddOns")
  local info = A and A.GetAddOnInfo or rawget(G, "GetAddOnInfo")
  local loaded = A and A.IsAddOnLoaded or rawget(G, "IsAddOnLoaded")
  if not (count and info) then return out end
  for i = 1, count() do
    local ok, name = pcall(info, i)
    if ok and type(name) == "string" then
      out[name] = loaded and loaded(name) and "loaded" or "not loaded"
    end
  end
  return out
end

-------------------------------------------------------------------------------------------
-- The dump
-------------------------------------------------------------------------------------------

-- Enum and Constants keep their values one level down. C_* namespaces and Lua libraries keep every member. Other
-- tables (mixins, utility tables, UI data) keep only their functions, so big data tables don't swamp the file.
local DEEP = { Enum = true, Constants = true }

local function tableMembers(name, v)
  if DEEP[name] then return members(v, true, true) end
  local m = members(v, false, false)
  if name:find("^C_") or name == "string" or name == "table" or name == "math" or name == "bit" or name == "coroutine" then
    return m
  end
  local kept, other = {}, 0
  for k, c in pairs(m) do
    if type(c) == "string" and c:sub(1, 1) == "f" then kept[k] = c else other = other + 1 end
  end
  if other > 0 then kept["(non-function members)"] = "n:" .. other end
  return kept
end

local dumping

local function finishDump(d)
  d.widgets = dumpWidgets()
  local events = {}
  for _, name in ipairs(leads.events or {}) do events[#events + 1] = name end
  if db.live and db.live.events then
    for name in pairs(db.live.events) do events[#events + 1] = name end
  end
  d.events = checkEvents(events)
  d.cvars = dumpCVars()
  d.addons = dumpAddOns()
  d.meta.finished = now()
  db.dump = d
  dumping = nil
  local n = 0
  for _ in pairs(d.globals) do n = n + 1 end
  say(("dump done: %d globals. Type /reload to write it to disk."):format(n))
end

local function startDump(reason)
  if dumping then say("a dump is already running.") return end
  local version, build, date, toc = "?", "?", "?", 0
  local bi = rawget(G, "GetBuildInfo")
  if bi then version, build, date, toc = bi() end
  local meta = {
    probe = VERSION, at = now(), reason = reason, version = version, build = build, date = date, toc = toc,
    key = buildKey(), locale = rawget(G, "GetLocale") and GetLocale() or "?", lua = rawget(G, "_VERSION"),
    combat = inCombat(), leads = leads.build,
    fnPrint = (function() local ok, s = pcall(tostring, print) return ok and s:gsub("%x%x%x%x%x%x+", "#") or "?" end)(),
    fnPrintLua = (function() local ok, s = pcall(tostring, say) return ok and s:gsub("%x%x%x%x%x%x+", "#") or "?" end)(),
  }
  local d = { meta = meta, globals = {}, tainted = {}, tables = {} }
  local names = {}
  for k in pairs(G) do
    if type(k) == "string" then names[#names + 1] = k end
  end
  dumping = { d = d, names = names, i = 1 }
  say(("dumping %d globals..."):format(#names))
end

local function stepDump()
  local job = dumping
  local d, names = job.d, job.names
  local last = math.min(job.i + CHUNK - 1, #names)
  for i = job.i, last do
    local name = names[i]
    local v = rawget(G, name)
    local secure, by = taint(G, name)
    if not secure then
      local who = tostring(by or "?")
      local list = d.tainted[who] or {}
      d.tainted[who] = list
      list[#list + 1] = name
    else
      local c = code(v)
      d.globals[name] = c
      if c == "t" and v ~= G then
        local m = tableMembers(name, v)
        -- members an add-on replaced
        if issecurevariable then
          for k in pairs(m) do
            if type(k) == "string" then
              local ok, s, who = pcall(issecurevariable, v, k)
              if ok and not s then m[k] = m[k] .. "!" .. tostring(who) end
            end
          end
        end
        d.tables[name] = m
      end
    end
  end
  job.i = last + 1
  if job.i > #names then finishDump(d) end
end

-------------------------------------------------------------------------------------------
-- Calls: getters, in and out of combat
-------------------------------------------------------------------------------------------

-- The prefix must be followed by a capital or digit: "^Can" alone matched Cancel* (0.1.2 called CancelLogout).
local GETTER = { "^Get[%u%d]", "^Is[%u%d]", "^Has[%u%d]", "^Can[%u%d]", "^Should[%u%d]", "^Are[%u%d]",
  "^Does[%u%d]", "^Unit[%u%d]", "^Num[%u%d]" }
local NEVER = { GetQuestReward = true } -- names that act despite the prefix

local function isGetter(name)
  if NEVER[name] then return false end
  if name:find("Reward") or name:find("Request") or name:find("Cancel") or name:find("^UnitSet") then return false end
  for _, p in ipairs(GETTER) do
    if name:find(p) then return true end
  end
  return false
end

local function shape(v)
  if isSecret(v) then
    local ok, t = pcall(type, v)
    return "secret:" .. (ok and t or "?")
  end
  local t = type(v)
  if t ~= "table" then return t end
  if isWidget(v) then return "object:" .. objectType(v) end
  local keys, n = {}, 0
  local ok = pcall(function()
    for k, val in pairs(v) do
      n = n + 1
      if n <= MAX_KEYS then
        local kt = isSecret(k) and "<secret key>" or (type(k) == "string" and k or ("[" .. type(k) .. "]"))
        keys[#keys + 1] = kt .. "=" .. (isSecret(val) and "secret" or type(val))
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
  for i = 1, math.min(n, 30) do out[i] = shape((select(i, ...))) end
  return out
end

-- The call plan: leads.calls (from Blizzard's docs) plus undocumented built-in getters found in the dump.
local function buildPlan()
  local plan, seen = {}, {}
  for _, c in ipairs(leads.calls or {}) do
    local key = c[1] and (c[1] .. "." .. c[2]) or c[2]
    if not seen[key] then
      seen[key] = true
      plan[#plan + 1] = { key = key, ns = c[1], fn = c[2], arg = c[3], from = "docs" }
    end
  end
  local documented = leads.documented or {}
  local uiGetters = leads.uiGetters or {}
  local d = db.dump
  if d then
    for name, c in pairs(d.globals) do
      local builtin = c == "fC" or (c == "f?" and not uiGetters[name])
      if builtin and isGetter(name) and not documented[name] and not seen[name] then
        seen[name] = true
        plan[#plan + 1] = { key = name, fn = name, arg = name:find("^Unit") and "unit" or nil, from = "undocumented" }
      end
    end
  end
  table.sort(plan, function(a, b) return a.key < b.key end)
  return plan
end

local function restrictionState()
  local out = {}
  local ra = rawget(G, "C_RestrictedActions")
  local E = rawget(G, "Enum") and Enum.AddOnRestrictionType
  if not (ra and ra.IsAddOnRestrictionActive and E) then return "unavailable" end
  for key, value in pairs(E) do
    local ok, on = pcall(ra.IsAddOnRestrictionActive, value)
    out[key] = not ok and "error" or isSecret(on) and "secret" or (on and true or false)
  end
  return out
end

local running -- { phase, plan, i }

local function phaseRecord(phase)
  db.calls = db.calls or {}
  local p = db.calls[phase]
  if not p or p.build ~= buildKey() then
    p = { build = buildKey(), results = {}, done = false }
    db.calls[phase] = p
  end
  return p
end

-- Sample arguments, read from the player's own state when a run starts. Only their kinds reach the SavedVariables:
-- a result records the descriptor ("spell", "n:1"), never the value it stood for.
local function plain(v) if v ~= nil and not isSecret(v) then return v end end
local function try(f, ...) local ok, v = pcall(f, ...) if ok then return plain(v) end end
local SAMPLERS = {
  unit = function() return "player" end,
  guid = function() return rawget(G, "UnitGUID") and try(UnitGUID, "player") end,
  item = function() return 6948 end, -- Hearthstone: every character has heard of it
  spell = function()
    local book, bank = rawget(G, "C_SpellBook"), rawget(G, "Enum") and Enum.SpellBookSpellBank
    if book and book.GetSpellBookItemInfo and bank then
      for i = 1, 30 do
        local info = try(book.GetSpellBookItemInfo, i, bank.Player)
        if type(info) == "table" and plain(info.spellID) and not info.isPassive then return info.spellID end
      end
    end
    return 6603 -- Auto Attack
  end,
  itemloc = function()
    local L = rawget(G, "ItemLocation")
    if not (L and L.CreateFromEquipmentSlot and rawget(G, "GetInventoryItemID")) then return end
    for slot = 1, 19 do
      if try(GetInventoryItemID, "player", slot) then return try(L.CreateFromEquipmentSlot, L, slot) end
    end
  end,
  map = function() local M = rawget(G, "C_Map") return M and M.GetBestMapForUnit and try(M.GetBestMapForUnit, "player") end,
  quest = function()
    local Q = rawget(G, "C_QuestLog")
    if not (Q and Q.GetNumQuestLogEntries and Q.GetInfo) then return end
    for i = 1, (try(Q.GetNumQuestLogEntries) or 0) do
      local info = try(Q.GetInfo, i)
      if type(info) == "table" and not info.isHeader and plain(info.questID) then return info.questID end
    end
  end,
  class = function() local ok, _, _, id = pcall(UnitClass, "player") return ok and plain(id) end,
  race = function() local ok, _, _, id = pcall(UnitRace, "player") return ok and plain(id) end,
  club = function() local C = rawget(G, "C_Club") return C and C.GetGuildClubId and try(C.GetGuildClubId) end,
  playerloc = function() local P = rawget(G, "PlayerLocation") return P and P.CreateFromUnit and try(P.CreateFromUnit, P, "player") end,
}

local function readSamples()
  local out = {}
  for name, f in pairs(SAMPLERS) do
    local ok, v = pcall(f)
    if ok and v ~= nil then out[name] = v end
  end
  return out
end

-- descriptors -> values, n; or nil, the descriptor that had no sample
local function resolve(args, samples)
  local vals = {}
  for i, d in ipairs(args) do
    if d == "nil" then vals[i] = nil
    elseif d:sub(1, 2) == "n:" then vals[i] = tonumber(d:sub(3))
    elseif d:sub(1, 2) == "s:" then vals[i] = d:sub(3)
    elseif d == "b:false" then vals[i] = false
    elseif samples[d] ~= nil then vals[i] = samples[d]
    else return nil, d end
  end
  return vals, #args
end

local function startCalls(phase)
  if running then return end
  if not db.dump then say("run /apiprobe dump first.") return end
  local p = phaseRecord(phase)
  p.started = p.started or now()
  p.restrictions = restrictionState()
  local samples = readSamples()
  p.samples = {}
  for k in pairs(SAMPLERS) do p.samples[k] = samples[k] ~= nil end -- which samples existed, not their values
  running = { phase = phase, plan = buildPlan(), i = p.next or 1, p = p, samples = samples }
  say(("calling %d getters (%s)..."):format(#running.plan - running.i + 1, phase))
end

local function stepCalls()
  local job = running
  local p = job.p
  if job.phase == "combat" and not inCombat() then
    p.next = job.i
    running = nil
    say(("combat ended at %d of %d getters; the rest run in your next combat."):format(job.i - 1, #job.plan))
    return
  end
  local last = math.min(job.i + CALLS_PER_FRAME - 1, #job.plan)
  for i = job.i, last do
    local c = job.plan[i]
    local fn
    if c.ns then
      local t = rawget(G, c.ns)
      fn = type(t) == "table" and rawget(t, c.fn)
    else
      fn = rawget(G, c.fn)
    end
    local rec
    -- a string local, so a client crash log's Lua stack names the call (crash logs print locals)
    local callKey = c.key
    local why = skipped(callKey)
    if not why and not isGetter(c.fn) then why = "not a getter" end -- second guard, whatever leads.lua says
    if why then
      rec = { skipped = why }
    elseif type(fn) ~= "function" then
      rec = { missing = true }
    else
      local vals, n = nil, 0
      if type(c.arg) == "table" then
        vals, n = resolve(c.arg, job.samples)
        if not vals then rec = { skipped = "no sample for " .. tostring(n) } end
      end
      if not rec then
        currentCall, forbiddenHit = callKey, nil
        if c.arg == "unit" then
          rec = capture(pcall(fn, "player"))
        elseif vals then
          rec = capture(pcall(fn, unpack(vals, 1, n)))
        else
          rec = capture(pcall(fn))
        end
        currentCall = nil
        if forbiddenHit then rec.forbidden = true end
      end
    end
    rec.from = c.from
    rec.arg = type(c.arg) == "table" and table.concat(c.arg, ",") or c.arg
    p.results[c.key] = rec
  end
  job.i = last + 1
  if job.i > #job.plan then
    p.done, p.finished, p.next = true, now(), nil
    running = nil
    say(("%s calls done. /reload to save."):format(job.phase))
    if job.phase == "combat" then db.armed = nil end
    if job.phase == "outside" and not (db.calls.combat and db.calls.combat.done) then
      db.armed = true
      say("armed: the same getters run again in your next combat.")
    end
  end
end

-------------------------------------------------------------------------------------------
-- Live events
-------------------------------------------------------------------------------------------

local function signature(...)
  local n = select("#", ...)
  if n == 0 then return "" end
  local parts = {}
  for i = 1, math.min(n, 20) do
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

local function liveEvent(event, ...)
  local live = db.live
  if not live or not live.on then return end
  local rec = live.events[event]
  if not rec then
    rec = { n = 0, combat = 0, first = now(), sigs = {} }
    live.events[event] = rec
  end
  rec.n = rec.n + 1
  if inCombat() then rec.combat = rec.combat + 1 end
  local sig = signature(...)
  if rec.sigs[sig] then
    rec.sigs[sig] = rec.sigs[sig] + 1
  else
    local count = 0
    for _ in pairs(rec.sigs) do count = count + 1 end
    if count < MAX_SIGS then rec.sigs[sig] = 1 end
  end
end

-------------------------------------------------------------------------------------------
-- Wiring
-------------------------------------------------------------------------------------------

local frame = CreateFrame("Frame")
local live = CreateFrame("Frame")

frame:SetScript("OnUpdate", function()
  if dumping then stepDump() end
  if running then stepCalls() end
end)

frame:SetScript("OnEvent", function(_, event, a1, a2)
  if event == "ADDON_LOADED" and a1 == ADDON then
    db = ApiProbeDB
    db.blocked = db.blocked or {}
    db.live = db.live or { on = true, events = {} }
    db.live.events = db.live.events or {}
    db.live.since = db.live.since or now()
    if db.live.build ~= buildKey() then
      db.live = { on = db.live.on ~= false, events = {}, since = now(), build = buildKey() }
    end
    if db.live.on then pcall(live.RegisterAllEvents, live) end
  elseif event == "PLAYER_LOGIN" then
    local d = db.dump
    if not d or d.meta.key ~= buildKey() or d.meta.probe ~= VERSION or d.meta.leads ~= leads.build then
      C_Timer.After(5, function() startDump("login") end)
    end
  elseif event == "PLAYER_REGEN_DISABLED" then
    if db.armed and not running and db.dump then startCalls("combat") end
  elseif event == "ADDON_ACTION_BLOCKED" or event == "ADDON_ACTION_FORBIDDEN" then
    if a1 == ADDON then
      db.blocked[#db.blocked + 1] = { event = event, fn = tostring(a2), during = currentCall, at = now(), combat = inCombat() }
      if currentCall then
        -- never again: each one costs Maro a popup
        forbiddenHit = true
        db.skip = db.skip or {}
        db.skip[currentCall] = event == "ADDON_ACTION_FORBIDDEN" and "forbidden" or "blocked"
      end
    end
  end
end)
for _, e in ipairs({ "ADDON_LOADED", "PLAYER_LOGIN", "PLAYER_REGEN_DISABLED", "ADDON_ACTION_BLOCKED", "ADDON_ACTION_FORBIDDEN" }) do
  frame:RegisterEvent(e)
end

live:SetScript("OnEvent", function(_, event, ...) liveEvent(event, ...) end)

local function count(t)
  local n = 0
  if t then for _ in pairs(t) do n = n + 1 end end
  return n
end

local function status()
  local d = db.dump
  say(("v%s on %s"):format(VERSION, buildKey()))
  say(d and ("dump: %d globals, %d tables, %d events checked (%s)"):format(count(d.globals), count(d.tables), count(d.events), d.meta.key) or "dump: none yet (/apiprobe dump)")
  local c = db.calls or {}
  for _, phase in ipairs({ "outside", "combat" }) do
    local p = c[phase]
    say(("%s combat calls: %s"):format(phase == "outside" and "out of" or "in",
      p and (p.done and ("done, %d results"):format(count(p.results)) or ("partial, %d results"):format(count(p.results))) or "not run"))
  end
  if db.armed then say("armed: calls run at the start of your next combat.") end
  say(("live events: %s, %d kinds seen"):format(db.live.on and "on" or "off", count(db.live.events)))
  if #db.blocked > 0 then say(("|cffff8080%d blocked-action reports|r recorded."):format(#db.blocked)) end
end

SLASH_APIPROBE1 = "/apiprobe"
SlashCmdList.APIPROBE = function(msg)
  msg = (msg or ""):lower():match("^%s*(.-)%s*$")
  if msg == "dump" then
    if inCombat() then say("leave combat first.") return end
    startDump("command")
  elseif msg == "calls" then
    if inCombat() then say("start this out of combat; it re-runs in combat by itself.") return end
    db.calls = nil
    startCalls("outside")
  elseif msg == "events on" or msg == "events off" then
    db.live.on = msg == "events on"
    if db.live.on then pcall(live.RegisterAllEvents, live) else live:UnregisterAllEvents() end
    say("live events " .. (db.live.on and "on." or "off."))
  elseif msg == "reset" then
    local skip = db.skip -- what this client forbids or crashes on stays known
    ApiProbeDB = { skip = skip }
    db = ApiProbeDB
    db.blocked, db.live = {}, { on = true, events = {}, since = now(), build = buildKey() }
    dumping, running = nil, nil
    say("cleared.")
  else
    status()
    say("commands: dump, calls, events on|off, reset")
  end
end
