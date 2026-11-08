# PerksActivities

Namespace: `C_PerksActivities`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PerksActivities.AddTrackedPerksActivity](#c_perksactivitiesaddtrackedperksactivity) |  |  |
| ✅ | [C_PerksActivities.ClearPerksActivitiesPendingCompletion](#c_perksactivitiesclearperksactivitiespendingcompletion) |  |  |
| ✅ | [C_PerksActivities.GetAllPerksActivityTags](#c_perksactivitiesgetallperksactivitytags) | 1 value | 1 value |
| ✅ | [C_PerksActivities.GetPerksActivitiesInfo](#c_perksactivitiesgetperksactivitiesinfo) | 1 value | 1 value |
| ✅ | [C_PerksActivities.GetPerksActivitiesPendingCompletion](#c_perksactivitiesgetperksactivitiespendingcompletion) | 1 value | 1 value |
| ✅ | [C_PerksActivities.GetPerksActivityChatLink](#c_perksactivitiesgetperksactivitychatlink) |  |  |
| ✅ | [C_PerksActivities.GetPerksActivityInfo](#c_perksactivitiesgetperksactivityinfo) |  |  |
| ✅ | [C_PerksActivities.GetPerksUIThemePrefix](#c_perksactivitiesgetperksuithemeprefix) | 1 value | 1 value |
| ✅ | [C_PerksActivities.GetTrackedPerksActivities](#c_perksactivitiesgettrackedperksactivities) | 1 value | 1 value |
| ✅ | [C_PerksActivities.RemoveTrackedPerksActivity](#c_perksactivitiesremovetrackedperksactivity) |  |  |

### C_PerksActivities.AddTrackedPerksActivity

`C_PerksActivities.AddTrackedPerksActivity(perksActivityID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.ClearPerksActivitiesPendingCompletion

`C_PerksActivities.ClearPerksActivitiesPendingCompletion()`

- Status: ✅ verified (function)
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetAllPerksActivityTags

`C_PerksActivities.GetAllPerksActivityTags() → tags: PerksActivityTags`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{tagName=table}`
- Called in combat: returned 1 value: `table{tagName=table}`
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetPerksActivitiesInfo

`C_PerksActivities.GetPerksActivitiesInfo() → info: PerksActivitiesInfo`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{activePerksMonth=number,activities=table,displayMonthName=string,secondsRemaining=number,thresholds=table}`
- Called in combat: returned 1 value: `table{activePerksMonth=number,activities=table,displayMonthName=string,secondsRemaining=number,thresholds=table}`
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetPerksActivitiesPendingCompletion

`C_PerksActivities.GetPerksActivitiesPendingCompletion() → pending: PerksActivitiesPending`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{pendingIDs=table}`
- Called in combat: returned 1 value: `table{pendingIDs=table}`
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetPerksActivityChatLink

`C_PerksActivities.GetPerksActivityChatLink(perksActivityID: number) → link: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetPerksActivityInfo

`C_PerksActivities.GetPerksActivityInfo(perksActivityID: number) → info: PerksActivityInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetPerksUIThemePrefix

`C_PerksActivities.GetPerksUIThemePrefix() → kitPrefix: string`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetTrackedPerksActivities

`C_PerksActivities.GetTrackedPerksActivities() → trackedPerksActivities: PerksActivitiesTracked`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{trackedIDs=table}`
- Called in combat: returned 1 value: `table{trackedIDs=table}`
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.RemoveTrackedPerksActivity

`C_PerksActivities.RemoveTrackedPerksActivity(perksActivityID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksActivitiesDocumentation.lua`

## Events

### PERKS_ACTIVITIES_TRACKED_LIST_CHANGED

- Status: ✅ verified
- Payload: `perksActivityID: number`, `added: bool`
- fires synchronously (Blizzard's docs)

### PERKS_ACTIVITIES_TRACKED_UPDATED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 4 times (0 in combat); argument kinds: ``

### PERKS_ACTIVITIES_UPDATED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 4 times (0 in combat); argument kinds: ``

### PERKS_ACTIVITY_COMPLETED

- Status: ✅ verified
- Payload: `perksActivityID: number`
- fires synchronously (Blizzard's docs)

## Types

### PerksActivitiesInfo

- Structure
  - `activePerksMonth`: number
  - `displayMonthName`: cstring
  - `secondsRemaining`: time_t
  - `activities`: PerksActivityInfo[]
  - `thresholds`: PerksActivityThresholdInfo[]

### PerksActivitiesPending

- Structure
  - `pendingIDs`: number[]

### PerksActivitiesTracked

- Structure
  - `trackedIDs`: number[]

### PerksActivityCondition

- Structure
  - `isMet`: bool
  - `text`: cstring
  - `uiPriority`: number

### PerksActivityInfo

- Structure
  - `ID`: number
  - `activityName`: cstring
  - `description`: string
  - `thresholdContributionAmount`: number
  - `completed`: bool
  - `inProgress`: bool
  - `tracked`: bool
  - `supersedes`: number
  - `uiPriority`: number
  - `areAllConditionsMet`: bool
  - `conditions`: PerksActivityCondition[]
  - `eventName`: cstring?
  - `eventStartTime`: time_t?
  - `eventEndTime`: time_t?
  - `requirementsList`: CriteriaRequirement[]
  - `criteriaList`: CriteriaRequiredValue[]
  - `tagNames`: string[]

### PerksActivityTags

- Structure
  - `tagName`: string[]

### PerksActivityThresholdInfo

- Structure
  - `thresholdOrderIndex`: number
  - `currencyAwardAmount`: number
  - `requiredContributionAmount`: number
  - `pendingReward`: bool
  - `itemReward`: number?
