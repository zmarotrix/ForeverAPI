# ExpansionInfo

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [ClassicExpansionAtLeast](#classicexpansionatleast) |  |  |
| ✅ | [ClassicExpansionAtMost](#classicexpansionatmost) |  |  |
| ✅ | [GetClassicExpansionLevel](#getclassicexpansionlevel) |  |  |

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
- Source: client docs `ExpansionInfoDocumentation.lua`
