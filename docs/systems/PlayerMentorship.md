# PlayerMentorship

Namespace: `C_PlayerMentorship`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_PlayerMentorship.GetMentorLevelRequirement](#c_playermentorshipgetmentorlevelrequirement) |  |  |
| ❔ | [C_PlayerMentorship.GetMentorRequirements](#c_playermentorshipgetmentorrequirements) |  |  |
| ❔ | [C_PlayerMentorship.GetMentorshipStatus](#c_playermentorshipgetmentorshipstatus) |  |  |
| ❔ | [C_PlayerMentorship.IsActivePlayerConsideredNewcomer](#c_playermentorshipisactiveplayerconsiderednewcomer) |  |  |
| ❔ | [C_PlayerMentorship.IsMentorRestricted](#c_playermentorshipismentorrestricted) |  |  |

### C_PlayerMentorship.GetMentorLevelRequirement

`C_PlayerMentorship.GetMentorLevelRequirement() → level: number?`

- Status: ❔ unverified
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.GetMentorRequirements

`C_PlayerMentorship.GetMentorRequirements() → achievementIDs: number[], optionalAchievementIDs: number[], optionalCompleteAtLeastCount: number`

- Status: ❔ unverified
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.GetMentorshipStatus

`C_PlayerMentorship.GetMentorshipStatus(playerLocation: PlayerLocation) → status: PlayerMentorshipStatus`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.IsActivePlayerConsideredNewcomer

`C_PlayerMentorship.IsActivePlayerConsideredNewcomer() → isConsideredNewcomer: bool`

- Status: ❔ unverified
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.IsMentorRestricted

`C_PlayerMentorship.IsMentorRestricted() → isRestricted: bool`

- Status: ❔ unverified
- Source: client docs `PlayerMentorshipDocumentation.lua`

## Events

### MENTORSHIP_STATUS_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### NEWCOMER_GRADUATION

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
