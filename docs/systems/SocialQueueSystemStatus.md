# SocialQueueSystemStatus

Namespace: `C_SocialQueue`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SocialQueue.IsSystemEnabled](#c_socialqueueissystemenabled) | 1 value |  |
| ✅ | [C_SocialQueue.IsSystemSupported](#c_socialqueueissystemsupported) | 1 value |  |

### C_SocialQueue.IsSystemEnabled

`C_SocialQueue.IsSystemEnabled() → isSystemEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `SocialQueueSystemStatusDocumentation.lua`

### C_SocialQueue.IsSystemSupported

`C_SocialQueue.IsSystemSupported() → isSystemSupported: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `SocialQueueSystemStatusDocumentation.lua`

## Events

### SOCIAL_UI_SOCIAL_QUEUE_SYSTEM_STATUS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
