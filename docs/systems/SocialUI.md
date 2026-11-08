# SocialUI

Namespace: `C_SocialUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_SocialUI.IsSystemEnabled](#c_socialuiissystemenabled) |  |  |

### C_SocialUI.IsSystemEnabled

`C_SocialUI.IsSystemEnabled() → isSocialUISystemEnabled: bool`

- Status: ❔ unverified
- Source: client docs `SocialUIDocumentation.lua`

## Events

### SOCIAL_UI_SYSTEM_STATUS_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### SocialSystemType

- Enumeration — ❔ unverified
  - `Friends` = 0
  - `QuickJoin` = 1
  - `RaidList` = 2
  - `RecruitAFriend` = 3
  - `RecentAllies` = 4

### SocialUIBlockType

- Enumeration — ❔ unverified
  - `None` = 0
  - `Ignore` = 1
  - `BattleNetInviteBlock` = 2

### SocialUIPresenceType

- Enumeration — ❔ unverified
  - `Unknown` = 0
  - `Online` = 1
  - `Offline` = 2
  - `Away` = 3
  - `Busy` = 4
  - `AppearOffline` = 5
