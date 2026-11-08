# Loot

Namespace: `C_Loot`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Loot.GetLootRollDuration](#c_lootgetlootrollduration) |  |  |
| ✅ | [C_Loot.IsLegacyLootModeEnabled](#c_lootislegacylootmodeenabled) | 1 value | 1 value |

### C_Loot.GetLootRollDuration

`C_Loot.GetLootRollDuration(rollID: number) → duration: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LootDocumentation.lua`

### C_Loot.IsLegacyLootModeEnabled

`C_Loot.IsLegacyLootModeEnabled() → isLegacyLootModeEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LootDocumentation.lua`

## Events

### AZERITE_EMPOWERED_ITEM_LOOTED

- Status: ✅ verified
- Payload: `itemLink: cstring`
- fires synchronously (Blizzard's docs)

### BONUS_ROLL_ACTIVATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BONUS_ROLL_DEACTIVATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BONUS_ROLL_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BONUS_ROLL_RESULT

- Status: ✅ verified
- Payload: `typeIdentifier: cstring`, `itemLink: cstring`, `quantity: number`, `specID: number`, `sex: number`, `personalLootToast: bool`, `currencyID: number?`, `isSecondaryResult: bool`, `corrupted: bool`
- fires synchronously (Blizzard's docs)

### BONUS_ROLL_STARTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CANCEL_ALL_LOOT_ROLLS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 29 times (0 in combat); argument kinds: ``

### CANCEL_LOOT_ROLL

- Status: ✅ verified
- Payload: `rollID: number`
- fires synchronously (Blizzard's docs)
- Seen firing 50 times (13 in combat); argument kinds: `n`

### CONFIRM_DISENCHANT_ROLL

- Status: ✅ verified
- Payload: `rollID: number`, `rollType: number`
- fires synchronously (Blizzard's docs)

### CONFIRM_LOOT_ROLL

- Status: ✅ verified
- Payload: `rollID: number`, `rollType: number`, `confirmReason: cstring`
- fires synchronously (Blizzard's docs)

### ENCOUNTER_LOOT_RECEIVED

- Status: ✅ verified
- Payload: `encounterID: number`, `itemID: number`, `itemLink: cstring`, `quantity: number`, `itemName: cstring`, `fileName: cstring`
- fires synchronously (Blizzard's docs)

### GARRISON_MISSION_BONUS_ROLL_LOOT

- Status: ✅ verified
- Payload: `itemID: number`, `quantity: number`
- fires synchronously (Blizzard's docs)

### ITEM_PUSH

- Status: ✅ verified
- Payload: `bagSlot: luaIndex`, `iconFileID: number`
- fires synchronously (Blizzard's docs)
- Seen firing 237 times (48 in combat); argument kinds: `n,n`

### LEGACY_LOOT_RULES_CHANGED

- Status: ✅ verified
- Payload: `isLegacyLootModeEnabled: bool`
- fires synchronously (Blizzard's docs)

### LOOT_BIND_CONFIRM

- Status: ✅ verified
- Payload: `lootSlot: luaIndex`
- fires synchronously (Blizzard's docs)

### LOOT_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 458 times (124 in combat); argument kinds: ``

### LOOT_ITEM_AVAILABLE

- Status: ✅ verified
- Payload: `itemTooltip: cstring`, `lootHandle: number`
- fires synchronously (Blizzard's docs)

### LOOT_ITEM_ROLL_WON

- Status: ✅ verified
- Payload: `itemLink: cstring`, `rollQuantity: number`, `rollType: number`, `roll: number`, `upgraded: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 9 times (3 in combat); argument kinds: `s,n,n,n,b`

### LOOT_OPENED

- Status: ✅ verified
- Payload: `autoLoot: bool`, `isFromItem: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 115 times (38 in combat); argument kinds: `b,b`

### LOOT_READY

- Status: ✅ verified
- Payload: `autoloot: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 387 times (127 in combat); argument kinds: `b`

### LOOT_ROLLS_COMPLETE

- Status: ✅ verified
- Payload: `lootHandle: number`
- fires synchronously (Blizzard's docs)
- Seen firing 50 times (12 in combat); argument kinds: `n`

### LOOT_SLOT_CHANGED

- Status: ✅ verified
- Payload: `lootSlot: luaIndex`
- fires synchronously (Blizzard's docs)

### LOOT_SLOT_CLEARED

- Status: ✅ verified
- Payload: `lootSlot: luaIndex`
- fires synchronously (Blizzard's docs)
- Seen firing 410 times (124 in combat); argument kinds: `n`

### MAIN_SPEC_NEED_ROLL

- Status: ✅ verified
- Payload: `rollID: number`, `roll: number`, `isWinning: bool`
- fires synchronously (Blizzard's docs)

### OPEN_MASTER_LOOT_LIST

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_LOOT_RECEIVED

- Status: ✅ verified
- Payload: `typeIdentifier: cstring`, `itemLink: cstring`, `quantity: number`
- fires synchronously (Blizzard's docs)

### PLAYER_LOOT_SPEC_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### QUEST_CURRENCY_LOOT_RECEIVED

- Status: ✅ verified
- Payload: `questID: number`, `currencyId: number`, `quantity: number`
- fires synchronously (Blizzard's docs)
- Seen firing 6 times (0 in combat); argument kinds: `n,n,n`

### QUEST_LOOT_RECEIVED

- Status: ✅ verified
- Payload: `questID: number`, `itemLink: cstring`, `quantity: number`
- fires synchronously (Blizzard's docs)
- Seen firing 18 times (0 in combat); argument kinds: `n,s,n`

### SHOW_LOOT_TOAST

- Status: ✅ verified
- Payload: `typeIdentifier: cstring`, `itemLink: cstring`, `quantity: number`, `specID: number`, `sex: number`, `personalLootToast: bool`, `toastMethod: number`, `lessAwesome: bool`, `upgraded: bool`, `corrupted: bool`
- fires synchronously (Blizzard's docs)

### SHOW_LOOT_TOAST_LEGENDARY_LOOTED

- Status: ✅ verified
- Payload: `itemLink: cstring`
- fires synchronously (Blizzard's docs)

### SHOW_LOOT_TOAST_UPGRADE

- Status: ✅ verified
- Payload: `itemLink: cstring`, `quantity: number`, `specID: number`, `sex: number`, `baseQuality: number`, `personalLootToast: bool`, `lessAwesome: bool`
- fires synchronously (Blizzard's docs)

### SHOW_PVP_FACTION_LOOT_TOAST

- Status: ✅ verified
- Payload: `typeIdentifier: cstring`, `itemLink: cstring`, `quantity: number`, `specID: number`, `sex: number`, `personalLootToast: bool`, `lessAwesome: bool`
- fires synchronously (Blizzard's docs)

### SHOW_RATED_PVP_REWARD_TOAST

- Status: ✅ verified
- Payload: `typeIdentifier: cstring`, `itemLink: cstring`, `quantity: number`, `specID: number`, `sex: number`, `personalLootToast: bool`, `lessAwesome: bool`
- fires synchronously (Blizzard's docs)

### START_LOOT_ROLL

- Status: ✅ verified
- Payload: `rollID: number`, `rollTime: number`, `lootHandle: number?`
- fires synchronously (Blizzard's docs)
- Seen firing 50 times (24 in combat); argument kinds: `n,n,n`

### TRIAL_CAP_REACHED_MONEY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_MASTER_LOOT_LIST

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
