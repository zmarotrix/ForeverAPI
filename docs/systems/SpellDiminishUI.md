# SpellDiminishUI

Namespace: `C_SpellDiminish`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_SpellDiminish.GetAllSpellDiminishCategories](#c_spelldiminishgetallspelldiminishcategories) |  |  |
| ❔ | [C_SpellDiminish.GetSpellDiminishCategoryInfo](#c_spelldiminishgetspelldiminishcategoryinfo) |  |  |
| ❔ | [C_SpellDiminish.IsSystemSupported](#c_spelldiminishissystemsupported) |  |  |
| ❔ | [C_SpellDiminish.ShouldTrackSpellDiminishCategory](#c_spelldiminishshouldtrackspelldiminishcategory) |  |  |

### C_SpellDiminish.GetAllSpellDiminishCategories

`C_SpellDiminish.GetAllSpellDiminishCategories(ruleset: SpellDiminishRuleset?) → categories: SpellDiminishCategoryInfo[]`

- Status: ❔ unverified
- RequiresSpellDiminishUI (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpellDiminishUIDocumentation.lua`

### C_SpellDiminish.GetSpellDiminishCategoryInfo

`C_SpellDiminish.GetSpellDiminishCategoryInfo(category: SpellDiminishCategory) → categoryInfo: SpellDiminishCategoryInfo?`

- Status: ❔ unverified
- RequiresSpellDiminishUI (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpellDiminishUIDocumentation.lua`

### C_SpellDiminish.IsSystemSupported

`C_SpellDiminish.IsSystemSupported() → isSystemSupported: bool`

- Status: ❔ unverified
- Source: client docs `SpellDiminishUIDocumentation.lua`

### C_SpellDiminish.ShouldTrackSpellDiminishCategory

`C_SpellDiminish.ShouldTrackSpellDiminishCategory(category: SpellDiminishCategory, ruleset: SpellDiminishRuleset) → isTracked: bool`

- Status: ❔ unverified
- RequiresSpellDiminishUI (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- always returns secret values (Blizzard's docs; not checked in game)
- Source: client docs `SpellDiminishUIDocumentation.lua`

## Events

### UNIT_SPELL_DIMINISH_CATEGORY_STATE_UPDATED

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`, `trackerInfo: SpellDiminishTrackerInfo`
- SecretPayloads (Blizzard's docs)
- fires synchronously (Blizzard's docs)

## Types

### SpellDiminishCategoryInfo

- Structure
  - `category`: SpellDiminishCategory
  - `name`: cstring
  - `icon`: fileID?

### SpellDiminishTrackerInfo

- Structure
  - `category`: SpellDiminishCategory
  - `startTime`: number
  - `duration`: number
  - `showCountdown`: bool
  - `isImmune`: bool
