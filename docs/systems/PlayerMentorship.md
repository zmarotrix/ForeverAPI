# PlayerMentorship

Namespace: `C_PlayerMentorship`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PlayerMentorship.GetMentorLevelRequirement](#c_playermentorshipgetmentorlevelrequirement) | 1 value | 1 value |
| ✅ | [C_PlayerMentorship.GetMentorRequirements](#c_playermentorshipgetmentorrequirements) | 3 values | 3 values |
| ✅ | [C_PlayerMentorship.GetMentorshipStatus](#c_playermentorshipgetmentorshipstatus) | 1 value | 1 value |
| ✅ | [C_PlayerMentorship.IsActivePlayerConsideredNewcomer](#c_playermentorshipisactiveplayerconsiderednewcomer) | 1 value | 1 value |
| ✅ | [C_PlayerMentorship.IsMentorRestricted](#c_playermentorshipismentorrestricted) | 1 value | 1 value |

### C_PlayerMentorship.GetMentorLevelRequirement

`C_PlayerMentorship.GetMentorLevelRequirement() → level: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.GetMentorRequirements

`C_PlayerMentorship.GetMentorRequirements() → achievementIDs: number[], optionalAchievementIDs: number[], optionalCompleteAtLeastCount: number`

- Status: ✅ verified (function)
- Called out of combat: returned 3 values: `table{}`, `table{}`, `number`
- Called in combat: returned 3 values: `table{}`, `table{}`, `number`
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.GetMentorshipStatus

`C_PlayerMentorship.GetMentorshipStatus(playerLocation: PlayerLocation) → status: PlayerMentorshipStatus`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `playerloc`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.IsActivePlayerConsideredNewcomer

`C_PlayerMentorship.IsActivePlayerConsideredNewcomer() → isConsideredNewcomer: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerMentorshipDocumentation.lua`

### C_PlayerMentorship.IsMentorRestricted

`C_PlayerMentorship.IsMentorRestricted() → isRestricted: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerMentorshipDocumentation.lua`

## Events

### MENTORSHIP_STATUS_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 61 times (0 in combat); argument kinds: ``

### NEWCOMER_GRADUATION

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
