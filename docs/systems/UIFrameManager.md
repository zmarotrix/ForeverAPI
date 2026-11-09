# UIFrameManager

Namespace: `C_FrameManager`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_FrameManager.GetFrameVisibilityState](#c_framemanagergetframevisibilitystate) | 1 value | 1 value |

### C_FrameManager.GetFrameVisibilityState

`C_FrameManager.GetFrameVisibilityState(frameType: UIFrameType) → shouldShow: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `UIFrameManagerDocumentation.lua`

## Events

### FRAME_MANAGER_UPDATE_ALL

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 57 times (0 in combat); argument kinds: ``

### FRAME_MANAGER_UPDATE_FRAME

- Status: ✅ verified
- Payload: `type: UIFrameType`, `show: bool`
- fires synchronously (Blizzard's docs)

## Types

### UIFrameType

- Enumeration — ✅ verified
  - `JailersTowerBuffs` = 0
  - `InterruptTutorial` = 1
