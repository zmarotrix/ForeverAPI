# WorldSafeLocsUIInternal

Namespace: `C_WorldSafeLocsUIInternal`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ⛔ | [C_WorldSafeLocsUIInternal.GetWorldSafeLocs](#c_worldsafelocsuiinternalgetworldsafelocs) | missing |  |

### C_WorldSafeLocsUIInternal.GetWorldSafeLocs

`C_WorldSafeLocsUIInternal.GetWorldSafeLocs() → worldSafeLocs: WorldSafeLocInfo[]`

- Status: ⛔ in Blizzard's docs, not in game
- Called out of combat: missing at call time
- Source: client docs `WorldSafeLocsUIInternalDocumentation.lua`

## Types

### WorldSafeLocInfo

- Structure
  - `name`: string
  - `continent`: number
  - `loc`: vector3
  - `facing`: number
