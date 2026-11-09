# MapUI

Namespace: `C_Map`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Map.CanSetUserWaypointOnMap](#c_mapcansetuserwaypointonmap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.ClearUserWaypoint](#c_mapclearuserwaypoint) |  |  |
| ✅ | [C_Map.CloseWorldMapInteraction](#c_mapcloseworldmapinteraction) |  |  |
| ✅ | [C_Map.GetAreaInfo](#c_mapgetareainfo) |  |  |
| ✅ | [C_Map.GetBestMapForUnit](#c_mapgetbestmapforunit) | 1 value | 1 value |
| ✅ | [C_Map.GetBountySetMaps](#c_mapgetbountysetmaps) |  |  |
| ✅ | [C_Map.GetFallbackWorldMapID](#c_mapgetfallbackworldmapid) | 1 value | 1 value |
| ✅ | [C_Map.GetMapArtBackgroundAtlas](#c_mapgetmapartbackgroundatlas) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapArtHelpTextPosition](#c_mapgetmaparthelptextposition) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapArtID](#c_mapgetmapartid) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapArtLayerTextures](#c_mapgetmapartlayertextures) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapArtLayers](#c_mapgetmapartlayers) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapArtZoneTextPosition](#c_mapgetmapartzonetextposition) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapBannersForMap](#c_mapgetmapbannersformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapChildrenInfo](#c_mapgetmapchildreninfo) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapDisplayInfo](#c_mapgetmapdisplayinfo) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapGroupID](#c_mapgetmapgroupid) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapGroupMembersInfo](#c_mapgetmapgroupmembersinfo) |  |  |
| ✅ | [C_Map.GetMapHighlightInfoAtPosition](#c_mapgetmaphighlightinfoatposition) |  |  |
| ✅ | [C_Map.GetMapHighlightPulseInfo](#c_mapgetmaphighlightpulseinfo) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapInfo](#c_mapgetmapinfo) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapInfoAtPosition](#c_mapgetmapinfoatposition) |  |  |
| ✅ | [C_Map.GetMapLevels](#c_mapgetmaplevels) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapLinksForMap](#c_mapgetmaplinksformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetMapPosFromWorldPos](#c_mapgetmapposfromworldpos) |  |  |
| ✅ | [C_Map.GetMapRectOnMap](#c_mapgetmaprectonmap) |  |  |
| ✅ | [C_Map.GetMapWorldSize](#c_mapgetmapworldsize) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetPlayerMapPosition](#c_mapgetplayermapposition) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetUserWaypoint](#c_mapgetuserwaypoint) | 0 values | 0 values |
| ✅ | [C_Map.GetUserWaypointFromHyperlink](#c_mapgetuserwaypointfromhyperlink) |  |  |
| ✅ | [C_Map.GetUserWaypointHyperlink](#c_mapgetuserwaypointhyperlink) | 0 values | 0 values |
| ✅ | [C_Map.GetUserWaypointPositionForMap](#c_mapgetuserwaypointpositionformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.GetWorldPosFromMapPos](#c_mapgetworldposfrommappos) |  |  |
| ✅ | [C_Map.HasUserWaypoint](#c_maphasuserwaypoint) | 1 value | 1 value |
| ✅ | [C_Map.IsCityMap](#c_mapiscitymap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.IsMapValidForNavBarDropdown](#c_mapismapvalidfornavbardropdown) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Map.MapHasArt](#c_mapmaphasart) |  |  |
| ✅ | [C_Map.OpenWorldMap](#c_mapopenworldmap) |  |  |
| ✅ | [C_Map.RequestPreloadMap](#c_maprequestpreloadmap) |  |  |
| ✅ | [C_Map.SetUserWaypoint](#c_mapsetuserwaypoint) |  |  |

### C_Map.CanSetUserWaypointOnMap

`C_Map.CanSetUserWaypointOnMap(uiMapID: number) → canSet: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.ClearUserWaypoint

`C_Map.ClearUserWaypoint()`

- Status: ✅ verified (function)
- Source: client docs `MapDocumentation.lua`

### C_Map.CloseWorldMapInteraction

`C_Map.CloseWorldMapInteraction()`

- Status: ✅ verified (function)
- Source: client docs `MapDocumentation.lua`

### C_Map.GetAreaInfo

`C_Map.GetAreaInfo(areaID: number) → name: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.GetBestMapForUnit

`C_Map.GetBestMapForUnit(unitToken: UnitToken) → uiMapID: number?`

- Status: ✅ verified (function)
- Blizzard: Only works for the player and party members.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `player`: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `MapDocumentation.lua`

### C_Map.GetBountySetMaps

`C_Map.GetBountySetMaps(bountySetID: number) → mapIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.GetFallbackWorldMapID

`C_Map.GetFallbackWorldMapID() → uiMapID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapArtBackgroundAtlas

`C_Map.GetMapArtBackgroundAtlas(uiMapID: number) → atlasName: textureAtlas`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapArtHelpTextPosition

`C_Map.GetMapArtHelpTextPosition(uiMapID: number) → position: MapCanvasPosition`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapArtID

`C_Map.GetMapArtID(uiMapID: number) → uiMapArtID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapArtLayerTextures

`C_Map.GetMapArtLayerTextures(uiMapID: number, layerIndex: luaIndex) → textures: fileID[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map,n:1`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapArtLayers

`C_Map.GetMapArtLayers(uiMapID: number) → layerInfo: UiMapLayerInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapArtZoneTextPosition

`C_Map.GetMapArtZoneTextPosition(uiMapID: number) → position: MapCanvasPosition`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapBannersForMap

`C_Map.GetMapBannersForMap(uiMapID: number) → mapBanners: MapBannerInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapChildrenInfo

`C_Map.GetMapChildrenInfo(uiMapID: number, mapType: UIMapType?, allDescendants: bool?) → info: UiMapDetails[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapDisplayInfo

`C_Map.GetMapDisplayInfo(uiMapID: number) → hideIcons: bool`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapGroupID

`C_Map.GetMapGroupID(uiMapID: number) → uiMapGroupID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapGroupMembersInfo

`C_Map.GetMapGroupMembersInfo(uiMapGroupID: number) → info: UiMapGroupMemberInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapHighlightInfoAtPosition

`C_Map.GetMapHighlightInfoAtPosition(uiMapID: number, x: number, y: number) → fileDataID: fileID, atlasID: textureAtlas, texturePercentageX: number, texturePercentageY: number, textureX: number, textureY: number, scrollChildX: number, scrollChildY: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapHighlightPulseInfo

`C_Map.GetMapHighlightPulseInfo(uiMapID: number) → fileDataID: fileID, atlasID: textureAtlas, texturePercentageX: number, texturePercentageY: number, textureX: number, textureY: number, scrollChildX: number, scrollChildY: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapInfo

`C_Map.GetMapInfo(uiMapID: number) → info: UiMapDetails`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapInfoAtPosition

`C_Map.GetMapInfoAtPosition(uiMapID: number, x: number, y: number, ignoreZoneMapPositionData: bool?) → info: UiMapDetails`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapLevels

`C_Map.GetMapLevels(uiMapID: number) → playerMinLevel: number, playerMaxLevel: number, petMinLevel: number, petMaxLevel: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapLinksForMap

`C_Map.GetMapLinksForMap(uiMapID: number) → mapLinks: MapLinkInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapPosFromWorldPos

`C_Map.GetMapPosFromWorldPos(continentID: number, worldPosition: vector2, overrideUiMapID: number?) → uiMapID: number, mapPosition: vector2`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapRectOnMap

`C_Map.GetMapRectOnMap(uiMapID: number, topUiMapID: number) → minX: number, maxX: number, minY: number, maxY: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.GetMapWorldSize

`C_Map.GetMapWorldSize(uiMapID: number) → width: number, height: number`

- Status: ✅ verified (function)
- Blizzard: Returns the size in yards of the area represented by the map.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetPlayerMapPosition

`C_Map.GetPlayerMapPosition(uiMapID: number, unitToken: UnitToken) → position: vector2?`

- Status: ✅ verified (function)
- Blizzard: Only works for the player and party members.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map,unit`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetUserWaypoint

`C_Map.GetUserWaypoint() → point: UiMapPoint`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `MapDocumentation.lua`

### C_Map.GetUserWaypointFromHyperlink

`C_Map.GetUserWaypointFromHyperlink(hyperlink: string) → point: UiMapPoint`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.GetUserWaypointHyperlink

`C_Map.GetUserWaypointHyperlink() → hyperlink: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `MapDocumentation.lua`

### C_Map.GetUserWaypointPositionForMap

`C_Map.GetUserWaypointPositionForMap(uiMapID: number) → mapPosition: vector2`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.GetWorldPosFromMapPos

`C_Map.GetWorldPosFromMapPos(uiMapID: number, mapPosition: vector2) → continentID: number, worldPosition: vector2`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.HasUserWaypoint

`C_Map.HasUserWaypoint() → hasUserWaypoint: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MapDocumentation.lua`

### C_Map.IsCityMap

`C_Map.IsCityMap(uiMapID: number) → isCityMap: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.IsMapValidForNavBarDropdown

`C_Map.IsMapValidForNavBarDropdown(uiMapID: number) → isValid: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `MapDocumentation.lua`

### C_Map.MapHasArt

`C_Map.MapHasArt(uiMapID: number) → hasArt: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.OpenWorldMap

`C_Map.OpenWorldMap(uiMapID: number?)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.RequestPreloadMap

`C_Map.RequestPreloadMap(uiMapID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

### C_Map.SetUserWaypoint

`C_Map.SetUserWaypoint(point: UiMapPoint) → wasSet: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapDocumentation.lua`

## Events

### NEW_WMO_CHUNK

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1107 times (94 in combat); argument kinds: ``

### PLAYER_MAP_CHANGED

- Status: ✅ verified
- Payload: `oldMapID: number`, `newMapID: number`
- fires synchronously (Blizzard's docs)
- Seen firing 53 times (0 in combat); argument kinds: `n,n`

### USER_WAYPOINT_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 4 times (0 in combat); argument kinds: ``

### WORLD_MAP_OPEN

- Status: ✅ verified
- Payload: `uiMapID: number?`
- fires synchronously (Blizzard's docs)

### ZONE_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 671 times (13 in combat); argument kinds: ``

### ZONE_CHANGED_INDOORS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 313 times (29 in combat); argument kinds: ``

### ZONE_CHANGED_NEW_AREA

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 177 times (2 in combat); argument kinds: ``

## Types

### MapBannerInfo

- Structure
  - `areaPoiID`: number
  - `name`: cstring
  - `atlasName`: string
  - `uiTextureKit`: textureKit?

### MapLinkInfo

- Structure
  - `areaPoiID`: number
  - `position`: vector2
  - `name`: cstring
  - `atlasName`: string
  - `linkedUiMapID`: number

### UiMapDetails

- Structure
  - `mapID`: number
  - `name`: cstring
  - `mapType`: UIMapType
  - `parentMapID`: number
  - `flags`: UIMapFlag

### UiMapGroupMemberInfo

- Structure
  - `mapID`: number
  - `relativeHeightIndex`: number
  - `name`: cstring

### UiMapHighlightInfo

- Structure
  - `fileDataID`: fileID
  - `atlasID`: textureAtlas
  - `texturePercentageX`: number
  - `texturePercentageY`: number
  - `textureX`: number
  - `textureY`: number
  - `scrollChildX`: number
  - `scrollChildY`: number

### UiMapLayerInfo

- Structure
  - `layerWidth`: number
  - `layerHeight`: number
  - `tileWidth`: number
  - `tileHeight`: number
  - `minScale`: number
  - `maxScale`: number
  - `additionalZoomSteps`: number
