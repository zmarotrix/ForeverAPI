# CombatText

Namespace: `C_CombatText`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_CombatText.GetActiveUnit](#c_combattextgetactiveunit) |  |  |
| ✅ | [C_CombatText.GetCurrentEventInfo](#c_combattextgetcurrenteventinfo) |  |  |
| ✅ | [C_CombatText.SetActiveUnit](#c_combattextsetactiveunit) |  |  |

### C_CombatText.GetActiveUnit

`C_CombatText.GetActiveUnit() → unitTarget: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `CombatTextDocumentation.lua`

### C_CombatText.GetCurrentEventInfo

`C_CombatText.GetCurrentEventInfo()`

- Status: ✅ verified (function)
- always returns secret values (Blizzard's docs; not checked in game)
- Source: client docs `CombatTextDocumentation.lua`

### C_CombatText.SetActiveUnit

`C_CombatText.SetActiveUnit(unitToken: UnitToken)`

- Status: ✅ verified (function)
- RequiresDeclassifiedUnitIdentity (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatTextDocumentation.lua`

## Events

### COMBAT_TEXT_UPDATE

- Status: ✅ verified
- Payload: `combatTextType: cstring`
- fires synchronously (Blizzard's docs)
