# BarberShop

Namespace: `C_BarberShopInternal`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_BarberShop.ApplyCustomizationChoices](#c_barbershopapplycustomizationchoices) |  |  |
| ✅ | [C_BarberShop.Cancel](#c_barbershopcancel) |  |  |
| ✅ | [C_BarberShop.ClearPreviewChoices](#c_barbershopclearpreviewchoices) |  |  |
| ✅ | [C_BarberShop.GetAvailableCustomizations](#c_barbershopgetavailablecustomizations) |  |  |
| ✅ | [C_BarberShop.GetCurrentCameraZoom](#c_barbershopgetcurrentcamerazoom) |  |  |
| ✅ | [C_BarberShop.GetCurrentCharacterData](#c_barbershopgetcurrentcharacterdata) |  |  |
| ✅ | [C_BarberShop.GetCurrentCost](#c_barbershopgetcurrentcost) |  |  |
| ✅ | [C_BarberShop.GetViewingChrModel](#c_barbershopgetviewingchrmodel) |  |  |
| ✅ | [C_BarberShop.HasAlteredForm](#c_barbershophasalteredform) |  |  |
| ✅ | [C_BarberShop.HasAnyChanges](#c_barbershophasanychanges) |  |  |
| ✅ | [C_BarberShop.HasCustomizationFeature](#c_barbershophascustomizationfeature) |  |  |
| ✅ | [C_BarberShop.IsViewingAlteredForm](#c_barbershopisviewingalteredform) |  |  |
| ✅ | [C_BarberShop.MarkCustomizationChoiceAsSeen](#c_barbershopmarkcustomizationchoiceasseen) |  |  |
| ✅ | [C_BarberShop.MarkCustomizationOptionAsSeen](#c_barbershopmarkcustomizationoptionasseen) |  |  |
| ✅ | [C_BarberShop.PreviewCustomizationChoice](#c_barbershoppreviewcustomizationchoice) |  |  |
| ✅ | [C_BarberShop.RandomizeCustomizationChoices](#c_barbershoprandomizecustomizationchoices) |  |  |
| ✅ | [C_BarberShop.ResetCameraRotation](#c_barbershopresetcamerarotation) |  |  |
| ✅ | [C_BarberShop.ResetCustomizationChoices](#c_barbershopresetcustomizationchoices) |  |  |
| ✅ | [C_BarberShop.RotateCamera](#c_barbershoprotatecamera) |  |  |
| ✅ | [C_BarberShop.SaveSeenChoices](#c_barbershopsaveseenchoices) |  |  |
| ✅ | [C_BarberShop.SetCameraDistanceOffset](#c_barbershopsetcameradistanceoffset) |  |  |
| ✅ | [C_BarberShop.SetCameraZoomLevel](#c_barbershopsetcamerazoomlevel) |  |  |
| ✅ | [C_BarberShop.SetCustomizationChoice](#c_barbershopsetcustomizationchoice) |  |  |
| ✅ | [C_BarberShop.SetModelDressState](#c_barbershopsetmodeldressstate) |  |  |
| ✅ | [C_BarberShop.SetSelectedSex](#c_barbershopsetselectedsex) |  |  |
| ✅ | [C_BarberShop.SetViewingAlteredForm](#c_barbershopsetviewingalteredform) |  |  |
| ✅ | [C_BarberShop.SetViewingChrModel](#c_barbershopsetviewingchrmodel) |  |  |
| ✅ | [C_BarberShop.SetViewingShapeshiftForm](#c_barbershopsetviewingshapeshiftform) |  |  |
| ✅ | [C_BarberShop.ZoomCamera](#c_barbershopzoomcamera) |  |  |
| ⛔ | [C_BarberShopInternal.SetQAMode](#c_barbershopinternalsetqamode) |  |  |

### C_BarberShop.ApplyCustomizationChoices

`C_BarberShop.ApplyCustomizationChoices() → success: bool`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.Cancel

`C_BarberShop.Cancel()`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.ClearPreviewChoices

`C_BarberShop.ClearPreviewChoices(clearSavedChoices: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.GetAvailableCustomizations

`C_BarberShop.GetAvailableCustomizations() → categories: CharCustomizationCategory[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.GetCurrentCameraZoom

`C_BarberShop.GetCurrentCameraZoom() → zoomLevel: number`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.GetCurrentCharacterData

`C_BarberShop.GetCurrentCharacterData() → characterData: PlayerInfoCharacterData`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.GetCurrentCost

`C_BarberShop.GetCurrentCost() → cost: number`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.GetViewingChrModel

`C_BarberShop.GetViewingChrModel() → chrModelID: number?`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.HasAlteredForm

`C_BarberShop.HasAlteredForm() → hasAlteredForm: bool`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.HasAnyChanges

`C_BarberShop.HasAnyChanges() → hasChanges: bool`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.HasCustomizationFeature

`C_BarberShop.HasCustomizationFeature(featureMask: ChrModelFeatureFlags) → hasCustomizationFeature: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.IsViewingAlteredForm

`C_BarberShop.IsViewingAlteredForm() → isViewingAlteredForm: bool`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.MarkCustomizationChoiceAsSeen

`C_BarberShop.MarkCustomizationChoiceAsSeen(choiceID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.MarkCustomizationOptionAsSeen

`C_BarberShop.MarkCustomizationOptionAsSeen(optionID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.PreviewCustomizationChoice

`C_BarberShop.PreviewCustomizationChoice(optionID: number, choiceID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.RandomizeCustomizationChoices

`C_BarberShop.RandomizeCustomizationChoices()`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.ResetCameraRotation

`C_BarberShop.ResetCameraRotation()`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.ResetCustomizationChoices

`C_BarberShop.ResetCustomizationChoices()`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.RotateCamera

`C_BarberShop.RotateCamera(diffDegrees: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.SaveSeenChoices

`C_BarberShop.SaveSeenChoices()`

- Status: ✅ verified (function)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.SetCameraDistanceOffset

`C_BarberShop.SetCameraDistanceOffset(offset: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.SetCameraZoomLevel

`C_BarberShop.SetCameraZoomLevel(zoomLevel: number, keepCustomZoom: bool?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.SetCustomizationChoice

`C_BarberShop.SetCustomizationChoice(optionID: number, choiceID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.SetModelDressState

`C_BarberShop.SetModelDressState(dressedState: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.SetSelectedSex

`C_BarberShop.SetSelectedSex(sex: UnitSex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.SetViewingAlteredForm

`C_BarberShop.SetViewingAlteredForm(isViewingAlteredForm: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.SetViewingChrModel

`C_BarberShop.SetViewingChrModel(chrModelID: number?, spellShapeshiftFormID: number?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.SetViewingShapeshiftForm

`C_BarberShop.SetViewingShapeshiftForm(shapeshiftFormID: number?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShop.ZoomCamera

`C_BarberShop.ZoomCamera(zoomAmount: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopDocumentation.lua`

### C_BarberShopInternal.SetQAMode

`C_BarberShopInternal.SetQAMode(qaModeEnabled: bool)`

- Status: ⛔ in Blizzard's docs, not in game
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BarberShopInternalDocumentation.lua`

## Events

### BARBER_SHOP_APPEARANCE_APPLIED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### BARBER_SHOP_CAMERA_VALUES_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BARBER_SHOP_CLOSE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BARBER_SHOP_COST_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BARBER_SHOP_FORCE_CUSTOMIZATIONS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BARBER_SHOP_OPEN

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BARBER_SHOP_RESULT

- Status: ✅ verified
- Payload: `success: bool`
- fires synchronously (Blizzard's docs)
