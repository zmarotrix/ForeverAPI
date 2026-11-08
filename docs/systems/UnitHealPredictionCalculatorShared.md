# UnitHealPredictionCalculatorShared

## Types

### UnitDamageAbsorbClampMode

- Enumeration — ✅ verified
  - `MissingHealth` = 0
  - `MissingHealthWithoutIncomingHeals` = 1
  - `MaximumHealth` = 2

### UnitDamageAbsorbInfo

- Structure
  - `amount`: number
  - `clamped`: bool

### UnitHealAbsorbClampMode

- Enumeration — ✅ verified
  - `CurrentHealth` = 0
  - `MaximumHealth` = 1

### UnitHealAbsorbInfo

- Structure
  - `amount`: number
  - `clamped`: bool

### UnitHealAbsorbMode

- Enumeration — ✅ verified
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

- Enumeration — ✅ verified
  - `MissingHealth` = 0
  - `MaximumHealth` = 1

### UnitIncomingHealInfo

- Structure
  - `amount`: number
  - `amountFromHealer`: number
  - `amountFromOthers`: number
  - `clamped`: bool

### UnitMaximumHealthMode

- Enumeration — ✅ verified
  - `Default` = 0
  - `WithAbsorbs` = 1
