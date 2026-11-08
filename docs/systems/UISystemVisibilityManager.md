# UISystemVisibilityManager

Namespace: `C_SystemVisibilityManager`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SystemVisibilityManager.IsSystemVisible](#c_systemvisibilitymanagerissystemvisible) | 1 value | 1 value |

### C_SystemVisibilityManager.IsSystemVisible

`C_SystemVisibilityManager.IsSystemVisible(system: UISystemType) → visible: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `UISystemVisibilityManagerDocumentation.lua`

## Events

### SYSTEM_VISIBILITY_CHANGED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

## Types

### UISystemType

- Enumeration — ✅ verified
  - `InGameNavigation` = 0
