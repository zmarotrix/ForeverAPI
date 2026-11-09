# RecruitAFriend

Namespace: `C_RecruitAFriend`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_RecruitAFriend.CanSummonFriend](#c_recruitafriendcansummonfriend) | 2 values | 2 values |
| ✅ | [C_RecruitAFriend.ClaimActivityReward](#c_recruitafriendclaimactivityreward) |  |  |
| ✅ | [C_RecruitAFriend.ClaimNextReward](#c_recruitafriendclaimnextreward) |  |  |
| ✅ | [C_RecruitAFriend.GenerateRecruitmentLink](#c_recruitafriendgeneraterecruitmentlink) |  |  |
| ✅ | [C_RecruitAFriend.GetRAFInfo](#c_recruitafriendgetrafinfo) | 1 value | 1 value |
| ✅ | [C_RecruitAFriend.GetRAFSystemInfo](#c_recruitafriendgetrafsysteminfo) | 1 value | 1 value |
| ✅ | [C_RecruitAFriend.GetRecruitActivityRequirementsText](#c_recruitafriendgetrecruitactivityrequirementstext) |  |  |
| ✅ | [C_RecruitAFriend.GetRecruitInfo](#c_recruitafriendgetrecruitinfo) | 2 values | 2 values |
| ✅ | [C_RecruitAFriend.GetSummonFriendCooldown](#c_recruitafriendgetsummonfriendcooldown) | 3 values | 3 values |
| ✅ | [C_RecruitAFriend.IsRecruitAFriendLinked](#c_recruitafriendisrecruitafriendlinked) | 1 value | 1 value |
| ✅ | [C_RecruitAFriend.IsRecruitingEnabled](#c_recruitafriendisrecruitingenabled) | 1 value | 1 value |
| ✅ | [C_RecruitAFriend.IsSystemEnabled](#c_recruitafriendissystemenabled) | 1 value | 1 value |
| ✅ | [C_RecruitAFriend.IsSystemSupported](#c_recruitafriendissystemsupported) | 1 value | 1 value |
| ✅ | [C_RecruitAFriend.RemoveRAFRecruit](#c_recruitafriendremoverafrecruit) |  |  |
| ✅ | [C_RecruitAFriend.RequestUpdatedRecruitmentInfo](#c_recruitafriendrequestupdatedrecruitmentinfo) |  |  |
| ✅ | [C_RecruitAFriend.SummonFriend](#c_recruitafriendsummonfriend) |  |  |

### C_RecruitAFriend.CanSummonFriend

`C_RecruitAFriend.CanSummonFriend(guid: WOWGUID) → canSummon: bool, reason: RecruitAFriendFailure`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 2 values: `boolean`, `number`
- Called in combat: returned 2 values: `boolean`, `number`
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.ClaimActivityReward

`C_RecruitAFriend.ClaimActivityReward(activityID: number, acceptanceID: RecruitAcceptanceID) → success: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.ClaimNextReward

`C_RecruitAFriend.ClaimNextReward(rafVersion: RecruitAFriendRewardsVersion?) → success: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GenerateRecruitmentLink

`C_RecruitAFriend.GenerateRecruitmentLink() → success: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GetRAFInfo

`C_RecruitAFriend.GetRAFInfo() → info: RafInfo`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{claimInProgress=boolean,recruits=table,versions=table}`
- Called in combat: returned 1 value: `table{claimInProgress=boolean,recruits=table,versions=table}`
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GetRAFSystemInfo

`C_RecruitAFriend.GetRAFSystemInfo() → systemInfo: RafSystemInfo`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{daysInCycle=number,maxRecruitMonths=number,maxRecruitmentUses=number,maxRecruits=number}`
- Called in combat: returned 1 value: `table{daysInCycle=number,maxRecruitMonths=number,maxRecruitmentUses=number,maxRecruits=number}`
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GetRecruitActivityRequirementsText

`C_RecruitAFriend.GetRecruitActivityRequirementsText(activityID: number, acceptanceID: RecruitAcceptanceID) → requirementsText: string[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GetRecruitInfo

`C_RecruitAFriend.GetRecruitInfo() → active: bool, faction: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `number`
- Called in combat: returned 2 values: `boolean`, `number`
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GetSummonFriendCooldown

`C_RecruitAFriend.GetSummonFriendCooldown() → startTimeSeconds: number, durationSeconds: number, enableCooldownTimer: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 3 values: `number`, `number`, `boolean`
- Called in combat: returned 3 values: `number`, `number`, `boolean`
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.IsRecruitAFriendLinked

`C_RecruitAFriend.IsRecruitAFriendLinked(guid: WOWGUID) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.IsRecruitingEnabled

`C_RecruitAFriend.IsRecruitingEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.IsSystemEnabled

`C_RecruitAFriend.IsSystemEnabled() → isSystemEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.IsSystemSupported

`C_RecruitAFriend.IsSystemSupported() → isSystemSupported: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.RemoveRAFRecruit

`C_RecruitAFriend.RemoveRAFRecruit(wowAccountGUID: WOWGUID) → success: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.RequestUpdatedRecruitmentInfo

`C_RecruitAFriend.RequestUpdatedRecruitmentInfo() → success: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.SummonFriend

`C_RecruitAFriend.SummonFriend(target: WOWGUID, name: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

## Events

### RAF_INFO_UPDATED

- Status: ✅ verified
- Payload: `info: RafInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 5 times (0 in combat); argument kinds: `t`

### RAF_RECRUITING_ENABLED_STATUS

- Status: ✅ verified
- Payload: `enabled: bool`
- fires synchronously (Blizzard's docs)

### RAF_REWARD_CLAIM_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### RAF_SYSTEM_ENABLED_STATUS

- Status: ✅ verified
- Payload: `enabled: bool`
- fires synchronously (Blizzard's docs)

### RAF_SYSTEM_INFO_UPDATED

- Status: ✅ verified
- Payload: `systemInfo: RafSystemInfo`
- fires synchronously (Blizzard's docs)

## Types

### RafAppearanceInfo

- Structure
  - `appearanceID`: number

### RafAppearanceSetInfo

- Structure
  - `setID`: number
  - `setName`: string
  - `appearanceIDs`: number[]

### RafIllusionInfo

- Structure
  - `spellItemEnchantmentID`: number

### RafInfo

- Structure
  - `versions`: RafVersionInfo[]
  - `recruitmentInfo`: RafRecruitmentinfo?
  - `recruits`: RafRecruit[]
  - `claimInProgress`: bool

### RafMonthCount

- Structure
  - `lifetimeMonths`: number
  - `spentMonths`: number
  - `availableMonths`: number

### RafMountInfo

- Structure
  - `spellID`: number
  - `mountID`: number

### RafPetInfo

- Structure
  - `creatureID`: number
  - `speciesID`: number
  - `displayID`: number
  - `speciesName`: string
  - `description`: string

### RafRecruit

- Structure
  - `bnetAccountID`: number
  - `wowAccountGUID`: WOWGUID
  - `battleTag`: string
  - `monthsRemaining`: number
  - `subStatus`: RafRecruitSubStatus
  - `acceptanceID`: RecruitAcceptanceID
  - `versionRecruited`: RecruitAFriendRewardsVersion
  - `activities`: RafRecruitActivity[]

### RafRecruitActivity

- Structure
  - `activityID`: number
  - `rewardQuestID`: number
  - `state`: RafRecruitActivityState

### RafRecruitActivityState

- Enumeration — ✅ verified
  - `Incomplete` = 0
  - `Complete` = 1
  - `RewardClaimed` = 2

### RafRecruitSubStatus

- Enumeration — ✅ verified
  - `Trial` = 0
  - `Active` = 1
  - `Inactive` = 2

### RafRecruitmentinfo

- Structure
  - `recruitmentCode`: string
  - `recruitmentURL`: string
  - `expireTime`: number
  - `remainingTimeSeconds`: number
  - `totalUses`: number
  - `remainingUses`: number
  - `sourceRealm`: string
  - `sourceFaction`: string

### RafReward

- Structure
  - `rewardID`: number
  - `rafVersion`: RecruitAFriendRewardsVersion
  - `itemID`: number
  - `rewardType`: RafRewardType
  - `petInfo`: RafPetInfo?
  - `mountInfo`: RafMountInfo?
  - `appearanceInfo`: RafAppearanceInfo?
  - `titleInfo`: RafTitleInfo?
  - `appearanceSetInfo`: RafAppearanceSetInfo?
  - `illusionInfo`: RafIllusionInfo?
  - `canClaim`: bool
  - `claimed`: bool
  - `canAfford`: bool
  - `repeatable`: bool
  - `repeatableClaimCount`: number
  - `monthsRequired`: number
  - `monthCost`: number
  - `availableInMonths`: number
  - `iconID`: fileID

### RafRewardType

- Enumeration — ✅ verified
  - `Pet` = 0
  - `Mount` = 1
  - `Appearance` = 2
  - `Title` = 3
  - `GameTime` = 4
  - `AppearanceSet` = 5
  - `Illusion` = 6
  - `Invalid` = 7

### RafSystemInfo

- Structure
  - `maxRecruits`: number
  - `maxRecruitMonths`: number
  - `maxRecruitmentUses`: number
  - `daysInCycle`: number

### RafTitleInfo

- Structure
  - `titleMaskID`: number

### RafVersionInfo

- Structure
  - `rafVersion`: RecruitAFriendRewardsVersion
  - `monthCount`: RafMonthCount
  - `rewards`: RafReward[]
  - `nextReward`: RafReward?
  - `numAffordableRewards`: number
  - `numRecruits`: number
