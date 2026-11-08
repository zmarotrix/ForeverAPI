# Totem

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [DestroyTotem](#destroytotem) |  |  |
| ✅ | [GetNumTotemSlots](#getnumtotemslots) | 1 value |  |
| ✅ | [GetTotemCannotDismiss](#gettotemcannotdismiss) |  |  |
| ✅ | [GetTotemDuration](#gettotemduration) |  |  |
| ✅ | [GetTotemInfo](#gettoteminfo) |  |  |
| ✅ | [GetTotemTimeLeft](#gettotemtimeleft) |  |  |
| ✅ | [TargetTotem](#targettotem) |  |  |

### DestroyTotem

`DestroyTotem(slot: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

### GetNumTotemSlots

`GetNumTotemSlots() → numSlots: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `TotemDocumentation.lua`

### GetTotemCannotDismiss

`GetTotemCannotDismiss(slot: luaIndex) → cannotDismiss: bool?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

### GetTotemDuration

`GetTotemDuration(slot: luaIndex) → duration: LuaDurationObject`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

### GetTotemInfo

`GetTotemInfo(slot: luaIndex) → haveTotem: bool, totemName: cstring, startTime: number, duration: number, icon: fileID, modRate: number, spellID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenTotemSlotSecret (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

### GetTotemTimeLeft

`GetTotemTimeLeft(slot: luaIndex) → timeLeft: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenTotemSlotSecret (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

### TargetTotem

`TargetTotem(slot: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

## Types

### TotemInfoScript

- Structure
  - `haveTotem`: bool
  - `totemName`: cstring
  - `startTime`: number
  - `duration`: number
  - `icon`: fileID
  - `modRate`: number
  - `spellID`: number
