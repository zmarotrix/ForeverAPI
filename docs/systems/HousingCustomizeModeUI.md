# HousingCustomizeModeUI

Namespace: `C_HousingCustomizeMode`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_HousingCustomizeMode.ApplyDyeToSelectedDecor](#c_housingcustomizemodeapplydyetoselecteddecor) |  |  |
| ✅ | [C_HousingCustomizeMode.ApplyPetToSelectedDecor](#c_housingcustomizemodeapplypettoselecteddecor) |  |  |
| ✅ | [C_HousingCustomizeMode.ApplyThemeToRoom](#c_housingcustomizemodeapplythemetoroom) |  |  |
| ✅ | [C_HousingCustomizeMode.ApplyThemeToSelectedRoomComponent](#c_housingcustomizemodeapplythemetoselectedroomcomponent) |  |  |
| ✅ | [C_HousingCustomizeMode.ApplyWallpaperToAllWalls](#c_housingcustomizemodeapplywallpapertoallwalls) |  |  |
| ✅ | [C_HousingCustomizeMode.ApplyWallpaperToSelectedRoomComponent](#c_housingcustomizemodeapplywallpapertoselectedroomcomponent) |  |  |
| ✅ | [C_HousingCustomizeMode.CancelActiveEditing](#c_housingcustomizemodecancelactiveediting) | 0 values |  |
| ✅ | [C_HousingCustomizeMode.ClearDyesForSelectedDecor](#c_housingcustomizemodecleardyesforselecteddecor) |  |  |
| ✅ | [C_HousingCustomizeMode.ClearTargetRoomComponent](#c_housingcustomizemodecleartargetroomcomponent) |  |  |
| ✅ | [C_HousingCustomizeMode.CommitDyesForSelectedDecor](#c_housingcustomizemodecommitdyesforselecteddecor) |  |  |
| ✅ | [C_HousingCustomizeMode.GetHoveredDecorInfo](#c_housingcustomizemodegethovereddecorinfo) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.GetHoveredRoomComponentInfo](#c_housingcustomizemodegethoveredroomcomponentinfo) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.GetNumDyesToRemoveOnSelectedDecor](#c_housingcustomizemodegetnumdyestoremoveonselecteddecor) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.GetNumDyesToSpendOnSelectedDecor](#c_housingcustomizemodegetnumdyestospendonselecteddecor) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.GetPreviewDyesOnSelectedDecor](#c_housingcustomizemodegetpreviewdyesonselecteddecor) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.GetRecentlyUsedDyes](#c_housingcustomizemodegetrecentlyuseddyes) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.GetRecentlyUsedThemeSets](#c_housingcustomizemodegetrecentlyusedthemesets) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.GetRecentlyUsedWallpapers](#c_housingcustomizemodegetrecentlyusedwallpapers) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.GetSelectedDecorInfo](#c_housingcustomizemodegetselecteddecorinfo) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.GetSelectedDecorPetInfo](#c_housingcustomizemodegetselecteddecorpetinfo) | 2 values |  |
| ✅ | [C_HousingCustomizeMode.GetSelectedRoomComponentInfo](#c_housingcustomizemodegetselectedroomcomponentinfo) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.GetThemeSetInfo](#c_housingcustomizemodegetthemesetinfo) |  |  |
| ✅ | [C_HousingCustomizeMode.GetWallpapersForRoomComponentType](#c_housingcustomizemodegetwallpapersforroomcomponenttype) |  |  |
| ✅ | [C_HousingCustomizeMode.IsDecorSelected](#c_housingcustomizemodeisdecorselected) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.IsHouseExteriorDoorHovered](#c_housingcustomizemodeishouseexteriordoorhovered) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.IsHoveringDecor](#c_housingcustomizemodeishoveringdecor) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.IsHoveringRoomComponent](#c_housingcustomizemodeishoveringroomcomponent) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.IsRoomComponentSelected](#c_housingcustomizemodeisroomcomponentselected) | 1 value |  |
| ✅ | [C_HousingCustomizeMode.RoomComponentSupportsVariant](#c_housingcustomizemoderoomcomponentsupportsvariant) |  |  |
| ✅ | [C_HousingCustomizeMode.RoomConnectionSupportsDoorType](#c_housingcustomizemoderoomconnectionsupportsdoortype) |  |  |
| ✅ | [C_HousingCustomizeMode.SetRoomComponentCeilingType](#c_housingcustomizemodesetroomcomponentceilingtype) |  |  |
| ✅ | [C_HousingCustomizeMode.SetRoomComponentDoorType](#c_housingcustomizemodesetroomcomponentdoortype) |  |  |

### C_HousingCustomizeMode.ApplyDyeToSelectedDecor

`C_HousingCustomizeMode.ApplyDyeToSelectedDecor(dyeSlotID: number, dyeColorID: number?)`

- Status: ✅ verified (function)
- Blizzard: If a dyeable decor is selected, applies a specific dye color in a specific slot as a preview; See CommitDyesForSelectedDecor to actually save applied dye changes
- `dyeColorID`: If not provided, clears the dye from the specified dye slot, returning that part of the decor asset to its default color
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.ApplyPetToSelectedDecor

`C_HousingCustomizeMode.ApplyPetToSelectedDecor(petID: WOWGUID?, petBehavior: HousingPetBehaviorType)`

- Status: ✅ verified (function)
- Blizzard: If a decor is selected that supports pets, applies a specific petID to be shown on that decor
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.ApplyThemeToRoom

`C_HousingCustomizeMode.ApplyThemeToRoom(themeSetID: number)`

- Status: ✅ verified (function)
- Blizzard: Attempt to apply a specific theme set (aka style) to all applicable room components in the current room
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.ApplyThemeToSelectedRoomComponent

`C_HousingCustomizeMode.ApplyThemeToSelectedRoomComponent(themeSetID: number)`

- Status: ✅ verified (function)
- Blizzard: Attempt to apply a specific theme set (aka style) to the currently selected room component only
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.ApplyWallpaperToAllWalls

`C_HousingCustomizeMode.ApplyWallpaperToAllWalls(roomComponentTextureRecID: number)`

- Status: ✅ verified (function)
- Blizzard: Attempt to apply a specific wallpaper (aka material/texture) to all applicable room components in the current room
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.ApplyWallpaperToSelectedRoomComponent

`C_HousingCustomizeMode.ApplyWallpaperToSelectedRoomComponent(roomComponentTextureRecID: number)`

- Status: ✅ verified (function)
- Blizzard: Attempt to apply a specific wallpaper (aka material/texture) to the currently selected room component only
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.CancelActiveEditing

`C_HousingCustomizeMode.CancelActiveEditing()`

- Status: ✅ verified (function)
- Blizzard: Cancels all in-progress editing of the selected target, which will reset any unapplied customization changes and deselect the active target
- Called out of combat: returned 0 values
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.ClearDyesForSelectedDecor

`C_HousingCustomizeMode.ClearDyesForSelectedDecor()`

- Status: ✅ verified (function)
- Blizzard: Clears all previewed dye changes on the selected decor; Does not clear any already saved dyes that were previously applied
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.ClearTargetRoomComponent

`C_HousingCustomizeMode.ClearTargetRoomComponent()`

- Status: ✅ verified (function)
- Blizzard: Deselect the currently selected room component, if there is one
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.CommitDyesForSelectedDecor

`C_HousingCustomizeMode.CommitDyesForSelectedDecor() → hasChanges: bool`

- Status: ✅ verified (function)
- Blizzard: Attempt to save all previewed dye changes made to the selected decor
- `hasChanges`: True if there were any changes to save
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetHoveredDecorInfo

`C_HousingCustomizeMode.GetHoveredDecorInfo() → info: HousingDecorInstanceInfo?`

- Status: ✅ verified (function)
- Blizzard: Returns info for the placed decor instance currently being hovered, if there is one
- Called out of combat: returned 1 value: `nil`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetHoveredRoomComponentInfo

`C_HousingCustomizeMode.GetHoveredRoomComponentInfo() → info: HousingRoomComponentInstanceInfo?`

- Status: ✅ verified (function)
- Blizzard: Returns info for the room component currently being hovered, if there is one
- Called out of combat: returned 1 value: `nil`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetNumDyesToRemoveOnSelectedDecor

`C_HousingCustomizeMode.GetNumDyesToRemoveOnSelectedDecor() → numDyesToRemove: number`

- Status: ✅ verified (function)
- Blizzard: If a dyeable decor instance is selected, returns how many dye slots would be cleared on applying all currently previewed dye changes
- Called out of combat: returned 1 value: `number`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetNumDyesToSpendOnSelectedDecor

`C_HousingCustomizeMode.GetNumDyesToSpendOnSelectedDecor() → numDyesToSpend: number`

- Status: ✅ verified (function)
- Blizzard: If a dyeable decor instance is selected, returns how many dye items would be spent on applying all currently previewed dye changes
- Called out of combat: returned 1 value: `number`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetPreviewDyesOnSelectedDecor

`C_HousingCustomizeMode.GetPreviewDyesOnSelectedDecor() → previewDyes: PreviewDyeSlotInfo[]`

- Status: ✅ verified (function)
- Blizzard: If a dyeable decor instance is selected, returns info structs for each new/changed dye currently being previewed
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetRecentlyUsedDyes

`C_HousingCustomizeMode.GetRecentlyUsedDyes() → recentDyes: number[]`

- Status: ✅ verified (function)
- Blizzard: Returns a list of ids for the dyes most recently applied by the player, if any
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetRecentlyUsedThemeSets

`C_HousingCustomizeMode.GetRecentlyUsedThemeSets() → recentThemeSets: number[]`

- Status: ✅ verified (function)
- Blizzard: Returns a list of ids for the theme sets (aka styles) most recently applied by the player, if any
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetRecentlyUsedWallpapers

`C_HousingCustomizeMode.GetRecentlyUsedWallpapers() → recentWallpapers: number[]`

- Status: ✅ verified (function)
- Blizzard: Returns a list of ids for the wallpapers most recently applied by the player, if any
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetSelectedDecorInfo

`C_HousingCustomizeMode.GetSelectedDecorInfo() → info: HousingDecorInstanceInfo?`

- Status: ✅ verified (function)
- Blizzard: Returns info for the decor instance that's currently selected, if there is one
- Called out of combat: returned 1 value: `nil`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetSelectedDecorPetInfo

`C_HousingCustomizeMode.GetSelectedDecorPetInfo() → petID: WOWGUID?, petBehavior: HousingPetBehaviorType`

- Status: ✅ verified (function)
- Blizzard: If a decor is selected that supports pets, gets petID and behavior type from decor
- Called out of combat: returned 2 values: `nil`, `number`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetSelectedRoomComponentInfo

`C_HousingCustomizeMode.GetSelectedRoomComponentInfo() → info: HousingRoomComponentInstanceInfo?`

- Status: ✅ verified (function)
- Blizzard: Returns info for the currently selected room component, if there is one
- Called out of combat: returned 1 value: `nil`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetThemeSetInfo

`C_HousingCustomizeMode.GetThemeSetInfo(themeSetID: number) → name: string?`

- Status: ✅ verified (function)
- Blizzard: Returns the name of the specified theme set (aka style) if it exists
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.GetWallpapersForRoomComponentType

`C_HousingCustomizeMode.GetWallpapersForRoomComponentType(type: HousingRoomComponentType) → availableWallpapers: RoomComponentWallpaper[]`

- Status: ✅ verified (function)
- Blizzard: Get all wallpapers (aka materials/textures) available for the selected room component type, if any
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.IsDecorSelected

`C_HousingCustomizeMode.IsDecorSelected() → hasSelectedDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a decor instance is currently selected for customization
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.IsHouseExteriorDoorHovered

`C_HousingCustomizeMode.IsHouseExteriorDoorHovered() → isHouseExteriorDoorHovered: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the entry door of the house's exterior is currently being hovered
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.IsHoveringDecor

`C_HousingCustomizeMode.IsHoveringDecor() → isHoveringDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a placed decor instance is currently being hovered
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.IsHoveringRoomComponent

`C_HousingCustomizeMode.IsHoveringRoomComponent() → isHovering: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a room component is currently being hovered
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.IsRoomComponentSelected

`C_HousingCustomizeMode.IsRoomComponentSelected() → hasSelectedComponent: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a room component is currently selected for customization
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.RoomComponentSupportsVariant

`C_HousingCustomizeMode.RoomComponentSupportsVariant(componentID: number, variant: number) → variantSupported: bool`

- Status: ✅ verified (function)
- Blizzard: Check whether a specific room component supports a particular variant; What kind of id or enum 'variant' equates to is complicated, as it depends on the component type
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.RoomConnectionSupportsDoorType

`C_HousingCustomizeMode.RoomConnectionSupportsDoorType(roomGUID: WOWGUID, componentID: number, newDoortype: HousingRoomComponentDoorType) → doorTypeSupported: bool`

- Status: ✅ verified (function)
- Blizzard: Check whether a specific room component, within a specific room, supports a particular doorType
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.SetRoomComponentCeilingType

`C_HousingCustomizeMode.SetRoomComponentCeilingType(roomGUID: WOWGUID, componentID: number, ceilingType: HousingRoomComponentCeilingType)`

- Status: ✅ verified (function)
- Blizzard: Attempt to set a specific ceiling component, within a specific room, to a specific new ceiling type
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

### C_HousingCustomizeMode.SetRoomComponentDoorType

`C_HousingCustomizeMode.SetRoomComponentDoorType(roomGUID: WOWGUID, componentID: number, newDoortype: HousingRoomComponentDoorType)`

- Status: ✅ verified (function)
- Blizzard: Attempt to set a specific door component, within a specific room, to a specific new door type
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCustomizeModeUIDocumentation.lua`

## Events

### HOUSING_CUSTOMIZE_MODE_HOVERED_TARGET_CHANGED

- Status: ✅ verified
- Payload: `hasHoveredTarget: bool`, `targetType: HousingCustomizeModeTargetType`
- fires synchronously (Blizzard's docs)

### HOUSING_CUSTOMIZE_MODE_SELECTED_TARGET_CHANGED

- Status: ✅ verified
- Payload: `hasSelectedTarget: bool`, `targetType: HousingCustomizeModeTargetType`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_CUSTOMIZATION_CHANGED

- Status: ✅ verified
- Payload: `decorGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_DYE_FAILURE

- Status: ✅ verified
- Payload: `decorGUID: WOWGUID`, `housingResult: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_ROOM_COMPONENT_CUSTOMIZATION_CHANGED

- Status: ✅ verified
- Payload: `roomGUID: WOWGUID`, `componentID: number`
- fires synchronously (Blizzard's docs)

### HOUSING_ROOM_COMPONENT_CUSTOMIZATION_CHANGE_FAILED

- Status: ✅ verified
- Payload: `roomGUID: WOWGUID`, `componentID: number`, `housingResult: HousingResult`
- fires synchronously (Blizzard's docs)

## Types

### HousingCustomizeModeTargetType

- Enumeration — ✅ verified
  - `None` = 0
  - `Decor` = 1
  - `RoomComponent` = 2
  - `ExteriorHouse` = 3

### HousingRoomComponentInstanceInfo

- Structure
  - `roomGUID`: WOWGUID
  - `type`: HousingRoomComponentType
  - `componentID`: number
  - `canBeCustomized`: bool
  - `currentThemeSet`: number?
  - `availableThemeSets`: number[]
  - `currentWallpaper`: number?
  - `currentRoomComponentTextureRecID`: number?
  - `ceilingType`: HousingRoomComponentCeilingType
  - `doorType`: HousingRoomComponentDoorType

### PreviewDyeSlotInfo

- Structure
  - `dyeColorID`: number
  - `dyeSlotID`: number

### RoomComponentWallpaper

- Structure
  - `name`: cstring
  - `roomComponentTextureRecID`: number
