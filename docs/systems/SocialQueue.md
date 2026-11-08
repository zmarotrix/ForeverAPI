# SocialQueue

Namespace: `C_SocialQueue`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SocialQueue.GetAllGroups](#c_socialqueuegetallgroups) | 1 value | 1 value |
| ✅ | [C_SocialQueue.GetConfig](#c_socialqueuegetconfig) | 1 value | 1 value |
| ✅ | [C_SocialQueue.GetGroupForPlayer](#c_socialqueuegetgroupforplayer) | 0 values | 0 values |
| ✅ | [C_SocialQueue.GetGroupInfo](#c_socialqueuegetgroupinfo) | 0 values | 0 values |
| ✅ | [C_SocialQueue.GetGroupMembers](#c_socialqueuegetgroupmembers) | 0 values | 0 values |
| ✅ | [C_SocialQueue.GetGroupQueues](#c_socialqueuegetgroupqueues) | 0 values | 0 values |
| ✅ | [C_SocialQueue.RequestToJoin](#c_socialqueuerequesttojoin) |  |  |
| ✅ | [C_SocialQueue.SignalToastDisplayed](#c_socialqueuesignaltoastdisplayed) |  |  |

### C_SocialQueue.GetAllGroups

`C_SocialQueue.GetAllGroups(allowNonJoinable: bool = False, allowNonQueuedGroups: bool = False) → groupGUIDs: WOWGUID[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `SocialQueueDocumentation.lua`

### C_SocialQueue.GetConfig

`C_SocialQueue.GetConfig() → config: SocialQueueConfig`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{DELAY_DURATION=number,PLAYER_FRIEND_VALUE=number,PLAYER_GUILD_VALUE=number,PLAYER_MULTIPLIER=number,QUEUE_MULTIPLIER=number,THROTTLE_DECAY_TIME=number,THROTTLE_DF_BEST_PRIORITY=number,THROTTLE_DF_MAX_ITEM_LEVEL=number,THROTTLE_INITIAL_THRESHOLD=number,THROTTLE_LFGLIST_ILVL_SCALING_ABOVE=number,THROTTLE_LFGLIST_ILVL_SCALING_BELOW=number,THROTTLE_LFGLIST_PRIORITY_ABOVE=number,THROTTLE_LFGLIST_PRIORITY_BELOW=number,THROTTLE_LFGLIST_PRIORITY_DEFAULT=number,THROTTLE_MIN_THRESHOLD=number,THROTTLE_PRIORITY_SPIKE=number,THROTTLE_PVP_HONOR_THRESHOLD=number,THROTTLE_PVP_PRIORITY_LOW=number,THROTTLE_PVP_PRIORITY_NORMAL=number,THROTTLE_RF_ILVL_SCALING_ABOVE=number,THROTTLE_RF_PRIORITY_ABOVE=number,TOASTS_DISABLED=boolean,TOAST_DURATION=number}`
- Called in combat: returned 1 value: `table{DELAY_DURATION=number,PLAYER_FRIEND_VALUE=number,PLAYER_GUILD_VALUE=number,PLAYER_MULTIPLIER=number,QUEUE_MULTIPLIER=number,THROTTLE_DECAY_TIME=number,THROTTLE_DF_BEST_PRIORITY=number,THROTTLE_DF_MAX_ITEM_LEVEL=number,THROTTLE_INITIAL_THRESHOLD=number,THROTTLE_LFGLIST_ILVL_SCALING_ABOVE=number,THROTTLE_LFGLIST_ILVL_SCALING_BELOW=number,THROTTLE_LFGLIST_PRIORITY_ABOVE=number,THROTTLE_LFGLIST_PRIORITY_BELOW=number,THROTTLE_LFGLIST_PRIORITY_DEFAULT=number,THROTTLE_MIN_THRESHOLD=number,THROTTLE_PRIORITY_SPIKE=number,THROTTLE_PVP_HONOR_THRESHOLD=number,THROTTLE_PVP_PRIORITY_LOW=number,THROTTLE_PVP_PRIORITY_NORMAL=number,THROTTLE_RF_ILVL_SCALING_ABOVE=number,THROTTLE_RF_PRIORITY_ABOVE=number,TOASTS_DISABLED=boolean,TOAST_DURATION=number}`
- Source: client docs `SocialQueueDocumentation.lua`

### C_SocialQueue.GetGroupForPlayer

`C_SocialQueue.GetGroupForPlayer(playerGUID: WOWGUID) → groupGUID: WOWGUID, isSoloQueueParty: bool`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `SocialQueueDocumentation.lua`

### C_SocialQueue.GetGroupInfo

`C_SocialQueue.GetGroupInfo(groupGUID: WOWGUID) → canJoin: bool, numQueues: number, needTank: bool, needHealer: bool, needDamage: bool, isSoloQueueParty: bool, questSessionActive: bool, leaderGUID: WOWGUID`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `SocialQueueDocumentation.lua`

### C_SocialQueue.GetGroupMembers

`C_SocialQueue.GetGroupMembers(groupGUID: WOWGUID) → groupMembers: SocialQueuePlayerInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `SocialQueueDocumentation.lua`

### C_SocialQueue.GetGroupQueues

`C_SocialQueue.GetGroupQueues(groupGUID: WOWGUID) → queues: SocialQueueGroupQueueInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `SocialQueueDocumentation.lua`

### C_SocialQueue.RequestToJoin

`C_SocialQueue.RequestToJoin(groupGUID: WOWGUID, applyAsTank: bool = False, applyAsHealer: bool = False, applyAsDamage: bool = False) → requestSuccessful: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SocialQueueDocumentation.lua`

### C_SocialQueue.SignalToastDisplayed

`C_SocialQueue.SignalToastDisplayed(groupGUID: WOWGUID, priority: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SocialQueueDocumentation.lua`

## Events

### SOCIAL_QUEUE_CONFIG_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 31 times (12 in combat); argument kinds: ``

### SOCIAL_QUEUE_UPDATE

- Status: ✅ verified
- Payload: `groupGUID: WOWGUID`, `numAddedItems: number?`
- fires synchronously (Blizzard's docs)
- Seen firing 158 times (25 in combat); argument kinds: `s,-` / `s,n`

## Types

### SocialQueueConfig

- Structure
  - `TOASTS_DISABLED`: bool
  - `TOAST_DURATION`: number
  - `DELAY_DURATION`: number
  - `QUEUE_MULTIPLIER`: number
  - `PLAYER_MULTIPLIER`: number
  - `PLAYER_FRIEND_VALUE`: number
  - `PLAYER_GUILD_VALUE`: number
  - `THROTTLE_INITIAL_THRESHOLD`: number
  - `THROTTLE_DECAY_TIME`: number
  - `THROTTLE_PRIORITY_SPIKE`: number
  - `THROTTLE_MIN_THRESHOLD`: number
  - `THROTTLE_PVP_PRIORITY_NORMAL`: number
  - `THROTTLE_PVP_PRIORITY_LOW`: number
  - `THROTTLE_PVP_HONOR_THRESHOLD`: number
  - `THROTTLE_LFGLIST_PRIORITY_DEFAULT`: number
  - `THROTTLE_LFGLIST_PRIORITY_ABOVE`: number
  - `THROTTLE_LFGLIST_PRIORITY_BELOW`: number
  - `THROTTLE_LFGLIST_ILVL_SCALING_ABOVE`: number
  - `THROTTLE_LFGLIST_ILVL_SCALING_BELOW`: number
  - `THROTTLE_RF_PRIORITY_ABOVE`: number
  - `THROTTLE_RF_ILVL_SCALING_ABOVE`: number
  - `THROTTLE_DF_MAX_ITEM_LEVEL`: number
  - `THROTTLE_DF_BEST_PRIORITY`: number

### SocialQueueGroupInfo

- Structure
  - `canJoin`: bool
  - `numQueues`: number
  - `needTank`: bool
  - `needHealer`: bool
  - `needDamage`: bool
  - `isSoloQueueParty`: bool
  - `questSessionActive`: bool
  - `leaderGUID`: WOWGUID

### SocialQueueGroupQueueInfo

- Structure
  - `clientID`: number
  - `eligible`: bool
  - `needTank`: bool
  - `needHealer`: bool
  - `needDamage`: bool
  - `isAutoAccept`: bool
  - `queueData`: QueueSpecificInfo

### SocialQueuePlayerInfo

- Structure
  - `guid`: WOWGUID
  - `clubId`: ClubId?
