# Totem

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [DestroyTotem](#destroytotem) |  |  |
| ✅ | [GetNumTotemSlots](#getnumtotemslots) | 1 value | 1 value |
| ✅ | [GetTotemCannotDismiss](#gettotemcannotdismiss) | 1 value | 1 value |
| ✅ | [GetTotemDuration](#gettotemduration) | 1 value | 1 value |
| ✅ | [GetTotemInfo](#gettoteminfo) | 7 values | partly secret |
| ✅ | [GetTotemTimeLeft](#gettotemtimeleft) | 1 value | 1 value |
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
- Called in combat: returned 1 value: `number`
- Source: client docs `TotemDocumentation.lua`

### GetTotemCannotDismiss

`GetTotemCannotDismiss(slot: luaIndex) → cannotDismiss: bool?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `TotemDocumentation.lua`

### GetTotemDuration

`GetTotemDuration(slot: luaIndex) → duration: LuaDurationObject`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `TotemDocumentation.lua`

### GetTotemInfo

`GetTotemInfo(slot: luaIndex) → haveTotem: bool, totemName: cstring, startTime: number, duration: number, icon: fileID, modRate: number, spellID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenTotemSlotSecret (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 7 values: `boolean`, `string`, `number`, `number`, `nil`, `number`, `number`
- Called in combat: returned 7 values: `secret:boolean`, `secret:string`, `secret:number`, `secret:number`, `nil`, `secret:number`, `secret:number`
- Source: client docs `TotemDocumentation.lua`

### GetTotemTimeLeft

`GetTotemTimeLeft(slot: luaIndex) → timeLeft: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenTotemSlotSecret (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
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
