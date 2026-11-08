# QuestLineUI

Namespace: `C_QuestLine`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_QuestLine.GetAvailableQuestLines](#c_questlinegetavailablequestlines) |  |  |
| ✅ | [C_QuestLine.GetForceVisibleQuests](#c_questlinegetforcevisiblequests) |  |  |
| ✅ | [C_QuestLine.GetQuestLineInfo](#c_questlinegetquestlineinfo) |  |  |
| ✅ | [C_QuestLine.GetQuestLineQuests](#c_questlinegetquestlinequests) |  |  |
| ✅ | [C_QuestLine.IsComplete](#c_questlineiscomplete) |  |  |
| ✅ | [C_QuestLine.QuestLineIgnoresAccountCompletedFiltering](#c_questlinequestlineignoresaccountcompletedfiltering) |  |  |
| ✅ | [C_QuestLine.RequestQuestLinesForMap](#c_questlinerequestquestlinesformap) |  |  |

### C_QuestLine.GetAvailableQuestLines

`C_QuestLine.GetAvailableQuestLines(uiMapID: number) → questLines: QuestLineInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestLineInfoDocumentation.lua`

### C_QuestLine.GetForceVisibleQuests

`C_QuestLine.GetForceVisibleQuests(uiMapID: number) → questIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestLineInfoDocumentation.lua`

### C_QuestLine.GetQuestLineInfo

`C_QuestLine.GetQuestLineInfo(questID: number, uiMapID: number?, displayableOnly: bool = False) → questLineInfo: QuestLineInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestLineInfoDocumentation.lua`

### C_QuestLine.GetQuestLineQuests

`C_QuestLine.GetQuestLineQuests(questLineID: number) → questIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestLineInfoDocumentation.lua`

### C_QuestLine.IsComplete

`C_QuestLine.IsComplete(questLineID: number) → isComplete: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestLineInfoDocumentation.lua`

### C_QuestLine.QuestLineIgnoresAccountCompletedFiltering

`C_QuestLine.QuestLineIgnoresAccountCompletedFiltering(uiMapID: number, questLineID: number) → questLineIgnoresAccountCompletedFiltering: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestLineInfoDocumentation.lua`

### C_QuestLine.RequestQuestLinesForMap

`C_QuestLine.RequestQuestLinesForMap(uiMapID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestLineInfoDocumentation.lua`

## Types

### QuestLineFloorLocation

- Enumeration — ✅ verified
  - `Above` = 0
  - `Below` = 1
  - `Same` = 2

### QuestLineInfo

- Structure
  - `questLineName`: cstring
  - `questName`: cstring
  - `questLineID`: number
  - `questID`: number
  - `x`: number
  - `y`: number
  - `isHidden`: bool
  - `isLegendary`: bool
  - `isLocalStory`: bool
  - `isDaily`: bool
  - `isCampaign`: bool
  - `isImportant`: bool
  - `isAccountCompleted`: bool
  - `isCombatAllyQuest`: bool
  - `isMeta`: bool
  - `inProgress`: bool
  - `isQuestStart`: bool
  - `floorLocation`: QuestLineFloorLocation
  - `startMapID`: number
