# Threat

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetThreatStatusColor](#getthreatstatuscolor) |  |  |
| ✅ | [IsThreatWarningEnabled](#isthreatwarningenabled) | 1 value |  |

### GetThreatStatusColor

`GetThreatStatusColor(gameErrorIndex: number) → colorR: number, colorG: number, colorB: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ThreatDocumentation.lua`

### IsThreatWarningEnabled

`IsThreatWarningEnabled() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ThreatDocumentation.lua`
