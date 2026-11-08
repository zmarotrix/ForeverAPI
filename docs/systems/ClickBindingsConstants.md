# ClickBindingsConstants

## Types

### ClickBindingInfo

- Structure
  - `type`: ClickBindingType
  - `actionID`: number
  - `button`: cstring
  - `modifiers`: number

### ClickBindingInteraction

- Enumeration — ❔ unverified
  - `Target` = 1
  - `OpenContextMenu` = 2

### ClickBindingType

- Enumeration — ❔ unverified
  - `None` = 0
  - `Spell` = 1
  - `Macro` = 2
  - `Interaction` = 3
  - `PetAction` = 4
