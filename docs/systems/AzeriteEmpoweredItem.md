# AzeriteEmpoweredItem

Namespace: `C_AzeriteEmpoweredItem`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AzeriteEmpoweredItem.CanSelectPower](#c_azeriteempowereditemcanselectpower) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.ConfirmAzeriteEmpoweredItemRespec](#c_azeriteempowereditemconfirmazeriteempowereditemrespec) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.GetAllTierInfo](#c_azeriteempowereditemgetalltierinfo) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.GetAllTierInfoByItemID](#c_azeriteempowereditemgetalltierinfobyitemid) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.GetAzeriteEmpoweredItemRespecCost](#c_azeriteempowereditemgetazeriteempowereditemrespeccost) | 1 value |  |
| ✅ | [C_AzeriteEmpoweredItem.GetPowerInfo](#c_azeriteempowereditemgetpowerinfo) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.GetPowerText](#c_azeriteempowereditemgetpowertext) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.GetSpecsForPower](#c_azeriteempowereditemgetspecsforpower) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.HasAnyUnselectedPowers](#c_azeriteempowereditemhasanyunselectedpowers) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.HasBeenViewed](#c_azeriteempowereditemhasbeenviewed) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.IsAzeriteEmpoweredItem](#c_azeriteempowereditemisazeriteempowereditem) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.IsAzeriteEmpoweredItemByID](#c_azeriteempowereditemisazeriteempowereditembyid) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.IsAzeritePreviewSourceDisplayable](#c_azeriteempowereditemisazeritepreviewsourcedisplayable) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.IsHeartOfAzerothEquipped](#c_azeriteempowereditemisheartofazerothequipped) | 1 value |  |
| ✅ | [C_AzeriteEmpoweredItem.IsPowerAvailableForSpec](#c_azeriteempowereditemispoweravailableforspec) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.IsPowerSelected](#c_azeriteempowereditemispowerselected) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.SelectPower](#c_azeriteempowereditemselectpower) |  |  |
| ✅ | [C_AzeriteEmpoweredItem.SetHasBeenViewed](#c_azeriteempowereditemsethasbeenviewed) |  |  |

### C_AzeriteEmpoweredItem.CanSelectPower

`C_AzeriteEmpoweredItem.CanSelectPower(azeriteEmpoweredItemLocation: AzeriteEmpoweredItemLocation, powerID: number) → canSelect: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.ConfirmAzeriteEmpoweredItemRespec

`C_AzeriteEmpoweredItem.ConfirmAzeriteEmpoweredItemRespec(azeriteEmpoweredItemLocation: AzeriteEmpoweredItemLocation)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.GetAllTierInfo

`C_AzeriteEmpoweredItem.GetAllTierInfo(azeriteEmpoweredItemLocation: AzeriteEmpoweredItemLocation) → tierInfo: AzeriteEmpoweredItemTierInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.GetAllTierInfoByItemID

`C_AzeriteEmpoweredItem.GetAllTierInfoByItemID(itemInfo: ItemInfo, classID: number?) → tierInfo: AzeriteEmpoweredItemTierInfo[]`

- Status: ✅ verified (function)
- `classID`: Specify a class ID to get tier information about that class, otherwise uses the player's class if left nil
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.GetAzeriteEmpoweredItemRespecCost

`C_AzeriteEmpoweredItem.GetAzeriteEmpoweredItemRespecCost() → cost: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.GetPowerInfo

`C_AzeriteEmpoweredItem.GetPowerInfo(powerID: number) → powerInfo: AzeriteEmpoweredItemPowerInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.GetPowerText

`C_AzeriteEmpoweredItem.GetPowerText(azeriteEmpoweredItemLocation: AzeriteEmpoweredItemLocation, powerID: number, level: AzeritePowerLevel) → powerText: AzeriteEmpoweredItemPowerText`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.GetSpecsForPower

`C_AzeriteEmpoweredItem.GetSpecsForPower(powerID: number) → specInfo: AzeriteSpecInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.HasAnyUnselectedPowers

`C_AzeriteEmpoweredItem.HasAnyUnselectedPowers(azeriteEmpoweredItemLocation: AzeriteEmpoweredItemLocation) → hasAnyUnselectedPowers: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.HasBeenViewed

`C_AzeriteEmpoweredItem.HasBeenViewed(azeriteEmpoweredItemLocation: AzeriteEmpoweredItemLocation) → hasBeenViewed: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.IsAzeriteEmpoweredItem

`C_AzeriteEmpoweredItem.IsAzeriteEmpoweredItem(itemLocation: ItemLocation) → isAzeriteEmpoweredItem: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.IsAzeriteEmpoweredItemByID

`C_AzeriteEmpoweredItem.IsAzeriteEmpoweredItemByID(itemInfo: ItemInfo) → isAzeriteEmpoweredItem: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.IsAzeritePreviewSourceDisplayable

`C_AzeriteEmpoweredItem.IsAzeritePreviewSourceDisplayable(itemInfo: ItemInfo, classID: number?) → isAzeritePreviewSourceDisplayable: bool`

- Status: ✅ verified (function)
- `classID`: Specify a class ID to determine if its displayable for that class, otherwise uses the player's class if left nil
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.IsHeartOfAzerothEquipped

`C_AzeriteEmpoweredItem.IsHeartOfAzerothEquipped() → isHeartOfAzerothEquipped: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.IsPowerAvailableForSpec

`C_AzeriteEmpoweredItem.IsPowerAvailableForSpec(powerID: number, specID: number) → isPowerAvailableForSpec: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.IsPowerSelected

`C_AzeriteEmpoweredItem.IsPowerSelected(azeriteEmpoweredItemLocation: AzeriteEmpoweredItemLocation, powerID: number) → isSelected: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.SelectPower

`C_AzeriteEmpoweredItem.SelectPower(azeriteEmpoweredItemLocation: AzeriteEmpoweredItemLocation, powerID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

### C_AzeriteEmpoweredItem.SetHasBeenViewed

`C_AzeriteEmpoweredItem.SetHasBeenViewed(azeriteEmpoweredItemLocation: AzeriteEmpoweredItemLocation)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEmpoweredItemDocumentation.lua`

## Events

### AZERITE_EMPOWERED_ITEM_EQUIPPED_STATUS_CHANGED

- Status: ✅ verified
- Payload: `isHeartEquipped: bool`
- fires synchronously (Blizzard's docs)

### AZERITE_EMPOWERED_ITEM_SELECTION_UPDATED

- Status: ✅ verified
- Payload: `azeriteEmpoweredItemLocation: AzeriteEmpoweredItemLocation`
- fires synchronously (Blizzard's docs)

## Types

### AzeriteEmpoweredItemPowerInfo

- Structure
  - `azeritePowerID`: number
  - `spellID`: number

### AzeriteEmpoweredItemPowerText

- Structure
  - `name`: string
  - `description`: string

### AzeriteEmpoweredItemTierInfo

- Structure
  - `azeritePowerIDs`: number[]
  - `unlockLevel`: number

### AzeritePowerLevel

- Enumeration — ✅ verified
  - `Base` = 0
  - `Upgraded` = 1
  - `Downgraded` = 2

### AzeriteSpecInfo

- Structure
  - `classID`: number
  - `specID`: number
