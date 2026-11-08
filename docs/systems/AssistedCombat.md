# AssistedCombat

Namespace: `C_AssistedCombat`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_AssistedCombat.GetActionSpell](#c_assistedcombatgetactionspell) |  |  |
| ❔ | [C_AssistedCombat.GetNextCastSpell](#c_assistedcombatgetnextcastspell) |  |  |
| ❔ | [C_AssistedCombat.GetRotationSpells](#c_assistedcombatgetrotationspells) |  |  |
| ❔ | [C_AssistedCombat.IsAvailable](#c_assistedcombatisavailable) |  |  |

### C_AssistedCombat.GetActionSpell

`C_AssistedCombat.GetActionSpell() → spellID: number?`

- Status: ❔ unverified
- Source: client docs `AssistedCombatDocumentation.lua`

### C_AssistedCombat.GetNextCastSpell

`C_AssistedCombat.GetNextCastSpell(checkForVisibleButton: bool = False) → spellID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AssistedCombatDocumentation.lua`

### C_AssistedCombat.GetRotationSpells

`C_AssistedCombat.GetRotationSpells() → spellIDs: number[]`

- Status: ❔ unverified
- Source: client docs `AssistedCombatDocumentation.lua`

### C_AssistedCombat.IsAvailable

`C_AssistedCombat.IsAvailable() → isAvailable: bool, failureReason: string`

- Status: ❔ unverified
- Source: client docs `AssistedCombatDocumentation.lua`

## Events

### ASSISTED_COMBAT_ACTION_SPELL_CAST

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
