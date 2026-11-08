# HousingCleanupModeUI

Namespace: `C_HousingCleanupMode`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_HousingCleanupMode.GetHoveredDecorInfo](#c_housingcleanupmodegethovereddecorinfo) |  |  |
| ❔ | [C_HousingCleanupMode.IsHoveringDecor](#c_housingcleanupmodeishoveringdecor) |  |  |
| ❔ | [C_HousingCleanupMode.RemoveSelectedDecor](#c_housingcleanupmoderemoveselecteddecor) |  |  |

### C_HousingCleanupMode.GetHoveredDecorInfo

`C_HousingCleanupMode.GetHoveredDecorInfo() → info: HousingDecorInstanceInfo?`

- Status: ❔ unverified
- Source: client docs `HousingCleanupModeUIDocumentation.lua`

### C_HousingCleanupMode.IsHoveringDecor

`C_HousingCleanupMode.IsHoveringDecor() → isHoveringDecor: bool`

- Status: ❔ unverified
- Source: client docs `HousingCleanupModeUIDocumentation.lua`

### C_HousingCleanupMode.RemoveSelectedDecor

`C_HousingCleanupMode.RemoveSelectedDecor()`

- Status: ❔ unverified
- Source: client docs `HousingCleanupModeUIDocumentation.lua`

## Events

### HOUSING_CLEANUP_MODE_HOVERED_TARGET_CHANGED

- Status: ❔ unverified
- Payload: `hasHoveredTarget: bool`, `targetType: HousingCleanupModeTargetType`
- fires synchronously (Blizzard's docs)

### HOUSING_CLEANUP_MODE_TARGET_SELECTED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### HousingCleanupModeTargetType

- Enumeration — ❔ unverified
  - `None` = 0
  - `Decor` = 1
  - `HouseExterior` = 2
