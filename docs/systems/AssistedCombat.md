# AssistedCombat

Namespace: `C_AssistedCombat`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AssistedCombat.GetActionSpell](#c_assistedcombatgetactionspell) | 1 value |  |
| ✅ | [C_AssistedCombat.GetNextCastSpell](#c_assistedcombatgetnextcastspell) | 1 value |  |
| ✅ | [C_AssistedCombat.GetRotationSpells](#c_assistedcombatgetrotationspells) | 1 value |  |
| ✅ | [C_AssistedCombat.IsAvailable](#c_assistedcombatisavailable) | 2 values |  |

### C_AssistedCombat.GetActionSpell

`C_AssistedCombat.GetActionSpell() → spellID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Source: client docs `AssistedCombatDocumentation.lua`

### C_AssistedCombat.GetNextCastSpell

`C_AssistedCombat.GetNextCastSpell(checkForVisibleButton: bool = False) → spellID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `nil`
- Source: client docs `AssistedCombatDocumentation.lua`

### C_AssistedCombat.GetRotationSpells

`C_AssistedCombat.GetRotationSpells() → spellIDs: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `AssistedCombatDocumentation.lua`

### C_AssistedCombat.IsAvailable

`C_AssistedCombat.IsAvailable() → isAvailable: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Source: client docs `AssistedCombatDocumentation.lua`

## Events

### ASSISTED_COMBAT_ACTION_SPELL_CAST

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
