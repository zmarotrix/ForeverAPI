# UIFrameManager

Namespace: `C_FrameManager`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_FrameManager.GetFrameVisibilityState](#c_framemanagergetframevisibilitystate) |  |  |

### C_FrameManager.GetFrameVisibilityState

`C_FrameManager.GetFrameVisibilityState(frameType: UIFrameType) → shouldShow: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIFrameManagerDocumentation.lua`

## Events

### FRAME_MANAGER_UPDATE_ALL

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### FRAME_MANAGER_UPDATE_FRAME

- Status: ❔ unverified
- Payload: `type: UIFrameType`, `show: bool`
- fires synchronously (Blizzard's docs)

## Types

### UIFrameType

- Enumeration — ❔ unverified
  - `JailersTowerBuffs` = 0
  - `InterruptTutorial` = 1
