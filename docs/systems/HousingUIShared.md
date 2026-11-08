# HousingUIShared

## Types

### HouseInfo

- Structure
  - `plotID`: number
  - `houseName`: string?
  - `ownerName`: string?
  - `plotCost`: number?
  - `neighborhoodName`: string?
  - `moveOutTime`: time_t?
  - `plotReserved`: bool?
  - `neighborhoodGUID`: WOWGUID?
  - `houseGUID`: WOWGUID?

### HouseLevelFavor

- Structure
  - `houseGUID`: WOWGUID?
  - `houseLevel`: number
  - `houseFavor`: number

### HouseLevelInfo

- Structure
  - `level`: number
  - `interiorDecorPlacementBudget`: number
  - `exteriorDecorPlacementBudget`: number
  - `roomPlacementBudget`: number
  - `exteriorFixtureBudget`: number

### HouseLevelReward

- Structure
  - `type`: HouseLevelRewardType
  - `asset`: ModelAsset?
  - `iconTexture`: FileAsset?
  - `iconAtlas`: textureAtlas?
  - `objectName`: string?
  - `tooltipText`: string?
  - `valueType`: HouseLevelRewardValueType?
  - `oldValue`: number?
  - `newValue`: number?

### HouseLevelRewardType

- Enumeration — ✅ verified
  - `Value` = 0
  - `Object` = 1

### HouseLevelRewardValueType

- Enumeration — ✅ verified
  - `ExteriorDecor` = 0
  - `InteriorDecor` = 1
  - `Rooms` = 2
  - `Fixtures` = 3

### HouseOwnerCharacterInfo

- Structure
  - `characterName`: string
  - `classID`: number
  - `error`: HouseOwnerError
  - `playerGUID`: WOWGUID

### HouseVisitType

- Enumeration — ✅ verified
  - `Unknown` = 0
  - `Friend` = 1
  - `Guild` = 2
  - `Party` = 3

### HouseholdMemberInfo

- Structure
  - `characterName`: string
  - `classID`: number

### NeighborhoodInfo

- Structure
  - `neighborhoodType`: NeighborhoodType
  - `neighborhoodOwnerType`: NeighborhoodOwnerType
  - `neighborhoodName`: string
  - `neighborhoodGUID`: WOWGUID
  - `ownerGUID`: WOWGUID
  - `suggestionReason`: HouseFinderSuggestionReason?
  - `ownerName`: string?
  - `locationName`: string?

### NeighborhoodPlotMapInfo

- Structure
  - `mapPosition`: vector2
  - `plotDataID`: number
  - `plotID`: number
  - `ownerType`: HousingPlotOwnerType
  - `plotCost`: number?
  - `ownerName`: string?

### NeighborhoodRosterMemberInfo

- Structure
  - `playerGUID`: WOWGUID
  - `residentName`: string
  - `residentType`: ResidentType
  - `isOnline`: bool
  - `plotID`: number
  - `subdivision`: number?

### NeighborhoodRosterMemberUpdateInfo

- Structure
  - `playerGUID`: WOWGUID
  - `residentType`: ResidentType
  - `isOnline`: bool
