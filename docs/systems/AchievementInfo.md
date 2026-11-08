# AchievementInfo

Namespace: `C_AchievementInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AchievementInfo.AreGuildAchievementsEnabled](#c_achievementinfoareguildachievementsenabled) | 1 value | 1 value |
| ✅ | [C_AchievementInfo.GetRewardItemID](#c_achievementinfogetrewarditemid) |  |  |
| ✅ | [C_AchievementInfo.GetSupercedingAchievements](#c_achievementinfogetsupercedingachievements) |  |  |
| ✅ | [C_AchievementInfo.IsGuildAchievement](#c_achievementinfoisguildachievement) |  |  |
| ✅ | [C_AchievementInfo.IsValidAchievement](#c_achievementinfoisvalidachievement) |  |  |
| ✅ | [C_AchievementInfo.SetPortraitTexture](#c_achievementinfosetportraittexture) |  |  |

### C_AchievementInfo.AreGuildAchievementsEnabled

`C_AchievementInfo.AreGuildAchievementsEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `AchievementInfoDocumentation.lua`

### C_AchievementInfo.GetRewardItemID

`C_AchievementInfo.GetRewardItemID(achievementID: number) → rewardItemID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AchievementInfoDocumentation.lua`

### C_AchievementInfo.GetSupercedingAchievements

`C_AchievementInfo.GetSupercedingAchievements(achievementID: number) → supercedingAchievements: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AchievementInfoDocumentation.lua`

### C_AchievementInfo.IsGuildAchievement

`C_AchievementInfo.IsGuildAchievement(achievementId: number) → isGuild: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AchievementInfoDocumentation.lua`

### C_AchievementInfo.IsValidAchievement

`C_AchievementInfo.IsValidAchievement(achievementId: number) → isValidAchievement: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AchievementInfoDocumentation.lua`

### C_AchievementInfo.SetPortraitTexture

`C_AchievementInfo.SetPortraitTexture(textureObject: SimpleTexture)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AchievementInfoDocumentation.lua`

## Events

### ACHIEVEMENT_EARNED

- Status: ✅ verified
- Payload: `achievementID: number`, `alreadyEarned: bool?`
- fires synchronously (Blizzard's docs)

### ACHIEVEMENT_PLAYER_NAME

- Status: ✅ verified
- Payload: `achievementID: number`
- fires synchronously (Blizzard's docs)

### ACHIEVEMENT_SEARCH_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRITERIA_COMPLETE

- Status: ✅ verified
- Payload: `criteriaID: number`
- fires synchronously (Blizzard's docs)

### CRITERIA_EARNED

- Status: ✅ verified
- Payload: `achievementID: number`, `description: cstring`, `achievementAlreadyEarnedOnAccount: bool`
- fires synchronously (Blizzard's docs)

### CRITERIA_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 102 times (87 in combat); argument kinds: ``

### INSPECT_ACHIEVEMENT_READY

- Status: ✅ verified
- Payload: `guid: WOWGUID`
- fires synchronously (Blizzard's docs)

### RECEIVED_ACHIEVEMENT_LIST

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 4 times (0 in combat); argument kinds: ``

### RECEIVED_ACHIEVEMENT_MEMBER_LIST

- Status: ✅ verified
- Payload: `achievementID: number`
- fires synchronously (Blizzard's docs)

### TRACKED_ACHIEVEMENT_LIST_CHANGED

- Status: ✅ verified
- Payload: `achievementID: number?`, `added: bool?`
- fires synchronously (Blizzard's docs)

### TRACKED_ACHIEVEMENT_UPDATE

- Status: ✅ verified
- Payload: `achievementID: number`, `criteriaID: number?`, `elapsed: time_t?`, `duration: number?`
- fires synchronously (Blizzard's docs)
