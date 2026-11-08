# RestrictedActions

Namespace: `C_RestrictedActions`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_RestrictedActions.CheckAllowProtectedFunctions](#c_restrictedactionscheckallowprotectedfunctions) |  |  |
| ✅ | [C_RestrictedActions.GetAddOnRestrictionState](#c_restrictedactionsgetaddonrestrictionstate) |  |  |
| ⛔ | [C_RestrictedActions.InCombatLockdown](#c_restrictedactionsincombatlockdown) |  |  |
| ✅ | [C_RestrictedActions.IsAddOnRestrictionActive](#c_restrictedactionsisaddonrestrictionactive) |  |  |

### C_RestrictedActions.CheckAllowProtectedFunctions

`C_RestrictedActions.CheckAllowProtectedFunctions(object: FrameScriptObject, silent: bool = False) → protectedFunctionsAllowed: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the calling context has permissions to call protected functions on the supplied object.
- `silent`: If true, don't signal blocked action errors if protected function calls are disallowed.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RestrictedActionsDocumentation.lua`

### C_RestrictedActions.GetAddOnRestrictionState

`C_RestrictedActions.GetAddOnRestrictionState(type: AddOnRestrictionType) → state: AddOnRestrictionState`

- Status: ✅ verified (function)
- Blizzard: Returns the current state of an addon restriction type.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RestrictedActionsDocumentation.lua`

### C_RestrictedActions.InCombatLockdown

`C_RestrictedActions.InCombatLockdown() → inCombatLockdown: bool`

- Status: ⛔ in Blizzard's docs, not in game
- Namespace:  (Blizzard's docs; not checked in game)
- Source: client docs `RestrictedActionsDocumentation.lua`

### C_RestrictedActions.IsAddOnRestrictionActive

`C_RestrictedActions.IsAddOnRestrictionActive(type: AddOnRestrictionType) → active: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if an addon restriction type is in an active state. Will always return false during dispatch of ADDON_RESTRICTION_STATE_CHANGED.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RestrictedActionsDocumentation.lua`

## Events

### ADDON_ACTION_BLOCKED

- Status: ✅ verified
- Payload: `isTainted: cstring`, `function: cstring`
- fires synchronously (Blizzard's docs)

### ADDON_ACTION_FORBIDDEN

- Status: ✅ verified
- Payload: `isTainted: cstring`, `function: cstring`
- fires synchronously (Blizzard's docs)
- Seen firing 8 times (0 in combat); argument kinds: `s,s`

### ADDON_RESTRICTION_STATE_CHANGED

- Status: ✅ verified
- Payload: `type: AddOnRestrictionType`, `state: AddOnRestrictionState`
- Blizzard: Fired when the state of an addon restriction type is changing. This event is sequenced such that it will always be fired before a restriction becomes active, or after it is deactivated.
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (0 in combat); argument kinds: `n,n`

### MACRO_ACTION_BLOCKED

- Status: ✅ verified
- Payload: `function: cstring`
- fires synchronously (Blizzard's docs)

### MACRO_ACTION_FORBIDDEN

- Status: ✅ verified
- Payload: `function: cstring`
- fires synchronously (Blizzard's docs)
