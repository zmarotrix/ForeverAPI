# PartyPose

Namespace: `C_PartyPose`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PartyPose.ExtraAction](#c_partyposeextraaction) |  |  |
| ✅ | [C_PartyPose.GetPartyPoseInfoByID](#c_partyposegetpartyposeinfobyid) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_PartyPose.GetPartyPoseInfoByMapID](#c_partyposegetpartyposeinfobymapid) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_PartyPose.HasExtraAction](#c_partyposehasextraaction) |  |  |

### C_PartyPose.ExtraAction

`C_PartyPose.ExtraAction(partyPoseID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PartyPoseUIDocumentation.lua`

### C_PartyPose.GetPartyPoseInfoByID

`C_PartyPose.GetPartyPoseInfoByID(mapID: number) → info: PartyPoseInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `PartyPoseUIDocumentation.lua`

### C_PartyPose.GetPartyPoseInfoByMapID

`C_PartyPose.GetPartyPoseInfoByMapID(mapID: number) → info: PartyPoseInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `PartyPoseUIDocumentation.lua`

### C_PartyPose.HasExtraAction

`C_PartyPose.HasExtraAction(partyPoseID: number) → hasExtraAction: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PartyPoseUIDocumentation.lua`

## Events

### SHOW_PARTY_POSE_UI

- Status: ✅ verified
- Payload: `mapID: number`, `won: bool`
- fires synchronously (Blizzard's docs)

## Types

### PartyPoseInfo

- Structure
  - `partyPoseID`: number
  - `mapID`: number
  - `widgetSetID`: number?
  - `victoryModelSceneID`: number
  - `defeatModelSceneID`: number
  - `victorySoundKitID`: number
  - `defeatSoundKitID`: number
  - `uiTextureKit`: textureKit?
  - `titleText`: string?
  - `extraButtonText`: string?
  - `flags`: PartyPoseFlags
