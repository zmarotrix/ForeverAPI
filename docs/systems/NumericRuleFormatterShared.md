# NumericRuleFormatterShared

## Types

### NumericRuleFormatBreakpoint

- Structure
  - `threshold`: number
  - `step`: number?
  - `rounding`: NumericRuleFormatRounding
  - `min`: number?
  - `max`: number?
  - `format`: string
  - `components`: NumericRuleFormatComponent[]?

### NumericRuleFormatComponent

- Structure
  - `div`: number?
  - `mod`: number?
  - `step`: number?
  - `rounding`: NumericRuleFormatRounding

### NumericRuleFormatRounding

- Enumeration — ✅ verified
  - `Nearest` = 0
  - `Up` = 1
  - `Down` = 2
