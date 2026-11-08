# UnitHealPredictionCalculatorShared

## Types

### UnitDamageAbsorbClampMode

- Enumeration — ❔ unverified
  - `MissingHealth` = 0
  - `MissingHealthWithoutIncomingHeals` = 1
  - `MaximumHealth` = 2

### UnitDamageAbsorbInfo

- Structure
  - `amount`: number
  - `clamped`: bool

### UnitHealAbsorbClampMode

- Enumeration — ❔ unverified
  - `CurrentHealth` = 0
  - `MaximumHealth` = 1

### UnitHealAbsorbInfo

- Structure
  - `amount`: number
  - `clamped`: bool

### UnitHealAbsorbMode

- Enumeration — ❔ unverified
  - `ReducedByIncomingHeals` = 0
  - `Total` = 1

### UnitHealPredictionValues

- Structure
  - `health`: number
  - `healthMax`: number
  - `totalIncomingHeals`: number
  - `totalIncomingHealsFromHealer`: number
  - `totalDamageAbsorbs`: number
  - `totalHealAbsorbs`: number

### UnitIncomingHealClampMode

- Enumeration — ❔ unverified
  - `MissingHealth` = 0
  - `MaximumHealth` = 1

### UnitIncomingHealInfo

- Structure
  - `amount`: number
  - `amountFromHealer`: number
  - `amountFromOthers`: number
  - `clamped`: bool

### UnitMaximumHealthMode

- Enumeration — ❔ unverified
  - `Default` = 0
  - `WithAbsorbs` = 1
