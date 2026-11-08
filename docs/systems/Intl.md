# Intl

Namespace: `C_Intl`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Intl.CompareStrings](#c_intlcomparestrings) |  |  |
| ✅ | [C_Intl.CreateLocaleContext](#c_intlcreatelocalecontext) |  |  |
| ✅ | [C_Intl.FindBreaks](#c_intlfindbreaks) |  |  |
| ✅ | [C_Intl.FindStringMatches](#c_intlfindstringmatches) |  |  |
| ✅ | [C_Intl.FoldCase](#c_intlfoldcase) |  |  |
| ✅ | [C_Intl.FormatCurrency](#c_intlformatcurrency) |  |  |
| ✅ | [C_Intl.FormatDate](#c_intlformatdate) |  |  |
| ✅ | [C_Intl.FormatDateTime](#c_intlformatdatetime) |  |  |
| ✅ | [C_Intl.FormatNumber](#c_intlformatnumber) |  |  |
| ✅ | [C_Intl.FormatTime](#c_intlformattime) |  |  |
| ✅ | [C_Intl.GetCharacterProperties](#c_intlgetcharacterproperties) |  |  |
| ✅ | [C_Intl.GetCurrencyFractionDigits](#c_intlgetcurrencyfractiondigits) |  |  |
| ✅ | [C_Intl.GetCurrencyName](#c_intlgetcurrencyname) |  |  |
| ✅ | [C_Intl.GetCurrentLocale](#c_intlgetcurrentlocale) | 1 value | 1 value |
| ✅ | [C_Intl.GetDisplayName](#c_intlgetdisplayname) |  |  |
| ✅ | [C_Intl.GetSortKey](#c_intlgetsortkey) |  |  |
| ✅ | [C_Intl.IsNormalized](#c_intlisnormalized) |  |  |
| ✅ | [C_Intl.Length](#c_intllength) |  |  |
| ✅ | [C_Intl.Normalize](#c_intlnormalize) |  |  |
| ✅ | [C_Intl.ParseCurrency](#c_intlparsecurrency) |  |  |
| ✅ | [C_Intl.ParseNumber](#c_intlparsenumber) |  |  |
| ✅ | [C_Intl.SelectPlural](#c_intlselectplural) |  |  |
| ✅ | [C_Intl.ToLower](#c_intltolower) |  |  |
| ✅ | [C_Intl.ToTitle](#c_intltotitle) |  |  |
| ✅ | [C_Intl.ToUpper](#c_intltoupper) |  |  |
| ✅ | [C_Intl.TransformLocale](#c_intltransformlocale) |  |  |
| ✅ | [C_Intl.Transliterate](#c_intltransliterate) |  |  |

### C_Intl.CompareStrings

`C_Intl.CompareStrings(left: cstring, right: cstring, strength: CollationStrength) → result: number`

- Status: ✅ verified (function)
- Blizzard: Compares two UTF-8 strings using the options specified on a collator.
- `left`: The first UTF-8 string passed to collation comparison.
- `right`: The second UTF-8 string passed to collation comparison.
- `strength`: The comparison level used by the collator for ordering and equality.
- `result`: The comparison result: less than, equal to, or greater than zero.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.CreateLocaleContext

`C_Intl.CreateLocaleContext(locale: cstring) → context: LuaLocaleContext`

- Status: ✅ verified (function)
- Blizzard: Creates a locale context object for locale-scoped internationalization operations.
- `locale`: The locale ID used to initialize the locale context object.
- `context`: A locale context userdata object for calling locale-scoped APIs.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.FindBreaks

`C_Intl.FindBreaks(text: cstring, breakType: BreakType) → byteOffsets: luaIndex[]`

- Status: ✅ verified (function)
- Blizzard: Opens a break iterator for locating text boundaries in a specified locale.
- `text`: The UTF-8 text whose boundary offsets are requested.
- `breakType`: The break iterator kind to use for boundary analysis.
- `byteOffsets`: The native UTF-8 string indices for the text boundaries (returned with 1-based indexes for lua convenience).
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.FindStringMatches

`C_Intl.FindStringMatches(text: cstring, pattern: cstring, strength: CollationStrength) → byteOffsets: luaIndex[]`

- Status: ✅ verified (function)
- Blizzard: Creates a string search iterator using a collator and returns every match position.
- `text`: The UTF-8 text scanned by the string search iterator.
- `pattern`: The UTF-8 pattern whose collation-aware matches are returned.
- `strength`: The comparison level used by the collator while searching for matches.
- `byteOffsets`: The UTF-8 byte offsets of matches in the text (returned with 1-based indexes for lua convenience).
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.FoldCase

`C_Intl.FoldCase(text: cstring) → result: string`

- Status: ✅ verified (function)
- Blizzard: Case-folds the characters in a string; case-folding is locale-independent and not context-sensitive.
- `text`: The UTF-8 text converted with locale-independent case folding.
- `result`: The case-folded string, which may be longer or shorter than the original.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.FormatCurrency

`C_Intl.FormatCurrency(number: number, currencyCode: cstring) → result: string`

- Status: ✅ verified (function)
- Blizzard: Formats a double as a localized currency value using the provided ISO 4217 currency code.
- `number`: The double value formatted by the locale currency formatter.
- `currencyCode`: The 3-letter null-terminated ISO 4217 currency code for currency formatting.
- `result`: The localized currency text produced by the formatter.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.FormatDate

`C_Intl.FormatDate(unixTimeSeconds: number, style: DateTimeStyle, timeZone: cstring) → result: string`

- Status: ✅ verified (function)
- Blizzard: Formats Unix time as localized date text using locale date patterns, symbols, style, and optional time zone.
- `unixTimeSeconds`: The date as seconds since the Unix epoch; this API converts it to milliseconds.
- `style`: The date format length; None omits the date portion.
- `timeZone`: The time zone ID applied to the formatter; empty strings keep the formatter default.
- `result`: The formatted date string.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.FormatDateTime

`C_Intl.FormatDateTime(unixTimeSeconds: number, dateStyle: DateTimeStyle, timeStyle: DateTimeStyle, timeZone: cstring) → result: string`

- Status: ✅ verified (function)
- Blizzard: Formats Unix time as localized date and time text using locale patterns, symbols, styles, and optional time zone.
- `unixTimeSeconds`: The date and time as seconds since the Unix epoch; this API converts it to milliseconds.
- `dateStyle`: The date format length; None omits the date portion.
- `timeStyle`: The time format length; None omits the time portion.
- `timeZone`: The time zone ID applied to the formatter; empty strings keep the formatter default.
- `result`: The formatted date and time string.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.FormatNumber

`C_Intl.FormatNumber(number: number, style: NumberStyle) → result: string`

- Status: ✅ verified (function)
- Blizzard: Formats a double with locale number formatting using locale symbols, grouping, and the selected non-currency style.
- `number`: The double value formatted according to the selected number formatter.
- `style`: The number style to format with; Currency is not accepted here, use FormatCurrency instead.
- `result`: The localized number text produced by the formatter.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.FormatTime

`C_Intl.FormatTime(unixTimeSeconds: number, style: DateTimeStyle, timeZone: cstring) → result: string`

- Status: ✅ verified (function)
- Blizzard: Formats Unix time as localized time text using locale time patterns, symbols, style, and optional time zone.
- `unixTimeSeconds`: The time as seconds since the Unix epoch; this API converts it to milliseconds.
- `style`: The time format length; None omits the time portion.
- `timeZone`: The time zone ID applied to the formatter; empty strings keep the formatter default.
- `result`: The formatted time string.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.GetCharacterProperties

`C_Intl.GetCharacterProperties(text: cstring) → result: CharacterProperties`

- Status: ✅ verified (function)
- Blizzard: Returns Unicode property values for the first code point in a string.
- `text`: The string whose first code point is tested.
- `result`: Unicode property values for the first code point.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.GetCurrencyFractionDigits

`C_Intl.GetCurrencyFractionDigits(currencyCode: cstring) → result: number`

- Status: ✅ verified (function)
- Blizzard: Returns the number of fraction digits that should be displayed for the given currency.
- `currencyCode`: The null-terminated 3-letter ISO 4217 currency code.
- `result`: The non-negative number of fraction digits to be displayed, or 0 if the lookup fails.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.GetCurrencyName

`C_Intl.GetCurrencyName(currencyCode: cstring, nameStyle: CurrencyNameStyle) → result: string`

- Status: ✅ verified (function)
- Blizzard: Returns the display name for a currency in the given locale.
- `currencyCode`: The null-terminated 3-letter ISO 4217 currency code.
- `nameStyle`: The selector for which kind of currency name to return.
- `result`: The display string for the currency, or the currency code itself if no localized name is available.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.GetCurrentLocale

`C_Intl.GetCurrentLocale() → result: cstring`

- Status: ✅ verified (function)
- Blizzard: Gets the current locale used by C_Intl.
- `result`: The current locale ID.
- Called out of combat: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `IntlDocumentation.lua`

### C_Intl.GetDisplayName

`C_Intl.GetDisplayName(displayLocale: cstring) → result: string`

- Status: ✅ verified (function)
- Blizzard: Gets a display name suitable for the specified locale.
- `displayLocale`: The locale whose language conventions are used for the display name
- `result`: The displayable name for the locale.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.GetSortKey

`C_Intl.GetSortKey(text: cstring, strength: CollationStrength) → sortKey: string`

- Status: ✅ verified (function)
- Blizzard: Transforms a string into a collation sort key.
- `text`: The UTF-8 text converted into collation sort-key bytes.
- `strength`: The comparison level used by the collator; lower strengths ignore later-level differences.
- `sortKey`: The sort key bytes excluding the terminating zero byte.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.IsNormalized

`C_Intl.IsNormalized(text: cstring, form: NormalizationForm) → isNormalized: bool`

- Status: ✅ verified (function)
- Blizzard: Tests if the string is normalized according to the specified normalization form.
- `text`: The UTF-8 text checked against the requested normalization form.
- `form`: The normalization form to test against.
- `isNormalized`: True if the string is normalized according to the specified form.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.Length

`C_Intl.Length(text: cstring) → result: number`

- Status: ✅ verified (function)
- Blizzard: Counts character break boundaries in UTF-8 text.
- `text`: The UTF-8 text counted by character break iteration.
- `result`: The number of character boundaries minus the initial boundary.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.Normalize

`C_Intl.Normalize(text: cstring, form: NormalizationForm) → result: string`

- Status: ✅ verified (function)
- Blizzard: Writes the normalized form of the source string to the destination string.
- `text`: The UTF-8 text that is normalized.
- `form`: The normalization form to write.
- `result`: The normalized form of the source string.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.ParseCurrency

`C_Intl.ParseCurrency(text: cstring) → result: CurrencyParseResult`

- Status: ✅ verified (function)
- Blizzard: Parses an entire localized currency string into a double amount and ISO 4217 currency code.
- `text`: The localized currency text to parse for both amount and ISO 4217 code.
- `result`: The numeric amount and ISO 4217 currency code parsed from the localized currency text.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.ParseNumber

`C_Intl.ParseNumber(text: cstring, style: NumberStyle) → result: number`

- Status: ✅ verified (function)
- Blizzard: Parses an entire localized number string into a double using the selected non-currency number formatter.
- `text`: The localized numeric text to parse with the selected style.
- `style`: The number style to parse with; Currency is not accepted here, use ParseCurrency instead.
- `result`: The numeric value parsed from the localized number text.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.SelectPlural

`C_Intl.SelectPlural(number: number, pluralType: PluralType) → result: string`

- Status: ✅ verified (function)
- Blizzard: Returns the keyword of the first plural rule that applies to a number.
- `number`: The number for which the plural rule has to be determined.
- `pluralType`: The plural rule type, cardinal or ordinal.
- `result`: The plural keyword for the rule that applies to the number.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.ToLower

`C_Intl.ToLower(text: cstring) → result: string`

- Status: ✅ verified (function)
- Blizzard: Lowercases the characters in a string; casing is locale-dependent and context-sensitive.
- `text`: The UTF-8 text whose characters are lowercased.
- `result`: The lowercased string, which may be longer or shorter than the original.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.ToTitle

`C_Intl.ToTitle(text: cstring) → result: string`

- Status: ✅ verified (function)
- Blizzard: Titlecases a string using titlecase positions determined by the default Unicode algorithm.
- `text`: The UTF-8 text whose titlecase positions are mapped.
- `result`: The titlecased string, which may be longer or shorter than the original.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.ToUpper

`C_Intl.ToUpper(text: cstring) → result: string`

- Status: ✅ verified (function)
- Blizzard: Uppercases the characters in a string; casing is locale-dependent and context-sensitive.
- `text`: The UTF-8 text whose characters are uppercased.
- `result`: The uppercased string, which may be longer or shorter than the original.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.TransformLocale

`C_Intl.TransformLocale(transform: LocaleTransform) → result: string`

- Status: ✅ verified (function)
- Blizzard: Applies a locale transform to the current locale and returns the transformed locale string.
- `transform`: The locale transform to apply.
- `result`: The transformed locale string.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`

### C_Intl.Transliterate

`C_Intl.Transliterate(text: cstring, transliteratorID: cstring) → result: string`

- Status: ✅ verified (function)
- Blizzard: Opens a system transliterator by ID and transliterates the text in place.
- `text`: The UTF-8 text converted by the opened transliterator.
- `transliteratorID`: A registered transliterator ID, such as a source-target system transliterator.
- `result`: The UTF-8 text after transliterator rules are applied.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- TransliteratorAllowed (Blizzard's docs; not checked in game)
- Source: client docs `IntlDocumentation.lua`
