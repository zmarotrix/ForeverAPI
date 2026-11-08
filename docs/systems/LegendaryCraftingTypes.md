# LegendaryCraftingTypes

## Types

### CurrencyCost

- Structure
  - `currencyID`: number
  - `amount`: number

### RuneforgeItemPreviewInfo

- Structure
  - `itemGUID`: WOWGUID
  - `itemLevel`: number
  - `itemName`: string

### RuneforgeLegendaryComponentInfo

- Structure
  - `powerID`: number
  - `modifiers`: number[]

### RuneforgeLegendaryCraftDescription

- Structure
  - `baseItem`: ItemLocation
  - `runeforgePowerID`: number
  - `modifiers`: number[]

### RuneforgePower

- Structure
  - `runeforgePowerID`: number
  - `state`: RuneforgePowerState
  - `name`: cstring
  - `descriptionSpellID`: number
  - `description`: string
  - `source`: cstring?
  - `iconFileID`: fileID
  - `specName`: cstring?
  - `matchesSpec`: bool
  - `matchesCovenant`: bool
  - `covenantID`: number?
  - `slots`: cstring[]

### RuneforgePowerFilter

- Enumeration — ❔ unverified
  - `All` = 0
  - `Relevant` = 1
  - `Available` = 2
  - `Unavailable` = 3

### RuneforgePowerState

- Enumeration — ❔ unverified
  - `Available` = 0
  - `Unavailable` = 1
  - `Invalid` = 2
