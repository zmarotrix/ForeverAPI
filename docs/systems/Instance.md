# Instance

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [CanChangePlayerDifficulty](#canchangeplayerdifficulty) |  |  |
| ❔ | [CanMapChangeDifficulty](#canmapchangedifficulty) |  |  |
| ❔ | [CanShowResetInstances](#canshowresetinstances) |  |  |
| ❔ | [GetBaseDifficultyID](#getbasedifficultyid) |  |  |
| ❔ | [GetDifficultyInfo](#getdifficultyinfo) |  |  |
| ❔ | [GetDungeonDifficultyID](#getdungeondifficultyid) |  |  |
| ❔ | [GetInstanceBootTimeRemaining](#getinstanceboottimeremaining) |  |  |
| ❔ | [GetInstanceInfo](#getinstanceinfo) |  |  |
| ❔ | [GetInstanceLockTimeRemaining](#getinstancelocktimeremaining) |  |  |
| ❔ | [GetInstanceLockTimeRemainingEncounter](#getinstancelocktimeremainingencounter) |  |  |
| ❔ | [GetLegacyRaidDifficultyID](#getlegacyraiddifficultyid) |  |  |
| ❔ | [GetRaidDifficultyID](#getraiddifficultyid) |  |  |
| ❔ | [IsInInstance](#isininstance) |  |  |
| ❔ | [IsLegacyDifficulty](#islegacydifficulty) |  |  |
| ❔ | [ResetInstances](#resetinstances) |  |  |
| ❔ | [SetDungeonDifficultyID](#setdungeondifficultyid) |  |  |
| ❔ | [SetLegacyRaidDifficultyID](#setlegacyraiddifficultyid) |  |  |
| ❔ | [SetRaidDifficultyID](#setraiddifficultyid) |  |  |

### CanChangePlayerDifficulty

`CanChangePlayerDifficulty() → canChange: bool, notOnCooldown: bool`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### CanMapChangeDifficulty

`CanMapChangeDifficulty(mapID: number?) → canChange: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### CanShowResetInstances

`CanShowResetInstances() → result: bool`

- Status: ❔ unverified
- Source: client docs `InstanceDocumentation.lua`

### GetBaseDifficultyID

`GetBaseDifficultyID(difficultyID: number) → baseDifficultyID: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### GetDifficultyInfo

`GetDifficultyInfo(difficultyID: number) → name: cstring, instanceType: cstring, isHeroic: bool, isChallengeMode: bool, displayHeroic: bool, displayMythic: bool, toggleDifficultyID: number?, isLFR: bool, minPlayers: number?, maxPlayers: number?, isUserSelectable: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### GetDungeonDifficultyID

`GetDungeonDifficultyID() → result: number`

- Status: ❔ unverified
- Source: client docs `InstanceDocumentation.lua`

### GetInstanceBootTimeRemaining

`GetInstanceBootTimeRemaining() → result: number`

- Status: ❔ unverified
- Source: client docs `InstanceDocumentation.lua`

### GetInstanceInfo

`GetInstanceInfo() → name: cstring, instanceType: cstring, difficultyID: number, difficultyName: cstring, maxPlayers: number, dynamicDifficulty: number, isDynamic: bool?, instanceID: number, instanceGroupSize: number, lfgDungeonID: number?, hasWorldTier: bool`

- Status: ❔ unverified
- Source: client docs `InstanceDocumentation.lua`

### GetInstanceLockTimeRemaining

`GetInstanceLockTimeRemaining() → timeLeft: number, extending: bool, encountersTotal: number, encountersCompleted: number`

- Status: ❔ unverified
- Source: client docs `InstanceDocumentation.lua`

### GetInstanceLockTimeRemainingEncounter

`GetInstanceLockTimeRemainingEncounter(encounterIndex: luaIndex) → encounterName: cstring, texture: cstring, isKilled: bool, ineligible: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### GetLegacyRaidDifficultyID

`GetLegacyRaidDifficultyID() → result: number?`

- Status: ❔ unverified
- Source: client docs `InstanceDocumentation.lua`

### GetRaidDifficultyID

`GetRaidDifficultyID() → result: number?`

- Status: ❔ unverified
- Source: client docs `InstanceDocumentation.lua`

### IsInInstance

`IsInInstance() → isInInstance: bool, instanceType: cstring`

- Status: ❔ unverified
- Source: client docs `InstanceDocumentation.lua`

### IsLegacyDifficulty

`IsLegacyDifficulty(difficultyID: number) → result: bool?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### ResetInstances

`ResetInstances()`

- Status: ❔ unverified
- Source: client docs `InstanceDocumentation.lua`

### SetDungeonDifficultyID

`SetDungeonDifficultyID(difficultyID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### SetLegacyRaidDifficultyID

`SetLegacyRaidDifficultyID(difficultyID: number, force: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InstanceDocumentation.lua`

### SetRaidDifficultyID

`SetRaidDifficultyID(difficultyID: number, force: bool = False)`

- Status: ❔ unverified
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
