# Threat

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetThreatStatusColor](#getthreatstatuscolor) |  |  |
| ✅ | [IsThreatWarningEnabled](#isthreatwarningenabled) |  |  |

### GetThreatStatusColor

`GetThreatStatusColor(gameErrorIndex: number) → colorR: number, colorG: number, colorB: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ThreatDocumentation.lua`

### IsThreatWarningEnabled

`IsThreatWarningEnabled() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `ThreatDocumentation.lua`
