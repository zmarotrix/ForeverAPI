-- /fapi export: everything the modules recorded, as one text block to submit at
-- https://github.com/zmarotrix/ForeverAPI/issues/new?template=api-data.yml
--
--   FAPI:1:{"build":...,"enc":"cbor"}:<base64>   CBOR, compressed (C_EncodingUtil), Base64
--   FAPI:1:{"build":...,"enc":"lua"}:<base64>    a Lua table literal, Base64 (when C_EncodingUtil is missing)
--
-- The header carries the client build, the add-on version, which modules ran, and a random contributor ID made
-- once per account (so two exports from one person count once). No names, no values: the data is the same
-- shapes the modules keep in their SavedVariables. The probe's full API dump is left out (it's large and the
-- reference already has one per build); its getter results and event counts go in.

local FORMAT = 1

local function contributorId()
  local db = ForeverAPIProbeDB
  if not db.contributor then
    local hex = {}
    for i = 1, 16 do hex[i] = string.format("%x", math.random(0, 15)) end
    db.contributor = table.concat(hex)
  end
  return db.contributor
end

local function buildKey()
  local version, build = GetBuildInfo()
  return tostring(version) .. "." .. tostring(build)
end

function FAPI.ExportPayload()
  local data, modules = {}, {}
  local probe = rawget(_G, "ApiProbeDB")
  if FAPI.running.probe and type(probe) == "table" then
    data.probe = { calls = probe.calls, live = probe.live, blocked = probe.blocked,
      meta = probe.dump and probe.dump.meta or nil }
    modules[#modules + 1] = "probe"
  end
  for _, pair in ipairs({ { "watch", "ApiWatchDB" }, { "timeline", "ApiTimelineDB" }, { "widgets", "ApiWidgetsDB" },
    { "checks", "ApiChecksDB" } }) do
    local t = rawget(_G, pair[2])
    if FAPI.running[pair[1]] and type(t) == "table" and t.build then
      data[pair[1]] = t
      modules[#modules + 1] = pair[1]
    end
  end
  return data, modules
end

local function serialize(value, out)
  local t = type(value)
  if t == "table" then
    out[#out + 1] = "{"
    for k, v in pairs(value) do
      if type(k) == "number" then
        out[#out + 1] = "[" .. string.format("%.17g", k) .. "]="
      else
        out[#out + 1] = "[" .. string.format("%q", tostring(k)) .. "]="
      end
      serialize(v, out)
      out[#out + 1] = ","
    end
    out[#out + 1] = "}"
  elseif t == "string" then
    out[#out + 1] = string.format("%q", value)
  elseif t == "number" then
    out[#out + 1] = string.format("%.17g", value)
  elseif t == "boolean" then
    out[#out + 1] = tostring(value)
  else
    out[#out + 1] = "nil"
  end
end

local B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
local function base64(data)
  local out, n = {}, #data
  for i = 1, n, 3 do
    local a, b, c = data:byte(i, i + 2)
    local v = a * 65536 + (b or 0) * 256 + (c or 0)
    local c1, c2 = math.floor(v / 262144) % 64, math.floor(v / 4096) % 64
    local c3, c4 = math.floor(v / 64) % 64, v % 64
    out[#out + 1] = B64:sub(c1 + 1, c1 + 1) .. B64:sub(c2 + 1, c2 + 1)
      .. (b and B64:sub(c3 + 1, c3 + 1) or "=") .. (c and B64:sub(c4 + 1, c4 + 1) or "=")
  end
  return table.concat(out)
end

local function header(enc, modules)
  return ('{"build":"%s","probe":"%s","enc":"%s","modules":"%s","contributor":"%s"}'):format(
    buildKey(), FAPI.version, enc, table.concat(modules, ","), contributorId())
end

function FAPI.ExportString()
  local data, modules = FAPI.ExportPayload()
  if #modules == 0 then return nil end
  local E = C_EncodingUtil
  if E and E.SerializeCBOR and E.CompressString and E.EncodeBase64 then
    local ok, encoded = pcall(function() return E.EncodeBase64(E.CompressString(E.SerializeCBOR(data))) end)
    if ok and type(encoded) == "string" and encoded ~= "" then
      return "FAPI:" .. FORMAT .. ":" .. header("cbor", modules) .. ":" .. encoded, modules
    end
  end
  local out = {}
  serialize(data, out)
  return "FAPI:" .. FORMAT .. ":" .. header("lua", modules) .. ":" .. base64(table.concat(out)), modules
end

-------------------------------------------------------------------------------------------
-- Copy window
-------------------------------------------------------------------------------------------

local window
local function createWindow()
  local f = CreateFrame("Frame", "ForeverAPIProbeExport", UIParent, "BackdropTemplate")
  f:SetSize(520, 190)
  f:SetPoint("CENTER")
  f:SetFrameStrata("DIALOG")
  f:SetMovable(true)
  f:EnableMouse(true)
  f:RegisterForDrag("LeftButton")
  f:SetScript("OnDragStart", f.StartMoving)
  f:SetScript("OnDragStop", f.StopMovingOrSizing)
  if f.SetBackdrop then
    f:SetBackdrop({ bgFile = "Interface\\Buttons\\WHITE8X8", edgeFile = "Interface\\Buttons\\WHITE8X8", edgeSize = 1 })
    f:SetBackdropColor(0.06, 0.07, 0.09, 0.97)
    f:SetBackdropBorderColor(0.62, 0.78, 1, 0.8)
  end
  f.title = f:CreateFontString(nil, "OVERLAY", "GameFontHighlightLarge")
  f.title:SetPoint("TOPLEFT", 14, -12)
  f.title:SetText("ForeverAPI Probe: export")
  f.x = CreateFrame("Button", nil, f, "UIPanelCloseButton")
  f.x:SetPoint("TOPRIGHT", 2, 2)
  f.help = f:CreateFontString(nil, "OVERLAY", "GameFontHighlightSmall")
  f.help:SetPoint("TOPLEFT", 14, -40)
  f.help:SetWidth(490)
  f.help:SetJustifyH("LEFT")
  f.box = CreateFrame("EditBox", nil, f, "InputBoxTemplate")
  f.box:SetPoint("BOTTOMLEFT", 20, 44)
  f.box:SetPoint("BOTTOMRIGHT", -14, 44)
  f.box:SetHeight(24)
  f.box:SetAutoFocus(false)
  f.box:SetMaxLetters(0)
  -- read-only: typing puts the export back and keeps it selected for Ctrl+C
  f.box:SetScript("OnTextChanged", function(self, userInput)
    if userInput and window.text then
      self:SetText(window.text)
      self:HighlightText()
    end
  end)
  f.box:SetScript("OnEditFocusGained", function(self) self:HighlightText() end)
  f.box:SetScript("OnEscapePressed", function() f:Hide() end)
  f.size = f:CreateFontString(nil, "OVERLAY", "GameFontDisableSmall")
  f.size:SetPoint("BOTTOMLEFT", 16, 18)
  f.close = CreateFrame("Button", nil, f, "UIPanelButtonTemplate")
  f.close:SetSize(90, 22)
  f.close:SetPoint("BOTTOMRIGHT", -12, 12)
  f.close:SetText(CLOSE or "Close")
  f.close:SetScript("OnClick", function() f:Hide() end)
  table.insert(UISpecialFrames, "ForeverAPIProbeExport")
  return f
end

function FAPI.ShowExport()
  local text, modules = FAPI.ExportString()
  if not text then
    FAPI.say("nothing to export yet: switch a module on (/fapi), play a while, then try again.")
    return
  end
  window = window or createWindow()
  window.text = text
  window.help:SetText(("Holds what these modules recorded: %s. No names or values.\n\nClick the box, press Ctrl+C, then open "
    .. "github.com/zmarotrix/ForeverAPI, New issue, \"API data\", and paste it there (or save it to a .txt file and drag "
    .. "that in). Thank you!"):format(table.concat(modules, ", ")))
  window.size:SetText(("%d characters"):format(#text))
  window.box:SetText(text)
  window:Show()
  window.box:SetFocus()
  window.box:HighlightText()
end
