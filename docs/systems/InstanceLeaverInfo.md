# InstanceLeaverInfo

Namespace: `C_InstanceLeaver`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_InstanceLeaver.IsPlayerLeaver](#c_instanceleaverisplayerleaver) | 1 value | 1 value |

### C_InstanceLeaver.IsPlayerLeaver

`C_InstanceLeaver.IsPlayerLeaver() → isLeaver: bool`

- Status: ✅ verified (function)
- Blizzard: Returns whether the player is considered a leaver for repeatedly abandoning mythic+ groups.
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `InstanceLeaverInfoDocumentation.lua`

## Events

### INSTANCE_LEAVER_STATUS_CHANGED

- Status: ✅ verified
- Payload: `isLeaver: bool`
- fires synchronously (Blizzard's docs)
