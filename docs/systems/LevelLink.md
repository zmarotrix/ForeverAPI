# LevelLink

Namespace: `C_LevelLink`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_LevelLink.IsActionLocked](#c_levellinkisactionlocked) | 1 value | 1 value |
| ✅ | [C_LevelLink.IsSpellLocked](#c_levellinkisspelllocked) | 1 value | 1 value |

### C_LevelLink.IsActionLocked

`C_LevelLink.IsActionLocked(actionID: luaIndex) → isLocked: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LevelLinkDocumentation.lua`

### C_LevelLink.IsSpellLocked

`C_LevelLink.IsSpellLocked(spellID: number) → isLocked: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `spell`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LevelLinkDocumentation.lua`
