# HousingBlueprintConstants

## Types

### HousingBlueprintBudgetEntry

- Structure
  - `budgetType`: HousingBudgetType
  - `cost`: number
  - `max`: number?
  - `current`: number?

### HousingBlueprintBudgetInfo

- Structure
  - `exteriorBudgets`: HousingBlueprintBudgetEntry[]
  - `interiorBudgets`: HousingBlueprintBudgetEntry[]

### HousingBlueprintCollection

- Structure
- Blizzard: List of Blueprints, separated into like groups
  - `groups`: HousingBlueprintGroup[]

### HousingBlueprintContentEntry

- Structure
- Blizzard: A single specific object that makes up a Blueprint's contents
  - `contentType`: HousingBlueprintContentType
  - `recordID`: number
  - `name`: string
  - `total`: number
  - `numMissing`: number
  - `invalid`: bool
  - `tooltip`: string?

### HousingBlueprintContentGroup

- Structure
- Blizzard: Group of entries of one specific type of object within a Blueprint
  - `contentType`: HousingBlueprintContentType
  - `entries`: HousingBlueprintContentEntry[]

### HousingBlueprintContentInfo

- Structure
  - `shareCode`: string
  - `targetHouseGUID`: WOWGUID?
  - `budgetInfo`: HousingBlueprintBudgetInfo
  - `contentGroups`: HousingBlueprintContentGroup[]
  - `unmetRequirementFlags`: HousingBlueprintUnmetRequirementFlags
  - `blockingRequirementFlags`: HousingBlueprintUnmetRequirementFlags

### HousingBlueprintContentType

- Enumeration — ❔ unverified
  - `None` = 0
  - `HouseType` = 1
  - `Room` = 2
  - `Decor` = 3
  - `Dye` = 4
  - `Fixture` = 5
  - `Other` = 6

### HousingBlueprintGroup

- Structure
- Blizzard: Group of Blueprints of the same or similar types
  - `name`: cstring
  - `entries`: HousingBlueprintInfo[]

### HousingBlueprintInfo

- Structure
- Blizzard: List of entries of one specific type of object within a Blueprint
  - `blueprintID`: BigUInteger
  - `shareCode`: string
  - `name`: string
  - `blueprintType`: HousingBlueprintType
  - `creationTime`: time_t
  - `isAutoSave`: bool

### HousingBlueprintUnmetRequirementFlags

- Enumeration — ❔ unverified
  - `InsufficientBudget` = 1
  - `MissingRoom` = 2
  - `MissingFixture` = 4
  - `MissingDecor` = 8
  - `MissingDye` = 16
  - `MismatchedExteriorFaction` = 32
  - `HouseTypeLocked` = 64
  - `HouseSizeLocked` = 128
