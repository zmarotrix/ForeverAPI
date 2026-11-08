# RecruitAFriend

Namespace: `C_RecruitAFriend`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_RecruitAFriend.CanSummonFriend](#c_recruitafriendcansummonfriend) |  |  |
| ❔ | [C_RecruitAFriend.ClaimActivityReward](#c_recruitafriendclaimactivityreward) |  |  |
| ❔ | [C_RecruitAFriend.ClaimNextReward](#c_recruitafriendclaimnextreward) |  |  |
| ❔ | [C_RecruitAFriend.GenerateRecruitmentLink](#c_recruitafriendgeneraterecruitmentlink) |  |  |
| ❔ | [C_RecruitAFriend.GetRAFInfo](#c_recruitafriendgetrafinfo) |  |  |
| ❔ | [C_RecruitAFriend.GetRAFSystemInfo](#c_recruitafriendgetrafsysteminfo) |  |  |
| ❔ | [C_RecruitAFriend.GetRecruitActivityRequirementsText](#c_recruitafriendgetrecruitactivityrequirementstext) |  |  |
| ❔ | [C_RecruitAFriend.GetRecruitInfo](#c_recruitafriendgetrecruitinfo) |  |  |
| ❔ | [C_RecruitAFriend.GetSummonFriendCooldown](#c_recruitafriendgetsummonfriendcooldown) |  |  |
| ❔ | [C_RecruitAFriend.IsRecruitAFriendLinked](#c_recruitafriendisrecruitafriendlinked) |  |  |
| ❔ | [C_RecruitAFriend.IsRecruitingEnabled](#c_recruitafriendisrecruitingenabled) |  |  |
| ❔ | [C_RecruitAFriend.IsSystemEnabled](#c_recruitafriendissystemenabled) |  |  |
| ❔ | [C_RecruitAFriend.IsSystemSupported](#c_recruitafriendissystemsupported) |  |  |
| ❔ | [C_RecruitAFriend.RemoveRAFRecruit](#c_recruitafriendremoverafrecruit) |  |  |
| ❔ | [C_RecruitAFriend.RequestUpdatedRecruitmentInfo](#c_recruitafriendrequestupdatedrecruitmentinfo) |  |  |
| ❔ | [C_RecruitAFriend.SummonFriend](#c_recruitafriendsummonfriend) |  |  |

### C_RecruitAFriend.CanSummonFriend

`C_RecruitAFriend.CanSummonFriend(guid: WOWGUID) → canSummon: bool, reason: RecruitAFriendFailure`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.ClaimActivityReward

`C_RecruitAFriend.ClaimActivityReward(activityID: number, acceptanceID: RecruitAcceptanceID) → success: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.ClaimNextReward

`C_RecruitAFriend.ClaimNextReward(rafVersion: RecruitAFriendRewardsVersion?) → success: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GenerateRecruitmentLink

`C_RecruitAFriend.GenerateRecruitmentLink() → success: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GetRAFInfo

`C_RecruitAFriend.GetRAFInfo() → info: RafInfo`

- Status: ❔ unverified
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GetRAFSystemInfo

`C_RecruitAFriend.GetRAFSystemInfo() → systemInfo: RafSystemInfo`

- Status: ❔ unverified
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GetRecruitActivityRequirementsText

`C_RecruitAFriend.GetRecruitActivityRequirementsText(activityID: number, acceptanceID: RecruitAcceptanceID) → requirementsText: string[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GetRecruitInfo

`C_RecruitAFriend.GetRecruitInfo() → active: bool, faction: number`

- Status: ❔ unverified
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.GetSummonFriendCooldown

`C_RecruitAFriend.GetSummonFriendCooldown() → startTimeSeconds: number, durationSeconds: number, enableCooldownTimer: bool`

- Status: ❔ unverified
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.IsRecruitAFriendLinked

`C_RecruitAFriend.IsRecruitAFriendLinked(guid: WOWGUID) → result: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.IsRecruitingEnabled

`C_RecruitAFriend.IsRecruitingEnabled() → enabled: bool`

- Status: ❔ unverified
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.IsSystemEnabled

`C_RecruitAFriend.IsSystemEnabled() → isSystemEnabled: bool`

- Status: ❔ unverified
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.IsSystemSupported

`C_RecruitAFriend.IsSystemSupported() → isSystemSupported: bool`

- Status: ❔ unverified
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.RemoveRAFRecruit

`C_RecruitAFriend.RemoveRAFRecruit(wowAccountGUID: WOWGUID) → success: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.RequestUpdatedRecruitmentInfo

`C_RecruitAFriend.RequestUpdatedRecruitmentInfo() → success: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

### C_RecruitAFriend.SummonFriend

`C_RecruitAFriend.SummonFriend(target: WOWGUID, name: cstring)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecruitAFriendDocumentation.lua`

## Events

### RAF_INFO_UPDATED

- Status: ❔ unverified
- Payload: `info: RafInfo`
- fires synchronously (Blizzard's docs)

### RAF_RECRUITING_ENABLED_STATUS

- Status: ❔ unverified
- Payload: `enabled: bool`
- fires synchronously (Blizzard's docs)

### RAF_REWARD_CLAIM_FAILED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### RAF_SYSTEM_ENABLED_STATUS

- Status: ❔ unverified
- Payload: `enabled: bool`
- fires synchronously (Blizzard's docs)

### RAF_SYSTEM_INFO_UPDATED

- Status: ❔ unverified
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

- Enumeration — ❔ unverified
  - `Incomplete` = 0
  - `Complete` = 1
  - `RewardClaimed` = 2

### RafRecruitSubStatus

- Enumeration — ❔ unverified
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

- Enumeration — ❔ unverified
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
