# LuaStringExtensions

Namespace: `string`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [string.contains](#stringcontains) |  |  |
| ✅ | [string.endswith](#stringendswith) |  |  |
| ✅ | [string.ltrim](#stringltrim) |  |  |
| ✅ | [string.rtrim](#stringrtrim) |  |  |
| ✅ | [string.startswith](#stringstartswith) |  |  |
| ✅ | [string.trim](#stringtrim) |  |  |

### string.contains

`string.contains(str: stringView, substring: stringView) → contains: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a string contains the specified literal substring.
- `str`: The string to search.
- `substring`: The literal substring for which to search.
- `contains`: True if the string contains the specified substring; otherwise false.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaStringExtensionsDocumentation.lua`

### string.endswith

`string.endswith(str: stringView, suffix: stringView) → endsWith: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a string ends with the specified suffix.
- `str`: The string to inspect.
- `suffix`: The suffix for which to search.
- `endsWith`: True if the string ends with the specified suffix; otherwise false.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaStringExtensionsDocumentation.lua`

### string.ltrim

`string.ltrim(str: stringView, characters: stringView =  \r\n\t) → trimmed: stringView`

- Status: ✅ verified (function)
- Blizzard: Returns a string with all bytes in the specified character set removed from the start.
- `str`: The string to trim.
- `characters`: The set of bytes to remove.
- `trimmed`: The left-trimmed string.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaStringExtensionsDocumentation.lua`

### string.rtrim

`string.rtrim(str: stringView, characters: stringView =  \r\n\t) → trimmed: stringView`

- Status: ✅ verified (function)
- Blizzard: Returns a string with all bytes in the specified character set removed from the end.
- `str`: The string to trim.
- `characters`: The set of bytes to remove.
- `trimmed`: The right-trimmed string.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaStringExtensionsDocumentation.lua`

### string.startswith

`string.startswith(str: stringView, prefix: stringView) → startsWith: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a string starts with the specified prefix.
- `str`: The string to inspect.
- `prefix`: The prefix for which to search.
- `startsWith`: True if the string starts with the specified prefix; otherwise false.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaStringExtensionsDocumentation.lua`

### string.trim

`string.trim(str: stringView, characters: stringView =  \r\n\t) → trimmed: stringView`

- Status: ✅ verified (function)
- Blizzard: Returns a string with all bytes in the specified character set removed from both ends.
- `str`: The string to trim.
- `characters`: The set of bytes to remove.
- `trimmed`: The trimmed string.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaStringExtensionsDocumentation.lua`
