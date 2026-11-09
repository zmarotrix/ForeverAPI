# LibForever-1.0

A library for WoW Forever add-ons. It handles what the Forever client doesn't do for you:

- the classic functions that are gone (`Compat`)
- secret values (`Secret`, `LF.Plain`, `LF.Call`)
- combat lockdown (`LF:AfterCombat`, `LF:Restricted`)
- first and last names (`Names`)
- saved variables with upgrades (`LF:SavedVars`)

It's a LibStub library: copy `LibForever-1.0/` into your add-on's `libs/`, and load `LibStub` and then the files in
`LibForever-1.0.xml`'s order. If several add-ons ship copies, the newest one runs and takes over the older one's
event frame and queues.

```lua
local LF = LibStub("LibForever-1.0")
LF:On("PLAYER_LOGIN", "MyAddon", function()
  local name, rank = LF.Compat.GetSpellInfo(8936)
  LF:Print(name .. " (" .. tostring(rank) .. ")", "MyAddon")
end)
```

Every function has LuaLS annotations. NorgannonDB Core embeds the library and uses its own names for it
(`Core:On`, `Core.Compat`, ...).

**Status: not released.** This is phase 1 of `docs/forever-toolkit-plan.md` in Maro's suite. The licence, the
release zip and the reference pages come in phase 4. Until then, the code is All Rights Reserved like the rest of
this repo.

Tests: `python tools/test_libforever.py` (stub client, needs `lupa`). `python tools/compat_gen.py` regenerates
`CompatList.lua` from `docs/compat.json`.
