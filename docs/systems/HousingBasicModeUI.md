# HousingBasicModeUI

Namespace: `C_HousingBasicMode`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_HousingBasicMode.CancelActiveEditing](#c_housingbasicmodecancelactiveediting) | 0 values | 0 values |
| ✅ | [C_HousingBasicMode.CommitDecorMovement](#c_housingbasicmodecommitdecormovement) |  |  |
| ✅ | [C_HousingBasicMode.CommitHouseExteriorPosition](#c_housingbasicmodecommithouseexteriorposition) |  |  |
| ✅ | [C_HousingBasicMode.FinishPlacingNewDecor](#c_housingbasicmodefinishplacingnewdecor) |  |  |
| ✅ | [C_HousingBasicMode.GetHoveredDecorInfo](#c_housingbasicmodegethovereddecorinfo) | 1 value | 1 value |
| ✅ | [C_HousingBasicMode.GetSelectedDecorInfo](#c_housingbasicmodegetselecteddecorinfo) | 1 value | 1 value |
| ✅ | [C_HousingBasicMode.IsDecorSelected](#c_housingbasicmodeisdecorselected) | 1 value | 1 value |
| ✅ | [C_HousingBasicMode.IsFreePlaceEnabled](#c_housingbasicmodeisfreeplaceenabled) | 1 value | 1 value |
| ✅ | [C_HousingBasicMode.IsGridSnapEnabled](#c_housingbasicmodeisgridsnapenabled) | 1 value | 1 value |
| ✅ | [C_HousingBasicMode.IsGridVisible](#c_housingbasicmodeisgridvisible) | 1 value | 1 value |
| ✅ | [C_HousingBasicMode.IsHouseExteriorHovered](#c_housingbasicmodeishouseexteriorhovered) | 1 value | 1 value |
| ✅ | [C_HousingBasicMode.IsHouseExteriorSelected](#c_housingbasicmodeishouseexteriorselected) | 1 value | 1 value |
| ✅ | [C_HousingBasicMode.IsHoveringDecor](#c_housingbasicmodeishoveringdecor) | 1 value | 1 value |
| ✅ | [C_HousingBasicMode.IsPlacingNewDecor](#c_housingbasicmodeisplacingnewdecor) | 1 value | 1 value |
| ✅ | [C_HousingBasicMode.RemoveSelectedDecor](#c_housingbasicmoderemoveselecteddecor) |  |  |
| ✅ | [C_HousingBasicMode.RotateDecor](#c_housingbasicmoderotatedecor) |  |  |
| ✅ | [C_HousingBasicMode.RotateHouseExterior](#c_housingbasicmoderotatehouseexterior) |  |  |
| ✅ | [C_HousingBasicMode.SetFreePlaceEnabled](#c_housingbasicmodesetfreeplaceenabled) |  |  |
| ✅ | [C_HousingBasicMode.SetGridSnapEnabled](#c_housingbasicmodesetgridsnapenabled) |  |  |
| ✅ | [C_HousingBasicMode.SetGridVisible](#c_housingbasicmodesetgridvisible) |  |  |
| ✅ | [C_HousingBasicMode.StartPlacingNewDecor](#c_housingbasicmodestartplacingnewdecor) |  |  |
| ✅ | [C_HousingBasicMode.StartPlacingPreviewDecor](#c_housingbasicmodestartplacingpreviewdecor) |  |  |

### C_HousingBasicMode.CancelActiveEditing

`C_HousingBasicMode.CancelActiveEditing()`

- Status: ✅ verified (function)
- Blizzard: Cancels all in-progress editing of the selected target, which will reset any unsaved changes and deselect the active target; Un-placed decor will be returned to the house chest
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.CommitDecorMovement

`C_HousingBasicMode.CommitDecorMovement()`

- Status: ✅ verified (function)
- Blizzard: Attempt to save the changes made to the currently selected decor instance
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.CommitHouseExteriorPosition

`C_HousingBasicMode.CommitHouseExteriorPosition()`

- Status: ✅ verified (function)
- Blizzard: Attempt to save the changes made to the House Exterior's position within the plot
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.FinishPlacingNewDecor

`C_HousingBasicMode.FinishPlacingNewDecor()`

- Status: ✅ verified (function)
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.GetHoveredDecorInfo

`C_HousingBasicMode.GetHoveredDecorInfo() → info: HousingDecorInstanceInfo?`

- Status: ✅ verified (function)
- Blizzard: Returns info for the placed decor instance currently being hovered, if there is one
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.GetSelectedDecorInfo

`C_HousingBasicMode.GetSelectedDecorInfo() → info: HousingDecorInstanceInfo?`

- Status: ✅ verified (function)
- Blizzard: Returns info for the decor instance that's currently selected, if there is one
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.IsDecorSelected

`C_HousingBasicMode.IsDecorSelected() → hasSelectedDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a decor instance is currently selected and being dragged
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.IsFreePlaceEnabled

`C_HousingBasicMode.IsFreePlaceEnabled() → freePlaceEnabled: bool`

- Status: ✅ verified (function)
- Blizzard: When free place is enabled, collision checks while dragging decor/the house exterior are ignored
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.IsGridSnapEnabled

`C_HousingBasicMode.IsGridSnapEnabled() → isGridSnapEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.IsGridVisible

`C_HousingBasicMode.IsGridVisible() → gridVisible: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.IsHouseExteriorHovered

`C_HousingBasicMode.IsHouseExteriorHovered() → isHouseExteriorHovered: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the house's exterior is currently being hovered
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.IsHouseExteriorSelected

`C_HousingBasicMode.IsHouseExteriorSelected() → isHouseExteriorSelected: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the house's exterior is currently selected and being moved
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.IsHoveringDecor

`C_HousingBasicMode.IsHoveringDecor() → isHoveringDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a placed decor instance is currently being hovered
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.IsPlacingNewDecor

`C_HousingBasicMode.IsPlacingNewDecor() → hasPendingDecor: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.RemoveSelectedDecor

`C_HousingBasicMode.RemoveSelectedDecor()`

- Status: ✅ verified (function)
- Blizzard: Attempt to return the currently selected decor instance back to the house chest
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.RotateDecor

`C_HousingBasicMode.RotateDecor(rotDegrees: number)`

- Status: ✅ verified (function)
- Blizzard: Rotates the currently selected decor along a single axis; For wall decor, rotates such that the object stays flat against its current wall; For all other decor, rotates around the Z (vertical) axis
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.RotateHouseExterior

`C_HousingBasicMode.RotateHouseExterior(rotDegrees: number)`

- Status: ✅ verified (function)
- Blizzard: Rotates the House Exterior around the Z (vertical) axis
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.SetFreePlaceEnabled

`C_HousingBasicMode.SetFreePlaceEnabled(freePlaceEnabled: bool)`

- Status: ✅ verified (function)
- Blizzard: Set whether free place is enabled; When free place is enabled, collision checks while dragging decor/the house exterior are ignored
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.SetGridSnapEnabled

`C_HousingBasicMode.SetGridSnapEnabled(isGridSnapEnabled: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.SetGridVisible

`C_HousingBasicMode.SetGridVisible(gridVisible: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.StartPlacingNewDecor

`C_HousingBasicMode.StartPlacingNewDecor(catalogEntryVariantID: HousingCatalogEntryVariantID)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBasicModeUIDocumentation.lua`

### C_HousingBasicMode.StartPlacingPreviewDecor

`C_HousingBasicMode.StartPlacingPreviewDecor(decorRecordID: number, bundleCatalogShopProductID: number?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBasicModeUIDocumentation.lua`

## Events

### HOUSING_BASIC_MODE_HOVERED_TARGET_CHANGED

- Status: ✅ verified
- Payload: `hasHoveredTarget: bool`, `targetType: HousingBasicModeTargetType`
- fires synchronously (Blizzard's docs)

### HOUSING_BASIC_MODE_PLACEMENT_FLAGS_UPDATED

- Status: ✅ verified
- Payload: `targetType: HousingBasicModeTargetType`, `activeFlags: HousingDecorPlacementRestriction`
- fires synchronously (Blizzard's docs)

### HOUSING_BASIC_MODE_SELECTED_TARGET_CHANGED

- Status: ✅ verified
- Payload: `hasSelectedTarget: bool`, `targetType: HousingBasicModeTargetType`, `isPreview: bool`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_FREE_PLACE_STATUS_CHANGED

- Status: ✅ verified
- Payload: `isFreePlaceEnabled: bool`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_GRID_SNAP_OCCURRED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_GRID_SNAP_STATUS_CHANGED

- Status: ✅ verified
- Payload: `isGridSnapEnabled: bool`
- fires synchronously (Blizzard's docs)

## Types

### HousingBasicModeTargetType

- Enumeration — ✅ verified
  - `None` = 0
  - `Decor` = 1
  - `House` = 2
