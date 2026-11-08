# DyeColorInfo

Namespace: `C_DyeColor`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_DyeColor.GetAllDyeColorCategories](#c_dyecolorgetalldyecolorcategories) |  |  |
| ❔ | [C_DyeColor.GetAllDyeColors](#c_dyecolorgetalldyecolors) |  |  |
| ❔ | [C_DyeColor.GetDyeColorCategoryInfo](#c_dyecolorgetdyecolorcategoryinfo) |  |  |
| ❔ | [C_DyeColor.GetDyeColorInfo](#c_dyecolorgetdyecolorinfo) |  |  |
| ❔ | [C_DyeColor.GetDyeColorsForItem](#c_dyecolorgetdyecolorsforitem) |  |  |
| ❔ | [C_DyeColor.GetDyeColorsForItemLocation](#c_dyecolorgetdyecolorsforitemlocation) |  |  |
| ❔ | [C_DyeColor.GetDyeColorsInCategory](#c_dyecolorgetdyecolorsincategory) |  |  |
| ❔ | [C_DyeColor.IsDyeColorOwned](#c_dyecolorisdyecolorowned) |  |  |

### C_DyeColor.GetAllDyeColorCategories

`C_DyeColor.GetAllDyeColorCategories() → dyeColorCategoryIDs: number[]`

- Status: ❔ unverified
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetAllDyeColors

`C_DyeColor.GetAllDyeColors(ownedColorsOnly: bool = False) → dyeColorIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetDyeColorCategoryInfo

`C_DyeColor.GetDyeColorCategoryInfo(dyeColorCategoryID: number) → dyeColorCategoryInfo: DyeColorCategoryDisplayInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetDyeColorInfo

`C_DyeColor.GetDyeColorInfo(dyeColorID: number) → dyeColorInfo: DyeColorDisplayInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetDyeColorsForItem

`C_DyeColor.GetDyeColorsForItem(itemLinkOrID: ItemInfo) → dyeColorIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetDyeColorsForItemLocation

`C_DyeColor.GetDyeColorsForItemLocation(itemLocation: ItemLocation) → dyeColorIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetDyeColorsInCategory

`C_DyeColor.GetDyeColorsInCategory(dyeColorCategory: number, ownedColorsOnly: bool = False) → dyeColorIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.IsDyeColorOwned

`C_DyeColor.IsDyeColorOwned(dyeColorID: number) → isOwned: bool`

- Status: ❔ unverified
- Blizzard: True if the player owns any of the consumable item used to apply the specified dye
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

## Events

### DYE_COLOR_CATEGORY_UPDATED

- Status: ❔ unverified
- Payload: `dyeColorCategoryID: number`
- fires synchronously (Blizzard's docs)

### DYE_COLOR_UPDATED

- Status: ❔ unverified
- Payload: `dyeColorID: number`
- fires synchronously (Blizzard's docs)
