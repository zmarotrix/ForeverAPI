# Minimap

Namespace: `C_Minimap`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Minimap.CanTrackBattlePets](#c_minimapcantrackbattlepets) |  |  |
| ❔ | [C_Minimap.ClearAllTracking](#c_minimapclearalltracking) |  |  |
| ❔ | [C_Minimap.ClearMinimapInsetInfo](#c_minimapclearminimapinsetinfo) |  |  |
| ❔ | [C_Minimap.GetDefaultTrackingValue](#c_minimapgetdefaulttrackingvalue) |  |  |
| ❔ | [C_Minimap.GetDrawGroundTextures](#c_minimapgetdrawgroundtextures) |  |  |
| ❔ | [C_Minimap.GetNumQuestPOIWorldEffects](#c_minimapgetnumquestpoiworldeffects) |  |  |
| ❔ | [C_Minimap.GetNumTrackingTypes](#c_minimapgetnumtrackingtypes) |  |  |
| ❔ | [C_Minimap.GetPOITextureCoords](#c_minimapgetpoitexturecoords) |  |  |
| ❔ | [C_Minimap.GetTrackingFilter](#c_minimapgettrackingfilter) |  |  |
| ❔ | [C_Minimap.GetTrackingInfo](#c_minimapgettrackinginfo) |  |  |
| ❔ | [C_Minimap.GetUiMapID](#c_minimapgetuimapid) |  |  |
| ❔ | [C_Minimap.GetViewRadius](#c_minimapgetviewradius) |  |  |
| ❔ | [C_Minimap.IsFilteredOut](#c_minimapisfilteredout) |  |  |
| ❔ | [C_Minimap.IsInsideQuestBlob](#c_minimapisinsidequestblob) |  |  |
| ❔ | [C_Minimap.IsRotateMinimapIgnored](#c_minimapisrotateminimapignored) |  |  |
| ❔ | [C_Minimap.IsTrackingAccountCompletedQuests](#c_minimapistrackingaccountcompletedquests) |  |  |
| ❔ | [C_Minimap.IsTrackingBattlePets](#c_minimapistrackingbattlepets) |  |  |
| ❔ | [C_Minimap.IsTrackingHiddenQuests](#c_minimapistrackinghiddenquests) |  |  |
| ❔ | [C_Minimap.SetDrawGroundTextures](#c_minimapsetdrawgroundtextures) |  |  |
| ❔ | [C_Minimap.SetIgnoreRotateMinimap](#c_minimapsetignorerotateminimap) |  |  |
| ❔ | [C_Minimap.SetMinimapInsetInfo](#c_minimapsetminimapinsetinfo) |  |  |
| ❔ | [C_Minimap.SetTracking](#c_minimapsettracking) |  |  |
| ❔ | [C_Minimap.ShouldUseHybridMinimap](#c_minimapshouldusehybridminimap) |  |  |

### C_Minimap.CanTrackBattlePets

`C_Minimap.CanTrackBattlePets() → CanTrackBattlePets: bool`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.ClearAllTracking

`C_Minimap.ClearAllTracking()`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.ClearMinimapInsetInfo

`C_Minimap.ClearMinimapInsetInfo()`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetDefaultTrackingValue

`C_Minimap.GetDefaultTrackingValue(filterType: MinimapTrackingFilter) → defaultValue: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetDrawGroundTextures

`C_Minimap.GetDrawGroundTextures() → draw: bool`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetNumQuestPOIWorldEffects

`C_Minimap.GetNumQuestPOIWorldEffects() → worldEffectCount: number`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetNumTrackingTypes

`C_Minimap.GetNumTrackingTypes() → numTrackingTypes: number`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetPOITextureCoords

`C_Minimap.GetPOITextureCoords(index: number?) → textureCoordsX: number, textureCoordsY: number, textureCoordsZ: number, textureCoordsW: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetTrackingFilter

`C_Minimap.GetTrackingFilter(spellIndex: luaIndex) → trackingType: MinimapScriptTrackingFilter`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetTrackingInfo

`C_Minimap.GetTrackingInfo(spellIndex: luaIndex) → trackingInfo: MinimapScriptTrackingInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetUiMapID

`C_Minimap.GetUiMapID() → uiMapID: number?`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetViewRadius

`C_Minimap.GetViewRadius() → yards: number`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsFilteredOut

`C_Minimap.IsFilteredOut(filterType: MinimapTrackingFilter) → isFiltered: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsInsideQuestBlob

`C_Minimap.IsInsideQuestBlob(questID: number) → isInside: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsRotateMinimapIgnored

`C_Minimap.IsRotateMinimapIgnored() → isIgnored: bool`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsTrackingAccountCompletedQuests

`C_Minimap.IsTrackingAccountCompletedQuests() → IsTrackingAccountCompletedQuests: bool`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsTrackingBattlePets

`C_Minimap.IsTrackingBattlePets() → isTrackingBattlePets: bool`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsTrackingHiddenQuests

`C_Minimap.IsTrackingHiddenQuests() → isTrackingHiddenQuests: bool`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.SetDrawGroundTextures

`C_Minimap.SetDrawGroundTextures(draw: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.SetIgnoreRotateMinimap

`C_Minimap.SetIgnoreRotateMinimap(ignore: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.SetMinimapInsetInfo

`C_Minimap.SetMinimapInsetInfo(minAngle: number, maxAngle: number, scalar: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.SetTracking

`C_Minimap.SetTracking(index: luaIndex, on: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.ShouldUseHybridMinimap

`C_Minimap.ShouldUseHybridMinimap() → shouldUse: bool`

- Status: ❔ unverified
- Source: client docs `MinimapDocumentation.lua`

## Events

### MINIMAP_PING

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`, `y: number`, `x: number`
- CallbackEvent (Blizzard's docs)
- restricted in some situations (Blizzard's docs)
- SecretPayloads (Blizzard's docs)

### MINIMAP_UPDATE_TRACKING

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### MINIMAP_UPDATE_ZOOM

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### PLAYER_INSIDE_QUEST_BLOB_STATE_CHANGED

- Status: ❔ unverified
- Payload: `questID: number`, `isInside: bool`
- fires synchronously (Blizzard's docs)

## Types

### MinimapScriptTrackingFilter

- Structure
  - `spellID`: number?
  - `filterID`: MinimapTrackingFilter?

### MinimapScriptTrackingInfo

- Structure
  - `name`: cstring
  - `texture`: fileID
  - `active`: bool
  - `type`: cstring
  - `subType`: number
  - `spellID`: number?
