# LFGListRoles

Namespace: `C_LFGListRoles`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_LFGListRoles.GetRoles](#c_lfglistrolesgetroles) | 1 value |  |
| ✅ | [C_LFGListRoles.GetSavedRoles](#c_lfglistrolesgetsavedroles) | 1 value |  |
| ✅ | [C_LFGListRoles.SetRoles](#c_lfglistrolessetroles) |  |  |

### C_LFGListRoles.GetRoles

`C_LFGListRoles.GetRoles() → roles: LFGRoles`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{dps=boolean,healer=boolean,tank=boolean}`
- Source: client docs `LFGListRolesDocumentation.lua`

### C_LFGListRoles.GetSavedRoles

`C_LFGListRoles.GetSavedRoles() → roles: LFGRoles`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{dps=boolean,healer=boolean,tank=boolean}`
- Source: client docs `LFGListRolesDocumentation.lua`

### C_LFGListRoles.SetRoles

`C_LFGListRoles.SetRoles(roles: LFGRoles, limitToClassRoles: bool = False) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGListRolesDocumentation.lua`

## Events

### LFG_LIST_ROLE_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
