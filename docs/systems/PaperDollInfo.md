# PaperDollInfo

Namespace: `C_PaperDollInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PaperDollInfo.AmmoNeeded](#c_paperdollinfoammoneeded) |  |  |
| ✅ | [C_PaperDollInfo.CanAutoEquipCursorItem](#c_paperdollinfocanautoequipcursoritem) | 1 value | 1 value |
| ✅ | [C_PaperDollInfo.CancelTemporaryEnchantment](#c_paperdollinfocanceltemporaryenchantment) |  |  |
| ✅ | [C_PaperDollInfo.CursorCanGoInSlot](#c_paperdollinfocursorcangoinslot) |  |  |
| ✅ | [C_PaperDollInfo.GetArmorEffectiveness](#c_paperdollinfogetarmoreffectiveness) |  |  |
| ✅ | [C_PaperDollInfo.GetArmorEffectivenessAgainstTarget](#c_paperdollinfogetarmoreffectivenessagainsttarget) |  |  |
| ✅ | [C_PaperDollInfo.GetInspectAzeriteItemEmpoweredChoices](#c_paperdollinfogetinspectazeriteitemempoweredchoices) | 0 values | 0 values |
| ✅ | [C_PaperDollInfo.GetInspectGuildInfo](#c_paperdollinfogetinspectguildinfo) |  |  |
| ✅ | [C_PaperDollInfo.GetInspectItemLevel](#c_paperdollinfogetinspectitemlevel) | 1 value | 1 value |
| ✅ | [C_PaperDollInfo.GetInspectRatedBGBlitzData](#c_paperdollinfogetinspectratedbgblitzdata) | 1 value | 1 value |
| ✅ | [C_PaperDollInfo.GetInspectRatedBGData](#c_paperdollinfogetinspectratedbgdata) | 1 value | 1 value |
| ✅ | [C_PaperDollInfo.GetInspectRatedSoloShuffleData](#c_paperdollinfogetinspectratedsoloshuffledata) | 1 value | 1 value |
| ✅ | [C_PaperDollInfo.GetInventorySlotInfo](#c_paperdollinfogetinventoryslotinfo) |  |  |
| ✅ | [C_PaperDollInfo.GetInventorySlotInfoForInvSlot](#c_paperdollinfogetinventoryslotinfoforinvslot) |  |  |
| ✅ | [C_PaperDollInfo.GetMinItemLevel](#c_paperdollinfogetminitemlevel) | 1 value | 1 value |
| ✅ | [C_PaperDollInfo.GetStaggerPercentage](#c_paperdollinfogetstaggerpercentage) | 2 values | 2 values |
| ✅ | [C_PaperDollInfo.GetTemporaryEnchantmentInfo](#c_paperdollinfogettemporaryenchantmentinfo) |  |  |
| ✅ | [C_PaperDollInfo.IsInventorySlotEnabled](#c_paperdollinfoisinventoryslotenabled) |  |  |
| ✅ | [C_PaperDollInfo.IsRangedSlotShown](#c_paperdollinfoisrangedslotshown) | 1 value | 1 value |
| ✅ | [C_PaperDollInfo.OffhandHasShield](#c_paperdollinfooffhandhasshield) |  |  |
| ✅ | [C_PaperDollInfo.OffhandHasWeapon](#c_paperdollinfooffhandhasweapon) |  |  |

### C_PaperDollInfo.AmmoNeeded

`C_PaperDollInfo.AmmoNeeded() → ammoNeeded: bool`

- Status: ✅ verified (function)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.CanAutoEquipCursorItem

`C_PaperDollInfo.CanAutoEquipCursorItem() → canAutoEquip: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.CancelTemporaryEnchantment

`C_PaperDollInfo.CancelTemporaryEnchantment(slot: LuaInventorySlot)`

- Status: ✅ verified (function)
- Blizzard: Cancels active temporary enchantments on inventory slot items. Imbue enchants take priority over temporary enchants.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.CursorCanGoInSlot

`C_PaperDollInfo.CursorCanGoInSlot(slotIndex: luaIndex) → canOccupySlot: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetArmorEffectiveness

`C_PaperDollInfo.GetArmorEffectiveness(armor: number, attackerLevel: number) → effectiveness: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetArmorEffectivenessAgainstTarget

`C_PaperDollInfo.GetArmorEffectivenessAgainstTarget(armor: number) → effectiveness: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectAzeriteItemEmpoweredChoices

`C_PaperDollInfo.GetInspectAzeriteItemEmpoweredChoices(unit: UnitToken, equipmentSlotIndex: luaIndex) → azeritePowerIDs: number[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `unit,n:1`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectGuildInfo

`C_PaperDollInfo.GetInspectGuildInfo(unitString: string) → achievementPoints: number, numMembers: number, guildName: string, realmName: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectItemLevel

`C_PaperDollInfo.GetInspectItemLevel(unit: UnitToken) → equippedItemLevel: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `player`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectRatedBGBlitzData

`C_PaperDollInfo.GetInspectRatedBGBlitzData() → ratedBGBlitzData: InspectPVPData`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{gamesPlayed=number,gamesWon=number,rating=number,roundsPlayed=number,roundsWon=number}`
- Called in combat: returned 1 value: `table{gamesPlayed=number,gamesWon=number,rating=number,roundsPlayed=number,roundsWon=number}`
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectRatedBGData

`C_PaperDollInfo.GetInspectRatedBGData() → ratedBGData: InspectRatedBGData`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{played=number,rating=number,won=number}`
- Called in combat: returned 1 value: `table{played=number,rating=number,won=number}`
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectRatedSoloShuffleData

`C_PaperDollInfo.GetInspectRatedSoloShuffleData() → ratedSoloShuffleData: InspectPVPData`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{gamesPlayed=number,gamesWon=number,rating=number,roundsPlayed=number,roundsWon=number}`
- Called in combat: returned 1 value: `table{gamesPlayed=number,gamesWon=number,rating=number,roundsPlayed=number,roundsWon=number}`
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInventorySlotInfo

`C_PaperDollInfo.GetInventorySlotInfo(slotName: cstring) → invSlot: number, slotTexture: fileID, checkRelic: bool`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInventorySlotInfoForInvSlot

`C_PaperDollInfo.GetInventorySlotInfoForInvSlot(invSlotValue: number) → invSlot: number, slotTexture: fileID, checkRelic: bool, slotName: cstring`

- Status: ✅ verified (function)
- `invSlotValue`: This is the Lua version of the INVSLOT enum, not a luaIndex
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetMinItemLevel

`C_PaperDollInfo.GetMinItemLevel() → minItemLevel: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetStaggerPercentage

`C_PaperDollInfo.GetStaggerPercentage(unit: UnitToken) → stagger: number, staggerAgainstTarget: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `player`: returned 2 values: `number`, `nil`
- Called in combat: returned 2 values: `number`, `nil`
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetTemporaryEnchantmentInfo

`C_PaperDollInfo.GetTemporaryEnchantmentInfo(slot: LuaInventorySlot) → enchantInfo: TemporaryItemEnchantInfo`

- Status: ✅ verified (function)
- Blizzard: Queries information about active temporary enchants on inventory slot items. Imbue enchants take priority over temporary enchants.
- `slot`: An appropriate INVSLOT_ constant.
- `enchantInfo`: Returns nothing if no temporary enchantment is active for this slot.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.IsInventorySlotEnabled

`C_PaperDollInfo.IsInventorySlotEnabled(slotName: stringView) → isEnabled: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.IsRangedSlotShown

`C_PaperDollInfo.IsRangedSlotShown() → isShown: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.OffhandHasShield

`C_PaperDollInfo.OffhandHasShield() → offhandHasShield: bool`

- Status: ✅ verified (function)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.OffhandHasWeapon

`C_PaperDollInfo.OffhandHasWeapon() → offhandHasWeapon: bool`

- Status: ✅ verified (function)
- Source: client docs `PaperDollInfoDocumentation.lua`

## Events

### AVOIDANCE_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHARACTER_POINTS_CHANGED

- Status: ✅ verified
- Payload: `change: number`
- fires synchronously (Blizzard's docs)

### CHARACTER_UPGRADE_SPELL_TIER_SET

- Status: ✅ verified
- Payload: `tierIndex: number`
- fires synchronously (Blizzard's docs)

### COMBAT_RATING_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 39 times (26 in combat); argument kinds: ``

### DISABLE_XP_GAIN

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ENABLE_XP_GAIN

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### EQUIP_BIND_CONFIRM

- Status: ✅ verified
- Payload: `slot: number`, `itemLocation: ItemLocation`
- fires synchronously (Blizzard's docs)

### INSPECT_HONOR_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 3 times (0 in combat); argument kinds: ``

### INSPECT_READY

- Status: ✅ verified
- Payload: `inspecteeGUID: WOWGUID`
- fires synchronously (Blizzard's docs)
- Seen firing 8 times (0 in combat); argument kinds: `s`

### LIFESTEAL_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### MASTERY_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_STATS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_AVG_ITEM_LEVEL_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 18 times (6 in combat); argument kinds: ``

### PLAYER_EQUIPMENT_CHANGED

- Status: ✅ verified
- Payload: `equipmentSlot: number`, `hasCurrent: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `n,b`

### PROFESSION_EQUIPMENT_CHANGED

- Status: ✅ verified
- Payload: `skillLineID: number`, `isTool: bool`
- fires synchronously (Blizzard's docs)

### PVP_POWER_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SPEED_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SPELL_POWER_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### STURDINESS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_FACTION

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 373 times (166 in combat); argument kinds: ``

### UPDATE_INVENTORY_ALERTS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (1 in combat); argument kinds: ``

### UPDATE_INVENTORY_DURABILITY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 638 times (283 in combat); argument kinds: ``

### WEAPON_SLOT_CHANGED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

## Types

### InspectGuildInfo

- Structure
  - `achievementPoints`: number
  - `numMembers`: number
  - `guildName`: string
  - `realmName`: string

### InspectPVPData

- Structure
  - `rating`: number
  - `gamesWon`: number
  - `gamesPlayed`: number
  - `roundsWon`: number
  - `roundsPlayed`: number

### InspectRatedBGData

- Structure
  - `rating`: number
  - `played`: number
  - `won`: number

### TemporaryItemEnchantInfo

- Structure
  - `enchantID`: number
  - `remainingTimeMs`: number
  - `chargesRemaining`: number
  - `hasExpirationTime`: bool
