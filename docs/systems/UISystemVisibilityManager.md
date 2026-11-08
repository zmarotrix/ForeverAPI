# UISystemVisibilityManager

Namespace: `C_SystemVisibilityManager`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_SystemVisibilityManager.IsSystemVisible](#c_systemvisibilitymanagerissystemvisible) |  |  |

### C_SystemVisibilityManager.IsSystemVisible

`C_SystemVisibilityManager.IsSystemVisible(system: UISystemType) → visible: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UISystemVisibilityManagerDocumentation.lua`

## Events

### SYSTEM_VISIBILITY_CHANGED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

## Types

### UISystemType

- Enumeration — ❔ unverified
  - `InGameNavigation` = 0
