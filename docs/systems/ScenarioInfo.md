# ScenarioInfo

Namespace: `C_ScenarioInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ScenarioInfo.GetCriteriaInfo](#c_scenarioinfogetcriteriainfo) |  |  |
| ✅ | [C_ScenarioInfo.GetCriteriaInfoByStep](#c_scenarioinfogetcriteriainfobystep) |  |  |
| ✅ | [C_ScenarioInfo.GetDisplayInfo](#c_scenarioinfogetdisplayinfo) | 0 values |  |
| ✅ | [C_ScenarioInfo.GetJailersTowerTypeString](#c_scenarioinfogetjailerstowertypestring) |  |  |
| ✅ | [C_ScenarioInfo.GetScenarioIconInfo](#c_scenarioinfogetscenarioiconinfo) |  |  |
| ✅ | [C_ScenarioInfo.GetScenarioInfo](#c_scenarioinfogetscenarioinfo) | 0 values |  |
| ✅ | [C_ScenarioInfo.GetScenarioStepInfo](#c_scenarioinfogetscenariostepinfo) | 0 values |  |
| ✅ | [C_ScenarioInfo.GetTieredEntranceActiveSpells](#c_scenarioinfogettieredentranceactivespells) | 1 value |  |
| ✅ | [C_ScenarioInfo.GetUnitCriteriaProgressValues](#c_scenarioinfogetunitcriteriaprogressvalues) | 0 values |  |
| ✅ | [C_ScenarioInfo.IsTieredEntranceScenario](#c_scenarioinfoistieredentrancescenario) | 1 value |  |

### C_ScenarioInfo.GetCriteriaInfo

`C_ScenarioInfo.GetCriteriaInfo(criteriaIndex: number) → scenarioCriteriaInfo: ScenarioCriteriaInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ScenarioInfoDocumentation.lua`

### C_ScenarioInfo.GetCriteriaInfoByStep

`C_ScenarioInfo.GetCriteriaInfoByStep(stepID: number, criteriaIndex: number) → scenarioCriteriaInfo: ScenarioCriteriaInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ScenarioInfoDocumentation.lua`

### C_ScenarioInfo.GetDisplayInfo

`C_ScenarioInfo.GetDisplayInfo() → info: ScenarioDisplayInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `ScenarioInfoDocumentation.lua`

### C_ScenarioInfo.GetJailersTowerTypeString

`C_ScenarioInfo.GetJailersTowerTypeString(runType: JailersTowerType) → typeString: cstring?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ScenarioInfoDocumentation.lua`

### C_ScenarioInfo.GetScenarioIconInfo

`C_ScenarioInfo.GetScenarioIconInfo(uiMapID: number) → scenarioInfos: ScenarioIconInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ScenarioInfoDocumentation.lua`

### C_ScenarioInfo.GetScenarioInfo

`C_ScenarioInfo.GetScenarioInfo() → scenarioInfo: ScenarioInformation`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `ScenarioInfoDocumentation.lua`

### C_ScenarioInfo.GetScenarioStepInfo

`C_ScenarioInfo.GetScenarioStepInfo(scenarioStepID: number?) → scenarioStepInfo: ScenarioStepInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `ScenarioInfoDocumentation.lua`

### C_ScenarioInfo.GetTieredEntranceActiveSpells

`C_ScenarioInfo.GetTieredEntranceActiveSpells() → spellIDs: number[]?`

- Status: ✅ verified (function)
- Blizzard: Returns list of active challenge spells if inside a tiered entrance scenario
- Called out of combat: returned 1 value: `nil`
- Source: client docs `ScenarioInfoDocumentation.lua`

### C_ScenarioInfo.GetUnitCriteriaProgressValues

`C_ScenarioInfo.GetUnitCriteriaProgressValues(unit: UnitToken) → actualValue: number, percentValue: number, percentValueString: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit identity is restricted (Blizzard's docs; not checked in game)
- Called out of combat with "player": returned 0 values
- Source: client docs `ScenarioInfoDocumentation.lua`

### C_ScenarioInfo.IsTieredEntranceScenario

`C_ScenarioInfo.IsTieredEntranceScenario() → isTieredEntrance: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ScenarioInfoDocumentation.lua`

## Events

### JAILERS_TOWER_LEVEL_UPDATE

- Status: ✅ verified
- Payload: `level: number`, `type: JailersTowerType`
- fires synchronously (Blizzard's docs)

### SCENARIO_BONUS_OBJECTIVE_COMPLETE

- Status: ✅ verified
- Payload: `bonusObjectiveID: number`
- fires synchronously (Blizzard's docs)

### SCENARIO_BONUS_VISIBILITY_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SCENARIO_COMPLETED

- Status: ✅ verified
- Payload: `questID: number?`, `xp: number?`, `money: number?`
- fires synchronously (Blizzard's docs)

### SCENARIO_CRITERIA_SHOW_STATE_UPDATE

- Status: ✅ verified
- Payload: `show: bool`
- fires synchronously (Blizzard's docs)

### SCENARIO_CRITERIA_UPDATE

- Status: ✅ verified
- Payload: `criteriaID: number`
- fires synchronously (Blizzard's docs)

### SCENARIO_POI_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SCENARIO_SPELL_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SCENARIO_UPDATE

- Status: ✅ verified
- Payload: `newStep: bool?`
- fires synchronously (Blizzard's docs)

## Types

### JailersTowerType

- Enumeration — ✅ verified
  - `TwistingCorridors` = 0
  - `SkoldusHalls` = 1
  - `FractureChambers` = 2
  - `Soulforges` = 3
  - `Coldheart` = 4
  - `Mortregar` = 5
  - `UpperReaches` = 6
  - `ArkobanHall` = 7
  - `TormentChamberJaina` = 8
  - `TormentChamberThrall` = 9
  - `TormentChamberAnduin` = 10
  - `AdamantVaults` = 11
  - `ForgottenCatacombs` = 12
  - `Ossuary` = 13
  - `BossRush` = 14

### ScenarioCriteriaInfo

- Structure
  - `description`: string
  - `criteriaType`: number
  - `completed`: bool
  - `quantity`: number
  - `totalQuantity`: number
  - `flags`: number
  - `assetID`: number
  - `criteriaID`: number
  - `duration`: number
  - `elapsed`: number
  - `failed`: bool
  - `isWeightedProgress`: bool
  - `isFormatted`: bool
  - `quantityString`: string

### ScenarioDisplayInfo

- Structure
  - `themeColor`: colorRGB?
  - `startSoundKitID`: number?

### ScenarioIconInfo

- Structure
  - `x`: number
  - `y`: number
  - `atlas`: textureAtlas
  - `description`: cstring

### ScenarioInformation

- Structure
  - `name`: string
  - `currentStage`: number
  - `numStages`: number
  - `flags`: number
  - `isComplete`: bool
  - `xp`: number
  - `money`: number
  - `type`: number
  - `area`: string
  - `uiTextureKit`: textureKit
  - `scenarioID`: number

### ScenarioStepInfo

- Structure
  - `title`: string
  - `description`: string
  - `numCriteria`: number
  - `stepFailed`: bool
  - `isBonusStep`: bool
  - `isForCurrentStepOnly`: bool
  - `shouldShowBonusObjective`: bool
  - `spells`: ScenarioStepSpellInfo[]
  - `weightedProgress`: number?
  - `rewardQuestID`: number
  - `widgetSetID`: number?
  - `stepID`: number

### ScenarioStepSpellInfo

- Structure
  - `spellID`: number
  - `name`: string
  - `icon`: number
