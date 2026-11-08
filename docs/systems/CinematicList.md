# CinematicList

Namespace: `C_CinematicList`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ⛔ | [C_CinematicList.GetUICinematicList](#c_cinematiclistgetuicinematiclist) | missing |  |

### C_CinematicList.GetUICinematicList

`C_CinematicList.GetUICinematicList() → cinematics: UICinematic[]`

- Status: ⛔ in Blizzard's docs, not in game
- Called out of combat: missing at call time
- Source: client docs `CinematicListDocumentation.lua`

## Types

### UICinematic

- Structure
  - `expansion`: number
  - `movieIDs`: number[]
  - `buttonUpAtlas`: textureAtlas
  - `buttonDownAtlas`: textureAtlas
  - `title`: string?
  - `disableAutoPlay`: bool
  - `orderID`: number
