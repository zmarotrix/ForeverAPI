# Locale

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetAvailableLocaleInfo](#getavailablelocaleinfo) |  |  |
| ✅ | [GetAvailableLocales](#getavailablelocales) |  |  |
| ✅ | [GetCurrentRegion](#getcurrentregion) |  |  |
| ✅ | [GetLocale](#getlocale) |  |  |
| ✅ | [GetOSLocale](#getoslocale) |  |  |

### GetAvailableLocaleInfo

`GetAvailableLocaleInfo(ignoreLocaleRestrictions: bool = False) → localeInfos: LocaleInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LocaleDocumentation.lua`

### GetAvailableLocales

`GetAvailableLocales(ignoreLocaleRestrictions: bool = False) → localeName: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LocaleDocumentation.lua`

### GetCurrentRegion

`GetCurrentRegion() → region: number`

- Status: ✅ verified (function)
- Source: client docs `LocaleDocumentation.lua`

### GetLocale

`GetLocale() → localeName: cstring`

- Status: ✅ verified (function)
- Source: client docs `LocaleDocumentation.lua`

### GetOSLocale

`GetOSLocale() → localeName: cstring`

- Status: ✅ verified (function)
- Source: client docs `LocaleDocumentation.lua`

## Types

### LocaleInfo

- Structure
  - `localeId`: number
  - `localeName`: cstring
