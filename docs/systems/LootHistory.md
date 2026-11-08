# LootHistory

Namespace: `C_LootHistory`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_LootHistory.GetAllEncounterInfos](#c_loothistorygetallencounterinfos) | 1 value | 1 value |
| ✅ | [C_LootHistory.GetInfoForEncounter](#c_loothistorygetinfoforencounter) |  |  |
| ✅ | [C_LootHistory.GetLootHistoryTime](#c_loothistorygetloothistorytime) | 1 value | 1 value |
| ✅ | [C_LootHistory.GetSortedDropsForEncounter](#c_loothistorygetsorteddropsforencounter) |  |  |
| ✅ | [C_LootHistory.GetSortedInfoForDrop](#c_loothistorygetsortedinfofordrop) |  |  |

### C_LootHistory.GetAllEncounterInfos

`C_LootHistory.GetAllEncounterInfos() → infos: EncounterLootInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `LootHistoryDocumentation.lua`

### C_LootHistory.GetInfoForEncounter

`C_LootHistory.GetInfoForEncounter(encounterID: number) → info: EncounterLootInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LootHistoryDocumentation.lua`

### C_LootHistory.GetLootHistoryTime

`C_LootHistory.GetLootHistoryTime() → time: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `LootHistoryDocumentation.lua`

### C_LootHistory.GetSortedDropsForEncounter

`C_LootHistory.GetSortedDropsForEncounter(encounterID: number) → drops: EncounterLootDropInfo[]?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LootHistoryDocumentation.lua`

### C_LootHistory.GetSortedInfoForDrop

`C_LootHistory.GetSortedInfoForDrop(encounterID: number, lootListKey: number) → info: EncounterLootDropInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LootHistoryDocumentation.lua`

## Events

### LOOT_HISTORY_CLEAR_HISTORY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (0 in combat); argument kinds: ``

### LOOT_HISTORY_GO_TO_ENCOUNTER

- Status: ✅ verified
- Payload: `encounterID: number`
- unique event (Blizzard's docs)

### LOOT_HISTORY_ONE_HUNDRED_ROLL

- Status: ✅ verified
- Payload: `encounterID: number`, `lootListKey: number`
- fires synchronously (Blizzard's docs)

### LOOT_HISTORY_UPDATE_DROP

- Status: ✅ verified
- Payload: `encounterID: number`, `lootListKey: number`
- unique event (Blizzard's docs)

### LOOT_HISTORY_UPDATE_ENCOUNTER

- Status: ✅ verified
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

- Enumeration — ✅ verified
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
