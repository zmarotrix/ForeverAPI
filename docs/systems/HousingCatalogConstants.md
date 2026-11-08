# HousingCatalogConstants

## Types

### HousingCatalogConsts

- Constants — ✅ verified
  - `HOUSING_CATALOG_FEATURED_CATEGORY_ID` = 17
  - `HOUSING_CATALOG_ALL_CATEGORY_ID` = 18
  - `HOUSING_CATALOG_DECOR_MODELSCENEID_DEFAULT` = 1317

### HousingCatalogEntryID

- Structure
- Blizzard: Identifier for base entries in the catalog
  - `recordID`: number
  - `entryType`: HousingCatalogEntryType

### HousingCatalogEntryModelScenePresets

- Enumeration — ✅ verified
  - `DecorDefault` = 1317
  - `DecorTiny` = 1333
  - `DecorSmall` = 1334
  - `DecorMedium` = 1335
  - `DecorLarge` = 1336
  - `DecorHuge` = 1337
  - `DecorCeiling` = 1338
  - `DecorWall` = 1339
  - `DecorFlat` = 1318
  - `DecorHorizontalSurface` = 1452

### HousingCatalogEntrySize

- Enumeration — ✅ verified
  - `None` = 0
  - `Tiny` = 65
  - `Small` = 66
  - `Medium` = 67
  - `Large` = 68
  - `Huge` = 69

### HousingCatalogEntryType

- Enumeration — ✅ verified
  - `Invalid` = 0
  - `Decor` = 1
  - `Room` = 2

### HousingCatalogEntryVariantID

- Structure
- Blizzard: Compound Identifier for entry variant stacks in the catalog
  - `recordID`: number
  - `entryType`: HousingCatalogEntryType
  - `variantIdentifier`: number

### HousingCatalogFilterTagGroupInfo

- Structure
  - `groupID`: number
  - `groupName`: cstring
  - `tags`: HousingCatalogFilterTagInfo[]

### HousingCatalogFilterTagInfo

- Structure
  - `tagID`: number
  - `tagName`: string
  - `orderIndex`: number
  - `anyAssociatedEntries`: bool

### HousingCatalogSortType

- Enumeration — ✅ verified
  - `DateAdded` = 0
  - `Alphabetical` = 1
