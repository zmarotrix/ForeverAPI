# LFGInfo

Namespace: `C_LFGInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_LFGInfo.AreCrossFactionGroupQueuesAllowed](#c_lfginfoarecrossfactiongroupqueuesallowed) |  |  |
| ✅ | [C_LFGInfo.CanPlayerUseGroupFinder](#c_lfginfocanplayerusegroupfinder) | 2 values | 2 values |
| ✅ | [C_LFGInfo.CanPlayerUseLFD](#c_lfginfocanplayeruselfd) | 2 values | 2 values |
| ✅ | [C_LFGInfo.CanPlayerUseLFR](#c_lfginfocanplayeruselfr) | 2 values | 2 values |
| ✅ | [C_LFGInfo.CanPlayerUsePVP](#c_lfginfocanplayerusepvp) | 2 values | 2 values |
| ✅ | [C_LFGInfo.CanPlayerUsePremadeGroup](#c_lfginfocanplayerusepremadegroup) | 2 values | 2 values |
| ✅ | [C_LFGInfo.CanPlayerUseScenarioFinder](#c_lfginfocanplayerusescenariofinder) | 2 values | 2 values |
| ✅ | [C_LFGInfo.ConfirmLfgExpandSearch](#c_lfginfoconfirmlfgexpandsearch) |  |  |
| ✅ | [C_LFGInfo.DoesActivePartyMeetPremadeLaunchCount](#c_lfginfodoesactivepartymeetpremadelaunchcount) |  |  |
| ✅ | [C_LFGInfo.DoesCrossFactionQueueRequireFullPremade](#c_lfginfodoescrossfactionqueuerequirefullpremade) |  |  |
| ✅ | [C_LFGInfo.GetActiveLFGDungeonName](#c_lfginfogetactivelfgdungeonname) | 1 value | 1 value |
| ✅ | [C_LFGInfo.GetAllEntriesForCategory](#c_lfginfogetallentriesforcategory) | 1 value | 1 value |
| ✅ | [C_LFGInfo.GetDungeonInfo](#c_lfginfogetdungeoninfo) |  |  |
| ✅ | [C_LFGInfo.GetLFDLockStates](#c_lfginfogetlfdlockstates) | 1 value | 1 value |
| ✅ | [C_LFGInfo.GetLevelUpInstances](#c_lfginfogetlevelupinstances) |  |  |
| ✅ | [C_LFGInfo.GetRoleCheckDifficultyDetails](#c_lfginfogetrolecheckdifficultydetails) | 2 values | 2 values |
| ✅ | [C_LFGInfo.HideNameFromUI](#c_lfginfohidenamefromui) |  |  |
| ✅ | [C_LFGInfo.IsGroupFinderEnabled](#c_lfginfoisgroupfinderenabled) | 1 value | 1 value |
| ✅ | [C_LFGInfo.IsInLFGFollowerDungeon](#c_lfginfoisinlfgfollowerdungeon) | 1 value | 1 value |
| ✅ | [C_LFGInfo.IsInMatchmadeRaidWithoutRoleRequirements](#c_lfginfoisinmatchmaderaidwithoutrolerequirements) | 1 value | 1 value |
| ✅ | [C_LFGInfo.IsLFDEnabled](#c_lfginfoislfdenabled) | 1 value | 1 value |
| ✅ | [C_LFGInfo.IsLFGFollowerDungeon](#c_lfginfoislfgfollowerdungeon) |  |  |
| ✅ | [C_LFGInfo.IsLFREnabled](#c_lfginfoislfrenabled) | 1 value | 1 value |

### C_LFGInfo.AreCrossFactionGroupQueuesAllowed

`C_LFGInfo.AreCrossFactionGroupQueuesAllowed(lfgDungeonID: number) → areCrossFactionGroupQueuesAllowed: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUseGroupFinder

`C_LFGInfo.CanPlayerUseGroupFinder() → canUse: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUseLFD

`C_LFGInfo.CanPlayerUseLFD() → canUse: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUseLFR

`C_LFGInfo.CanPlayerUseLFR() → canUse: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUsePVP

`C_LFGInfo.CanPlayerUsePVP() → canUse: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUsePremadeGroup

`C_LFGInfo.CanPlayerUsePremadeGroup() → canUse: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUseScenarioFinder

`C_LFGInfo.CanPlayerUseScenarioFinder() → canUse: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.ConfirmLfgExpandSearch

`C_LFGInfo.ConfirmLfgExpandSearch()`

- Status: ✅ verified (function)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.DoesActivePartyMeetPremadeLaunchCount

`C_LFGInfo.DoesActivePartyMeetPremadeLaunchCount(lfgDungeonID: number) → doesActivePartyMeetPremadeLaunchCount: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.DoesCrossFactionQueueRequireFullPremade

`C_LFGInfo.DoesCrossFactionQueueRequireFullPremade(lfgDungeonID: number) → doesCrossFactionQueueRequireFullPremade: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetActiveLFGDungeonName

`C_LFGInfo.GetActiveLFGDungeonName() → name: string`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetAllEntriesForCategory

`C_LFGInfo.GetAllEntriesForCategory(category: luaIndex) → lfgDungeonIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetDungeonInfo

`C_LFGInfo.GetDungeonInfo(lfgDungeonID: number) → dungeonInfo: LFGDungeonInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetLFDLockStates

`C_LFGInfo.GetLFDLockStates() → lockInfo: LFGLockInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetLevelUpInstances

`C_LFGInfo.GetLevelUpInstances(currPlayerLevel: number, isRaid: bool) → instances: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetRoleCheckDifficultyDetails

`C_LFGInfo.GetRoleCheckDifficultyDetails() → maxLevel: number?, isLevelReduced: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `nil`, `boolean`
- Called in combat: returned 2 values: `nil`, `boolean`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.HideNameFromUI

`C_LFGInfo.HideNameFromUI(dungeonID: number) → shouldHide: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsGroupFinderEnabled

`C_LFGInfo.IsGroupFinderEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsInLFGFollowerDungeon

`C_LFGInfo.IsInLFGFollowerDungeon() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsInMatchmadeRaidWithoutRoleRequirements

`C_LFGInfo.IsInMatchmadeRaidWithoutRoleRequirements() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsLFDEnabled

`C_LFGInfo.IsLFDEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsLFGFollowerDungeon

`C_LFGInfo.IsLFGFollowerDungeon(dungeonID: number) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsLFREnabled

`C_LFGInfo.IsLFREnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LFGInfoDocumentation.lua`

## Events

### ISLAND_COMPLETED

- Status: ✅ verified
- Payload: `mapID: number`, `winner: number`
- fires synchronously (Blizzard's docs)

### LFG_BOOT_PROPOSAL_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_COMPLETION_REWARD

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_COOLDOWNS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 314 times (31 in combat); argument kinds: ``

### LFG_ENABLED_STATE_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_INVALID_ERROR_MESSAGE

- Status: ✅ verified
- Payload: `reason: number`, `subReason1: number`, `subReason2: number`
- fires synchronously (Blizzard's docs)

### LFG_LOCK_INFO_RECEIVED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 82 times (4 in combat); argument kinds: ``

### LFG_OFFER_CONTINUE

- Status: ✅ verified
- Payload: `name: cstring`, `lfgDungeonsID: number`, `typeID: number`
- fires synchronously (Blizzard's docs)

### LFG_OPEN_FROM_GOSSIP

- Status: ✅ verified
- Payload: `dungeonID: number`
- fires synchronously (Blizzard's docs)

### LFG_PROPOSAL_DONE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_PROPOSAL_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_PROPOSAL_SHOW

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_PROPOSAL_SUCCEEDED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_PROPOSAL_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_QUEUE_STATUS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_READY_CHECK_DECLINED

- Status: ✅ verified
- Payload: `name: cstring`
- fires synchronously (Blizzard's docs)

### LFG_READY_CHECK_HIDE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_READY_CHECK_PLAYER_IS_READY

- Status: ✅ verified
- Payload: `name: cstring`
- fires synchronously (Blizzard's docs)

### LFG_READY_CHECK_SHOW

- Status: ✅ verified
- Payload: `isRequeue: bool`
- fires synchronously (Blizzard's docs)

### LFG_READY_CHECK_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_ROLE_CHECK_DECLINED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_ROLE_CHECK_HIDE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_ROLE_CHECK_ROLE_CHOSEN

- Status: ✅ verified
- Payload: `name: cstring`, `isTank: bool`, `isHealer: bool`, `isDamage: bool`
- fires synchronously (Blizzard's docs)

### LFG_ROLE_CHECK_SHOW

- Status: ✅ verified
- Payload: `isRequeue: bool`
- fires synchronously (Blizzard's docs)

### LFG_ROLE_CHECK_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_ROLE_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_UPDATE_RANDOM_INFO

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 82 times (4 in combat); argument kinds: ``

### SHOW_LFG_EXPAND_SEARCH_PROMPT

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_LFG_LIST

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### WARFRONT_COMPLETED

- Status: ✅ verified
- Payload: `mapID: number`, `winner: number`
- fires synchronously (Blizzard's docs)

## Types

### LFGDungeonInfo

- Structure
  - `name`: string
  - `iconID`: fileID
  - `link`: string?

### LFGLockInfo

- Structure
  - `lfgID`: number
  - `reason`: number
  - `hideEntry`: bool
