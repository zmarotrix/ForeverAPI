# LibForever-1.0

A library for WoW Forever add-ons. It handles what the Forever client doesn't do for you:

- the classic functions that are gone, with their classic answers (`Compat`)
- secret values, which can't be compared or added (`Secret`, `LF.Plain`, `LF.Call`)
- combat lockdown (`LF:AfterCombat`, `LF:Restricted`)
- first and last names: chat says "First Last", the roster says "First", and a whisper to "First" fails (`Names`)
- add-on messages that survive chat lockdown, compressed, with whispers to full names (`Net`)
- chat lines that arrive, or a ready chat box when the game won't send them (`LF:Say`)
- saved variables with defaults and ordered upgrades (`LF:SavedVars`)

It isn't a UI framework or a replacement for Ace3, and it works next to Ace3.

## Quick start

1. Download `LibForever-1.0.1.zip` from the
   [release](https://github.com/zmarotrix/ForeverAPI/releases/tag/libforever-1.0.1) (or use `lib/` here). Copy these
   folders into your add-on's `libs/` folder: `LibStub`, `CallbackHandler-1.0`,
   `AceComm-3.0` and `LibForever-1.0`. Skip any your add-on already has.
2. List them in your TOC, in this order:

   ```
   libs\LibStub\LibStub.lua
   libs\CallbackHandler-1.0\CallbackHandler-1.0.xml
   libs\AceComm-3.0\AceComm-3.0.xml
   libs\LibForever-1.0\LibForever-1.0.xml
   MyAddon.lua
   ```

3. Use it:

   ```lua
   local LF = LibStub("LibForever-1.0")

   LF:On("ADDON_LOADED", "MyAddon", function(_, name)
     if name ~= "MyAddon" then return end
     MyAddonDB = LF:SavedVars("MyAddonDB", { version = 1, defaults = { shown = true } })
   end)

   LF:On("PLAYER_LOGIN", "MyAddon", function()
     -- GetSpellInfo is gone on Forever; Compat gives classic's answer, rank included
     local name, rank = LF.Compat.GetSpellInfo(8936)
     LF:Print(name .. " (" .. tostring(rank) .. ")", "MyAddon")
   end)

   local bar = CreateFrame("StatusBar", nil, UIParent)
   LF:On("UNIT_HEALTH", "MyAddon", function(_, unit)
     if unit ~= "target" then return end
     -- health is secret: hand it to the bar, never compare it
     LF.SetSecret(bar, "SetMinMaxValues", 0, UnitHealthMax("target"))
     LF.SetSecret(bar, "SetValue", UnitHealth("target"))
   end)

   -- /myaddon Firstname: a whisper needs the full name, which Names learned from chat
   SLASH_MYADDON1 = "/myaddon"
   SlashCmdList.MYADDON = function(first) LF:Say("hello!", "WHISPER", first) end
   ```

Every function has LuaLS annotations. With ForeverAPI's VS Code definitions (the `ForeverAPI-LuaLS` download) you
get completion for the client and the library together.

## How copies get along

If several add-ons ship LibForever, the newest copy runs, whichever loads first, and it takes over the older one's
event frame, handlers and queues. Handlers are keyed by an owner you pass (`"MyAddon"` above), so one add-on can
never remove another's. Within `-1.0` nothing is removed or changed; a breaking change would be `LibForever-2.0`,
side by side.

## Support

Open an issue for a bug or a Forever problem. Pull requests are welcome. New features aren't promised.

## Licence

MIT (`LICENSE`), for the library and its tests. The bundled libraries keep their own licences:
`THIRD-PARTY-NOTICES.md`.

Tests: `python tools/test_libforever.py` (stub client, needs `lupa`). `python tools/compat_gen.py` regenerates
`CompatList.lua` from `docs/compat.json`.
