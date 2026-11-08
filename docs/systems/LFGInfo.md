# LFGInfo

Namespace: `C_LFGInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_LFGInfo.AreCrossFactionGroupQueuesAllowed](#c_lfginfoarecrossfactiongroupqueuesallowed) |  |  |
| ❔ | [C_LFGInfo.CanPlayerUseGroupFinder](#c_lfginfocanplayerusegroupfinder) |  |  |
| ❔ | [C_LFGInfo.CanPlayerUseLFD](#c_lfginfocanplayeruselfd) |  |  |
| ❔ | [C_LFGInfo.CanPlayerUseLFR](#c_lfginfocanplayeruselfr) |  |  |
| ❔ | [C_LFGInfo.CanPlayerUsePVP](#c_lfginfocanplayerusepvp) |  |  |
| ❔ | [C_LFGInfo.CanPlayerUsePremadeGroup](#c_lfginfocanplayerusepremadegroup) |  |  |
| ❔ | [C_LFGInfo.CanPlayerUseScenarioFinder](#c_lfginfocanplayerusescenariofinder) |  |  |
| ❔ | [C_LFGInfo.ConfirmLfgExpandSearch](#c_lfginfoconfirmlfgexpandsearch) |  |  |
| ❔ | [C_LFGInfo.DoesActivePartyMeetPremadeLaunchCount](#c_lfginfodoesactivepartymeetpremadelaunchcount) |  |  |
| ❔ | [C_LFGInfo.DoesCrossFactionQueueRequireFullPremade](#c_lfginfodoescrossfactionqueuerequirefullpremade) |  |  |
| ❔ | [C_LFGInfo.GetActiveLFGDungeonName](#c_lfginfogetactivelfgdungeonname) |  |  |
| ❔ | [C_LFGInfo.GetAllEntriesForCategory](#c_lfginfogetallentriesforcategory) |  |  |
| ❔ | [C_LFGInfo.GetDungeonInfo](#c_lfginfogetdungeoninfo) |  |  |
| ❔ | [C_LFGInfo.GetLFDLockStates](#c_lfginfogetlfdlockstates) |  |  |
| ❔ | [C_LFGInfo.GetLevelUpInstances](#c_lfginfogetlevelupinstances) |  |  |
| ❔ | [C_LFGInfo.GetRoleCheckDifficultyDetails](#c_lfginfogetrolecheckdifficultydetails) |  |  |
| ❔ | [C_LFGInfo.HideNameFromUI](#c_lfginfohidenamefromui) |  |  |
| ❔ | [C_LFGInfo.IsGroupFinderEnabled](#c_lfginfoisgroupfinderenabled) |  |  |
| ❔ | [C_LFGInfo.IsInLFGFollowerDungeon](#c_lfginfoisinlfgfollowerdungeon) |  |  |
| ❔ | [C_LFGInfo.IsInMatchmadeRaidWithoutRoleRequirements](#c_lfginfoisinmatchmaderaidwithoutrolerequirements) |  |  |
| ❔ | [C_LFGInfo.IsLFDEnabled](#c_lfginfoislfdenabled) |  |  |
| ❔ | [C_LFGInfo.IsLFGFollowerDungeon](#c_lfginfoislfgfollowerdungeon) |  |  |
| ❔ | [C_LFGInfo.IsLFREnabled](#c_lfginfoislfrenabled) |  |  |

### C_LFGInfo.AreCrossFactionGroupQueuesAllowed

`C_LFGInfo.AreCrossFactionGroupQueuesAllowed(lfgDungeonID: number) → areCrossFactionGroupQueuesAllowed: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUseGroupFinder

`C_LFGInfo.CanPlayerUseGroupFinder() → canUse: bool, failureReason: string`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUseLFD

`C_LFGInfo.CanPlayerUseLFD() → canUse: bool, failureReason: string`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUseLFR

`C_LFGInfo.CanPlayerUseLFR() → canUse: bool, failureReason: string`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUsePVP

`C_LFGInfo.CanPlayerUsePVP() → canUse: bool, failureReason: string`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUsePremadeGroup

`C_LFGInfo.CanPlayerUsePremadeGroup() → canUse: bool, failureReason: string`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.CanPlayerUseScenarioFinder

`C_LFGInfo.CanPlayerUseScenarioFinder() → canUse: bool, failureReason: string`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.ConfirmLfgExpandSearch

`C_LFGInfo.ConfirmLfgExpandSearch()`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.DoesActivePartyMeetPremadeLaunchCount

`C_LFGInfo.DoesActivePartyMeetPremadeLaunchCount(lfgDungeonID: number) → doesActivePartyMeetPremadeLaunchCount: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.DoesCrossFactionQueueRequireFullPremade

`C_LFGInfo.DoesCrossFactionQueueRequireFullPremade(lfgDungeonID: number) → doesCrossFactionQueueRequireFullPremade: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetActiveLFGDungeonName

`C_LFGInfo.GetActiveLFGDungeonName() → name: string`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetAllEntriesForCategory

`C_LFGInfo.GetAllEntriesForCategory(category: luaIndex) → lfgDungeonIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetDungeonInfo

`C_LFGInfo.GetDungeonInfo(lfgDungeonID: number) → dungeonInfo: LFGDungeonInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetLFDLockStates

`C_LFGInfo.GetLFDLockStates() → lockInfo: LFGLockInfo[]`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetLevelUpInstances

`C_LFGInfo.GetLevelUpInstances(currPlayerLevel: number, isRaid: bool) → instances: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.GetRoleCheckDifficultyDetails

`C_LFGInfo.GetRoleCheckDifficultyDetails() → maxLevel: number?, isLevelReduced: bool`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.HideNameFromUI

`C_LFGInfo.HideNameFromUI(dungeonID: number) → shouldHide: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsGroupFinderEnabled

`C_LFGInfo.IsGroupFinderEnabled() → enabled: bool`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsInLFGFollowerDungeon

`C_LFGInfo.IsInLFGFollowerDungeon() → result: bool`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsInMatchmadeRaidWithoutRoleRequirements

`C_LFGInfo.IsInMatchmadeRaidWithoutRoleRequirements() → result: bool`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsLFDEnabled

`C_LFGInfo.IsLFDEnabled() → enabled: bool`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsLFGFollowerDungeon

`C_LFGInfo.IsLFGFollowerDungeon(dungeonID: number) → result: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LFGInfoDocumentation.lua`

### C_LFGInfo.IsLFREnabled

`C_LFGInfo.IsLFREnabled() → enabled: bool`

- Status: ❔ unverified
- Source: client docs `LFGInfoDocumentation.lua`

## Events

### ISLAND_COMPLETED

- Status: ❔ unverified
- Payload: `mapID: number`, `winner: number`
- fires synchronously (Blizzard's docs)

### LFG_BOOT_PROPOSAL_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_COMPLETION_REWARD

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_COOLDOWNS_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_ENABLED_STATE_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_INVALID_ERROR_MESSAGE

- Status: ❔ unverified
- Payload: `reason: number`, `subReason1: number`, `subReason2: number`
- fires synchronously (Blizzard's docs)

### LFG_LOCK_INFO_RECEIVED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_OFFER_CONTINUE

- Status: ❔ unverified
- Payload: `name: cstring`, `lfgDungeonsID: number`, `typeID: number`
- fires synchronously (Blizzard's docs)

### LFG_OPEN_FROM_GOSSIP

- Status: ❔ unverified
- Payload: `dungeonID: number`
- fires synchronously (Blizzard's docs)

### LFG_PROPOSAL_DONE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_PROPOSAL_FAILED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_PROPOSAL_SHOW

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_PROPOSAL_SUCCEEDED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_PROPOSAL_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_QUEUE_STATUS_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_READY_CHECK_DECLINED

- Status: ❔ unverified
- Payload: `name: cstring`
- fires synchronously (Blizzard's docs)

### LFG_READY_CHECK_HIDE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_READY_CHECK_PLAYER_IS_READY

- Status: ❔ unverified
- Payload: `name: cstring`
- fires synchronously (Blizzard's docs)

### LFG_READY_CHECK_SHOW

- Status: ❔ unverified
- Payload: `isRequeue: bool`
- fires synchronously (Blizzard's docs)

### LFG_READY_CHECK_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_ROLE_CHECK_DECLINED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_ROLE_CHECK_HIDE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_ROLE_CHECK_ROLE_CHOSEN

- Status: ❔ unverified
- Payload: `name: cstring`, `isTank: bool`, `isHealer: bool`, `isDamage: bool`
- fires synchronously (Blizzard's docs)

### LFG_ROLE_CHECK_SHOW

- Status: ❔ unverified
- Payload: `isRequeue: bool`
- fires synchronously (Blizzard's docs)

### LFG_ROLE_CHECK_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_ROLE_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LFG_UPDATE_RANDOM_INFO

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHOW_LFG_EXPAND_SEARCH_PROMPT

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_LFG_LIST

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### WARFRONT_COMPLETED

- Status: ❔ unverified
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
