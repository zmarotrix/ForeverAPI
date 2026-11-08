# LFGListRoles

Namespace: `C_LFGListRoles`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_LFGListRoles.GetRoles](#c_lfglistrolesgetroles) |  |  |
| ❔ | [C_LFGListRoles.GetSavedRoles](#c_lfglistrolesgetsavedroles) |  |  |
| ❔ | [C_LFGListRoles.SetRoles](#c_lfglistrolessetroles) |  |  |

### C_LFGListRoles.GetRoles

`C_LFGListRoles.GetRoles() → roles: LFGRoles`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `LFGListRolesDocumentation.lua`

### C_LFGListRoles.GetSavedRoles

`C_LFGListRoles.GetSavedRoles() → roles: LFGRoles`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `LFGListRolesDocumentation.lua`

### C_LFGListRoles.SetRoles

`C_LFGListRoles.SetRoles(roles: LFGRoles, limitToClassRoles: bool = False) → success: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGListRolesDocumentation.lua`

## Events

### LFG_LIST_ROLE_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
