# PerksActivities

Namespace: `C_PerksActivities`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_PerksActivities.AddTrackedPerksActivity](#c_perksactivitiesaddtrackedperksactivity) |  |  |
| ❔ | [C_PerksActivities.ClearPerksActivitiesPendingCompletion](#c_perksactivitiesclearperksactivitiespendingcompletion) |  |  |
| ❔ | [C_PerksActivities.GetAllPerksActivityTags](#c_perksactivitiesgetallperksactivitytags) |  |  |
| ❔ | [C_PerksActivities.GetPerksActivitiesInfo](#c_perksactivitiesgetperksactivitiesinfo) |  |  |
| ❔ | [C_PerksActivities.GetPerksActivitiesPendingCompletion](#c_perksactivitiesgetperksactivitiespendingcompletion) |  |  |
| ❔ | [C_PerksActivities.GetPerksActivityChatLink](#c_perksactivitiesgetperksactivitychatlink) |  |  |
| ❔ | [C_PerksActivities.GetPerksActivityInfo](#c_perksactivitiesgetperksactivityinfo) |  |  |
| ❔ | [C_PerksActivities.GetPerksUIThemePrefix](#c_perksactivitiesgetperksuithemeprefix) |  |  |
| ❔ | [C_PerksActivities.GetTrackedPerksActivities](#c_perksactivitiesgettrackedperksactivities) |  |  |
| ❔ | [C_PerksActivities.RemoveTrackedPerksActivity](#c_perksactivitiesremovetrackedperksactivity) |  |  |

### C_PerksActivities.AddTrackedPerksActivity

`C_PerksActivities.AddTrackedPerksActivity(perksActivityID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.ClearPerksActivitiesPendingCompletion

`C_PerksActivities.ClearPerksActivitiesPendingCompletion()`

- Status: ❔ unverified
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetAllPerksActivityTags

`C_PerksActivities.GetAllPerksActivityTags() → tags: PerksActivityTags`

- Status: ❔ unverified
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetPerksActivitiesInfo

`C_PerksActivities.GetPerksActivitiesInfo() → info: PerksActivitiesInfo`

- Status: ❔ unverified
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetPerksActivitiesPendingCompletion

`C_PerksActivities.GetPerksActivitiesPendingCompletion() → pending: PerksActivitiesPending`

- Status: ❔ unverified
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetPerksActivityChatLink

`C_PerksActivities.GetPerksActivityChatLink(perksActivityID: number) → link: cstring`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetPerksActivityInfo

`C_PerksActivities.GetPerksActivityInfo(perksActivityID: number) → info: PerksActivityInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetPerksUIThemePrefix

`C_PerksActivities.GetPerksUIThemePrefix() → kitPrefix: string`

- Status: ❔ unverified
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.GetTrackedPerksActivities

`C_PerksActivities.GetTrackedPerksActivities() → trackedPerksActivities: PerksActivitiesTracked`

- Status: ❔ unverified
- Source: client docs `PerksActivitiesDocumentation.lua`

### C_PerksActivities.RemoveTrackedPerksActivity

`C_PerksActivities.RemoveTrackedPerksActivity(perksActivityID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksActivitiesDocumentation.lua`

## Events

### PERKS_ACTIVITIES_TRACKED_LIST_CHANGED

- Status: ❔ unverified
- Payload: `perksActivityID: number`, `added: bool`
- fires synchronously (Blizzard's docs)

### PERKS_ACTIVITIES_TRACKED_UPDATED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### PERKS_ACTIVITIES_UPDATED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### PERKS_ACTIVITY_COMPLETED

- Status: ❔ unverified
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
