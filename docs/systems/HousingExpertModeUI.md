# HousingExpertModeUI

Namespace: `C_HousingExpertMode`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_HousingExpertMode.CancelActiveEditing](#c_housingexpertmodecancelactiveediting) |  |  |
| ✅ | [C_HousingExpertMode.CommitDecorMovement](#c_housingexpertmodecommitdecormovement) |  |  |
| ✅ | [C_HousingExpertMode.CommitHouseExteriorPosition](#c_housingexpertmodecommithouseexteriorposition) |  |  |
| ✅ | [C_HousingExpertMode.GetHoveredDecorInfo](#c_housingexpertmodegethovereddecorinfo) |  |  |
| ✅ | [C_HousingExpertMode.GetPrecisionSubmode](#c_housingexpertmodegetprecisionsubmode) |  |  |
| ✅ | [C_HousingExpertMode.GetPrecisionSubmodeRestriction](#c_housingexpertmodegetprecisionsubmoderestriction) |  |  |
| ✅ | [C_HousingExpertMode.GetSelectedDecorInfo](#c_housingexpertmodegetselecteddecorinfo) |  |  |
| ✅ | [C_HousingExpertMode.IsDecorSelected](#c_housingexpertmodeisdecorselected) |  |  |
| ✅ | [C_HousingExpertMode.IsGridVisible](#c_housingexpertmodeisgridvisible) |  |  |
| ✅ | [C_HousingExpertMode.IsHouseExteriorHovered](#c_housingexpertmodeishouseexteriorhovered) |  |  |
| ✅ | [C_HousingExpertMode.IsHouseExteriorSelected](#c_housingexpertmodeishouseexteriorselected) |  |  |
| ✅ | [C_HousingExpertMode.IsHoveringDecor](#c_housingexpertmodeishoveringdecor) |  |  |
| ✅ | [C_HousingExpertMode.RemoveSelectedDecor](#c_housingexpertmoderemoveselecteddecor) |  |  |
| ✅ | [C_HousingExpertMode.ResetPrecisionChanges](#c_housingexpertmoderesetprecisionchanges) |  |  |
| ✅ | [C_HousingExpertMode.SelectNextRotationAxis](#c_housingexpertmodeselectnextrotationaxis) |  |  |
| ✅ | [C_HousingExpertMode.SetGridVisible](#c_housingexpertmodesetgridvisible) |  |  |
| ✅ | [C_HousingExpertMode.SetPrecisionIncrementingActive](#c_housingexpertmodesetprecisionincrementingactive) |  |  |
| ✅ | [C_HousingExpertMode.SetPrecisionSubmode](#c_housingexpertmodesetprecisionsubmode) |  |  |

### C_HousingExpertMode.CancelActiveEditing

`C_HousingExpertMode.CancelActiveEditing()`

- Status: ✅ verified (function)
- Blizzard: Cancels all in-progress editing of the selected target, which will reset any unsaved changes and deselect the active target; Will not reset any already-applied changes
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.CommitDecorMovement

`C_HousingExpertMode.CommitDecorMovement()`

- Status: ✅ verified (function)
- Blizzard: Attempt to save the changes made to the currently selected decor instance
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.CommitHouseExteriorPosition

`C_HousingExpertMode.CommitHouseExteriorPosition()`

- Status: ✅ verified (function)
- Blizzard: Attempt to save the changes made to the House Exterior's position within the plot
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.GetHoveredDecorInfo

`C_HousingExpertMode.GetHoveredDecorInfo() → info: HousingDecorInstanceInfo?`

- Status: ✅ verified (function)
- Blizzard: Returns info for the placed decor instance currently being hovered, if there is one
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.GetPrecisionSubmode

`C_HousingExpertMode.GetPrecisionSubmode() → activeSubMode: HousingPrecisionSubmode?`

- Status: ✅ verified (function)
- Blizzard: Returns the currently active Expert submode, if there is one
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.GetPrecisionSubmodeRestriction

`C_HousingExpertMode.GetPrecisionSubmodeRestriction(subMode: HousingPrecisionSubmode) → restriction: HousingExpertSubmodeRestriction`

- Status: ✅ verified (function)
- Blizzard: Returns the type of restriction currently active on the submode; Will return HousingExpertSubmodeRestriction:None if submode is not currently restricted
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.GetSelectedDecorInfo

`C_HousingExpertMode.GetSelectedDecorInfo() → info: HousingDecorInstanceInfo?`

- Status: ✅ verified (function)
- Blizzard: Returns info for the placed decor instance that's currently selected, if there is one
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.IsDecorSelected

`C_HousingExpertMode.IsDecorSelected() → hasSelectedDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a placed decor instance is currently selected
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.IsGridVisible

`C_HousingExpertMode.IsGridVisible() → gridVisible: bool`

- Status: ✅ verified (function)
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.IsHouseExteriorHovered

`C_HousingExpertMode.IsHouseExteriorHovered() → isHouseExteriorHovered: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the house's exterior is currently being hovered
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.IsHouseExteriorSelected

`C_HousingExpertMode.IsHouseExteriorSelected() → isHouseExteriorSelected: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the house's exterior is currently selected
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.IsHoveringDecor

`C_HousingExpertMode.IsHoveringDecor() → isHoveringDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a placed decor instance is currently being hovered
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.RemoveSelectedDecor

`C_HousingExpertMode.RemoveSelectedDecor()`

- Status: ✅ verified (function)
- Blizzard: Attempt to return the currently selected decor instance back to the house chest
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.ResetPrecisionChanges

`C_HousingExpertMode.ResetPrecisionChanges(activeSubmodeOnly: bool)`

- Status: ✅ verified (function)
- Blizzard: Reset the selected target's transform back to default values; This is NOT an undo, meaning it will completely reset the transform value to default, NOT just recently-made changes
- `activeSubmodeOnly`: If true, only transform values associated with the currently active submode with be reset (ex: in Scale submode, only target's scale will be reset); If false, all transform values will be reset
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.SelectNextRotationAxis

`C_HousingExpertMode.SelectNextRotationAxis()`

- Status: ✅ verified (function)
- Blizzard: In the rotation submode, swaps the selected axis to the next available one, in order of X -> Y -> Z (wrapping back around to X again, etc); If no axis is selected, selects the first available one, also in that order
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.SetGridVisible

`C_HousingExpertMode.SetGridVisible(gridVisible: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.SetPrecisionIncrementingActive

`C_HousingExpertMode.SetPrecisionIncrementingActive(incrementType: HousingIncrementType, active: bool)`

- Status: ✅ verified (function)
- Blizzard: Sets a specific type of incremental change active or inactive; Whilever that type is active and target stays selected, incremental changes of that type will continue to be made every frame
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingExpertModeUIDocumentation.lua`

### C_HousingExpertMode.SetPrecisionSubmode

`C_HousingExpertMode.SetPrecisionSubmode(subMode: HousingPrecisionSubmode)`

- Status: ✅ verified (function)
- Blizzard: Activate a specific Expert submode
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingExpertModeUIDocumentation.lua`

## Events

### HOUSING_DECOR_PRECISION_MANIPULATION_EVENT

- Status: ✅ verified
- Payload: `event: TransformManipulatorEvent`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_PRECISION_MANIPULATION_STATUS_CHANGED

- Status: ✅ verified
- Payload: `isManipulatingSelection: bool`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_PRECISION_SUBMODE_CHANGED

- Status: ✅ verified
- Payload: `activeSubmode: HousingPrecisionSubmode?`
- fires synchronously (Blizzard's docs)

### HOUSING_EXPERT_MODE_HOVERED_TARGET_CHANGED

- Status: ✅ verified
- Payload: `hasHoveredTarget: bool`, `targetType: HousingExpertModeTargetType`
- fires synchronously (Blizzard's docs)

### HOUSING_EXPERT_MODE_PLACEMENT_FLAGS_UPDATED

- Status: ✅ verified
- Payload: `targetType: HousingExpertModeTargetType`, `activeFlags: HousingDecorPlacementRestriction`
- fires synchronously (Blizzard's docs)

### HOUSING_EXPERT_MODE_SELECTED_TARGET_CHANGED

- Status: ✅ verified
- Payload: `hasSelectedTarget: bool`, `targetType: HousingExpertModeTargetType`
- fires synchronously (Blizzard's docs)

## Types

### HousingExpertModeTargetType

- Enumeration — ✅ verified
  - `None` = 0
  - `Decor` = 1
  - `House` = 2

### HousingExpertSubmodeRestriction

- Enumeration — ✅ verified
  - `None` = 0
  - `NotInExpertMode` = 1
  - `NoHouseExteriorScale` = 2
  - `NoWMOScale` = 3

### HousingIncrementType

- Enumeration — ✅ verified
  - `Left` = 1
  - `Right` = 2
  - `Forward` = 4
  - `Back` = 8
  - `Up` = 16
  - `Down` = 32
  - `RotateLeft` = 64
  - `RotateRight` = 128
  - `ScaleUp` = 256
  - `ScaleDown` = 512

### HousingPrecisionSubmode

- Enumeration — ✅ verified
  - `Translate` = 0
  - `Rotate` = 1
  - `Scale` = 2
