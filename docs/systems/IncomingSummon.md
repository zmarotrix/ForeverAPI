# IncomingSummon

Namespace: `C_IncomingSummon`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_IncomingSummon.HasIncomingSummon](#c_incomingsummonhasincomingsummon) | 1 value |  |
| ✅ | [C_IncomingSummon.IncomingSummonStatus](#c_incomingsummonincomingsummonstatus) |  |  |

### C_IncomingSummon.HasIncomingSummon

`C_IncomingSummon.HasIncomingSummon(unit: UnitToken) → summon: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with "player": returned 1 value: `boolean`
- Source: client docs `IncomingSummonDocumentation.lua`

### C_IncomingSummon.IncomingSummonStatus

`C_IncomingSummon.IncomingSummonStatus(unit: UnitToken) → status: SummonStatus`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `IncomingSummonDocumentation.lua`

## Types

### SummonStatus

- Enumeration — ✅ verified
  - `None` = 0
  - `Pending` = 1
  - `Accepted` = 2
  - `Declined` = 3
