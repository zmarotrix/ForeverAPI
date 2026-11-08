# DurationTextBindingShared

## Types

### DurationTextBindingColorOptions

- Structure
  - `curve`: LuaColorCurveObject
  - `property`: DurationTextBindingProperty

### DurationTextBindingFormatComponent

- Structure
  - `property`: DurationTextBindingProperty
  - `formatter`: NumericFormatter

### DurationTextBindingFormatOptions

- Structure
  - `formatString`: stringView
  - `components`: DurationTextBindingFormatComponent[]

### DurationTextBindingProperty

- Enumeration — ❔ unverified
  - `RemainingDuration` = 0
  - `RemainingPercent` = 1
  - `ElapsedDuration` = 2
  - `ElapsedPercent` = 3
  - `TotalDuration` = 4
  - `StartTime` = 5
  - `EndTime` = 6
