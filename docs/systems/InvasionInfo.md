# InvasionInfo

Namespace: `C_InvasionInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_InvasionInfo.AreInvasionsAvailable](#c_invasioninfoareinvasionsavailable) | 1 value | 1 value |
| ✅ | [C_InvasionInfo.GetInvasionForUiMapID](#c_invasioninfogetinvasionforuimapid) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_InvasionInfo.GetInvasionInfo](#c_invasioninfogetinvasioninfo) |  |  |
| ✅ | [C_InvasionInfo.GetInvasionTimeLeft](#c_invasioninfogetinvasiontimeleft) |  |  |

### C_InvasionInfo.AreInvasionsAvailable

`C_InvasionInfo.AreInvasionsAvailable() → areInvasionsAvailable: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if invasions are active in the same physical area as the player.
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `InvasionInfoDocumentation.lua`

### C_InvasionInfo.GetInvasionForUiMapID

`C_InvasionInfo.GetInvasionForUiMapID(uiMapID: number) → invasionID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `InvasionInfoDocumentation.lua`

### C_InvasionInfo.GetInvasionInfo

`C_InvasionInfo.GetInvasionInfo(invasionID: number) → invasionInfo: InvasionMapInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InvasionInfoDocumentation.lua`

### C_InvasionInfo.GetInvasionTimeLeft

`C_InvasionInfo.GetInvasionTimeLeft(invasionID: number) → timeLeftMinutes: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InvasionInfoDocumentation.lua`

## Types

### InvasionMapInfo

- Structure
  - `invasionID`: number
  - `name`: string
  - `position`: vector2
  - `atlasName`: textureAtlas
  - `rewardQuestID`: number?
