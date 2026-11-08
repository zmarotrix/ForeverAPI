# ContributionCollector

Namespace: `C_ContributionCollector`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ContributionCollector.Close](#c_contributioncollectorclose) |  |  |
| ✅ | [C_ContributionCollector.Contribute](#c_contributioncollectorcontribute) |  |  |
| ✅ | [C_ContributionCollector.GetActive](#c_contributioncollectorgetactive) | 0 values | 0 values |
| ✅ | [C_ContributionCollector.GetAtlases](#c_contributioncollectorgetatlases) |  |  |
| ✅ | [C_ContributionCollector.GetBuffs](#c_contributioncollectorgetbuffs) |  |  |
| ✅ | [C_ContributionCollector.GetContributionAppearance](#c_contributioncollectorgetcontributionappearance) |  |  |
| ✅ | [C_ContributionCollector.GetContributionCollectorsForMap](#c_contributioncollectorgetcontributioncollectorsformap) |  |  |
| ✅ | [C_ContributionCollector.GetContributionResult](#c_contributioncollectorgetcontributionresult) |  |  |
| ✅ | [C_ContributionCollector.GetDescription](#c_contributioncollectorgetdescription) |  |  |
| ✅ | [C_ContributionCollector.GetManagedContributionsForCreatureID](#c_contributioncollectorgetmanagedcontributionsforcreatureid) |  |  |
| ✅ | [C_ContributionCollector.GetName](#c_contributioncollectorgetname) |  |  |
| ✅ | [C_ContributionCollector.GetOrderIndex](#c_contributioncollectorgetorderindex) |  |  |
| ✅ | [C_ContributionCollector.GetRequiredContributionCurrency](#c_contributioncollectorgetrequiredcontributioncurrency) |  |  |
| ✅ | [C_ContributionCollector.GetRequiredContributionItem](#c_contributioncollectorgetrequiredcontributionitem) |  |  |
| ✅ | [C_ContributionCollector.GetRewardQuestID](#c_contributioncollectorgetrewardquestid) |  |  |
| ✅ | [C_ContributionCollector.GetState](#c_contributioncollectorgetstate) |  |  |
| ✅ | [C_ContributionCollector.HasPendingContribution](#c_contributioncollectorhaspendingcontribution) |  |  |
| ✅ | [C_ContributionCollector.IsAwaitingRewardQuestData](#c_contributioncollectorisawaitingrewardquestdata) |  |  |

### C_ContributionCollector.Close

`C_ContributionCollector.Close()`

- Status: ✅ verified (function)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.Contribute

`C_ContributionCollector.Contribute(contributionID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetActive

`C_ContributionCollector.GetActive() → contributionID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetAtlases

`C_ContributionCollector.GetAtlases(contributionID: number) → atlasName: textureAtlas[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetBuffs

`C_ContributionCollector.GetBuffs(contributionID: number) → spellID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetContributionAppearance

`C_ContributionCollector.GetContributionAppearance(contributionID: number, contributionState: ContributionState) → appearance: ContributionAppearance?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetContributionCollectorsForMap

`C_ContributionCollector.GetContributionCollectorsForMap(uiMapID: number) → contributionCollectors: ContributionMapInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetContributionResult

`C_ContributionCollector.GetContributionResult(contributionID: number) → result: ContributionResult`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetDescription

`C_ContributionCollector.GetDescription(contributionID: number) → description: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetManagedContributionsForCreatureID

`C_ContributionCollector.GetManagedContributionsForCreatureID(creatureID: number) → contributionID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetName

`C_ContributionCollector.GetName(contributionID: number) → name: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetOrderIndex

`C_ContributionCollector.GetOrderIndex(contributionID: number) → orderIndex: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetRequiredContributionCurrency

`C_ContributionCollector.GetRequiredContributionCurrency(contributionID: number) → currencyID: number, currencyAmount: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetRequiredContributionItem

`C_ContributionCollector.GetRequiredContributionItem(contributionID: number) → itemID: number, itemCount: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetRewardQuestID

`C_ContributionCollector.GetRewardQuestID(contributionID: number) → questID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.GetState

`C_ContributionCollector.GetState(contributionID: number) → contributionState: ContributionState, contributionPercentageComplete: number, timeOfNextStateChange: time_t?, startTime: time_t`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.HasPendingContribution

`C_ContributionCollector.HasPendingContribution(contributionID: number) → hasPending: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

### C_ContributionCollector.IsAwaitingRewardQuestData

`C_ContributionCollector.IsAwaitingRewardQuestData(contributionID: number) → awaitingData: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContributionCollectorDocumentation.lua`

## Events

### CONTRIBUTION_CHANGED

- Status: ✅ verified
- Payload: `state: ContributionState`, `result: ContributionResult`, `name: string`, `contributionID: number`
- fires synchronously (Blizzard's docs)

### CONTRIBUTION_COLLECTOR_PENDING

- Status: ✅ verified
- Payload: `contributionID: number`, `isPending: bool`, `result: number`
- fires synchronously (Blizzard's docs)

### CONTRIBUTION_COLLECTOR_UPDATE

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### CONTRIBUTION_COLLECTOR_UPDATE_SINGLE

- Status: ✅ verified
- Payload: `contributionID: number`
- fires synchronously (Blizzard's docs)

## Types

### ContributionAppearance

- Structure
  - `stateName`: cstring
  - `stateColor`: colorRGB
  - `tooltipLine`: cstring
  - `tooltipUseTimeRemaining`: bool
  - `statusBarAtlas`: textureAtlas
  - `borderAtlas`: textureAtlas
  - `bannerAtlas`: textureAtlas

### ContributionMapInfo

- Structure
  - `areaPoiID`: number
  - `position`: vector2
  - `name`: cstring
  - `atlasName`: string
  - `collectorCreatureID`: number

### ContributionResult

- Enumeration — ✅ verified
  - `Success` = 0
  - `MustBeNearNpc` = 1
  - `IncorrectState` = 2
  - `InvalidID` = 3
  - `QuestDataMissing` = 4
  - `FailedConditionCheck` = 5
  - `UnableToCompleteTurnIn` = 6
  - `InternalError` = 7
