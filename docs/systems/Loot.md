# Loot

Namespace: `C_Loot`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Loot.GetLootRollDuration](#c_lootgetlootrollduration) |  |  |
| ❔ | [C_Loot.IsLegacyLootModeEnabled](#c_lootislegacylootmodeenabled) |  |  |

### C_Loot.GetLootRollDuration

`C_Loot.GetLootRollDuration(rollID: number) → duration: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LootDocumentation.lua`

### C_Loot.IsLegacyLootModeEnabled

`C_Loot.IsLegacyLootModeEnabled() → isLegacyLootModeEnabled: bool`

- Status: ❔ unverified
- Source: client docs `LootDocumentation.lua`

## Events

### AZERITE_EMPOWERED_ITEM_LOOTED

- Status: ❔ unverified
- Payload: `itemLink: cstring`
- fires synchronously (Blizzard's docs)

### BONUS_ROLL_ACTIVATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### BONUS_ROLL_DEACTIVATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### BONUS_ROLL_FAILED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### BONUS_ROLL_RESULT

- Status: ❔ unverified
- Payload: `typeIdentifier: cstring`, `itemLink: cstring`, `quantity: number`, `specID: number`, `sex: number`, `personalLootToast: bool`, `currencyID: number?`, `isSecondaryResult: bool`, `corrupted: bool`
- fires synchronously (Blizzard's docs)

### BONUS_ROLL_STARTED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CANCEL_ALL_LOOT_ROLLS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CANCEL_LOOT_ROLL

- Status: ❔ unverified
- Payload: `rollID: number`
- fires synchronously (Blizzard's docs)

### CONFIRM_DISENCHANT_ROLL

- Status: ❔ unverified
- Payload: `rollID: number`, `rollType: number`
- fires synchronously (Blizzard's docs)

### CONFIRM_LOOT_ROLL

- Status: ❔ unverified
- Payload: `rollID: number`, `rollType: number`, `confirmReason: cstring`
- fires synchronously (Blizzard's docs)

### ENCOUNTER_LOOT_RECEIVED

- Status: ❔ unverified
- Payload: `encounterID: number`, `itemID: number`, `itemLink: cstring`, `quantity: number`, `itemName: cstring`, `fileName: cstring`
- fires synchronously (Blizzard's docs)

### GARRISON_MISSION_BONUS_ROLL_LOOT

- Status: ❔ unverified
- Payload: `itemID: number`, `quantity: number`
- fires synchronously (Blizzard's docs)

### ITEM_PUSH

- Status: ❔ unverified
- Payload: `bagSlot: luaIndex`, `iconFileID: number`
- fires synchronously (Blizzard's docs)

### LEGACY_LOOT_RULES_CHANGED

- Status: ❔ unverified
- Payload: `isLegacyLootModeEnabled: bool`
- fires synchronously (Blizzard's docs)

### LOOT_BIND_CONFIRM

- Status: ❔ unverified
- Payload: `lootSlot: luaIndex`
- fires synchronously (Blizzard's docs)

### LOOT_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LOOT_ITEM_AVAILABLE

- Status: ❔ unverified
- Payload: `itemTooltip: cstring`, `lootHandle: number`
- fires synchronously (Blizzard's docs)

### LOOT_ITEM_ROLL_WON

- Status: ❔ unverified
- Payload: `itemLink: cstring`, `rollQuantity: number`, `rollType: number`, `roll: number`, `upgraded: bool`
- fires synchronously (Blizzard's docs)

### LOOT_OPENED

- Status: ❔ unverified
- Payload: `autoLoot: bool`, `isFromItem: bool`
- fires synchronously (Blizzard's docs)

### LOOT_READY

- Status: ❔ unverified
- Payload: `autoloot: bool`
- fires synchronously (Blizzard's docs)

### LOOT_ROLLS_COMPLETE

- Status: ❔ unverified
- Payload: `lootHandle: number`
- fires synchronously (Blizzard's docs)

### LOOT_SLOT_CHANGED

- Status: ❔ unverified
- Payload: `lootSlot: luaIndex`
- fires synchronously (Blizzard's docs)

### LOOT_SLOT_CLEARED

- Status: ❔ unverified
- Payload: `lootSlot: luaIndex`
- fires synchronously (Blizzard's docs)

### MAIN_SPEC_NEED_ROLL

- Status: ❔ unverified
- Payload: `rollID: number`, `roll: number`, `isWinning: bool`
- fires synchronously (Blizzard's docs)

### OPEN_MASTER_LOOT_LIST

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_LOOT_RECEIVED

- Status: ❔ unverified
- Payload: `typeIdentifier: cstring`, `itemLink: cstring`, `quantity: number`
- fires synchronously (Blizzard's docs)

### PLAYER_LOOT_SPEC_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### QUEST_CURRENCY_LOOT_RECEIVED

- Status: ❔ unverified
- Payload: `questID: number`, `currencyId: number`, `quantity: number`
- fires synchronously (Blizzard's docs)

### QUEST_LOOT_RECEIVED

- Status: ❔ unverified
- Payload: `questID: number`, `itemLink: cstring`, `quantity: number`
- fires synchronously (Blizzard's docs)

### SHOW_LOOT_TOAST

- Status: ❔ unverified
- Payload: `typeIdentifier: cstring`, `itemLink: cstring`, `quantity: number`, `specID: number`, `sex: number`, `personalLootToast: bool`, `toastMethod: number`, `lessAwesome: bool`, `upgraded: bool`, `corrupted: bool`
- fires synchronously (Blizzard's docs)

### SHOW_LOOT_TOAST_LEGENDARY_LOOTED

- Status: ❔ unverified
- Payload: `itemLink: cstring`
- fires synchronously (Blizzard's docs)

### SHOW_LOOT_TOAST_UPGRADE

- Status: ❔ unverified
- Payload: `itemLink: cstring`, `quantity: number`, `specID: number`, `sex: number`, `baseQuality: number`, `personalLootToast: bool`, `lessAwesome: bool`
- fires synchronously (Blizzard's docs)

### SHOW_PVP_FACTION_LOOT_TOAST

- Status: ❔ unverified
- Payload: `typeIdentifier: cstring`, `itemLink: cstring`, `quantity: number`, `specID: number`, `sex: number`, `personalLootToast: bool`, `lessAwesome: bool`
- fires synchronously (Blizzard's docs)

### SHOW_RATED_PVP_REWARD_TOAST

- Status: ❔ unverified
- Payload: `typeIdentifier: cstring`, `itemLink: cstring`, `quantity: number`, `specID: number`, `sex: number`, `personalLootToast: bool`, `lessAwesome: bool`
- fires synchronously (Blizzard's docs)

### START_LOOT_ROLL

- Status: ❔ unverified
- Payload: `rollID: number`, `rollTime: number`, `lootHandle: number?`
- fires synchronously (Blizzard's docs)

### TRIAL_CAP_REACHED_MONEY

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_MASTER_LOOT_LIST

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
