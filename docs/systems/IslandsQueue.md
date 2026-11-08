# IslandsQueue

Namespace: `C_IslandsQueue`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_IslandsQueue.CloseIslandsQueueScreen](#c_islandsqueuecloseislandsqueuescreen) |  |  |
| ❔ | [C_IslandsQueue.GetIslandDifficultyInfo](#c_islandsqueuegetislanddifficultyinfo) |  |  |
| ❔ | [C_IslandsQueue.GetIslandsMaxGroupSize](#c_islandsqueuegetislandsmaxgroupsize) |  |  |
| ❔ | [C_IslandsQueue.GetIslandsWeeklyQuestID](#c_islandsqueuegetislandsweeklyquestid) |  |  |
| ❔ | [C_IslandsQueue.QueueForIsland](#c_islandsqueuequeueforisland) |  |  |
| ❔ | [C_IslandsQueue.RequestPreloadRewardData](#c_islandsqueuerequestpreloadrewarddata) |  |  |

### C_IslandsQueue.CloseIslandsQueueScreen

`C_IslandsQueue.CloseIslandsQueueScreen()`

- Status: ❔ unverified
- Source: client docs `IslandsQueueUIDocumentation.lua`

### C_IslandsQueue.GetIslandDifficultyInfo

`C_IslandsQueue.GetIslandDifficultyInfo() → islandDifficultyInfo: IslandsQueueDifficultyInfo[]`

- Status: ❔ unverified
- Source: client docs `IslandsQueueUIDocumentation.lua`

### C_IslandsQueue.GetIslandsMaxGroupSize

`C_IslandsQueue.GetIslandsMaxGroupSize() → maxGroupSize: number`

- Status: ❔ unverified
- Source: client docs `IslandsQueueUIDocumentation.lua`

### C_IslandsQueue.GetIslandsWeeklyQuestID

`C_IslandsQueue.GetIslandsWeeklyQuestID() → questID: number?`

- Status: ❔ unverified
- Source: client docs `IslandsQueueUIDocumentation.lua`

### C_IslandsQueue.QueueForIsland

`C_IslandsQueue.QueueForIsland(difficultyID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `IslandsQueueUIDocumentation.lua`

### C_IslandsQueue.RequestPreloadRewardData

`C_IslandsQueue.RequestPreloadRewardData(questId: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `IslandsQueueUIDocumentation.lua`

## Events

### ISLANDS_QUEUE_CLOSE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ISLANDS_QUEUE_OPEN

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### IslandsQueueDifficultyInfo

- Structure
  - `difficultyId`: number
  - `previewRewardQuestId`: number
