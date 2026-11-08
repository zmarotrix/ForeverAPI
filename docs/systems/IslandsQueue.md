# IslandsQueue

Namespace: `C_IslandsQueue`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_IslandsQueue.CloseIslandsQueueScreen](#c_islandsqueuecloseislandsqueuescreen) |  |  |
| ✅ | [C_IslandsQueue.GetIslandDifficultyInfo](#c_islandsqueuegetislanddifficultyinfo) | 1 value |  |
| ✅ | [C_IslandsQueue.GetIslandsMaxGroupSize](#c_islandsqueuegetislandsmaxgroupsize) | 1 value |  |
| ✅ | [C_IslandsQueue.GetIslandsWeeklyQuestID](#c_islandsqueuegetislandsweeklyquestid) | 1 value |  |
| ✅ | [C_IslandsQueue.QueueForIsland](#c_islandsqueuequeueforisland) |  |  |
| ✅ | [C_IslandsQueue.RequestPreloadRewardData](#c_islandsqueuerequestpreloadrewarddata) |  |  |

### C_IslandsQueue.CloseIslandsQueueScreen

`C_IslandsQueue.CloseIslandsQueueScreen()`

- Status: ✅ verified (function)
- Source: client docs `IslandsQueueUIDocumentation.lua`

### C_IslandsQueue.GetIslandDifficultyInfo

`C_IslandsQueue.GetIslandDifficultyInfo() → islandDifficultyInfo: IslandsQueueDifficultyInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table}`
- Source: client docs `IslandsQueueUIDocumentation.lua`

### C_IslandsQueue.GetIslandsMaxGroupSize

`C_IslandsQueue.GetIslandsMaxGroupSize() → maxGroupSize: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `IslandsQueueUIDocumentation.lua`

### C_IslandsQueue.GetIslandsWeeklyQuestID

`C_IslandsQueue.GetIslandsWeeklyQuestID() → questID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `IslandsQueueUIDocumentation.lua`

### C_IslandsQueue.QueueForIsland

`C_IslandsQueue.QueueForIsland(difficultyID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `IslandsQueueUIDocumentation.lua`

### C_IslandsQueue.RequestPreloadRewardData

`C_IslandsQueue.RequestPreloadRewardData(questId: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `IslandsQueueUIDocumentation.lua`

## Events

### ISLANDS_QUEUE_CLOSE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ISLANDS_QUEUE_OPEN

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### IslandsQueueDifficultyInfo

- Structure
  - `difficultyId`: number
  - `previewRewardQuestId`: number
