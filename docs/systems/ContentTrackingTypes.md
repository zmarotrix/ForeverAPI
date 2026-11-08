# ContentTrackingTypes

## Types

### ContentTrackingConsts

- Constants — ✅ verified
  - `MaxTrackedCollectableSources` = 15
  - `MaxTrackedAchievements` = 10

### ContentTrackingError

- Enumeration — ✅ verified
  - `Untrackable` = 0
  - `MaxTracked` = 1
  - `AlreadyTracked` = 2

### ContentTrackingMapInfo

- Structure
  - `x`: number
  - `y`: number
  - `trackableType`: ContentTrackingType
  - `trackableID`: number
  - `targetType`: ContentTrackingTargetType
  - `targetID`: number
  - `waypointText`: string

### ContentTrackingResult

- Enumeration — ✅ verified
  - `Success` = 0
  - `DataPending` = 1
  - `Failure` = 2

### ContentTrackingStopType

- Enumeration — ✅ verified
  - `Invalidated` = 0
  - `Collected` = 1
  - `Manual` = 2

### ContentTrackingTargetType

- Enumeration — ✅ verified
  - `JournalEncounter` = 0
  - `Vendor` = 1
  - `Achievement` = 2
  - `Profession` = 3
  - `Quest` = 4

### ContentTrackingType

- Enumeration — ✅ verified
  - `Appearance` = 0
  - `Mount` = 1
  - `Achievement` = 2
  - `Decor` = 3

### EncounterTrackingInfo

- Structure
  - `encounterName`: cstring
  - `journalEncounterID`: number?
  - `journalInstanceID`: number?
  - `instanceName`: cstring
  - `subText`: cstring?
  - `difficultyID`: number?
  - `lfgDungeonID`: number?
  - `groupFinderActivityID`: number?

### VendorTrackingInfo

- Structure
  - `creatureName`: cstring
  - `zoneName`: string?
  - `currencyType`: number?
  - `cost`: BigUInteger?
