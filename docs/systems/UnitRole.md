# UnitRole

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [AreClassRolesSoftSuggestions](#areclassrolessoftsuggestions) |  |  |
| ❔ | [CanShowSetRoleButton](#canshowsetrolebutton) |  |  |
| ❔ | [InitiateRolePoll](#initiaterolepoll) |  |  |
| ❔ | [UnitGetAvailableRoles](#unitgetavailableroles) |  |  |
| ❔ | [UnitSetRole](#unitsetrole) |  |  |
| ❔ | [UnitSetRoleEnum](#unitsetroleenum) |  |  |

### AreClassRolesSoftSuggestions

`AreClassRolesSoftSuggestions() → result: bool`

- Status: ❔ unverified
- Blizzard: If true, UnitGetAvailableRoles results should be treated as suggested role, not hard limits on what role the current player can display as.
- Source: client docs `UnitRoleDocumentation.lua`

### CanShowSetRoleButton

`CanShowSetRoleButton() → result: bool`

- Status: ❔ unverified
- Source: client docs `UnitRoleDocumentation.lua`

### InitiateRolePoll

`InitiateRolePoll() → result: bool`

- Status: ❔ unverified
- Source: client docs `UnitRoleDocumentation.lua`

### UnitGetAvailableRoles

`UnitGetAvailableRoles(unit: UnitToken) → tank: bool, healer: bool, dps: bool`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit identity is restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitRoleDocumentation.lua`

### UnitSetRole

`UnitSetRole(unit: UnitToken, roleStr: cstring?) → result: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitRoleDocumentation.lua`

### UnitSetRoleEnum

`UnitSetRoleEnum(unit: UnitToken, role: LFGRole?) → result: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitRoleDocumentation.lua`

## Events

### ROLE_CHANGED_INFORM

- Status: ❔ unverified
- Payload: `changedName: cstring`, `fromName: cstring`, `oldRole: cstring`, `newRole: cstring`
- fires synchronously (Blizzard's docs)

### ROLE_POLL_BEGIN

- Status: ❔ unverified
- Payload: `fromName: cstring`
- fires synchronously (Blizzard's docs)
