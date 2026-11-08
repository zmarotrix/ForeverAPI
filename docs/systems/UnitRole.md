# UnitRole

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [AreClassRolesSoftSuggestions](#areclassrolessoftsuggestions) | 1 value | 1 value |
| ✅ | [CanShowSetRoleButton](#canshowsetrolebutton) | 1 value | 1 value |
| ✅ | [InitiateRolePoll](#initiaterolepoll) |  |  |
| ✅ | [UnitGetAvailableRoles](#unitgetavailableroles) | 3 values | 3 values |
| ✅ | [UnitSetRole](#unitsetrole) | 💥 blocked | 💥 blocked |
| ✅ | [UnitSetRoleEnum](#unitsetroleenum) | 💥 blocked | 💥 blocked |

### AreClassRolesSoftSuggestions

`AreClassRolesSoftSuggestions() → result: bool`

- Status: ✅ verified (function)
- Blizzard: If true, UnitGetAvailableRoles results should be treated as suggested role, not hard limits on what role the current player can display as.
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `UnitRoleDocumentation.lua`

### CanShowSetRoleButton

`CanShowSetRoleButton() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `UnitRoleDocumentation.lua`

### InitiateRolePoll

`InitiateRolePoll() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `UnitRoleDocumentation.lua`

### UnitGetAvailableRoles

`UnitGetAvailableRoles(unit: UnitToken) → tank: bool, healer: bool, dps: bool`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit identity is restricted (Blizzard's docs; not checked in game)
- Called out of combat with "player": returned 3 values: `boolean`, `boolean`, `boolean`
- Called in combat: returned 3 values: `boolean`, `boolean`, `boolean`
- Source: client docs `UnitRoleDocumentation.lua`

### UnitSetRole

`UnitSetRole(unit: UnitToken, roleStr: cstring?) → result: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with "player": 💥 not called: blocked
- Called in combat: 💥 not called: blocked
- Source: client docs `UnitRoleDocumentation.lua`

### UnitSetRoleEnum

`UnitSetRoleEnum(unit: UnitToken, role: LFGRole?) → result: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with "player": 💥 not called: blocked
- Called in combat: 💥 not called: blocked
- Source: client docs `UnitRoleDocumentation.lua`

## Events

### ROLE_CHANGED_INFORM

- Status: ✅ verified
- Payload: `changedName: cstring`, `fromName: cstring`, `oldRole: cstring`, `newRole: cstring`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `s,s,s,s`

### ROLE_POLL_BEGIN

- Status: ✅ verified
- Payload: `fromName: cstring`
- fires synchronously (Blizzard's docs)
