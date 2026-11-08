# MythicPlusInfo

Namespace: `C_MythicPlus`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_MythicPlus.GetCurrentAffixes](#c_mythicplusgetcurrentaffixes) | 0 values |  |
| ✅ | [C_MythicPlus.GetCurrentSeason](#c_mythicplusgetcurrentseason) | 1 value |  |
| ✅ | [C_MythicPlus.GetCurrentSeasonValues](#c_mythicplusgetcurrentseasonvalues) | 3 values |  |
| ✅ | [C_MythicPlus.GetCurrentUIDisplaySeason](#c_mythicplusgetcurrentuidisplayseason) | 1 value |  |
| ✅ | [C_MythicPlus.GetEndOfRunGearSequenceLevel](#c_mythicplusgetendofrungearsequencelevel) |  |  |
| ✅ | [C_MythicPlus.GetLastWeeklyBestInformation](#c_mythicplusgetlastweeklybestinformation) | 0 values |  |
| ✅ | [C_MythicPlus.GetOwnedKeystoneChallengeMapID](#c_mythicplusgetownedkeystonechallengemapid) | 0 values |  |
| ✅ | [C_MythicPlus.GetOwnedKeystoneLevel](#c_mythicplusgetownedkeystonelevel) | 0 values |  |
| ✅ | [C_MythicPlus.GetOwnedKeystoneMapID](#c_mythicplusgetownedkeystonemapid) | 0 values |  |
| ✅ | [C_MythicPlus.GetRewardLevelForDifficultyLevel](#c_mythicplusgetrewardlevelfordifficultylevel) |  |  |
| ✅ | [C_MythicPlus.GetRewardLevelFromKeystoneLevel](#c_mythicplusgetrewardlevelfromkeystonelevel) |  |  |
| ✅ | [C_MythicPlus.GetRunHistory](#c_mythicplusgetrunhistory) | 1 value |  |
| ✅ | [C_MythicPlus.GetSeasonBestAffixScoreInfoForMap](#c_mythicplusgetseasonbestaffixscoreinfoformap) |  |  |
| ✅ | [C_MythicPlus.GetSeasonBestForMap](#c_mythicplusgetseasonbestformap) |  |  |
| ✅ | [C_MythicPlus.GetSeasonBestMythicRatingFromThisExpansion](#c_mythicplusgetseasonbestmythicratingfromthisexpansion) | 2 values |  |
| ✅ | [C_MythicPlus.GetWeeklyBestForMap](#c_mythicplusgetweeklybestformap) |  |  |
| ✅ | [C_MythicPlus.GetWeeklyChestRewardLevel](#c_mythicplusgetweeklychestrewardlevel) |  |  |
| ✅ | [C_MythicPlus.IsMythicPlusActive](#c_mythicplusismythicplusactive) | 1 value |  |
| ✅ | [C_MythicPlus.RequestCurrentAffixes](#c_mythicplusrequestcurrentaffixes) |  |  |
| ✅ | [C_MythicPlus.RequestMapInfo](#c_mythicplusrequestmapinfo) |  |  |
| ✅ | [C_MythicPlus.RequestRewards](#c_mythicplusrequestrewards) |  |  |

### C_MythicPlus.GetCurrentAffixes

`C_MythicPlus.GetCurrentAffixes() → affixIDs: MythicPlusKeystoneAffix[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetCurrentSeason

`C_MythicPlus.GetCurrentSeason() → seasonID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetCurrentSeasonValues

`C_MythicPlus.GetCurrentSeasonValues() → displaySeasonID: number, milestoneSeasonID: number, rewardSeasonID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 3 values: `number`, `number`, `number`
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetCurrentUIDisplaySeason

`C_MythicPlus.GetCurrentUIDisplaySeason() → seasonID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetEndOfRunGearSequenceLevel

`C_MythicPlus.GetEndOfRunGearSequenceLevel(keystoneLevel: number) → sequenceLevel: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetLastWeeklyBestInformation

`C_MythicPlus.GetLastWeeklyBestInformation() → challengeMapId: number, level: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetOwnedKeystoneChallengeMapID

`C_MythicPlus.GetOwnedKeystoneChallengeMapID() → challengeMapID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetOwnedKeystoneLevel

`C_MythicPlus.GetOwnedKeystoneLevel() → keyStoneLevel: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetOwnedKeystoneMapID

`C_MythicPlus.GetOwnedKeystoneMapID() → mapID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetRewardLevelForDifficultyLevel

`C_MythicPlus.GetRewardLevelForDifficultyLevel(difficultyLevel: number) → weeklyRewardLevel: number, endOfRunRewardLevel: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetRewardLevelFromKeystoneLevel

`C_MythicPlus.GetRewardLevelFromKeystoneLevel(keystoneLevel: number) → rewardLevel: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetRunHistory

`C_MythicPlus.GetRunHistory(includePreviousWeeks: bool = False, includeIncompleteRuns: bool = False, currentSeasonOnly: bool = False) → runs: MythicPlusRunInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetSeasonBestAffixScoreInfoForMap

`C_MythicPlus.GetSeasonBestAffixScoreInfoForMap(mapChallengeModeID: number) → affixScores: MythicPlusAffixScoreInfo[], bestOverAllScore: number`

- Status: ✅ verified (function)
- Blizzard: Gets the active players best runs by the seasonal tracked affixes as well as their overall score for the current season.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetSeasonBestForMap

`C_MythicPlus.GetSeasonBestForMap(mapChallengeModeID: number) → intimeInfo: MapSeasonBestInfo?, overtimeInfo: MapSeasonBestInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetSeasonBestMythicRatingFromThisExpansion

`C_MythicPlus.GetSeasonBestMythicRatingFromThisExpansion() → bestSeasonScore: number, bestSeason: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 2 values: `number`, `number`
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetWeeklyBestForMap

`C_MythicPlus.GetWeeklyBestForMap(mapChallengeModeID: number) → durationSec: number, level: number, completionDate: CalendarTime, affixIDs: number[], members: MythicPlusMember[], dungeonScore: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.GetWeeklyChestRewardLevel

`C_MythicPlus.GetWeeklyChestRewardLevel() → currentWeekBestLevel: number, weeklyRewardLevel: number, nextDifficultyWeeklyRewardLevel: number, nextBestLevel: number`

- Status: ✅ verified (function)
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.IsMythicPlusActive

`C_MythicPlus.IsMythicPlusActive() → isMythicPlusActive: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.RequestCurrentAffixes

`C_MythicPlus.RequestCurrentAffixes()`

- Status: ✅ verified (function)
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.RequestMapInfo

`C_MythicPlus.RequestMapInfo()`

- Status: ✅ verified (function)
- Source: client docs `MythicPlusInfoDocumentation.lua`

### C_MythicPlus.RequestRewards

`C_MythicPlus.RequestRewards()`

- Status: ✅ verified (function)
- Source: client docs `MythicPlusInfoDocumentation.lua`

## Events

### MYTHIC_PLUS_CURRENT_AFFIX_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### MYTHIC_PLUS_NEW_WEEKLY_RECORD

- Status: ✅ verified
- Payload: `mapChallengeModeID: number`, `completionMilliseconds: number`, `level: number`
- fires synchronously (Blizzard's docs)

## Types

### MapSeasonBestInfo

- Structure
  - `durationSec`: number
  - `level`: number
  - `completionDate`: CalendarTime
  - `affixIDs`: number[]
  - `members`: MythicPlusMember[]
  - `dungeonScore`: number

### MythicPlusDate

- Structure
  - `year`: number
  - `month`: number
  - `day`: number
  - `hour`: number
  - `minute`: number
  - `weekday`: luaIndex

### MythicPlusKeystoneAffix

- Structure
  - `id`: number
  - `seasonID`: number

### MythicPlusMember

- Structure
  - `name`: string?
  - `specID`: number
  - `classID`: number

### MythicPlusRunInfo

- Structure
  - `mapChallengeModeID`: number
  - `level`: number
  - `thisWeek`: bool
  - `completed`: bool
  - `runScore`: number
  - `durationSec`: number
  - `completionDate`: CalendarTime
  - `season`: number

### SeasonTimeInfo

- Structure
  - `bestTime`: number
  - `lastTime`: number
  - `medal`: number
