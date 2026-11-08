# SpecializationShared

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetSpecializationInfoForClassID](#getspecializationinfoforclassid) |  |  |
| ✅ | [GetSpecializationInfoForSpecID](#getspecializationinfoforspecid) |  |  |
| ✅ | [GetSpecializationNameForSpecID](#getspecializationnameforspecid) |  |  |
| ✅ | [GetSpecializationSystem](#getspecializationsystem) |  |  |
| ✅ | [HasLootSpecializations](#haslootspecializations) |  |  |

### GetSpecializationInfoForClassID

`GetSpecializationInfoForClassID(classID: number, index: luaIndex, gender: UnitSex?) → id: number, name: cstring, description: string, icon: fileID, role: cstring, recommended: bool, allowedForBoost: bool, masterySpell1: number?, masterySpell2: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationSharedDocumentation.lua`

### GetSpecializationInfoForSpecID

`GetSpecializationInfoForSpecID(specID: number, gender: UnitSex?) → id: number, name: cstring, description: string, icon: fileID, role: cstring, recommended: bool, allowedForBoost: bool, masterySpell1: number?, masterySpell2: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationSharedDocumentation.lua`

### GetSpecializationNameForSpecID

`GetSpecializationNameForSpecID(specID: number, gender: UnitSex?) → name: cstring?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationSharedDocumentation.lua`

### GetSpecializationSystem

`GetSpecializationSystem() → system: SpecializationSystem`

- Status: ✅ verified (function)
- Source: client docs `SpecializationSharedDocumentation.lua`

### HasLootSpecializations

`HasLootSpecializations() → hasLootSpecializations: bool`

- Status: ✅ verified (function)
- Source: client docs `SpecializationSharedDocumentation.lua`

## Types

### SpecializationInfoResult

- Structure
  - `id`: number
  - `name`: cstring
  - `description`: string
  - `icon`: fileID
  - `role`: cstring
  - `recommended`: bool
  - `allowedForBoost`: bool
  - `masterySpell1`: number?
  - `masterySpell2`: number?

### SpecializationSystem

- Enumeration — ✅ verified
  - `TalentTab` = 0
  - `ChrSpecialization` = 1
