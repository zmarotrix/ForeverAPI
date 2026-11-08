# ExpansionInfo

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [ClassicExpansionAtLeast](#classicexpansionatleast) |  |  |
| ✅ | [ClassicExpansionAtMost](#classicexpansionatmost) |  |  |
| ✅ | [GetClassicExpansionLevel](#getclassicexpansionlevel) | 1 value | 1 value |

### ClassicExpansionAtLeast

`ClassicExpansionAtLeast(expansionLevel: number) → isAtLeast: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ExpansionInfoDocumentation.lua`

### ClassicExpansionAtMost

`ClassicExpansionAtMost(expansionLevel: number) → isAtMost: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ExpansionInfoDocumentation.lua`

### GetClassicExpansionLevel

`GetClassicExpansionLevel() → expansionLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ExpansionInfoDocumentation.lua`
