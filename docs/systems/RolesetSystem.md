# RolesetSystem

Namespace: `C_Roleset`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Roleset.ApplyRolesetFilters](#c_rolesetapplyrolesetfilters) |  |  |
| ✅ | [C_Roleset.GetActiveAllowedRolesets](#c_rolesetgetactiveallowedrolesets) | 1 value |  |
| ✅ | [C_Roleset.GetActiveBlockedRolesets](#c_rolesetgetactiveblockedrolesets) | 1 value |  |

### C_Roleset.ApplyRolesetFilters

`C_Roleset.ApplyRolesetFilters(blockedRolesets: string[], allowedRolesets: string[])`

- Status: ✅ verified (function)
- Blizzard: Sets or clears both blocklist and allowlist filters atomically with a single visibility reevaluation. Pass an empty table to clear the corresponding filter. Blocked for tainted callers while in combat lockdown.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RolesetSystemDocumentation.lua`

### C_Roleset.GetActiveAllowedRolesets

`C_Roleset.GetActiveAllowedRolesets() → allowedRolesets: string[]`

- Status: ✅ verified (function)
- Blizzard: Returns the rolesets in the currently active allowlist.
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `RolesetSystemDocumentation.lua`

### C_Roleset.GetActiveBlockedRolesets

`C_Roleset.GetActiveBlockedRolesets() → blockedRolesets: string[]`

- Status: ✅ verified (function)
- Blizzard: Returns the rolesets in the currently active blocklist.
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `RolesetSystemDocumentation.lua`
