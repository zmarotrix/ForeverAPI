# SlashCommand

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [AreDangerousScriptsAllowed](#aredangerousscriptsallowed) | 1 value | 1 value |
| ✅ | [SetAllowDangerousScripts](#setallowdangerousscripts) |  |  |

### AreDangerousScriptsAllowed

`AreDangerousScriptsAllowed() → allowed: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SlashCommandDocumentation.lua`

### SetAllowDangerousScripts

`SetAllowDangerousScripts(allowed: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SlashCommandDocumentation.lua`
