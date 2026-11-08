# SocialUI

Namespace: `C_SocialUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SocialUI.IsSystemEnabled](#c_socialuiissystemenabled) | 1 value |  |

### C_SocialUI.IsSystemEnabled

`C_SocialUI.IsSystemEnabled() → isSocialUISystemEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `SocialUIDocumentation.lua`

## Events

### SOCIAL_UI_SYSTEM_STATUS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### SocialSystemType

- Enumeration — ✅ verified
  - `Friends` = 0
  - `QuickJoin` = 1
  - `RaidList` = 2
  - `RecruitAFriend` = 3
  - `RecentAllies` = 4

### SocialUIBlockType

- Enumeration — ✅ verified
  - `None` = 0
  - `Ignore` = 1
  - `BattleNetInviteBlock` = 2

### SocialUIPresenceType

- Enumeration — ✅ verified
  - `Unknown` = 0
  - `Online` = 1
  - `Offline` = 2
  - `Away` = 3
  - `Busy` = 4
  - `AppearOffline` = 5
