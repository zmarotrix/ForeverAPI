# StringUtil

Namespace: `C_StringUtil`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_StringUtil.CreateAbbreviatedNumberFormatter](#c_stringutilcreateabbreviatednumberformatter) |  |  |
| ✅ | [C_StringUtil.CreateNumericRuleFormatter](#c_stringutilcreatenumericruleformatter) |  |  |
| ✅ | [C_StringUtil.CreateSecondsFormatter](#c_stringutilcreatesecondsformatter) |  |  |
| ✅ | [C_StringUtil.EscapeDecimalNonPrintables](#c_stringutilescapedecimalnonprintables) |  |  |
| ✅ | [C_StringUtil.EscapeLuaFormatString](#c_stringutilescapeluaformatstring) |  |  |
| ✅ | [C_StringUtil.EscapeLuaPatterns](#c_stringutilescapeluapatterns) |  |  |
| ✅ | [C_StringUtil.EscapeQuotedCodes](#c_stringutilescapequotedcodes) |  |  |
| ✅ | [C_StringUtil.FloorToNearestString](#c_stringutilfloortoneareststring) |  |  |
| 🆕 | [C_StringUtil.GetDefaultAbbreviationBreakpoints](#c_stringutilgetdefaultabbreviationbreakpoints) |  |  |
| ✅ | [C_StringUtil.RemoveContiguousSpaces](#c_stringutilremovecontiguousspaces) |  |  |
| ✅ | [C_StringUtil.RoundToNearestString](#c_stringutilroundtoneareststring) |  |  |
| ✅ | [C_StringUtil.StripHyperlinks](#c_stringutilstriphyperlinks) |  |  |
| ✅ | [C_StringUtil.StripTextureMarkupForLooseFiles](#c_stringutilstriptexturemarkupforloosefiles) |  |  |
| ✅ | [C_StringUtil.TruncateWhenZero](#c_stringutiltruncatewhenzero) |  |  |
| ✅ | [C_StringUtil.WrapString](#c_stringutilwrapstring) |  |  |

### C_StringUtil.CreateAbbreviatedNumberFormatter

`C_StringUtil.CreateAbbreviatedNumberFormatter() → formatter: AbbreviatedNumberFormatter`

- Status: ✅ verified (function)
- Blizzard: Creates a numeric formatter that converts numbers to abbreviated strings, eg. 123456 -> '123k'.
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.CreateNumericRuleFormatter

`C_StringUtil.CreateNumericRuleFormatter() → formatter: NumericRuleFormatter`

- Status: ✅ verified (function)
- Blizzard: Creates a numeric formatter that converts numbers to strings with flexible rulesets.
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.CreateSecondsFormatter

`C_StringUtil.CreateSecondsFormatter() → formatter: SecondsFormatter`

- Status: ✅ verified (function)
- Blizzard: Creates a numeric formatter that converts numbers measuring durations in seconds to strings, eg. 93 -> '1m 33s'.
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.EscapeDecimalNonPrintables

`C_StringUtil.EscapeDecimalNonPrintables(text: stringView) → escapedText: string`

- Status: ✅ verified (function)
- Blizzard: Returns a string with ASCII control characters (except 
, , and 	) and invalid UTF-8 bytes replaced by decimal escape sequences (e.g. \127).
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.EscapeLuaFormatString

`C_StringUtil.EscapeLuaFormatString(text: string) → escapedText: stringView`

- Status: ✅ verified (function)
- Blizzard: Returns a string with Lua format string tokens ('%') escaped.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.EscapeLuaPatterns

`C_StringUtil.EscapeLuaPatterns(text: stringView) → escapedText: string`

- Status: ✅ verified (function)
- Blizzard: Returns a string with all Lua pattern characters escaped.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.EscapeQuotedCodes

`C_StringUtil.EscapeQuotedCodes(text: string) → escaped: stringView`

- Status: ✅ verified (function)
- Blizzard: Returns a string with all quoted code sequences ('|' characters) escaped.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.FloorToNearestString

`C_StringUtil.FloorToNearestString(number: number) → text: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.GetDefaultAbbreviationBreakpoints

`C_StringUtil.GetDefaultAbbreviationBreakpoints(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_StringUtil.RemoveContiguousSpaces

`C_StringUtil.RemoveContiguousSpaces(text: stringView, maxAllowedSpaces: number) → trimmedText: string`

- Status: ✅ verified (function)
- Blizzard: Returns a string with all contiguous occurrences of ASCII space characters truncated.
- `maxAllowedSpaces`: Maximum number of permitted contiguous space characters; excessive spaces will be truncated to this count.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.RoundToNearestString

`C_StringUtil.RoundToNearestString(number: number) → text: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.StripHyperlinks

`C_StringUtil.StripHyperlinks(text: string, maintainColor: bool = False, maintainBrackets: bool = False, stripNewlines: bool = False, maintainAtlases: bool = False, maintainTextures: bool = False) → stripped: stringView`

- Status: ✅ verified (function)
- `maintainColor`: If true, preserve all '|c' and '|r' quoted code sequences.
- `maintainBrackets`: If true, preserve all '[' and ']' characters.
- `stripNewlines`: If true, remove all '|n' quoted code sequences.
- `maintainAtlases`: If true, preserve all balanced '|A' and '|a' quoted code sequences.
- `maintainTextures`: If true, preserve all balanced '|T' and '|t' quoted code sequences.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.StripTextureMarkupForLooseFiles

`C_StringUtil.StripTextureMarkupForLooseFiles(text: string) → stripped: stringView`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.TruncateWhenZero

`C_StringUtil.TruncateWhenZero(number: number) → text: string`

- Status: ✅ verified (function)
- Blizzard: Formats the given number to a string as an integer (rounding down). If the integer is zero, returns an empty string.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

### C_StringUtil.WrapString

`C_StringUtil.WrapString(infix: stringView, prefix: stringView?, suffix: stringView?) → text: string`

- Status: ✅ verified (function)
- Blizzard: Returns a string with 'prefix' and 'suffix' joined to 'infix' iif 'infix' is not an empty string. Else, an empty string is returned.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `StringUtilDocumentation.lua`

## Types

### StripHyperlinkOptions

- Structure
  - `maintainColor`: bool
  - `maintainBrackets`: bool
  - `stripNewlines`: bool
  - `maintainAtlases`: bool
  - `maintainTextures`: bool
