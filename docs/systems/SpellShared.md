# SpellShared

## Types

### SpellChargeInfo

- Structure
  - `currentCharges`: number
  - `maxCharges`: number
  - `cooldownStartTime`: number
  - `cooldownDuration`: number
  - `chargeModRate`: number
  - `isActive`: bool

### SpellCooldownInfo

- Structure
  - `startTime`: number
  - `duration`: number
  - `isEnabled`: bool
  - `isActive`: bool
  - `modRate`: number
  - `activeCategory`: number?
  - `timeUntilEndOfStartRecovery`: number?
  - `isOnGCD`: bool?

### SpellLossOfControlInfo

- Structure
  - `startTime`: number
  - `duration`: number
  - `modRate`: number
  - `isActive`: bool
  - `shouldReplaceNormalCooldown`: bool

### SpellPowerCostInfo

- Structure
  - `type`: PowerType
  - `name`: string
  - `cost`: number
  - `minCost`: number
  - `costPercent`: number
  - `costPerSec`: number
  - `requiredAuraID`: number
  - `hasRequiredAura`: bool
