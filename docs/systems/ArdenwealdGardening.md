# ArdenwealdGardening

Namespace: `C_ArdenwealdGardening`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ArdenwealdGardening.GetGardenData](#c_ardenwealdgardeninggetgardendata) | 1 value |  |
| ✅ | [C_ArdenwealdGardening.IsGardenAccessible](#c_ardenwealdgardeningisgardenaccessible) | 1 value |  |

### C_ArdenwealdGardening.GetGardenData

`C_ArdenwealdGardening.GetGardenData() → data: ArdenwealdGardenData`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{active=number,ready=number,remainingSeconds=number}`
- Source: client docs `ArdenwealdGardeningDocumentation.lua`

### C_ArdenwealdGardening.IsGardenAccessible

`C_ArdenwealdGardening.IsGardenAccessible() → accessible: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ArdenwealdGardeningDocumentation.lua`

## Types

### ArdenwealdGardenData

- Structure
  - `active`: number
  - `ready`: number
  - `remainingSeconds`: time_t
