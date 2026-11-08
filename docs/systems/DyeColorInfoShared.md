# DyeColorInfoShared

## Types

### DyeColorCategoryDisplayInfo

- Structure
  - `ID`: number
  - `name`: cstring

### DyeColorDisplayInfo

- Structure
  - `ID`: number
  - `dyeColorCategoryID`: number
  - `name`: cstring
  - `sortOrder`: number
  - `swatchColorStart`: colorRGB
  - `swatchColorEnd`: colorRGB
  - `itemID`: number?
  - `numOwned`: number
