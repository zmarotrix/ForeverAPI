# HousingCleanupModeUI

Namespace: `C_HousingCleanupMode`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_HousingCleanupMode.GetHoveredDecorInfo](#c_housingcleanupmodegethovereddecorinfo) | 1 value |  |
| ✅ | [C_HousingCleanupMode.IsHoveringDecor](#c_housingcleanupmodeishoveringdecor) | 1 value |  |
| ✅ | [C_HousingCleanupMode.RemoveSelectedDecor](#c_housingcleanupmoderemoveselecteddecor) |  |  |

### C_HousingCleanupMode.GetHoveredDecorInfo

`C_HousingCleanupMode.GetHoveredDecorInfo() → info: HousingDecorInstanceInfo?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Source: client docs `HousingCleanupModeUIDocumentation.lua`

### C_HousingCleanupMode.IsHoveringDecor

`C_HousingCleanupMode.IsHoveringDecor() → isHoveringDecor: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `HousingCleanupModeUIDocumentation.lua`

### C_HousingCleanupMode.RemoveSelectedDecor

`C_HousingCleanupMode.RemoveSelectedDecor()`

- Status: ✅ verified (function)
- Source: client docs `HousingCleanupModeUIDocumentation.lua`

## Events

### HOUSING_CLEANUP_MODE_HOVERED_TARGET_CHANGED

- Status: ✅ verified
- Payload: `hasHoveredTarget: bool`, `targetType: HousingCleanupModeTargetType`
- fires synchronously (Blizzard's docs)

### HOUSING_CLEANUP_MODE_TARGET_SELECTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### HousingCleanupModeTargetType

- Enumeration — ✅ verified
  - `None` = 0
  - `Decor` = 1
  - `HouseExterior` = 2
