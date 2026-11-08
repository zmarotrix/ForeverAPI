# InstanceLeaverInfo

Namespace: `C_InstanceLeaver`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_InstanceLeaver.IsPlayerLeaver](#c_instanceleaverisplayerleaver) |  |  |

### C_InstanceLeaver.IsPlayerLeaver

`C_InstanceLeaver.IsPlayerLeaver() → isLeaver: bool`

- Status: ❔ unverified
- Blizzard: Returns whether the player is considered a leaver for repeatedly abandoning mythic+ groups.
- Source: client docs `InstanceLeaverInfoDocumentation.lua`

## Events

### INSTANCE_LEAVER_STATUS_CHANGED

- Status: ❔ unverified
- Payload: `isLeaver: bool`
- fires synchronously (Blizzard's docs)
