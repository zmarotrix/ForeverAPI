# UISystemVisibilityManager

Namespace: `C_SystemVisibilityManager`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SystemVisibilityManager.IsSystemVisible](#c_systemvisibilitymanagerissystemvisible) |  |  |

### C_SystemVisibilityManager.IsSystemVisible

`C_SystemVisibilityManager.IsSystemVisible(system: UISystemType) → visible: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
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
