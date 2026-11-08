# FogOfWar

Namespace: `C_FogOfWar`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_FogOfWar.GetFogOfWarForMap](#c_fogofwargetfogofwarformap) |  |  |
| ✅ | [C_FogOfWar.GetFogOfWarInfo](#c_fogofwargetfogofwarinfo) |  |  |

### C_FogOfWar.GetFogOfWarForMap

`C_FogOfWar.GetFogOfWarForMap(uiMapID: number) → fogOfWarID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FogOfWarDocumentation.lua`

### C_FogOfWar.GetFogOfWarInfo

`C_FogOfWar.GetFogOfWarInfo(fogOfWarID: number) → fogOfWarInfo: FogOfWarInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FogOfWarDocumentation.lua`

## Events

### FOG_OF_WAR_UPDATED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

## Types

### FogOfWarInfo

- Structure
  - `fogOfWarID`: number
  - `backgroundAtlas`: textureAtlas
  - `maskAtlas`: textureAtlas
  - `maskScalar`: number
