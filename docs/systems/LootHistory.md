# LootHistory

Namespace: `C_LootHistory`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_LootHistory.GetAllEncounterInfos](#c_loothistorygetallencounterinfos) |  |  |
| ❔ | [C_LootHistory.GetInfoForEncounter](#c_loothistorygetinfoforencounter) |  |  |
| ❔ | [C_LootHistory.GetLootHistoryTime](#c_loothistorygetloothistorytime) |  |  |
| ❔ | [C_LootHistory.GetSortedDropsForEncounter](#c_loothistorygetsorteddropsforencounter) |  |  |
| ❔ | [C_LootHistory.GetSortedInfoForDrop](#c_loothistorygetsortedinfofordrop) |  |  |

### C_LootHistory.GetAllEncounterInfos

`C_LootHistory.GetAllEncounterInfos() → infos: EncounterLootInfo[]`

- Status: ❔ unverified
- Source: client docs `LootHistoryDocumentation.lua`

### C_LootHistory.GetInfoForEncounter

`C_LootHistory.GetInfoForEncounter(encounterID: number) → info: EncounterLootInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LootHistoryDocumentation.lua`

### C_LootHistory.GetLootHistoryTime

`C_LootHistory.GetLootHistoryTime() → time: number`

- Status: ❔ unverified
- Source: client docs `LootHistoryDocumentation.lua`

### C_LootHistory.GetSortedDropsForEncounter

`C_LootHistory.GetSortedDropsForEncounter(encounterID: number) → drops: EncounterLootDropInfo[]?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LootHistoryDocumentation.lua`

### C_LootHistory.GetSortedInfoForDrop

`C_LootHistory.GetSortedInfoForDrop(encounterID: number, lootListKey: number) → info: EncounterLootDropInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LootHistoryDocumentation.lua`

## Events

### LOOT_HISTORY_CLEAR_HISTORY

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LOOT_HISTORY_GO_TO_ENCOUNTER

- Status: ❔ unverified
- Payload: `encounterID: number`
- unique event (Blizzard's docs)

### LOOT_HISTORY_ONE_HUNDRED_ROLL

- Status: ❔ unverified
- Payload: `encounterID: number`, `lootListKey: number`
- fires synchronously (Blizzard's docs)

### LOOT_HISTORY_UPDATE_DROP

- Status: ❔ unverified
- Payload: `encounterID: number`, `lootListKey: number`
- unique event (Blizzard's docs)

### LOOT_HISTORY_UPDATE_ENCOUNTER

- Status: ❔ unverified
- Payload: `encounterID: number`
- unique event (Blizzard's docs)

## Types

### EncounterLootDropInfo

- Structure
  - `lootListKey`: number
  - `itemHyperlink`: string
  - `playerRollState`: EncounterLootDropRollState
  - `currentLeader`: EncounterLootDropRollInfo?
  - `isTied`: bool
  - `winner`: EncounterLootDropRollInfo?
  - `allPassed`: bool
  - `rollInfos`: EncounterLootDropRollInfo[]
  - `startTime`: number
  - `duration`: number

### EncounterLootDropRollInfo

- Structure
  - `playerName`: string
  - `playerGUID`: WOWGUID
  - `playerClass`: string
  - `isSelf`: bool
  - `state`: EncounterLootDropRollState
  - `isWinner`: bool
  - `roll`: number?

### EncounterLootDropRollState

- Enumeration — ❔ unverified
  - `NeedMainSpec` = 0
  - `NeedOffSpec` = 1
  - `Transmog` = 2
  - `Greed` = 3
  - `NoRoll` = 4
  - `Pass` = 5

### EncounterLootDrops

- Structure
  - `encounterID`: number
  - `drops`: EncounterLootDropInfo[]

### EncounterLootInfo

- Structure
  - `encounterName`: string
  - `encounterID`: number
  - `startTime`: number
  - `duration`: number
