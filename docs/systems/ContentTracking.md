# ContentTracking

Namespace: `C_ContentTracking`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ContentTracking.GetBestMapForTrackable](#c_contenttrackinggetbestmapfortrackable) |  |  |
| ✅ | [C_ContentTracking.GetCollectableSourceTrackingEnabled](#c_contenttrackinggetcollectablesourcetrackingenabled) | 1 value | 1 value |
| ✅ | [C_ContentTracking.GetCollectableSourceTypes](#c_contenttrackinggetcollectablesourcetypes) | 1 value | 1 value |
| ✅ | [C_ContentTracking.GetCurrentTrackingTarget](#c_contenttrackinggetcurrenttrackingtarget) |  |  |
| ✅ | [C_ContentTracking.GetEncounterTrackingInfo](#c_contenttrackinggetencountertrackinginfo) |  |  |
| ✅ | [C_ContentTracking.GetNextWaypointForTrackable](#c_contenttrackinggetnextwaypointfortrackable) |  |  |
| ✅ | [C_ContentTracking.GetObjectiveText](#c_contenttrackinggetobjectivetext) |  |  |
| ✅ | [C_ContentTracking.GetTitle](#c_contenttrackinggettitle) |  |  |
| ✅ | [C_ContentTracking.GetTrackablesOnMap](#c_contenttrackinggettrackablesonmap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_ContentTracking.GetTrackedIDs](#c_contenttrackinggettrackedids) | 1 value | 1 value |
| ✅ | [C_ContentTracking.GetVendorTrackingInfo](#c_contenttrackinggetvendortrackinginfo) |  |  |
| ✅ | [C_ContentTracking.GetWaypointText](#c_contenttrackinggetwaypointtext) |  |  |
| ✅ | [C_ContentTracking.IsNavigable](#c_contenttrackingisnavigable) |  |  |
| ✅ | [C_ContentTracking.IsTrackable](#c_contenttrackingistrackable) |  |  |
| ✅ | [C_ContentTracking.IsTracking](#c_contenttrackingistracking) |  |  |
| ✅ | [C_ContentTracking.StartTracking](#c_contenttrackingstarttracking) |  |  |
| ✅ | [C_ContentTracking.StopTracking](#c_contenttrackingstoptracking) |  |  |
| ✅ | [C_ContentTracking.ToggleTracking](#c_contenttrackingtoggletracking) |  |  |

### C_ContentTracking.GetBestMapForTrackable

`C_ContentTracking.GetBestMapForTrackable(trackableType: ContentTrackingType, trackableID: number, ignoreWaypoint: bool = False) → result: ContentTrackingResult, mapID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetCollectableSourceTrackingEnabled

`C_ContentTracking.GetCollectableSourceTrackingEnabled() → isEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetCollectableSourceTypes

`C_ContentTracking.GetCollectableSourceTypes() → collectableSourceTypes: ContentTrackingType[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=number,[number]=number}`
- Called in combat: returned 1 value: `table{[number]=number,[number]=number}`
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetCurrentTrackingTarget

`C_ContentTracking.GetCurrentTrackingTarget(type: ContentTrackingType, id: number) → targetType: ContentTrackingTargetType, targetID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetEncounterTrackingInfo

`C_ContentTracking.GetEncounterTrackingInfo(journalEncounterID: number) → trackingInfo: EncounterTrackingInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetNextWaypointForTrackable

`C_ContentTracking.GetNextWaypointForTrackable(trackableType: ContentTrackingType, trackableID: number, uiMapID: number) → result: ContentTrackingResult, mapInfo: ContentTrackingMapInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetObjectiveText

`C_ContentTracking.GetObjectiveText(targetType: ContentTrackingTargetType, targetID: number, includeHyperlinks: bool = True) → objectiveText: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetTitle

`C_ContentTracking.GetTitle(trackableType: ContentTrackingType, trackableID: number) → title: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetTrackablesOnMap

`C_ContentTracking.GetTrackablesOnMap(trackableType: ContentTrackingType, uiMapID: number) → result: ContentTrackingResult, trackableMapInfos: ContentTrackingMapInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetTrackedIDs

`C_ContentTracking.GetTrackedIDs(trackableType: ContentTrackingType) → entryIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetVendorTrackingInfo

`C_ContentTracking.GetVendorTrackingInfo(collectableEntryID: number) → vendorTrackingInfo: VendorTrackingInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.GetWaypointText

`C_ContentTracking.GetWaypointText(trackableType: ContentTrackingType, trackableID: number) → waypointText: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.IsNavigable

`C_ContentTracking.IsNavigable(trackableType: ContentTrackingType, trackableID: number) → result: ContentTrackingResult, isNavigable: bool`

- Status: ✅ verified (function)
- Blizzard: If successful, returns if the trackable is either on your current map, or if we're able to determine a route to that map from your location via waypoints.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.IsTrackable

`C_ContentTracking.IsTrackable(type: ContentTrackingType, id: number) → isTrackable: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.IsTracking

`C_ContentTracking.IsTracking(type: ContentTrackingType, id: number) → isTracking: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.StartTracking

`C_ContentTracking.StartTracking(type: ContentTrackingType, id: number) → error: ContentTrackingError?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.StopTracking

`C_ContentTracking.StopTracking(type: ContentTrackingType, id: number, stopType: ContentTrackingStopType)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

### C_ContentTracking.ToggleTracking

`C_ContentTracking.ToggleTracking(type: ContentTrackingType, id: number, stopType: ContentTrackingStopType) → error: ContentTrackingError?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContentTrackingDocumentation.lua`

## Events

### CONTENT_TRACKING_IS_ENABLED_UPDATE

- Status: ✅ verified
- Payload: `isEnabled: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (0 in combat); argument kinds: `b`

### CONTENT_TRACKING_LIST_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 18 times (0 in combat); argument kinds: ``

### CONTENT_TRACKING_UPDATE

- Status: ✅ verified
- Payload: `type: ContentTrackingType`, `id: number`, `isTracked: bool`
- fires synchronously (Blizzard's docs)

### TRACKABLE_INFO_UPDATE

- Status: ✅ verified
- Payload: `type: ContentTrackingType`, `id: number`
- fires synchronously (Blizzard's docs)

### TRACKING_TARGET_INFO_UPDATE

- Status: ✅ verified
- Payload: `targetType: ContentTrackingTargetType`, `targetID: number`
- fires synchronously (Blizzard's docs)
