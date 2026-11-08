# QuestTaskInfo

Namespace: `C_TaskQuest`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_TaskQuest.DoesMapShowTaskQuestObjectives](#c_taskquestdoesmapshowtaskquestobjectives) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_TaskQuest.GetQuestInfoByQuestID](#c_taskquestgetquestinfobyquestid) | 0 values | 0 values |
| ✅ | [C_TaskQuest.GetQuestLocation](#c_taskquestgetquestlocation) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_TaskQuest.GetQuestProgressBarInfo](#c_taskquestgetquestprogressbarinfo) | 0 values | 0 values |
| ✅ | [C_TaskQuest.GetQuestTimeLeftMinutes](#c_taskquestgetquesttimeleftminutes) | 0 values | 0 values |
| ✅ | [C_TaskQuest.GetQuestTimeLeftSeconds](#c_taskquestgetquesttimeleftseconds) | 0 values | 0 values |
| ✅ | [C_TaskQuest.GetQuestUIWidgetSetByType](#c_taskquestgetquestuiwidgetsetbytype) | 0 values | 0 values |
| ✅ | [C_TaskQuest.GetQuestZoneID](#c_taskquestgetquestzoneid) | 0 values | 0 values |
| ✅ | [C_TaskQuest.GetQuestsOnMap](#c_taskquestgetquestsonmap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_TaskQuest.GetThreatQuests](#c_taskquestgetthreatquests) | 1 value | 1 value |
| ✅ | [C_TaskQuest.IsActive](#c_taskquestisactive) | 1 value | 1 value |
| ✅ | [C_TaskQuest.RequestPreloadRewardData](#c_taskquestrequestpreloadrewarddata) |  |  |

### C_TaskQuest.DoesMapShowTaskQuestObjectives

`C_TaskQuest.DoesMapShowTaskQuestObjectives(uiMapID: number) → showsTaskQuestObjectives: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.GetQuestInfoByQuestID

`C_TaskQuest.GetQuestInfoByQuestID(questID: number) → questTitle: cstring, factionID: number?, capped: bool?, displayAsObjective: bool?`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `quest`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.GetQuestLocation

`C_TaskQuest.GetQuestLocation(questID: number, uiMapID: number) → locationX: number, locationY: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `quest,map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.GetQuestProgressBarInfo

`C_TaskQuest.GetQuestProgressBarInfo(questID: number) → progress: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `quest`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.GetQuestTimeLeftMinutes

`C_TaskQuest.GetQuestTimeLeftMinutes(questID: number) → minutesLeft: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `quest`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.GetQuestTimeLeftSeconds

`C_TaskQuest.GetQuestTimeLeftSeconds(questID: number) → secondsLeft: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `quest`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.GetQuestUIWidgetSetByType

`C_TaskQuest.GetQuestUIWidgetSetByType(questID: number, type: MapIconUIWidgetSetType) → widgetSet: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `quest,n:0`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.GetQuestZoneID

`C_TaskQuest.GetQuestZoneID(questID: number) → uiMapID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `quest`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.GetQuestsOnMap

`C_TaskQuest.GetQuestsOnMap(uiMapID: number) → taskPOIs: QuestPOIMapInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.GetThreatQuests

`C_TaskQuest.GetThreatQuests() → quests: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.IsActive

`C_TaskQuest.IsActive(questID: number) → active: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `quest`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `QuestTaskInfoDocumentation.lua`

### C_TaskQuest.RequestPreloadRewardData

`C_TaskQuest.RequestPreloadRewardData(questID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestTaskInfoDocumentation.lua`
