# PlayerMentorship

Namespace: `C_PlayerMentorship`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PlayerMentorship.GetMentorLevelRequirement](#c_playermentorshipgetmentorlevelrequirement) |  |  |
| ✅ | [C_PlayerMentorship.GetMentorRequirements](#c_playermentorshipgetmentorrequirements) |  |  |
| ✅ | [C_PlayerMentorship.GetMentorshipStatus](#c_playermentorshipgetmentorshipstatus) |  |  |
| ✅ | [C_PlayerMentorship.IsActivePlayerConsideredNewcomer](#c_playermentorshipisactiveplayerconsiderednewcomer) |  |  |
| ✅ | [C_PlayerMentorship.IsMentorRestricted](#c_playermentorshipismentorrestricted) |  |  |

### C_PlayerMentorship.GetMentorLevelRequirement

`C_PlayerMentorship.GetMentorLevelRequirement() → level: number?`

- Status: ✅ verified (function)
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.GetMentorRequirements

`C_PlayerMentorship.GetMentorRequirements() → achievementIDs: number[], optionalAchievementIDs: number[], optionalCompleteAtLeastCount: number`

- Status: ✅ verified (function)
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.GetMentorshipStatus

`C_PlayerMentorship.GetMentorshipStatus(playerLocation: PlayerLocation) → status: PlayerMentorshipStatus`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.IsActivePlayerConsideredNewcomer

`C_PlayerMentorship.IsActivePlayerConsideredNewcomer() → isConsideredNewcomer: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.IsMentorRestricted

`C_PlayerMentorship.IsMentorRestricted() → isRestricted: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerMentorshipDocumentation.lua`

## Events

### MENTORSHIP_STATUS_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### NEWCOMER_GRADUATION

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
