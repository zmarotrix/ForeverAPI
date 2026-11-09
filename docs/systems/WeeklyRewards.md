# WeeklyRewards

Namespace: `C_WeeklyRewards`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_WeeklyRewards.AreRewardsForCurrentRewardPeriod](#c_weeklyrewardsarerewardsforcurrentrewardperiod) |  |  |
| ✅ | [C_WeeklyRewards.CanClaimRewards](#c_weeklyrewardscanclaimrewards) |  |  |
| ✅ | [C_WeeklyRewards.ClaimReward](#c_weeklyrewardsclaimreward) |  |  |
| ✅ | [C_WeeklyRewards.CloseInteraction](#c_weeklyrewardscloseinteraction) |  |  |
| ✅ | [C_WeeklyRewards.GetActivities](#c_weeklyrewardsgetactivities) | 1 value | 1 value |
| ✅ | [C_WeeklyRewards.GetActivityEncounterInfo](#c_weeklyrewardsgetactivityencounterinfo) |  |  |
| ✅ | [C_WeeklyRewards.GetConquestWeeklyProgress](#c_weeklyrewardsgetconquestweeklyprogress) | 1 value | 1 value |
| ✅ | [C_WeeklyRewards.GetDifficultyIDForActivityTier](#c_weeklyrewardsgetdifficultyidforactivitytier) |  |  |
| ✅ | [C_WeeklyRewards.GetExampleRewardItemHyperlinks](#c_weeklyrewardsgetexamplerewarditemhyperlinks) |  |  |
| ✅ | [C_WeeklyRewards.GetItemHyperlink](#c_weeklyrewardsgetitemhyperlink) |  |  |
| ✅ | [C_WeeklyRewards.GetNextActivitiesIncrease](#c_weeklyrewardsgetnextactivitiesincrease) |  |  |
| ✅ | [C_WeeklyRewards.GetNextMythicPlusIncrease](#c_weeklyrewardsgetnextmythicplusincrease) |  |  |
| ✅ | [C_WeeklyRewards.GetNumCompletedDungeonRuns](#c_weeklyrewardsgetnumcompleteddungeonruns) | 3 values | 3 values |
| ✅ | [C_WeeklyRewards.GetSortedProgressForActivity](#c_weeklyrewardsgetsortedprogressforactivity) |  |  |
| ✅ | [C_WeeklyRewards.HasAvailableRewards](#c_weeklyrewardshasavailablerewards) |  |  |
| ✅ | [C_WeeklyRewards.HasGeneratedRewards](#c_weeklyrewardshasgeneratedrewards) |  |  |
| ✅ | [C_WeeklyRewards.HasInteraction](#c_weeklyrewardshasinteraction) | 1 value | 1 value |
| ✅ | [C_WeeklyRewards.IsWeeklyChestRetired](#c_weeklyrewardsisweeklychestretired) | 1 value | 1 value |
| ✅ | [C_WeeklyRewards.OnUIInteract](#c_weeklyrewardsonuiinteract) |  |  |
| ✅ | [C_WeeklyRewards.ShouldShowFinalRetirementMessage](#c_weeklyrewardsshouldshowfinalretirementmessage) | 1 value | 1 value |
| ✅ | [C_WeeklyRewards.ShouldShowRetirementMessage](#c_weeklyrewardsshouldshowretirementmessage) | 1 value | 1 value |

### C_WeeklyRewards.AreRewardsForCurrentRewardPeriod

`C_WeeklyRewards.AreRewardsForCurrentRewardPeriod() → isCurrentPeriod: bool`

- Status: ✅ verified (function)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.CanClaimRewards

`C_WeeklyRewards.CanClaimRewards() → canClaimRewards: bool`

- Status: ✅ verified (function)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.ClaimReward

`C_WeeklyRewards.ClaimReward(id: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.CloseInteraction

`C_WeeklyRewards.CloseInteraction()`

- Status: ✅ verified (function)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.GetActivities

`C_WeeklyRewards.GetActivities(type: WeeklyRewardChestThresholdType?) → activities: WeeklyRewardActivityInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.GetActivityEncounterInfo

`C_WeeklyRewards.GetActivityEncounterInfo(type: WeeklyRewardChestThresholdType, index: luaIndex) → info: WeeklyRewardActivityEncounterInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.GetConquestWeeklyProgress

`C_WeeklyRewards.GetConquestWeeklyProgress() → weeklyProgress: ConquestWeeklyProgress`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{displayType=number,maxProgress=number,maxUnlocks=number,progress=number,sampleItemHyperlink=string,unlocksCompleted=number}`
- Called in combat: returned 1 value: `table{displayType=number,maxProgress=number,maxUnlocks=number,progress=number,sampleItemHyperlink=string,unlocksCompleted=number}`
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.GetDifficultyIDForActivityTier

`C_WeeklyRewards.GetDifficultyIDForActivityTier(activityTierID: number) → difficultyID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.GetExampleRewardItemHyperlinks

`C_WeeklyRewards.GetExampleRewardItemHyperlinks(id: number) → hyperlink: string, upgradeHyperlink: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.GetItemHyperlink

`C_WeeklyRewards.GetItemHyperlink(itemDBID: WeeklyRewardItemDBID) → hyperlink: cstring`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.GetNextActivitiesIncrease

`C_WeeklyRewards.GetNextActivitiesIncrease(activityTierID: number, level: number) → hasSeasonData: bool, nextActivityTierID: number?, nextLevel: number?, itemLevel: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.GetNextMythicPlusIncrease

`C_WeeklyRewards.GetNextMythicPlusIncrease(mythicPlusLevel: number) → hasSeasonData: bool, nextMythicPlusLevel: number?, itemLevel: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.GetNumCompletedDungeonRuns

`C_WeeklyRewards.GetNumCompletedDungeonRuns() → numHeroic: number, numMythic: number, numMythicPlus: number`

- Status: ✅ verified (function)
- Called out of combat: returned 3 values: `number`, `number`, `number`
- Called in combat: returned 3 values: `number`, `number`, `number`
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.GetSortedProgressForActivity

`C_WeeklyRewards.GetSortedProgressForActivity(type: WeeklyRewardChestThresholdType, combineSharedDifficulty: bool) → progress: WeeklyRewardActivityTierProgress[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.HasAvailableRewards

`C_WeeklyRewards.HasAvailableRewards() → hasAvailableRewards: bool`

- Status: ✅ verified (function)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.HasGeneratedRewards

`C_WeeklyRewards.HasGeneratedRewards() → hasGeneratedRewards: bool`

- Status: ✅ verified (function)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.HasInteraction

`C_WeeklyRewards.HasInteraction() → isInteracting: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.IsWeeklyChestRetired

`C_WeeklyRewards.IsWeeklyChestRetired() → isRetired: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.OnUIInteract

`C_WeeklyRewards.OnUIInteract()`

- Status: ✅ verified (function)
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.ShouldShowFinalRetirementMessage

`C_WeeklyRewards.ShouldShowFinalRetirementMessage() → showRetirementMessage: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `WeeklyRewardsDocumentation.lua`

### C_WeeklyRewards.ShouldShowRetirementMessage

`C_WeeklyRewards.ShouldShowRetirementMessage() → showRetirementMessage: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `WeeklyRewardsDocumentation.lua`

## Events

### WEEKLY_REWARDS_ITEM_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### WEEKLY_REWARDS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 5 times (0 in combat); argument kinds: ``

## Types

### ConquestProgressBarDisplayType

- Enumeration — ✅ verified
  - `FirstChest` = 0
  - `AdditionalChest` = 1
  - `Seasonal` = 2

### ConquestWeeklyProgress

- Structure
  - `progress`: number
  - `maxProgress`: number
  - `displayType`: ConquestProgressBarDisplayType
  - `unlocksCompleted`: number
  - `maxUnlocks`: number
  - `sampleItemHyperlink`: string

### WeeklyRewardActivityEncounterInfo

- Structure
  - `encounterID`: number
  - `bestDifficulty`: number
  - `uiOrder`: number
  - `instanceID`: number

### WeeklyRewardActivityInfo

- Structure
  - `type`: WeeklyRewardChestThresholdType
  - `index`: luaIndex
  - `threshold`: number
  - `progress`: number
  - `id`: number
  - `activityTierID`: number
  - `level`: number
  - `claimID`: number?
  - `raidString`: cstring?
  - `rewards`: WeeklyRewardActivityRewardInfo[]

### WeeklyRewardActivityRewardInfo

- Structure
  - `type`: CachedRewardType
  - `id`: number
  - `quantity`: number
  - `itemDBID`: WeeklyRewardItemDBID?

### WeeklyRewardActivityTierProgress

- Structure
  - `activityTierID`: number
  - `difficulty`: number
  - `numPoints`: number
