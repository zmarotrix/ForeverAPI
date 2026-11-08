# AchievementInfo

Namespace: `C_AchievementInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_AchievementInfo.AreGuildAchievementsEnabled](#c_achievementinfoareguildachievementsenabled) |  |  |
| ❔ | [C_AchievementInfo.GetRewardItemID](#c_achievementinfogetrewarditemid) |  |  |
| ❔ | [C_AchievementInfo.GetSupercedingAchievements](#c_achievementinfogetsupercedingachievements) |  |  |
| ❔ | [C_AchievementInfo.IsGuildAchievement](#c_achievementinfoisguildachievement) |  |  |
| ❔ | [C_AchievementInfo.IsValidAchievement](#c_achievementinfoisvalidachievement) |  |  |
| ❔ | [C_AchievementInfo.SetPortraitTexture](#c_achievementinfosetportraittexture) |  |  |

### C_AchievementInfo.AreGuildAchievementsEnabled

`C_AchievementInfo.AreGuildAchievementsEnabled() → enabled: bool`

- Status: ❔ unverified
- Source: client docs `AchievementInfoDocumentation.lua`

### C_AchievementInfo.GetRewardItemID

`C_AchievementInfo.GetRewardItemID(achievementID: number) → rewardItemID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AchievementInfoDocumentation.lua`

### C_AchievementInfo.GetSupercedingAchievements

`C_AchievementInfo.GetSupercedingAchievements(achievementID: number) → supercedingAchievements: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AchievementInfoDocumentation.lua`

### C_AchievementInfo.IsGuildAchievement

`C_AchievementInfo.IsGuildAchievement(achievementId: number) → isGuild: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AchievementInfoDocumentation.lua`

### C_AchievementInfo.IsValidAchievement

`C_AchievementInfo.IsValidAchievement(achievementId: number) → isValidAchievement: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AchievementInfoDocumentation.lua`

### C_AchievementInfo.SetPortraitTexture

`C_AchievementInfo.SetPortraitTexture(textureObject: SimpleTexture)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AchievementInfoDocumentation.lua`

## Events

### ACHIEVEMENT_EARNED

- Status: ❔ unverified
- Payload: `achievementID: number`, `alreadyEarned: bool?`
- fires synchronously (Blizzard's docs)

### ACHIEVEMENT_PLAYER_NAME

- Status: ❔ unverified
- Payload: `achievementID: number`
- fires synchronously (Blizzard's docs)

### ACHIEVEMENT_SEARCH_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRITERIA_COMPLETE

- Status: ❔ unverified
- Payload: `criteriaID: number`
- fires synchronously (Blizzard's docs)

### CRITERIA_EARNED

- Status: ❔ unverified
- Payload: `achievementID: number`, `description: cstring`, `achievementAlreadyEarnedOnAccount: bool`
- fires synchronously (Blizzard's docs)

### CRITERIA_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### INSPECT_ACHIEVEMENT_READY

- Status: ❔ unverified
- Payload: `guid: WOWGUID`
- fires synchronously (Blizzard's docs)

### RECEIVED_ACHIEVEMENT_LIST

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### RECEIVED_ACHIEVEMENT_MEMBER_LIST

- Status: ❔ unverified
- Payload: `achievementID: number`
- fires synchronously (Blizzard's docs)

### TRACKED_ACHIEVEMENT_LIST_CHANGED

- Status: ❔ unverified
- Payload: `achievementID: number?`, `added: bool?`
- fires synchronously (Blizzard's docs)

### TRACKED_ACHIEVEMENT_UPDATE

- Status: ❔ unverified
- Payload: `achievementID: number`, `criteriaID: number?`, `elapsed: time_t?`, `duration: number?`
- fires synchronously (Blizzard's docs)
