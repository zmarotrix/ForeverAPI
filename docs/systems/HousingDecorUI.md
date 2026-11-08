# HousingDecorUI

Namespace: `C_HousingDecor`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_HousingDecor.AnyDecorPlacedInRoom](#c_housingdecoranydecorplacedinroom) |  |  |
| ❔ | [C_HousingDecor.CancelActiveEditing](#c_housingdecorcancelactiveediting) |  |  |
| ❔ | [C_HousingDecor.CommitDecorMovement](#c_housingdecorcommitdecormovement) |  |  |
| ❔ | [C_HousingDecor.EnterPreviewState](#c_housingdecorenterpreviewstate) |  |  |
| ❔ | [C_HousingDecor.ExitPreviewState](#c_housingdecorexitpreviewstate) |  |  |
| ❔ | [C_HousingDecor.GetAllMaxPlacementBudgets](#c_housingdecorgetallmaxplacementbudgets) |  |  |
| ❔ | [C_HousingDecor.GetAllPlacedDecor](#c_housingdecorgetallplaceddecor) |  |  |
| ❔ | [C_HousingDecor.GetAllSpentPlacementBudgets](#c_housingdecorgetallspentplacementbudgets) |  |  |
| ❔ | [C_HousingDecor.GetDecorAssignedPetName](#c_housingdecorgetdecorassignedpetname) |  |  |
| ❔ | [C_HousingDecor.GetDecorCanAttachPet](#c_housingdecorgetdecorcanattachpet) |  |  |
| ❔ | [C_HousingDecor.GetDecorHyperlink](#c_housingdecorgetdecorhyperlink) |  |  |
| ❔ | [C_HousingDecor.GetDecorIcon](#c_housingdecorgetdecoricon) |  |  |
| ❔ | [C_HousingDecor.GetDecorInstanceInfoForGUID](#c_housingdecorgetdecorinstanceinfoforguid) |  |  |
| ❔ | [C_HousingDecor.GetDecorName](#c_housingdecorgetdecorname) |  |  |
| ❔ | [C_HousingDecor.GetHoveredDecorInfo](#c_housingdecorgethovereddecorinfo) |  |  |
| ❔ | [C_HousingDecor.GetMaxPetPlacementBudget](#c_housingdecorgetmaxpetplacementbudget) |  |  |
| ❔ | [C_HousingDecor.GetMaxPlacementBudget](#c_housingdecorgetmaxplacementbudget) |  |  |
| ❔ | [C_HousingDecor.GetNumDecorPlaced](#c_housingdecorgetnumdecorplaced) |  |  |
| ❔ | [C_HousingDecor.GetNumPreviewDecor](#c_housingdecorgetnumpreviewdecor) |  |  |
| ❔ | [C_HousingDecor.GetSelectedDecorInfo](#c_housingdecorgetselecteddecorinfo) |  |  |
| ❔ | [C_HousingDecor.GetSpentPetPlacementBudget](#c_housingdecorgetspentpetplacementbudget) |  |  |
| ❔ | [C_HousingDecor.GetSpentPlacementBudget](#c_housingdecorgetspentplacementbudget) |  |  |
| ❔ | [C_HousingDecor.HasMaxPlacementBudget](#c_housingdecorhasmaxplacementbudget) |  |  |
| ❔ | [C_HousingDecor.IsDecorSelected](#c_housingdecorisdecorselected) |  |  |
| ❔ | [C_HousingDecor.IsGridVisible](#c_housingdecorisgridvisible) |  |  |
| ❔ | [C_HousingDecor.IsHouseExteriorDoorHovered](#c_housingdecorishouseexteriordoorhovered) |  |  |
| ❔ | [C_HousingDecor.IsHouseExteriorHovered](#c_housingdecorishouseexteriorhovered) |  |  |
| ❔ | [C_HousingDecor.IsHoveringDecor](#c_housingdecorishoveringdecor) |  |  |
| ❔ | [C_HousingDecor.IsModeDisabledForPreviewState](#c_housingdecorismodedisabledforpreviewstate) |  |  |
| ❔ | [C_HousingDecor.IsPreviewState](#c_housingdecorispreviewstate) |  |  |
| ❔ | [C_HousingDecor.RemovePlacedDecorEntry](#c_housingdecorremoveplaceddecorentry) |  |  |
| ❔ | [C_HousingDecor.RemoveSelectedDecor](#c_housingdecorremoveselecteddecor) |  |  |
| ❔ | [C_HousingDecor.SetGridVisible](#c_housingdecorsetgridvisible) |  |  |
| ❔ | [C_HousingDecor.SetPlacedDecorEntryHovered](#c_housingdecorsetplaceddecorentryhovered) |  |  |
| ❔ | [C_HousingDecor.SetPlacedDecorEntrySelected](#c_housingdecorsetplaceddecorentryselected) |  |  |

### C_HousingDecor.AnyDecorPlacedInRoom

`C_HousingDecor.AnyDecorPlacedInRoom(roomGUID: WOWGUID) → isPlaced: bool`

- Status: ❔ unverified
- Blizzard: Returns true if any decor objects are placed in a given room
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.CancelActiveEditing

`C_HousingDecor.CancelActiveEditing()`

- Status: ❔ unverified
- Blizzard: Cancels all in-progress editing of the selected target, which will reset any unsaved changes and deselect the active target
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.CommitDecorMovement

`C_HousingDecor.CommitDecorMovement()`

- Status: ❔ unverified
- Blizzard: Attempt to save the changes made to the currently selected decor instance
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.EnterPreviewState

`C_HousingDecor.EnterPreviewState()`

- Status: ❔ unverified
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.ExitPreviewState

`C_HousingDecor.ExitPreviewState()`

- Status: ❔ unverified
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetAllMaxPlacementBudgets

`C_HousingDecor.GetAllMaxPlacementBudgets() → interiorMaxBudgets: number[]?, exteriorMaxBudgets: number[]?`

- Status: ❔ unverified
- Blizzard: Returns the interior and exterior max decor placement budgets for the current owned house interior or plot; Can be increased via house level
- `interiorMaxBudgets`: Map of budget type to max budget amount; Will be nil if not in an owned House or Plot
- `exteriorMaxBudgets`: Map of budget type to max budget amount; Will be nil if not in an owned House or Plot
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetAllPlacedDecor

`C_HousingDecor.GetAllPlacedDecor() → placedDecor: HousingDecorInstanceListEntry[]`

- Status: ❔ unverified
- Blizzard: Placed Decor List APIs currently restricted due to being potentially very expensive operations, may be reworked & opened up in the future
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetAllSpentPlacementBudgets

`C_HousingDecor.GetAllSpentPlacementBudgets() → interiorSpentBudgets: number[]?, exteriorSpentBudgets: number[]?`

- Status: ❔ unverified
- Blizzard: Returns how much of the interior and exterior placement budgets for the current owned house interior or plot's decor budget have been spent
- `interiorSpentBudgets`: Map of budget type to spent budget amount; Will be nil if not in an owned House or Plot
- `exteriorSpentBudgets`: Map of budget type to spent budget amount; Will be nil if not in an owned House or Plot
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetDecorAssignedPetName

`C_HousingDecor.GetDecorAssignedPetName(decorGUID: WOWGUID) → name: string?`

- Status: ❔ unverified
- Blizzard: Returns pet name for the placed decor instance associated with the passed Decor GUID, if there is one
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetDecorCanAttachPet

`C_HousingDecor.GetDecorCanAttachPet(decorID: number) → canAttachPet: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetDecorHyperlink

`C_HousingDecor.GetDecorHyperlink(decorID: number) → hyperLink: string`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetDecorIcon

`C_HousingDecor.GetDecorIcon(decorID: number) → icon: fileID`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetDecorInstanceInfoForGUID

`C_HousingDecor.GetDecorInstanceInfoForGUID(decorGUID: WOWGUID) → info: HousingDecorInstanceInfo?`

- Status: ❔ unverified
- Blizzard: Returns info for the placed decor instance associated with the passed Decor GUID, if there is one
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetDecorName

`C_HousingDecor.GetDecorName(decorID: number) → name: string`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetHoveredDecorInfo

`C_HousingDecor.GetHoveredDecorInfo() → info: HousingDecorInstanceInfo?`

- Status: ❔ unverified
- Blizzard: Returns info for the placed decor instance currently being hovered, if there is one
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetMaxPetPlacementBudget

`C_HousingDecor.GetMaxPetPlacementBudget() → maxBudget: number?`

- Status: ❔ unverified
- Blizzard: Returns the max pet decor placement budget for the current owned house interior or plot
- `maxBudget`: Will be nil if not in an owned House or Plot
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetMaxPlacementBudget

`C_HousingDecor.GetMaxPlacementBudget() → maxBudget: number?`

- Status: ❔ unverified
- Blizzard: Returns the max decor placement budget for the current owned house interior or plot; Can be increased via house level
- `maxBudget`: Will be nil if not in an owned House or Plot
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetNumDecorPlaced

`C_HousingDecor.GetNumDecorPlaced() → numPlaced: number`

- Status: ❔ unverified
- Blizzard: Returns the number of individual decor objects placed in the current house or plot; This is NOT the value used in placement budget calculations, see GetSpentPlacementBudget for that
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetNumPreviewDecor

`C_HousingDecor.GetNumPreviewDecor() → numDecor: number`

- Status: ❔ unverified
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetSelectedDecorInfo

`C_HousingDecor.GetSelectedDecorInfo() → info: HousingDecorInstanceInfo?`

- Status: ❔ unverified
- Blizzard: Returns info for the placed decor instance that's currently selected, if there is one
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetSpentPetPlacementBudget

`C_HousingDecor.GetSpentPetPlacementBudget() → totalCost: number?`

- Status: ❔ unverified
- Blizzard: Returns how much of the current owned house interior or plot's pet decor placement budget has been spent
- `totalCost`: Will be nil if not in an owned House or Plot
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.GetSpentPlacementBudget

`C_HousingDecor.GetSpentPlacementBudget() → totalCost: number?`

- Status: ❔ unverified
- Blizzard: Returns how much of the current owned house interior or plot's decor placement budget has been spent; Different kinds of decor take up different budget amounts, so this value isn't an individual decor count, see GetNumDecorPlaced for that
- `totalCost`: Will be nil if not in an owned House or Plot
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.HasMaxPlacementBudget

`C_HousingDecor.HasMaxPlacementBudget() → hasMaxBudget: bool`

- Status: ❔ unverified
- Blizzard: Returns whether there's a max decor placement budget available and active for the current player, in the current house interior or plot
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.IsDecorSelected

`C_HousingDecor.IsDecorSelected() → hasSelectedDecor: bool`

- Status: ❔ unverified
- Blizzard: Returns true if a placed decor instance is currently selected
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.IsGridVisible

`C_HousingDecor.IsGridVisible() → gridVisible: bool`

- Status: ❔ unverified
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.IsHouseExteriorDoorHovered

`C_HousingDecor.IsHouseExteriorDoorHovered() → isHouseExteriorDoorHovered: bool`

- Status: ❔ unverified
- Blizzard: Returns true if the entry door of the house's exterior is currently being hovered
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.IsHouseExteriorHovered

`C_HousingDecor.IsHouseExteriorHovered() → isHouseExteriorHovered: bool`

- Status: ❔ unverified
- Blizzard: Returns true if the house's exterior is currently being hovered
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.IsHoveringDecor

`C_HousingDecor.IsHoveringDecor() → isHoveringDecor: bool`

- Status: ❔ unverified
- Blizzard: Returns true if a placed decor instance is currently being hovered
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.IsModeDisabledForPreviewState

`C_HousingDecor.IsModeDisabledForPreviewState(mode: HouseEditorMode) → isModeDisabled: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.IsPreviewState

`C_HousingDecor.IsPreviewState() → isPreviewState: bool`

- Status: ❔ unverified
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.RemovePlacedDecorEntry

`C_HousingDecor.RemovePlacedDecorEntry(decorGUID: WOWGUID)`

- Status: ❔ unverified
- Blizzard: Placed Decor List APIs currently restricted due to being potentially very expensive operations, may be reworked & opened up in the future
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.RemoveSelectedDecor

`C_HousingDecor.RemoveSelectedDecor()`

- Status: ❔ unverified
- Blizzard: Attempt to return the currently selected decor instance back to the house chest
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.SetGridVisible

`C_HousingDecor.SetGridVisible(gridVisible: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.SetPlacedDecorEntryHovered

`C_HousingDecor.SetPlacedDecorEntryHovered(decorGUID: WOWGUID, hovered: bool)`

- Status: ❔ unverified
- Blizzard: Placed Decor List APIs currently restricted due to being potentially very expensive operations, may be reworked & opened up in the future
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

### C_HousingDecor.SetPlacedDecorEntrySelected

`C_HousingDecor.SetPlacedDecorEntrySelected(decorGUID: WOWGUID, selected: bool)`

- Status: ❔ unverified
- Blizzard: Placed Decor List APIs currently restricted due to being potentially very expensive operations, may be reworked & opened up in the future
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingDecorUIDocumentation.lua`

## Events

### HOUSE_DECOR_ADDED_TO_CHEST

- Status: ❔ unverified
- Payload: `decorGUID: WOWGUID`, `decorID: number`
- fires synchronously (Blizzard's docs)

### HOUSE_EXTERIOR_POSITION_FAILURE

- Status: ❔ unverified
- Payload: `housingResult: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSE_EXTERIOR_POSITION_SUCCESS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_GRID_VISIBILITY_STATUS_CHANGED

- Status: ❔ unverified
- Payload: `isGridVisible: bool`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_PLACE_FAILURE

- Status: ❔ unverified
- Payload: `housingResult: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_PLACE_SUCCESS

- Status: ❔ unverified
- Payload: `decorGUID: WOWGUID`, `size: HousingCatalogEntrySize`, `isNew: bool`, `isPreview: bool`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_PREVIEW_STATE_CHANGED

- Status: ❔ unverified
- Payload: `isPreviewState: bool`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_REMOVED

- Status: ❔ unverified
- Payload: `decorGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_SELECT_RESPONSE

- Status: ❔ unverified
- Payload: `result: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_NEW_DECOR_PLACE_COMPLETE

- Status: ❔ unverified
- Payload: `decorGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### HOUSING_NUM_DECOR_PLACED_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### HousingDecorInstanceListEntry

- Structure
- Blizzard: Smaller structs with the minimum fields from HousingDecorInstanceInfo needed to identify/display a slim list of placed decor
  - `decorGUID`: WOWGUID
  - `name`: cstring

### LightRadiusIndicatorType

- Enumeration — ❔ unverified
  - `Always` = 0
  - `Overlap` = 1
  - `Never` = 2
