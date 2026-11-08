# ChallengeModeInfo

Namespace: `C_ChallengeMode`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ChallengeMode.CanUseKeystoneInCurrentMap](#c_challengemodecanusekeystoneincurrentmap) |  |  |
| ✅ | [C_ChallengeMode.ClearKeystone](#c_challengemodeclearkeystone) |  |  |
| ✅ | [C_ChallengeMode.CloseKeystoneFrame](#c_challengemodeclosekeystoneframe) |  |  |
| ✅ | [C_ChallengeMode.GetActiveChallengeMapID](#c_challengemodegetactivechallengemapid) |  |  |
| ✅ | [C_ChallengeMode.GetActiveKeystoneInfo](#c_challengemodegetactivekeystoneinfo) |  |  |
| ✅ | [C_ChallengeMode.GetAffixInfo](#c_challengemodegetaffixinfo) |  |  |
| ✅ | [C_ChallengeMode.GetChallengeCompletionInfo](#c_challengemodegetchallengecompletioninfo) |  |  |
| ✅ | [C_ChallengeMode.GetDeathCount](#c_challengemodegetdeathcount) |  |  |
| ✅ | [C_ChallengeMode.GetDungeonScoreRarityColor](#c_challengemodegetdungeonscoreraritycolor) |  |  |
| ✅ | [C_ChallengeMode.GetGuildLeaders](#c_challengemodegetguildleaders) |  |  |
| ✅ | [C_ChallengeMode.GetKeystoneLevelRarityColor](#c_challengemodegetkeystonelevelraritycolor) |  |  |
| ✅ | [C_ChallengeMode.GetLeaverPenaltyWarningTimeLeft](#c_challengemodegetleaverpenaltywarningtimeleft) |  |  |
| ✅ | [C_ChallengeMode.GetMapScoreInfo](#c_challengemodegetmapscoreinfo) |  |  |
| ✅ | [C_ChallengeMode.GetMapTable](#c_challengemodegetmaptable) |  |  |
| ✅ | [C_ChallengeMode.GetMapUIInfo](#c_challengemodegetmapuiinfo) |  |  |
| ✅ | [C_ChallengeMode.GetOverallDungeonScore](#c_challengemodegetoveralldungeonscore) |  |  |
| ✅ | [C_ChallengeMode.GetPowerLevelDamageHealthMod](#c_challengemodegetpowerleveldamagehealthmod) |  |  |
| ✅ | [C_ChallengeMode.GetSlottedKeystoneInfo](#c_challengemodegetslottedkeystoneinfo) |  |  |
| ✅ | [C_ChallengeMode.GetSpecificDungeonOverallScoreRarityColor](#c_challengemodegetspecificdungeonoverallscoreraritycolor) |  |  |
| ✅ | [C_ChallengeMode.GetSpecificDungeonScoreRarityColor](#c_challengemodegetspecificdungeonscoreraritycolor) |  |  |
| ✅ | [C_ChallengeMode.GetStartTime](#c_challengemodegetstarttime) |  |  |
| ✅ | [C_ChallengeMode.HasSlottedKeystone](#c_challengemodehasslottedkeystone) |  |  |
| ✅ | [C_ChallengeMode.IsChallengeModeActive](#c_challengemodeischallengemodeactive) |  |  |
| ✅ | [C_ChallengeMode.IsChallengeModeResettable](#c_challengemodeischallengemoderesettable) |  |  |
| ✅ | [C_ChallengeMode.RemoveKeystone](#c_challengemoderemovekeystone) |  |  |
| ✅ | [C_ChallengeMode.RequestLeaders](#c_challengemoderequestleaders) |  |  |
| ✅ | [C_ChallengeMode.Reset](#c_challengemodereset) |  |  |
| ✅ | [C_ChallengeMode.SlotKeystone](#c_challengemodeslotkeystone) |  |  |
| ✅ | [C_ChallengeMode.StartChallengeMode](#c_challengemodestartchallengemode) |  |  |

### C_ChallengeMode.CanUseKeystoneInCurrentMap

`C_ChallengeMode.CanUseKeystoneInCurrentMap(itemLocation: ItemLocation) → canUse: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.ClearKeystone

`C_ChallengeMode.ClearKeystone()`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.CloseKeystoneFrame

`C_ChallengeMode.CloseKeystoneFrame()`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetActiveChallengeMapID

`C_ChallengeMode.GetActiveChallengeMapID() → mapChallengeModeID: number?`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetActiveKeystoneInfo

`C_ChallengeMode.GetActiveKeystoneInfo() → activeKeystoneLevel: number, activeAffixIDs: number[], wasActiveKeystoneCharged: bool`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetAffixInfo

`C_ChallengeMode.GetAffixInfo(affixID: number) → name: cstring, description: cstring, filedataid: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetChallengeCompletionInfo

`C_ChallengeMode.GetChallengeCompletionInfo() → info: ChallengeCompletionInfo`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetDeathCount

`C_ChallengeMode.GetDeathCount() → numDeaths: number, timeLost: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetDungeonScoreRarityColor

`C_ChallengeMode.GetDungeonScoreRarityColor(dungeonScore: number) → scoreColor: colorRGB`

- Status: ✅ verified (function)
- Blizzard: Returns a color value from the passed in overall season M+ rating.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetGuildLeaders

`C_ChallengeMode.GetGuildLeaders() → topAttempt: ChallengeModeGuildTopAttempt[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetKeystoneLevelRarityColor

`C_ChallengeMode.GetKeystoneLevelRarityColor(level: number) → levelScore: colorRGB`

- Status: ✅ verified (function)
- Blizzard: Returns a color value from the passed in keystone level.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetLeaverPenaltyWarningTimeLeft

`C_ChallengeMode.GetLeaverPenaltyWarningTimeLeft() → timeLeftSeconds: number`

- Status: ✅ verified (function)
- Blizzard: Returns how much time is left before player is automatically flagged as a leaver (and removed from the group) for exiting a restricted challenge mode instance
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetMapScoreInfo

`C_ChallengeMode.GetMapScoreInfo() → displayScores: MythicPlusRatingLinkInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetMapTable

`C_ChallengeMode.GetMapTable() → mapChallengeModeIDs: number[]`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetMapUIInfo

`C_ChallengeMode.GetMapUIInfo(mapChallengeModeID: number) → name: cstring, id: number, timeLimit: number, texture: number?, backgroundTexture: number, mapID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetOverallDungeonScore

`C_ChallengeMode.GetOverallDungeonScore() → overallDungeonScore: number`

- Status: ✅ verified (function)
- Blizzard: Gets the overall season mythic+ rating for the player.
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetPowerLevelDamageHealthMod

`C_ChallengeMode.GetPowerLevelDamageHealthMod(powerLevel: number) → damageMod: number, healthMod: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetSlottedKeystoneInfo

`C_ChallengeMode.GetSlottedKeystoneInfo() → mapChallengeModeID: number, affixIDs: number[], keystoneLevel: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetSpecificDungeonOverallScoreRarityColor

`C_ChallengeMode.GetSpecificDungeonOverallScoreRarityColor(specificDungeonOverallScore: number) → specificDungeonOverallScoreColor: colorRGB`

- Status: ✅ verified (function)
- Blizzard: Returns a color value from the passed in mythic+ rating from the combined affix scores for a specific dungeon
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetSpecificDungeonScoreRarityColor

`C_ChallengeMode.GetSpecificDungeonScoreRarityColor(specificDungeonScore: number) → specificDungeonScoreColor: colorRGB`

- Status: ✅ verified (function)
- Blizzard: Returns a color value from the passed in mythic+ rating for a specific dungeon.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.GetStartTime

`C_ChallengeMode.GetStartTime() → startTime: number`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.HasSlottedKeystone

`C_ChallengeMode.HasSlottedKeystone() → hasSlottedKeystone: bool`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.IsChallengeModeActive

`C_ChallengeMode.IsChallengeModeActive() → challengeModeActive: bool`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.IsChallengeModeResettable

`C_ChallengeMode.IsChallengeModeResettable() → canReset: bool`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.RemoveKeystone

`C_ChallengeMode.RemoveKeystone() → removalSuccessful: bool`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.RequestLeaders

`C_ChallengeMode.RequestLeaders(mapChallengeModeID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.Reset

`C_ChallengeMode.Reset()`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.SlotKeystone

`C_ChallengeMode.SlotKeystone()`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

### C_ChallengeMode.StartChallengeMode

`C_ChallengeMode.StartChallengeMode() → success: bool`

- Status: ✅ verified (function)
- Source: client docs `ChallengeModeInfoDocumentation.lua`

## Events

### CHALLENGE_MODE_COMPLETED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_COMPLETED_REWARDS

- Status: ✅ verified
- Payload: `mapID: number`, `medal: number`, `timeMS: number`, `money: number`, `rewards: ChallengeModeReward[]`
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_DEATH_COUNT_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_KEYSTONE_RECEPTABLE_OPEN

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_KEYSTONE_SLOTTED

- Status: ✅ verified
- Payload: `keystoneID: number`
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_LEADERBOARD_RESULT

- Status: ✅ verified
- Payload: `mapID: number`, `challengeModeID: number`, `page: number`, `results: MythicPlusLeaderboardResult[]`
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_LEADERS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_LEAVER_TIMER_ENDED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_LEAVER_TIMER_STARTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_MAPS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_MEMBER_INFO_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_NEW_RECORD

- Status: ✅ verified
- Payload: `mapID: number`, `timeMS: number`, `medal: number`
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_RESET

- Status: ✅ verified
- Payload: `mapID: number`
- fires synchronously (Blizzard's docs)

### CHALLENGE_MODE_START

- Status: ✅ verified
- Payload: `mapID: number`
- fires synchronously (Blizzard's docs)

## Types

### ChallengeCompletionInfo

- Structure
  - `mapChallengeModeID`: number
  - `level`: number
  - `time`: number
  - `onTime`: bool
  - `keystoneUpgradeLevels`: number
  - `practiceRun`: bool
  - `oldOverallDungeonScore`: number?
  - `newOverallDungeonScore`: number?
  - `isMapRecord`: bool
  - `isAffixRecord`: bool
  - `isEligibleForScore`: bool
  - `members`: ChallengeModeCompletionMemberInfo[]

### ChallengeModeBestTime

- Structure
  - `mapChallengeModeID`: number
  - `durationMs`: number
  - `members`: ChallengeModeBestTimeMember[]

### ChallengeModeBestTimeMember

- Structure
  - `name`: string
  - `classFileName`: cstring
  - `className`: cstring
  - `specializationID`: number

### ChallengeModeCompletionMemberInfo

- Structure
  - `memberGUID`: WOWGUID
  - `name`: string

### ChallengeModeGuildAttemptMember

- Structure
  - `name`: string
  - `classFileName`: cstring

### ChallengeModeGuildTopAttempt

- Structure
  - `name`: string
  - `classFileName`: cstring
  - `keystoneLevel`: number
  - `mapChallengeModeID`: number
  - `isYou`: bool
  - `members`: ChallengeModeGuildAttemptMember[]

### ChallengeModeReward

- Structure
  - `rewardID`: number
  - `displayInfoID`: number
  - `quantity`: number
  - `isCurrency`: bool
