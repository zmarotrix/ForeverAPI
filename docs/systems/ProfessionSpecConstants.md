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

- Enumeration — ✅ verified
  - `UnlocksSubpath` = 1
  - `IsMajorBonus` = 2

### ProfessionsSpecPathState

- Enumeration — ✅ verified
  - `Locked` = 0
  - `Progressing` = 1
  - `Completed` = 2

### ProfessionsSpecPerkState

- Enumeration — ✅ verified
  - `Unearned` = 0
  - `Pending` = 1
  - `Earned` = 2

### ProfessionsSpecTabState

- Enumeration — ✅ verified
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
