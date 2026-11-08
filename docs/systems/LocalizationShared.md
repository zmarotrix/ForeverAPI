# LocalizationShared

## Types

### AbbreviationDataError

- Enumeration — ✅ verified
  - `InvalidBreakpoint` = 1
  - `InvalidSignificandDivisor` = 2
  - `InvalidFractionDivisor` = 4
  - `NotMultipleOfTen` = 8

### NamePartType

- Enumeration — ✅ verified
  - `Firstname` = 0
  - `Surname` = 1
  - `Combined` = 2

### NumberAbbreviationBreakpoint

- Structure
  - `breakpoint`: number
  - `abbreviation`: string
  - `significandDivisor`: number
  - `fractionDivisor`: number
  - `abbreviationIsGlobal`: bool
