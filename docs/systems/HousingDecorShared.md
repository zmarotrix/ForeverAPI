# HousingDecorShared

## Types

### HousingDecorDyeSlot

- Structure
  - `ID`: number
  - `dyeColorCategoryID`: number
  - `orderIndex`: number
  - `channel`: number
  - `dyeColorID`: number?
  - `dyeColorName`: cstring?

### HousingDecorInstanceInfo

- Structure
- Blizzard: Info for an instance of Housing Decor that has been/is being placed within a House or its exterior Plot
  - `decorGUID`: WOWGUID
  - `decorID`: number
  - `name`: cstring
  - `isLocked`: bool
  - `canBeCustomized`: bool
  - `canBeRemoved`: bool
  - `isAllowedOutdoors`: bool
  - `isAllowedIndoors`: bool
  - `isRefundable`: bool
  - `canAttachPet`: bool
  - `dyeSlots`: HousingDecorDyeSlot[]
  - `dataTagsByID`: LuaValueVariant
  - `size`: HousingCatalogEntrySize

### HousingDecorPlacementRestriction

- Enumeration — ✅ verified
  - `TooFarAway` = 1
  - `OutsideRoomBounds` = 2
  - `OutsidePlotBounds` = 4
  - `ChildOutsideBounds` = 8
  - `InvalidTarget` = 16
  - `InvalidCollision` = 32
  - `InvalidLightOverlap` = 64
