# LootJournal

Namespace: `C_LootJournal`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_LootJournal.GetItemSetItems](#c_lootjournalgetitemsetitems) |  |  |
| ✅ | [C_LootJournal.GetItemSets](#c_lootjournalgetitemsets) | 1 value | 1 value |

### C_LootJournal.GetItemSetItems

`C_LootJournal.GetItemSetItems(setID: number) → items: LootJournalItemInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LootJournalDocumentation.lua`

### C_LootJournal.GetItemSets

`C_LootJournal.GetItemSets(classID: number?, specID: number?) → itemSets: LootJournalItemSetInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,...(158)}`
- Called in combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,...(158)}`
- Source: client docs `LootJournalDocumentation.lua`

## Events

### LOOT_JOURNAL_ITEM_UPDATE

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

## Types

### LootJournalItemInfo

- Structure
  - `itemID`: number
  - `icon`: fileID
  - `invType`: luaIndex

### LootJournalItemSetInfo

- Structure
  - `setID`: number
  - `itemLevel`: number
  - `name`: cstring
