# ProfessionSpecConstants

## Types

### ProfTabHighlight

- Structure
  - `description`: cstring

### ProfTabInfo

- Structure
  - `rootNodeID`: number
  - `name`: cstring
  - `description`: cstring
  - `rootIconID`: number
  - `highlights`: ProfTabHighlight[]

### ProfTraitPerkNodeFlags

- Enumeration — ❔ unverified
  - `UnlocksSubpath` = 1
  - `IsMajorBonus` = 2

### ProfessionsSpecPathState

- Enumeration — ❔ unverified
  - `Locked` = 0
  - `Progressing` = 1
  - `Completed` = 2

### ProfessionsSpecPerkState

- Enumeration — ❔ unverified
  - `Unearned` = 0
  - `Pending` = 1
  - `Earned` = 2

### ProfessionsSpecTabState

- Enumeration — ❔ unverified
  - `Locked` = 0
  - `Unlocked` = 1
  - `Unlockable` = 2

### SpecPerkInfo

- Structure
  - `perkID`: number
  - `isMajorPerk`: bool

### SpecializationCurrencyInfo

- Structure
  - `numAvailable`: number
  - `currencyName`: cstring

### SpecializationTabInfo

- Structure
  - `enabled`: bool
  - `errorReason`: cstring
