# PaperDollInfo

Namespace: `C_PaperDollInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_PaperDollInfo.AmmoNeeded](#c_paperdollinfoammoneeded) |  |  |
| ❔ | [C_PaperDollInfo.CanAutoEquipCursorItem](#c_paperdollinfocanautoequipcursoritem) |  |  |
| ❔ | [C_PaperDollInfo.CancelTemporaryEnchantment](#c_paperdollinfocanceltemporaryenchantment) |  |  |
| ❔ | [C_PaperDollInfo.CursorCanGoInSlot](#c_paperdollinfocursorcangoinslot) |  |  |
| ❔ | [C_PaperDollInfo.GetArmorEffectiveness](#c_paperdollinfogetarmoreffectiveness) |  |  |
| ❔ | [C_PaperDollInfo.GetArmorEffectivenessAgainstTarget](#c_paperdollinfogetarmoreffectivenessagainsttarget) |  |  |
| ❔ | [C_PaperDollInfo.GetInspectAzeriteItemEmpoweredChoices](#c_paperdollinfogetinspectazeriteitemempoweredchoices) |  |  |
| ❔ | [C_PaperDollInfo.GetInspectGuildInfo](#c_paperdollinfogetinspectguildinfo) |  |  |
| ❔ | [C_PaperDollInfo.GetInspectItemLevel](#c_paperdollinfogetinspectitemlevel) |  |  |
| ❔ | [C_PaperDollInfo.GetInspectRatedBGBlitzData](#c_paperdollinfogetinspectratedbgblitzdata) |  |  |
| ❔ | [C_PaperDollInfo.GetInspectRatedBGData](#c_paperdollinfogetinspectratedbgdata) |  |  |
| ❔ | [C_PaperDollInfo.GetInspectRatedSoloShuffleData](#c_paperdollinfogetinspectratedsoloshuffledata) |  |  |
| ❔ | [C_PaperDollInfo.GetInventorySlotInfo](#c_paperdollinfogetinventoryslotinfo) |  |  |
| ❔ | [C_PaperDollInfo.GetInventorySlotInfoForInvSlot](#c_paperdollinfogetinventoryslotinfoforinvslot) |  |  |
| ❔ | [C_PaperDollInfo.GetMinItemLevel](#c_paperdollinfogetminitemlevel) |  |  |
| ❔ | [C_PaperDollInfo.GetStaggerPercentage](#c_paperdollinfogetstaggerpercentage) |  |  |
| ❔ | [C_PaperDollInfo.GetTemporaryEnchantmentInfo](#c_paperdollinfogettemporaryenchantmentinfo) |  |  |
| ❔ | [C_PaperDollInfo.IsInventorySlotEnabled](#c_paperdollinfoisinventoryslotenabled) |  |  |
| ❔ | [C_PaperDollInfo.IsRangedSlotShown](#c_paperdollinfoisrangedslotshown) |  |  |
| ❔ | [C_PaperDollInfo.OffhandHasShield](#c_paperdollinfooffhandhasshield) |  |  |
| ❔ | [C_PaperDollInfo.OffhandHasWeapon](#c_paperdollinfooffhandhasweapon) |  |  |

### C_PaperDollInfo.AmmoNeeded

`C_PaperDollInfo.AmmoNeeded() → ammoNeeded: bool`

- Status: ❔ unverified
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.CanAutoEquipCursorItem

`C_PaperDollInfo.CanAutoEquipCursorItem() → canAutoEquip: bool`

- Status: ❔ unverified
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.CancelTemporaryEnchantment

`C_PaperDollInfo.CancelTemporaryEnchantment(slot: LuaInventorySlot)`

- Status: ❔ unverified
- Blizzard: Cancels active temporary enchantments on inventory slot items. Imbue enchants take priority over temporary enchants.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.CursorCanGoInSlot

`C_PaperDollInfo.CursorCanGoInSlot(slotIndex: luaIndex) → canOccupySlot: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetArmorEffectiveness

`C_PaperDollInfo.GetArmorEffectiveness(armor: number, attackerLevel: number) → effectiveness: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetArmorEffectivenessAgainstTarget

`C_PaperDollInfo.GetArmorEffectivenessAgainstTarget(armor: number) → effectiveness: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectAzeriteItemEmpoweredChoices

`C_PaperDollInfo.GetInspectAzeriteItemEmpoweredChoices(unit: UnitToken, equipmentSlotIndex: luaIndex) → azeritePowerIDs: number[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectGuildInfo

`C_PaperDollInfo.GetInspectGuildInfo(unitString: string) → achievementPoints: number, numMembers: number, guildName: string, realmName: string`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectItemLevel

`C_PaperDollInfo.GetInspectItemLevel(unit: UnitToken) → equippedItemLevel: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectRatedBGBlitzData

`C_PaperDollInfo.GetInspectRatedBGBlitzData() → ratedBGBlitzData: InspectPVPData`

- Status: ❔ unverified
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectRatedBGData

`C_PaperDollInfo.GetInspectRatedBGData() → ratedBGData: InspectRatedBGData`

- Status: ❔ unverified
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInspectRatedSoloShuffleData

`C_PaperDollInfo.GetInspectRatedSoloShuffleData() → ratedSoloShuffleData: InspectPVPData`

- Status: ❔ unverified
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInventorySlotInfo

`C_PaperDollInfo.GetInventorySlotInfo(slotName: cstring) → invSlot: number, slotTexture: fileID, checkRelic: bool`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetInventorySlotInfoForInvSlot

`C_PaperDollInfo.GetInventorySlotInfoForInvSlot(invSlotValue: number) → invSlot: number, slotTexture: fileID, checkRelic: bool, slotName: cstring`

- Status: ❔ unverified
- `invSlotValue`: This is the Lua version of the INVSLOT enum, not a luaIndex
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetMinItemLevel

`C_PaperDollInfo.GetMinItemLevel() → minItemLevel: number?`

- Status: ❔ unverified
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetStaggerPercentage

`C_PaperDollInfo.GetStaggerPercentage(unit: UnitToken) → stagger: number, staggerAgainstTarget: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.GetTemporaryEnchantmentInfo

`C_PaperDollInfo.GetTemporaryEnchantmentInfo(slot: LuaInventorySlot) → enchantInfo: TemporaryItemEnchantInfo`

- Status: ❔ unverified
- Blizzard: Queries information about active temporary enchants on inventory slot items. Imbue enchants take priority over temporary enchants.
- `slot`: An appropriate INVSLOT_ constant.
- `enchantInfo`: Returns nothing if no temporary enchantment is active for this slot.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.IsInventorySlotEnabled

`C_PaperDollInfo.IsInventorySlotEnabled(slotName: stringView) → isEnabled: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.IsRangedSlotShown

`C_PaperDollInfo.IsRangedSlotShown() → isShown: bool`

- Status: ❔ unverified
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.OffhandHasShield

`C_PaperDollInfo.OffhandHasShield() → offhandHasShield: bool`

- Status: ❔ unverified
- Source: client docs `PaperDollInfoDocumentation.lua`

### C_PaperDollInfo.OffhandHasWeapon

`C_PaperDollInfo.OffhandHasWeapon() → offhandHasWeapon: bool`

- Status: ❔ unverified
- Source: client docs `PaperDollInfoDocumentation.lua`

## Events

### AVOIDANCE_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHARACTER_POINTS_CHANGED

- Status: ❔ unverified
- Payload: `change: number`
- fires synchronously (Blizzard's docs)

### CHARACTER_UPGRADE_SPELL_TIER_SET

- Status: ❔ unverified
- Payload: `tierIndex: number`
- fires synchronously (Blizzard's docs)

### COMBAT_RATING_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### DISABLE_XP_GAIN

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ENABLE_XP_GAIN

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### EQUIP_BIND_CONFIRM

- Status: ❔ unverified
- Payload: `slot: number`, `itemLocation: ItemLocation`
- fires synchronously (Blizzard's docs)

### INSPECT_HONOR_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### INSPECT_READY

- Status: ❔ unverified
- Payload: `inspecteeGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### LIFESTEAL_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### MASTERY_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_STATS_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_AVG_ITEM_LEVEL_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_EQUIPMENT_CHANGED

- Status: ❔ unverified
- Payload: `equipmentSlot: number`, `hasCurrent: bool`
- fires synchronously (Blizzard's docs)

### PROFESSION_EQUIPMENT_CHANGED

- Status: ❔ unverified
- Payload: `skillLineID: number`, `isTool: bool`
- fires synchronously (Blizzard's docs)

### PVP_POWER_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SPEED_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SPELL_POWER_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### STURDINESS_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_FACTION

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_INVENTORY_ALERTS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_INVENTORY_DURABILITY

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### WEAPON_SLOT_CHANGED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

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
