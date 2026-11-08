# Totem

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [DestroyTotem](#destroytotem) |  |  |
| ❔ | [GetNumTotemSlots](#getnumtotemslots) |  |  |
| ❔ | [GetTotemCannotDismiss](#gettotemcannotdismiss) |  |  |
| ❔ | [GetTotemDuration](#gettotemduration) |  |  |
| ❔ | [GetTotemInfo](#gettoteminfo) |  |  |
| ❔ | [GetTotemTimeLeft](#gettotemtimeleft) |  |  |
| ❔ | [TargetTotem](#targettotem) |  |  |

### DestroyTotem

`DestroyTotem(slot: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

### GetNumTotemSlots

`GetNumTotemSlots() → numSlots: number`

- Status: ❔ unverified
- Source: client docs `TotemDocumentation.lua`

### GetTotemCannotDismiss

`GetTotemCannotDismiss(slot: luaIndex) → cannotDismiss: bool?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

### GetTotemDuration

`GetTotemDuration(slot: luaIndex) → duration: LuaDurationObject`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

### GetTotemInfo

`GetTotemInfo(slot: luaIndex) → haveTotem: bool, totemName: cstring, startTime: number, duration: number, icon: fileID, modRate: number, spellID: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenTotemSlotSecret (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

### GetTotemTimeLeft

`GetTotemTimeLeft(slot: luaIndex) → timeLeft: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenTotemSlotSecret (Blizzard's docs; not checked in game)
- Source: client docs `TotemDocumentation.lua`

### TargetTotem

`TargetTotem(slot: luaIndex)`

- Status: ❔ unverified
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
