# Minimap

Namespace: `C_Minimap`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Minimap.CanTrackBattlePets](#c_minimapcantrackbattlepets) | 1 value | 1 value |
| ✅ | [C_Minimap.ClearAllTracking](#c_minimapclearalltracking) |  |  |
| ✅ | [C_Minimap.ClearMinimapInsetInfo](#c_minimapclearminimapinsetinfo) |  |  |
| ✅ | [C_Minimap.GetDefaultTrackingValue](#c_minimapgetdefaulttrackingvalue) | 1 value | 1 value |
| ✅ | [C_Minimap.GetDrawGroundTextures](#c_minimapgetdrawgroundtextures) | 1 value | 1 value |
| ✅ | [C_Minimap.GetNumQuestPOIWorldEffects](#c_minimapgetnumquestpoiworldeffects) | 1 value | 1 value |
| ✅ | [C_Minimap.GetNumTrackingTypes](#c_minimapgetnumtrackingtypes) | 1 value | 1 value |
| ✅ | [C_Minimap.GetPOITextureCoords](#c_minimapgetpoitexturecoords) | 4 values | 4 values |
| ✅ | [C_Minimap.GetTrackingFilter](#c_minimapgettrackingfilter) | 1 value | 1 value |
| ✅ | [C_Minimap.GetTrackingInfo](#c_minimapgettrackinginfo) | 1 value | 1 value |
| ✅ | [C_Minimap.GetUiMapID](#c_minimapgetuimapid) | 1 value | 1 value |
| ✅ | [C_Minimap.GetViewRadius](#c_minimapgetviewradius) | 1 value | 1 value |
| ✅ | [C_Minimap.IsFilteredOut](#c_minimapisfilteredout) | 1 value | 1 value |
| ✅ | [C_Minimap.IsInsideQuestBlob](#c_minimapisinsidequestblob) | 1 value | 1 value |
| ✅ | [C_Minimap.IsRotateMinimapIgnored](#c_minimapisrotateminimapignored) | 1 value | 1 value |
| ✅ | [C_Minimap.IsTrackingAccountCompletedQuests](#c_minimapistrackingaccountcompletedquests) | 1 value | 1 value |
| ✅ | [C_Minimap.IsTrackingBattlePets](#c_minimapistrackingbattlepets) | 1 value | 1 value |
| ✅ | [C_Minimap.IsTrackingHiddenQuests](#c_minimapistrackinghiddenquests) | 1 value | 1 value |
| ✅ | [C_Minimap.SetDrawGroundTextures](#c_minimapsetdrawgroundtextures) |  |  |
| ✅ | [C_Minimap.SetIgnoreRotateMinimap](#c_minimapsetignorerotateminimap) |  |  |
| ✅ | [C_Minimap.SetMinimapInsetInfo](#c_minimapsetminimapinsetinfo) |  |  |
| ✅ | [C_Minimap.SetTracking](#c_minimapsettracking) |  |  |
| ✅ | [C_Minimap.ShouldUseHybridMinimap](#c_minimapshouldusehybridminimap) | 1 value | 1 value |

### C_Minimap.CanTrackBattlePets

`C_Minimap.CanTrackBattlePets() → CanTrackBattlePets: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.ClearAllTracking

`C_Minimap.ClearAllTracking()`

- Status: ✅ verified (function)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.ClearMinimapInsetInfo

`C_Minimap.ClearMinimapInsetInfo()`

- Status: ✅ verified (function)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetDefaultTrackingValue

`C_Minimap.GetDefaultTrackingValue(filterType: MinimapTrackingFilter) → defaultValue: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetDrawGroundTextures

`C_Minimap.GetDrawGroundTextures() → draw: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetNumQuestPOIWorldEffects

`C_Minimap.GetNumQuestPOIWorldEffects() → worldEffectCount: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetNumTrackingTypes

`C_Minimap.GetNumTrackingTypes() → numTrackingTypes: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetPOITextureCoords

`C_Minimap.GetPOITextureCoords(index: number?) → textureCoordsX: number, textureCoordsY: number, textureCoordsZ: number, textureCoordsW: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 4 values: `number`, `number`, `number`, `number`
- Called in combat: returned 4 values: `number`, `number`, `number`, `number`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetTrackingFilter

`C_Minimap.GetTrackingFilter(spellIndex: luaIndex) → trackingType: MinimapScriptTrackingFilter`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `table{filterID=number}`
- Called in combat: returned 1 value: `table{filterID=number}`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetTrackingInfo

`C_Minimap.GetTrackingInfo(spellIndex: luaIndex) → trackingInfo: MinimapScriptTrackingInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `table{active=boolean,name=string,subType=number,texture=number,type=string}`
- Called in combat: returned 1 value: `table{active=boolean,name=string,subType=number,texture=number,type=string}`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetUiMapID

`C_Minimap.GetUiMapID() → uiMapID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.GetViewRadius

`C_Minimap.GetViewRadius() → yards: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsFilteredOut

`C_Minimap.IsFilteredOut(filterType: MinimapTrackingFilter) → isFiltered: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsInsideQuestBlob

`C_Minimap.IsInsideQuestBlob(questID: number) → isInside: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `quest`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsRotateMinimapIgnored

`C_Minimap.IsRotateMinimapIgnored() → isIgnored: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsTrackingAccountCompletedQuests

`C_Minimap.IsTrackingAccountCompletedQuests() → IsTrackingAccountCompletedQuests: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsTrackingBattlePets

`C_Minimap.IsTrackingBattlePets() → isTrackingBattlePets: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.IsTrackingHiddenQuests

`C_Minimap.IsTrackingHiddenQuests() → isTrackingHiddenQuests: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.SetDrawGroundTextures

`C_Minimap.SetDrawGroundTextures(draw: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.SetIgnoreRotateMinimap

`C_Minimap.SetIgnoreRotateMinimap(ignore: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.SetMinimapInsetInfo

`C_Minimap.SetMinimapInsetInfo(minAngle: number, maxAngle: number, scalar: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.SetTracking

`C_Minimap.SetTracking(index: luaIndex, on: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MinimapDocumentation.lua`

### C_Minimap.ShouldUseHybridMinimap

`C_Minimap.ShouldUseHybridMinimap() → shouldUse: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MinimapDocumentation.lua`

## Events

### MINIMAP_PING

- Status: ⛔ in Blizzard's docs, not in game
- Payload: `unitTarget: UnitTokenVariant`, `y: number`, `x: number`
- CallbackEvent (Blizzard's docs)
- restricted in some situations (Blizzard's docs)
- SecretPayloads (Blizzard's docs)

### MINIMAP_UPDATE_TRACKING

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### MINIMAP_UPDATE_ZOOM

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 306 times (6 in combat); argument kinds: ``

### PLAYER_INSIDE_QUEST_BLOB_STATE_CHANGED

- Status: ✅ verified
- Payload: `questID: number`, `isInside: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 42 times (11 in combat); argument kinds: `n,b`

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
