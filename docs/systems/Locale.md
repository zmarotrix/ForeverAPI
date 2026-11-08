# Locale

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetAvailableLocaleInfo](#getavailablelocaleinfo) | 1 value | 1 value |
| ✅ | [GetAvailableLocales](#getavailablelocales) | 3 values | 3 values |
| ✅ | [GetCurrentRegion](#getcurrentregion) | 1 value | 1 value |
| ✅ | [GetLocale](#getlocale) | 1 value | 1 value |
| ✅ | [GetOSLocale](#getoslocale) | 1 value | 1 value |

### GetAvailableLocaleInfo

`GetAvailableLocaleInfo(ignoreLocaleRestrictions: bool = False) → localeInfos: LocaleInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table}`
- Called in combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table}`
- Source: client docs `LocaleDocumentation.lua`

### GetAvailableLocales

`GetAvailableLocales(ignoreLocaleRestrictions: bool = False) → localeName: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 3 values: `string`, `string`, `string`
- Called in combat: returned 3 values: `string`, `string`, `string`
- Source: client docs `LocaleDocumentation.lua`

### GetCurrentRegion

`GetCurrentRegion() → region: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `LocaleDocumentation.lua`

### GetLocale

`GetLocale() → localeName: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `LocaleDocumentation.lua`

### GetOSLocale

`GetOSLocale() → localeName: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `LocaleDocumentation.lua`

## Types

### LocaleInfo

- Structure
  - `localeId`: number
  - `localeName`: cstring
