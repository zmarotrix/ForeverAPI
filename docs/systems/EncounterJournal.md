# EncounterJournal

Namespace: `C_EncounterJournal`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_EncounterJournal.GetBaseDifficultyID](#c_encounterjournalgetbasedifficultyid) |  |  |
| ✅ | [C_EncounterJournal.GetDungeonEntrancesForMap](#c_encounterjournalgetdungeonentrancesformap) |  |  |
| ✅ | [C_EncounterJournal.GetEncounterJournalLink](#c_encounterjournalgetencounterjournallink) |  |  |
| ✅ | [C_EncounterJournal.GetEncountersOnMap](#c_encounterjournalgetencountersonmap) |  |  |
| ✅ | [C_EncounterJournal.GetInstanceForGameMap](#c_encounterjournalgetinstanceforgamemap) |  |  |
| ✅ | [C_EncounterJournal.GetLootInfo](#c_encounterjournalgetlootinfo) |  |  |
| ✅ | [C_EncounterJournal.GetLootInfoByIndex](#c_encounterjournalgetlootinfobyindex) |  |  |
| ✅ | [C_EncounterJournal.GetSectionIconFlags](#c_encounterjournalgetsectioniconflags) |  |  |
| ✅ | [C_EncounterJournal.GetSectionInfo](#c_encounterjournalgetsectioninfo) |  |  |
| ✅ | [C_EncounterJournal.GetSlotFilter](#c_encounterjournalgetslotfilter) | 1 value |  |
| ✅ | [C_EncounterJournal.InitalizeSelectedTier](#c_encounterjournalinitalizeselectedtier) |  |  |
| ✅ | [C_EncounterJournal.InstanceHasDifficultyID](#c_encounterjournalinstancehasdifficultyid) |  |  |
| ✅ | [C_EncounterJournal.InstanceHasLoot](#c_encounterjournalinstancehasloot) |  |  |
| ✅ | [C_EncounterJournal.IsEncounterComplete](#c_encounterjournalisencountercomplete) |  |  |
| ✅ | [C_EncounterJournal.OnClose](#c_encounterjournalonclose) |  |  |
| ✅ | [C_EncounterJournal.OnOpen](#c_encounterjournalonopen) |  |  |
| ✅ | [C_EncounterJournal.ResetSlotFilter](#c_encounterjournalresetslotfilter) |  |  |
| ✅ | [C_EncounterJournal.SetPreviewMythicPlusLevel](#c_encounterjournalsetpreviewmythicpluslevel) |  |  |
| ✅ | [C_EncounterJournal.SetPreviewPvpTier](#c_encounterjournalsetpreviewpvptier) |  |  |
| ✅ | [C_EncounterJournal.SetSlotFilter](#c_encounterjournalsetslotfilter) |  |  |
| ✅ | [C_EncounterJournal.SetTab](#c_encounterjournalsettab) |  |  |
| ✅ | [C_EncounterJournal.StartArathiRPE](#c_encounterjournalstartarathirpe) |  |  |

### C_EncounterJournal.GetBaseDifficultyID

`C_EncounterJournal.GetBaseDifficultyID(difficultyID: number) → baseDifficultyID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.GetDungeonEntrancesForMap

`C_EncounterJournal.GetDungeonEntrancesForMap(uiMapID: number) → dungeonEntrances: DungeonEntranceMapInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.GetEncounterJournalLink

`C_EncounterJournal.GetEncounterJournalLink(linkType: JournalLinkTypes, ID: number, displayText: string, difficultyID: number) → link: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.GetEncountersOnMap

`C_EncounterJournal.GetEncountersOnMap(uiMapID: number) → encounters: EncounterJournalMapEncounterInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.GetInstanceForGameMap

`C_EncounterJournal.GetInstanceForGameMap(mapID: number) → journalInstanceID: number?`

- Status: ✅ verified (function)
- Blizzard: GameMap as opposed to UIMap since we use a mapID not a uiMapID.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.GetLootInfo

`C_EncounterJournal.GetLootInfo(id: number) → itemInfo: EncounterJournalItemInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.GetLootInfoByIndex

`C_EncounterJournal.GetLootInfoByIndex(index: luaIndex, encounterIndex: luaIndex?) → itemInfo: EncounterJournalItemInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.GetSectionIconFlags

`C_EncounterJournal.GetSectionIconFlags(sectionID: number) → iconFlags: number[]?`

- Status: ✅ verified (function)
- Blizzard: Represents the icon indices for this EJ section.  An icon index can be used to arrive at texture coordinates for specific encounter types, e.g.: EncounterJournal_SetFlagIcon
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.GetSectionInfo

`C_EncounterJournal.GetSectionInfo(sectionID: number) → info: EncounterJournalSectionInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.GetSlotFilter

`C_EncounterJournal.GetSlotFilter() → filter: ItemSlotFilterType`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.InitalizeSelectedTier

`C_EncounterJournal.InitalizeSelectedTier()`

- Status: ✅ verified (function)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.InstanceHasDifficultyID

`C_EncounterJournal.InstanceHasDifficultyID(difficultyID: number) → hasDifficultyID: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.InstanceHasLoot

`C_EncounterJournal.InstanceHasLoot(instanceID: number?) → hasLoot: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.IsEncounterComplete

`C_EncounterJournal.IsEncounterComplete(journalEncounterID: number) → isEncounterComplete: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.OnClose

`C_EncounterJournal.OnClose()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.OnOpen

`C_EncounterJournal.OnOpen()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.ResetSlotFilter

`C_EncounterJournal.ResetSlotFilter()`

- Status: ✅ verified (function)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.SetPreviewMythicPlusLevel

`C_EncounterJournal.SetPreviewMythicPlusLevel(level: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.SetPreviewPvpTier

`C_EncounterJournal.SetPreviewPvpTier(tier: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.SetSlotFilter

`C_EncounterJournal.SetSlotFilter(filterSlot: ItemSlotFilterType)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.SetTab

`C_EncounterJournal.SetTab(tabIdx: number)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterJournalDocumentation.lua`

### C_EncounterJournal.StartArathiRPE

`C_EncounterJournal.StartArathiRPE()`

- Status: ✅ verified (function)
- Source: client docs `EncounterJournalDocumentation.lua`

## Events

### EJ_DIFFICULTY_UPDATE

- Status: ✅ verified
- Payload: `difficultyID: number`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `n`

### EJ_LOOT_DATA_RECIEVED

- Status: ✅ verified
- Payload: `itemID: number?`
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### SHOW_JOURNEYS_UI

- Status: ✅ verified
- Payload: `factionID: number`
- Blizzard: Signaled when the UI needs to display the journeys dashboard at a specific faction.
- fires synchronously (Blizzard's docs)

## Types

### DungeonEntranceMapInfo

- Structure
  - `areaPoiID`: number
  - `position`: vector2
  - `name`: cstring
  - `description`: cstring
  - `atlasName`: string
  - `journalInstanceID`: number

### EncounterJournalItemInfo

- Structure
  - `itemID`: number
  - `encounterID`: number?
  - `name`: string?
  - `itemQuality`: string?
  - `filterType`: ItemSlotFilterType?
  - `icon`: fileID?
  - `slot`: string?
  - `armorType`: string?
  - `link`: string?
  - `handError`: bool?
  - `weaponTypeError`: bool?
  - `displayAsPerPlayerLoot`: bool?
  - `displayAsVeryRare`: bool?
  - `displayAsExtremelyRare`: bool?
  - `displaySeasonID`: number?

### EncounterJournalMapEncounterInfo

- Structure
  - `encounterID`: number
  - `mapX`: number
  - `mapY`: number

### EncounterJournalSectionInfo

- Structure
  - `spellID`: number
  - `title`: cstring
  - `description`: string?
  - `headerType`: number
  - `abilityIcon`: fileID
  - `creatureDisplayID`: number
  - `uiModelSceneID`: number
  - `siblingSectionID`: number?
  - `firstChildSectionID`: number?
  - `filteredByDifficulty`: bool
  - `link`: string
  - `startsOpen`: bool

### ItemSlotFilterType

- Enumeration — ✅ verified
  - `Head` = 0
  - `Neck` = 1
  - `Shoulder` = 2
  - `Cloak` = 3
  - `Chest` = 4
  - `Wrist` = 5
  - `Hand` = 6
  - `Waist` = 7
  - `Legs` = 8
  - `Feet` = 9
  - `MainHand` = 10
  - `OffHand` = 11
  - `Finger` = 12
  - `Trinket` = 13
  - `Other` = 14
  - `NoFilter` = 15
