# FogOfWar

Namespace: `C_FogOfWar`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_FogOfWar.GetFogOfWarForMap](#c_fogofwargetfogofwarformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_FogOfWar.GetFogOfWarInfo](#c_fogofwargetfogofwarinfo) |  |  |

### C_FogOfWar.GetFogOfWarForMap

`C_FogOfWar.GetFogOfWarForMap(uiMapID: number) → fogOfWarID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
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
- Seen firing 1088 times (26 in combat); argument kinds: ``

## Types

### FogOfWarInfo

- Structure
  - `fogOfWarID`: number
  - `backgroundAtlas`: textureAtlas
  - `maskAtlas`: textureAtlas
  - `maskScalar`: number
