# Vignette

Namespace: `C_VignetteInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_VignetteInfo.FindBestUniqueVignette](#c_vignetteinfofindbestuniquevignette) |  |  |
| ✅ | [C_VignetteInfo.GetHealthPercent](#c_vignetteinfogethealthpercent) |  |  |
| ✅ | [C_VignetteInfo.GetRecommendedGroupSize](#c_vignetteinfogetrecommendedgroupsize) |  |  |
| ✅ | [C_VignetteInfo.GetVignetteInfo](#c_vignetteinfogetvignetteinfo) |  |  |
| ✅ | [C_VignetteInfo.GetVignettePosition](#c_vignetteinfogetvignetteposition) |  |  |
| ✅ | [C_VignetteInfo.GetVignettes](#c_vignetteinfogetvignettes) | 1 value |  |

### C_VignetteInfo.FindBestUniqueVignette

`C_VignetteInfo.FindBestUniqueVignette(vignetteGUIDs: WOWGUID[]) → bestUniqueVignetteIndex: luaIndex?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `VignetteInfoDocumentation.lua`

### C_VignetteInfo.GetHealthPercent

`C_VignetteInfo.GetHealthPercent(vignetteGUID: WOWGUID) → healthPct: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `VignetteInfoDocumentation.lua`

### C_VignetteInfo.GetRecommendedGroupSize

`C_VignetteInfo.GetRecommendedGroupSize(vignetteGUID: WOWGUID) → minGroupSize: number, maxGroupSize: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `VignetteInfoDocumentation.lua`

### C_VignetteInfo.GetVignetteInfo

`C_VignetteInfo.GetVignetteInfo(vignetteGUID: WOWGUID) → vignetteInfo: VignetteInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `VignetteInfoDocumentation.lua`

### C_VignetteInfo.GetVignettePosition

`C_VignetteInfo.GetVignettePosition(vignetteGUID: WOWGUID, uiMapID: number) → vignettePosition: vector2, vignetteFacing: number?`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `VignetteInfoDocumentation.lua`

### C_VignetteInfo.GetVignettes

`C_VignetteInfo.GetVignettes() → vignetteGUIDs: WOWGUID[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `VignetteInfoDocumentation.lua`

## Events

### VIGNETTES_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### VIGNETTE_MINIMAP_UPDATED

- Status: ✅ verified
- Payload: `vignetteGUID: WOWGUID`, `onMinimap: bool`
- unique event (Blizzard's docs)

## Types

### VignetteInfo

- Structure
  - `vignetteGUID`: WOWGUID
  - `objectGUID`: WOWGUID
  - `name`: cstring
  - `isDead`: bool
  - `onWorldMap`: bool
  - `zoneInfiniteAOI`: bool
  - `onMinimap`: bool
  - `isUnique`: bool
  - `inFogOfWar`: bool
  - `atlasName`: textureAtlas
  - `hasTooltip`: bool
  - `vignetteID`: number
  - `type`: VignetteType
  - `rewardQuestID`: number
  - `tooltipWidgetSet`: number?
  - `iconWidgetSet`: number?
  - `addPaddingAboveTooltipWidgets`: bool?
  - `mapPin`: UIMapPinInfo?
  - `objectiveType`: VignetteObjectiveType?
