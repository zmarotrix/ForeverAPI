# InvasionInfo

Namespace: `C_InvasionInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_InvasionInfo.AreInvasionsAvailable](#c_invasioninfoareinvasionsavailable) |  |  |
| ✅ | [C_InvasionInfo.GetInvasionForUiMapID](#c_invasioninfogetinvasionforuimapid) |  |  |
| ✅ | [C_InvasionInfo.GetInvasionInfo](#c_invasioninfogetinvasioninfo) |  |  |
| ✅ | [C_InvasionInfo.GetInvasionTimeLeft](#c_invasioninfogetinvasiontimeleft) |  |  |

### C_InvasionInfo.AreInvasionsAvailable

`C_InvasionInfo.AreInvasionsAvailable() → areInvasionsAvailable: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if invasions are active in the same physical area as the player.
- Source: client docs `InvasionInfoDocumentation.lua`

### C_InvasionInfo.GetInvasionForUiMapID

`C_InvasionInfo.GetInvasionForUiMapID(uiMapID: number) → invasionID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
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
