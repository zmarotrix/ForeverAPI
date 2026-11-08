# DyeColorInfo

Namespace: `C_DyeColor`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_DyeColor.GetAllDyeColorCategories](#c_dyecolorgetalldyecolorcategories) | 1 value |  |
| ✅ | [C_DyeColor.GetAllDyeColors](#c_dyecolorgetalldyecolors) | 1 value |  |
| ✅ | [C_DyeColor.GetDyeColorCategoryInfo](#c_dyecolorgetdyecolorcategoryinfo) |  |  |
| 🆕 | [C_DyeColor.GetDyeColorForItem](#c_dyecolorgetdyecolorforitem) |  |  |
| 🆕 | [C_DyeColor.GetDyeColorForItemLocation](#c_dyecolorgetdyecolorforitemlocation) |  |  |
| ✅ | [C_DyeColor.GetDyeColorInfo](#c_dyecolorgetdyecolorinfo) |  |  |
| ✅ | [C_DyeColor.GetDyeColorsForItem](#c_dyecolorgetdyecolorsforitem) |  |  |
| ✅ | [C_DyeColor.GetDyeColorsForItemLocation](#c_dyecolorgetdyecolorsforitemlocation) |  |  |
| ✅ | [C_DyeColor.GetDyeColorsInCategory](#c_dyecolorgetdyecolorsincategory) |  |  |
| ✅ | [C_DyeColor.IsDyeColorOwned](#c_dyecolorisdyecolorowned) |  |  |

### C_DyeColor.GetAllDyeColorCategories

`C_DyeColor.GetAllDyeColorCategories() → dyeColorCategoryIDs: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetAllDyeColors

`C_DyeColor.GetAllDyeColors(ownedColorsOnly: bool = False) → dyeColorIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetDyeColorCategoryInfo

`C_DyeColor.GetDyeColorCategoryInfo(dyeColorCategoryID: number) → dyeColorCategoryInfo: DyeColorCategoryDisplayInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetDyeColorForItem

`C_DyeColor.GetDyeColorForItem(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_DyeColor.GetDyeColorForItemLocation

`C_DyeColor.GetDyeColorForItemLocation(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_DyeColor.GetDyeColorInfo

`C_DyeColor.GetDyeColorInfo(dyeColorID: number) → dyeColorInfo: DyeColorDisplayInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetDyeColorsForItem

`C_DyeColor.GetDyeColorsForItem(itemLinkOrID: ItemInfo) → dyeColorIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetDyeColorsForItemLocation

`C_DyeColor.GetDyeColorsForItemLocation(itemLocation: ItemLocation) → dyeColorIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.GetDyeColorsInCategory

`C_DyeColor.GetDyeColorsInCategory(dyeColorCategory: number, ownedColorsOnly: bool = False) → dyeColorIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

### C_DyeColor.IsDyeColorOwned

`C_DyeColor.IsDyeColorOwned(dyeColorID: number) → isOwned: bool`

- Status: ✅ verified (function)
- Blizzard: True if the player owns any of the consumable item used to apply the specified dye
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DyeColorInfoDocumentation.lua`

## Events

### DYE_COLOR_CATEGORY_UPDATED

- Status: ✅ verified
- Payload: `dyeColorCategoryID: number`
- fires synchronously (Blizzard's docs)

### DYE_COLOR_UPDATED

- Status: ✅ verified
- Payload: `dyeColorID: number`
- fires synchronously (Blizzard's docs)
