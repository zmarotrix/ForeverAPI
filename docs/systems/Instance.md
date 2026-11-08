# Instance

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [CanChangePlayerDifficulty](#canchangeplayerdifficulty) | 2 values | 2 values |
| ✅ | [CanMapChangeDifficulty](#canmapchangedifficulty) | 1 value | 1 value |
| ✅ | [CanShowResetInstances](#canshowresetinstances) | 1 value | 1 value |
| ✅ | [GetBaseDifficultyID](#getbasedifficultyid) |  |  |
| ✅ | [GetDifficultyInfo](#getdifficultyinfo) |  |  |
| ✅ | [GetDungeonDifficultyID](#getdungeondifficultyid) | 1 value | 1 value |
| ✅ | [GetInstanceBootTimeRemaining](#getinstanceboottimeremaining) | 1 value | 1 value |
| ✅ | [GetInstanceInfo](#getinstanceinfo) | 11 values | 11 values |
| ✅ | [GetInstanceLockTimeRemaining](#getinstancelocktimeremaining) | 4 values | 4 values |
| ✅ | [GetInstanceLockTimeRemainingEncounter](#getinstancelocktimeremainingencounter) | 4 values | 4 values |
| ✅ | [GetLegacyRaidDifficultyID](#getlegacyraiddifficultyid) | 1 value | 1 value |
| ✅ | [GetRaidDifficultyID](#getraiddifficultyid) | 1 value | 1 value |
| ✅ | [IsInInstance](#isininstance) | 2 values | 2 values |
| ✅ | [IsLegacyDifficulty](#islegacydifficulty) |  |  |
| ✅ | [ResetInstances](#resetinstances) |  |  |
| ✅ | [SetDungeonDifficultyID](#setdungeondifficultyid) |  |  |
| ✅ | [SetLegacyRaidDifficultyID](#setlegacyraiddifficultyid) |  |  |
| ✅ | [SetRaidDifficultyID](#setraiddifficultyid) |  |  |

### CanChangePlayerDifficulty

`CanChangePlayerDifficulty() → canChange: bool, notOnCooldown: bool`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 2 values: `boolean`, `boolean`
- Called in combat: returned 2 values: `boolean`, `boolean`
- Source: client docs `InstanceDocumentation.lua`

### CanMapChangeDifficulty

`CanMapChangeDifficulty(mapID: number?) → canChange: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `InstanceDocumentation.lua`

### CanShowResetInstances

`CanShowResetInstances() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `InstanceDocumentation.lua`

### GetBaseDifficultyID

`GetBaseDifficultyID(difficultyID: number) → baseDifficultyID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### GetDifficultyInfo

`GetDifficultyInfo(difficultyID: number) → name: cstring, instanceType: cstring, isHeroic: bool, isChallengeMode: bool, displayHeroic: bool, displayMythic: bool, toggleDifficultyID: number?, isLFR: bool, minPlayers: number?, maxPlayers: number?, isUserSelectable: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### GetDungeonDifficultyID

`GetDungeonDifficultyID() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `InstanceDocumentation.lua`

### GetInstanceBootTimeRemaining

`GetInstanceBootTimeRemaining() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `InstanceDocumentation.lua`

### GetInstanceInfo

`GetInstanceInfo() → name: cstring, instanceType: cstring, difficultyID: number, difficultyName: cstring, maxPlayers: number, dynamicDifficulty: number, isDynamic: bool?, instanceID: number, instanceGroupSize: number, lfgDungeonID: number?, hasWorldTier: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 11 values: `string`, `string`, `number`, `string`, `number`, `number`, `boolean`, `number`, `number`, `nil`, `boolean`
- Called in combat: returned 11 values: `string`, `string`, `number`, `string`, `number`, `number`, `boolean`, `number`, `number`, `nil`, `boolean`
- Source: client docs `InstanceDocumentation.lua`

### GetInstanceLockTimeRemaining

`GetInstanceLockTimeRemaining() → timeLeft: number, extending: bool, encountersTotal: number, encountersCompleted: number`

- Status: ✅ verified (function)
- Called out of combat: returned 4 values: `number`, `boolean`, `number`, `number`
- Called in combat: returned 4 values: `number`, `boolean`, `number`, `number`
- Source: client docs `InstanceDocumentation.lua`

### GetInstanceLockTimeRemainingEncounter

`GetInstanceLockTimeRemainingEncounter(encounterIndex: luaIndex) → encounterName: cstring, texture: cstring, isKilled: bool, ineligible: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 4 values: `string`, `nil`, `boolean`, `boolean`
- Called in combat: returned 4 values: `string`, `nil`, `boolean`, `boolean`
- Source: client docs `InstanceDocumentation.lua`

### GetLegacyRaidDifficultyID

`GetLegacyRaidDifficultyID() → result: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `InstanceDocumentation.lua`

### GetRaidDifficultyID

`GetRaidDifficultyID() → result: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `InstanceDocumentation.lua`

### IsInInstance

`IsInInstance() → isInInstance: bool, instanceType: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `InstanceDocumentation.lua`

### IsLegacyDifficulty

`IsLegacyDifficulty(difficultyID: number) → result: bool?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### ResetInstances

`ResetInstances()`

- Status: ✅ verified (function)
- Source: client docs `InstanceDocumentation.lua`

### SetDungeonDifficultyID

`SetDungeonDifficultyID(difficultyID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### SetLegacyRaidDifficultyID

`SetLegacyRaidDifficultyID(difficultyID: number, force: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### SetRaidDifficultyID

`SetRaidDifficultyID(difficultyID: number, force: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

## Types

### DifficultyInfo

- Structure
  - `name`: cstring
  - `instanceType`: cstring
  - `isHeroic`: bool
  - `isChallengeMode`: bool
  - `displayHeroic`: bool
  - `displayMythic`: bool
  - `toggleDifficultyID`: number?
  - `isLFR`: bool
  - `minPlayers`: number?
  - `maxPlayers`: number?
  - `isUserSelectable`: bool

### DungeonEncounterInfo

- Structure
  - `encounterName`: cstring
  - `texture`: cstring
  - `isKilled`: bool
  - `ineligible`: bool

### InstanceInfo

- Structure
  - `name`: cstring
  - `instanceType`: cstring
  - `difficultyID`: number
  - `difficultyName`: cstring
  - `maxPlayers`: number
  - `dynamicDifficulty`: number
  - `isDynamic`: bool?
  - `instanceID`: number
  - `instanceGroupSize`: number
  - `lfgDungeonID`: number?
  - `hasWorldTier`: bool
