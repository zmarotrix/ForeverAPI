# MapExplorationInfo

Namespace: `C_MapExplorationInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_MapExplorationInfo.GetExploredAreaIDsAtPosition](#c_mapexplorationinfogetexploredareaidsatposition) |  |  |
| ❔ | [C_MapExplorationInfo.GetExploredMapTextures](#c_mapexplorationinfogetexploredmaptextures) |  |  |

### C_MapExplorationInfo.GetExploredAreaIDsAtPosition

`C_MapExplorationInfo.GetExploredAreaIDsAtPosition(uiMapID: number, normalizedPosition: vector2) → areaID: number[]?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapExplorationDocumentation.lua`

### C_MapExplorationInfo.GetExploredMapTextures

`C_MapExplorationInfo.GetExploredMapTextures(uiMapID: number) → overlayInfo: UiMapExplorationInfo[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MapExplorationDocumentation.lua`

## Events

### MAP_EXPLORATION_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### UiMapExplorationHitRect

- Structure
  - `top`: number
  - `bottom`: number
  - `left`: number
  - `right`: number

### UiMapExplorationInfo

- Structure
  - `textureWidth`: number
  - `textureHeight`: number
  - `offsetX`: number
  - `offsetY`: number
  - `isShownByMouseOver`: bool
  - `isDrawOnTopLayer`: bool
  - `fileDataIDs`: number[]
  - `hitRect`: UiMapExplorationHitRect
