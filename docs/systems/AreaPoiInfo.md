# AreaPoiInfo

Namespace: `C_AreaPoiInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AreaPoiInfo.GetAreaPOIForMap](#c_areapoiinfogetareapoiformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_AreaPoiInfo.GetAreaPOIInfo](#c_areapoiinfogetareapoiinfo) |  |  |
| ✅ | [C_AreaPoiInfo.GetAreaPOISecondsLeft](#c_areapoiinfogetareapoisecondsleft) |  |  |
| ✅ | [C_AreaPoiInfo.GetDelvesForMap](#c_areapoiinfogetdelvesformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_AreaPoiInfo.GetDragonridingRacesForMap](#c_areapoiinfogetdragonridingracesformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_AreaPoiInfo.GetEventsForMap](#c_areapoiinfogeteventsformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_AreaPoiInfo.GetQuestHubsForMap](#c_areapoiinfogetquesthubsformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_AreaPoiInfo.IsAreaPOITimed](#c_areapoiinfoisareapoitimed) |  |  |

### C_AreaPoiInfo.GetAreaPOIForMap

`C_AreaPoiInfo.GetAreaPOIForMap(uiMapID: number) → areaPoiIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `AreaPoiInfoDocumentation.lua`

### C_AreaPoiInfo.GetAreaPOIInfo

`C_AreaPoiInfo.GetAreaPOIInfo(uiMapID: number?, areaPoiID: number) → poiInfo: AreaPOIInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AreaPoiInfoDocumentation.lua`

### C_AreaPoiInfo.GetAreaPOISecondsLeft

`C_AreaPoiInfo.GetAreaPOISecondsLeft(areaPoiID: number) → secondsLeft: number`

- Status: ✅ verified (function)
- Blizzard: Returns the number of seconds until the POI expires.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AreaPoiInfoDocumentation.lua`

### C_AreaPoiInfo.GetDelvesForMap

`C_AreaPoiInfo.GetDelvesForMap(uiMapID: number) → areaPoiIDs: number[]`

- Status: ✅ verified (function)
- Blizzard: Returns all area POIInfos flagged as delves for the given map.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `AreaPoiInfoDocumentation.lua`

### C_AreaPoiInfo.GetDragonridingRacesForMap

`C_AreaPoiInfo.GetDragonridingRacesForMap(uiMapID: number) → areaPoiIDs: number[]`

- Status: ✅ verified (function)
- Blizzard: Returns all area POIInfos flagged as dragonriding races for the given map.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `AreaPoiInfoDocumentation.lua`

### C_AreaPoiInfo.GetEventsForMap

`C_AreaPoiInfo.GetEventsForMap(uiMapID: number) → areaPoiIDs: number[]`

- Status: ✅ verified (function)
- Blizzard: Returns all area POIInfos flagged as events for the given map.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `AreaPoiInfoDocumentation.lua`

### C_AreaPoiInfo.GetQuestHubsForMap

`C_AreaPoiInfo.GetQuestHubsForMap(uiMapID: number) → areaPoiIDs: number[]`

- Status: ✅ verified (function)
- Blizzard: Returns all area POIInfos flagged as quest hubs for the given map.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `AreaPoiInfoDocumentation.lua`

### C_AreaPoiInfo.IsAreaPOITimed

`C_AreaPoiInfo.IsAreaPOITimed(areaPoiID: number) → isTimed: bool, hideTimerInTooltip: bool?`

- Status: ✅ verified (function)
- Blizzard: This statically determines if the POI is timed, GetAreaPOITimeLeft retrieves the value from the server and may return nothing for long intervals
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AreaPoiInfoDocumentation.lua`

## Events

### AREA_POIS_UPDATED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 2396 times (142 in combat); argument kinds: ``

## Types

### AreaPOIInfo

- Structure
  - `areaPoiID`: number
  - `position`: vector2
  - `name`: cstring
  - `description`: cstring?
  - `linkedUiMapID`: number?
  - `textureIndex`: number?
  - `tooltipWidgetSet`: number?
  - `iconWidgetSet`: number?
  - `atlasName`: string?
  - `uiTextureKit`: textureKit?
  - `shouldGlow`: bool
  - `factionID`: number?
  - `isPrimaryMapForPOI`: bool
  - `isAlwaysOnFlightmap`: bool
  - `addPaddingAboveTooltipWidgets`: bool?
  - `highlightWorldQuestsOnHover`: bool
  - `highlightVignettesOnHover`: bool
  - `isCurrentEvent`: bool
  - `isSuppressible`: bool
  - `isLocked`: bool
