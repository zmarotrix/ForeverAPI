# TaxiMap

Namespace: `C_TaxiMap`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_TaxiMap.GetAllTaxiNodes](#c_taximapgetalltaxinodes) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_TaxiMap.GetTaxiNodesForMap](#c_taximapgettaxinodesformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_TaxiMap.ShouldMapShowTaxiNodes](#c_taximapshouldmapshowtaxinodes) | 💥 no sample for map | 💥 no sample for map |

### C_TaxiMap.GetAllTaxiNodes

`C_TaxiMap.GetAllTaxiNodes(uiMapID: number) → taxiNodes: TaxiNodeInfo[]`

- Status: ✅ verified (function)
- Blizzard: Returns information on taxi nodes at the current flight master.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `TaxiMapDocumentation.lua`

### C_TaxiMap.GetTaxiNodesForMap

`C_TaxiMap.GetTaxiNodesForMap(uiMapID: number) → mapTaxiNodes: MapTaxiNodeInfo[]`

- Status: ✅ verified (function)
- Blizzard: Returns information on taxi nodes for a given map, without considering the current flight master.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `TaxiMapDocumentation.lua`

### C_TaxiMap.ShouldMapShowTaxiNodes

`C_TaxiMap.ShouldMapShowTaxiNodes(uiMapID: number) → shouldShowNodes: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `TaxiMapDocumentation.lua`

## Events

### TAXIMAP_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 18 times (0 in combat); argument kinds: ``

### TAXIMAP_OPENED

- Status: ✅ verified
- Payload: `system: number`
- fires synchronously (Blizzard's docs)

### TAXI_NODE_STATUS_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### FlightPathFaction

- Enumeration — ✅ verified
  - `Neutral` = 0
  - `Horde` = 1
  - `Alliance` = 2

### FlightPathState

- Enumeration — ✅ verified
  - `Current` = 0
  - `Reachable` = 1
  - `Unreachable` = 2

### MapTaxiNodeInfo

- Structure
  - `nodeID`: number
  - `position`: vector2
  - `name`: cstring
  - `atlasName`: cstring
  - `faction`: FlightPathFaction
  - `textureKit`: textureKit
  - `isUndiscovered`: bool

### TaxiNodeInfo

- Structure
  - `nodeID`: number
  - `position`: vector2
  - `name`: cstring
  - `state`: FlightPathState
  - `slotIndex`: luaIndex
  - `textureKit`: textureKit
  - `useSpecialIcon`: bool
  - `specialIconCostString`: string?
  - `isMapLayerTransition`: bool
