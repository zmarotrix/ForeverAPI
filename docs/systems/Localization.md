# Localization

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [AbbreviateLargeNumbers](#abbreviatelargenumbers) |  |  |
| ✅ | [AbbreviateNumbers](#abbreviatenumbers) |  |  |
| ✅ | [BreakUpLargeNumbers](#breakuplargenumbers) |  |  |
| ✅ | [CaseAccentInsensitiveParse](#caseaccentinsensitiveparse) |  |  |
| ✅ | [CreateAbbreviateConfig](#createabbreviateconfig) |  |  |
| ✅ | [DeclineName](#declinename) |  |  |
| ⛔ | [GetDefaultAbbreviationBreakpoints](#getdefaultabbreviationbreakpoints) | missing | missing |
| ✅ | [GetNumDeclensionSets](#getnumdeclensionsets) |  |  |
| ✅ | [IsEuropeanNumbers](#iseuropeannumbers) | 1 value | 1 value |
| ✅ | [LocalizedClassList](#localizedclasslist) |  |  |
| ✅ | [SetEuropeanNumbers](#seteuropeannumbers) |  |  |

### AbbreviateLargeNumbers

`AbbreviateLargeNumbers(number: number, options: NumberAbbrevOptions?) → result: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `LocalizationDocumentation.lua`

### AbbreviateNumbers

`AbbreviateNumbers(number: number, options: NumberAbbrevOptions?) → result: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `LocalizationDocumentation.lua`

### BreakUpLargeNumbers

`BreakUpLargeNumbers(largeNumber: number, natural: bool = False) → result: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `LocalizationDocumentation.lua`

### CaseAccentInsensitiveParse

`CaseAccentInsensitiveParse(name: cstring) → result: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LocalizationDocumentation.lua`

### CreateAbbreviateConfig

`CreateAbbreviateConfig(data: NumberAbbreviationBreakpoint[]) → config: AbbreviateConfig`

- Status: ✅ verified (function)
- RequiresRestrictedAbbreviationBreakpoints (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `LocalizationDocumentation.lua`

### DeclineName

`DeclineName(name: cstring, gender: UnitSex?, declensionSet: luaIndex, namePartType: NamePartType?) → declinedNames: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LocalizationDocumentation.lua`

### GetDefaultAbbreviationBreakpoints

`GetDefaultAbbreviationBreakpoints(locale: WowLocale?) → breakpoints: NumberAbbreviationBreakpoint[]`

- Status: ⛔ in Blizzard's docs, not in game
- Namespace: C_StringUtil (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: missing at call time
- Called in combat: missing at call time
- Source: client docs `LocalizationDocumentation.lua`

### GetNumDeclensionSets

`GetNumDeclensionSets(name: cstring, gender: UnitSex?, namePartType: NamePartType?) → numDeclensionSets: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LocalizationDocumentation.lua`

### IsEuropeanNumbers

`IsEuropeanNumbers() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LocalizationDocumentation.lua`

### LocalizedClassList

`LocalizedClassList(isFemale: bool = False) → result: LuaValueVariant`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LocalizationDocumentation.lua`

### SetEuropeanNumbers

`SetEuropeanNumbers(enabled: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LocalizationDocumentation.lua`

## Types

### NumberAbbrevOptions

- Structure
  - `breakpointData`: NumberAbbreviationBreakpoint[]?
  - `locale`: cstring?
  - `config`: AbbreviateConfig?
