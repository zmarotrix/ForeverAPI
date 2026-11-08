# NeighborhoodInitiative

Namespace: `C_NeighborhoodInitiative`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_NeighborhoodInitiative.AddTrackedInitiativeTask](#c_neighborhoodinitiativeaddtrackedinitiativetask) |  |  |
| ✅ | [C_NeighborhoodInitiative.GetActiveNeighborhood](#c_neighborhoodinitiativegetactiveneighborhood) | 1 value | 1 value |
| ✅ | [C_NeighborhoodInitiative.GetAvailableHouseXP](#c_neighborhoodinitiativegetavailablehousexp) | 1 value | 1 value |
| ✅ | [C_NeighborhoodInitiative.GetInitiativeActivityLogInfo](#c_neighborhoodinitiativegetinitiativeactivityloginfo) | 1 value | 1 value |
| ✅ | [C_NeighborhoodInitiative.GetInitiativeTaskChatLink](#c_neighborhoodinitiativegetinitiativetaskchatlink) |  |  |
| ✅ | [C_NeighborhoodInitiative.GetInitiativeTaskInfo](#c_neighborhoodinitiativegetinitiativetaskinfo) |  |  |
| ✅ | [C_NeighborhoodInitiative.GetInitiativeTaskRewardScaling](#c_neighborhoodinitiativegetinitiativetaskrewardscaling) |  |  |
| ✅ | [C_NeighborhoodInitiative.GetNeighborhoodInitiativeInfo](#c_neighborhoodinitiativegetneighborhoodinitiativeinfo) | 1 value | 1 value |
| ✅ | [C_NeighborhoodInitiative.GetRequiredLevel](#c_neighborhoodinitiativegetrequiredlevel) | 1 value | 1 value |
| ✅ | [C_NeighborhoodInitiative.GetTrackedInitiativeTasks](#c_neighborhoodinitiativegettrackedinitiativetasks) | 1 value | 1 value |
| ✅ | [C_NeighborhoodInitiative.IsInitiativeEnabled](#c_neighborhoodinitiativeisinitiativeenabled) | 1 value | 1 value |
| ✅ | [C_NeighborhoodInitiative.IsPlayerInNeighborhoodGroup](#c_neighborhoodinitiativeisplayerinneighborhoodgroup) | 1 value | 1 value |
| ✅ | [C_NeighborhoodInitiative.IsViewingActiveNeighborhood](#c_neighborhoodinitiativeisviewingactiveneighborhood) | 1 value | 1 value |
| ✅ | [C_NeighborhoodInitiative.PlayerHasInitiativeAccess](#c_neighborhoodinitiativeplayerhasinitiativeaccess) |  |  |
| ✅ | [C_NeighborhoodInitiative.PlayerMeetsRequiredLevel](#c_neighborhoodinitiativeplayermeetsrequiredlevel) |  |  |
| ✅ | [C_NeighborhoodInitiative.RemoveTrackedInitiativeTask](#c_neighborhoodinitiativeremovetrackedinitiativetask) |  |  |
| ✅ | [C_NeighborhoodInitiative.RequestInitiativeActivityLog](#c_neighborhoodinitiativerequestinitiativeactivitylog) |  |  |
| ✅ | [C_NeighborhoodInitiative.RequestNeighborhoodInitiativeInfo](#c_neighborhoodinitiativerequestneighborhoodinitiativeinfo) |  |  |
| ✅ | [C_NeighborhoodInitiative.SetActiveNeighborhood](#c_neighborhoodinitiativesetactiveneighborhood) |  |  |
| ✅ | [C_NeighborhoodInitiative.SetViewingNeighborhood](#c_neighborhoodinitiativesetviewingneighborhood) |  |  |

### C_NeighborhoodInitiative.AddTrackedInitiativeTask

`C_NeighborhoodInitiative.AddTrackedInitiativeTask(initiativeTaskID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.GetActiveNeighborhood

`C_NeighborhoodInitiative.GetActiveNeighborhood() → neighborhoodGUID: WOWGUID`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.GetAvailableHouseXP

`C_NeighborhoodInitiative.GetAvailableHouseXP() → availabeXP: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.GetInitiativeActivityLogInfo

`C_NeighborhoodInitiative.GetInitiativeActivityLogInfo() → info: InitiativeActivityLogInfo?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{isLoaded=boolean,nextUpdateTime=number,taskActivity=table}`
- Called in combat: returned 1 value: `table{isLoaded=boolean,nextUpdateTime=number,taskActivity=table}`
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.GetInitiativeTaskChatLink

`C_NeighborhoodInitiative.GetInitiativeTaskChatLink(initiativeTaskID: number) → link: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.GetInitiativeTaskInfo

`C_NeighborhoodInitiative.GetInitiativeTaskInfo(initiativeTaskID: number) → info: InitiativeTaskInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.GetInitiativeTaskRewardScaling

`C_NeighborhoodInitiative.GetInitiativeTaskRewardScaling(taskID: number, numItems: number) → scaledAmount: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.GetNeighborhoodInitiativeInfo

`C_NeighborhoodInitiative.GetNeighborhoodInitiativeInfo() → info: NeighborhoodInitiativeInfo?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{currentCycleID=number,currentProgress=number,description=string,duration=number,initiativeID=number,isLoaded=boolean,milestones=table,playerTotalContribution=number,progressRequired=number,tasks=table,title=string}`
- Called in combat: returned 1 value: `table{currentCycleID=number,currentProgress=number,description=string,duration=number,initiativeID=number,isLoaded=boolean,milestones=table,playerTotalContribution=number,progressRequired=number,tasks=table,title=string}`
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.GetRequiredLevel

`C_NeighborhoodInitiative.GetRequiredLevel() → reqLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.GetTrackedInitiativeTasks

`C_NeighborhoodInitiative.GetTrackedInitiativeTasks() → trackedInitiativeTasks: InitiativeTasksTracked`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{trackedIDs=table}`
- Called in combat: returned 1 value: `table{trackedIDs=table}`
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.IsInitiativeEnabled

`C_NeighborhoodInitiative.IsInitiativeEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.IsPlayerInNeighborhoodGroup

`C_NeighborhoodInitiative.IsPlayerInNeighborhoodGroup() → inValidGroup: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.IsViewingActiveNeighborhood

`C_NeighborhoodInitiative.IsViewingActiveNeighborhood() → isViewingActiveNeighborhood: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.PlayerHasInitiativeAccess

`C_NeighborhoodInitiative.PlayerHasInitiativeAccess() → success: bool`

- Status: ✅ verified (function)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.PlayerMeetsRequiredLevel

`C_NeighborhoodInitiative.PlayerMeetsRequiredLevel() → success: bool`

- Status: ✅ verified (function)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.RemoveTrackedInitiativeTask

`C_NeighborhoodInitiative.RemoveTrackedInitiativeTask(initiativeTaskID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.RequestInitiativeActivityLog

`C_NeighborhoodInitiative.RequestInitiativeActivityLog()`

- Status: ✅ verified (function)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.RequestNeighborhoodInitiativeInfo

`C_NeighborhoodInitiative.RequestNeighborhoodInitiativeInfo()`

- Status: ✅ verified (function)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.SetActiveNeighborhood

`C_NeighborhoodInitiative.SetActiveNeighborhood(neighborhoodGUID: WOWGUID)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

### C_NeighborhoodInitiative.SetViewingNeighborhood

`C_NeighborhoodInitiative.SetViewingNeighborhood(neighborhoodGUID: WOWGUID)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NeighborhoodInitiativeDocumentation.lua`

## Events

### INITIATIVE_ACTIVITY_LOG_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### INITIATIVE_COMPLETED

- Status: ✅ verified
- Payload: `initiativeTitle: string`
- fires synchronously (Blizzard's docs)

### INITIATIVE_TASKS_TRACKED_LIST_CHANGED

- Status: ✅ verified
- Payload: `initiativeTaskID: number`, `added: bool`
- fires synchronously (Blizzard's docs)

### INITIATIVE_TASKS_TRACKED_UPDATED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### INITIATIVE_TASK_COMPLETED

- Status: ✅ verified
- Payload: `taskName: string`
- fires synchronously (Blizzard's docs)

### NEIGHBORHOOD_INITIATIVE_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

## Types

### InitiativeActivityLogEntry

- Structure
  - `taskID`: number
  - `playerName`: string
  - `taskName`: cstring
  - `completionTime`: time_t
  - `amount`: number

### InitiativeActivityLogInfo

- Structure
  - `isLoaded`: bool
  - `neighborhoodGUID`: WOWGUID
  - `nextUpdateTime`: time_t
  - `taskActivity`: InitiativeActivityLogEntry[]

### InitiativeMilestoneInfo

- Structure
  - `milestoneOrderIndex`: number
  - `requiredContributionAmount`: number
  - `rewards`: InitiativeMilestoneRewardInfo[]

### InitiativeMilestoneRewardInfo

- Structure
  - `title`: string
  - `description`: string
  - `decorID`: number
  - `decorQuantity`: number
  - `favor`: number
  - `money`: WOWMONEY
  - `rewardQuestID`: number

### InitiativeTaskInfo

- Structure
  - `ID`: number
  - `taskName`: cstring
  - `description`: string
  - `progressContributionAmount`: number
  - `tracked`: bool
  - `supersedes`: number
  - `timesCompleted`: number
  - `completed`: bool
  - `inProgress`: bool
  - `taskType`: NeighborhoodInitiativeTaskType
  - `sortOrder`: number
  - `rewardQuestID`: number
  - `requirementsList`: CriteriaRequirement[]
  - `criteriaList`: CriteriaRequiredValue[]

### InitiativeTasksTracked

- Structure
  - `trackedIDs`: number[]

### NeighborhoodInitiativeInfo

- Structure
  - `isLoaded`: bool
  - `neighborhoodGUID`: WOWGUID
  - `initiativeID`: number
  - `currentCycleID`: number
  - `progressRequired`: number
  - `currentProgress`: number
  - `playerTotalContribution`: number
  - `duration`: time_t
  - `tasks`: InitiativeTaskInfo[]
  - `milestones`: InitiativeMilestoneInfo[]
  - `title`: string
  - `description`: string
