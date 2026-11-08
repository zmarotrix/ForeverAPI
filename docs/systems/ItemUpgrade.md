# ItemUpgrade

Namespace: `C_ItemUpgrade`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ItemUpgrade.CanUpgradeItem](#c_itemupgradecanupgradeitem) |  |  |
| ✅ | [C_ItemUpgrade.ClearItemUpgrade](#c_itemupgradeclearitemupgrade) |  |  |
| ✅ | [C_ItemUpgrade.CloseItemUpgrade](#c_itemupgradecloseitemupgrade) |  |  |
| ✅ | [C_ItemUpgrade.GetHighWatermarkForItem](#c_itemupgradegethighwatermarkforitem) |  |  |
| ✅ | [C_ItemUpgrade.GetHighWatermarkForSlot](#c_itemupgradegethighwatermarkforslot) |  |  |
| ✅ | [C_ItemUpgrade.GetHighWatermarkSlotForItem](#c_itemupgradegethighwatermarkslotforitem) |  |  |
| ✅ | [C_ItemUpgrade.GetItemHyperlink](#c_itemupgradegetitemhyperlink) | 0 values |  |
| ✅ | [C_ItemUpgrade.GetItemUpgradeCurrentLevel](#c_itemupgradegetitemupgradecurrentlevel) | 0 values |  |
| ✅ | [C_ItemUpgrade.GetItemUpgradeEffect](#c_itemupgradegetitemupgradeeffect) |  |  |
| ✅ | [C_ItemUpgrade.GetItemUpgradeItemInfo](#c_itemupgradegetitemupgradeiteminfo) | 0 values |  |
| ✅ | [C_ItemUpgrade.GetItemUpgradePvpItemLevelDeltaValues](#c_itemupgradegetitemupgradepvpitemleveldeltavalues) |  |  |
| ✅ | [C_ItemUpgrade.GetNumItemUpgradeEffects](#c_itemupgradegetnumitemupgradeeffects) | 1 value |  |
| ✅ | [C_ItemUpgrade.IsItemBound](#c_itemupgradeisitembound) | 1 value |  |
| ✅ | [C_ItemUpgrade.SetItemUpgradeFromCursorItem](#c_itemupgradesetitemupgradefromcursoritem) |  |  |
| ✅ | [C_ItemUpgrade.SetItemUpgradeFromLocation](#c_itemupgradesetitemupgradefromlocation) |  |  |
| ✅ | [C_ItemUpgrade.UpgradeItem](#c_itemupgradeupgradeitem) |  |  |

### C_ItemUpgrade.CanUpgradeItem

`C_ItemUpgrade.CanUpgradeItem(baseItem: ItemLocation) → isValid: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.ClearItemUpgrade

`C_ItemUpgrade.ClearItemUpgrade()`

- Status: ✅ verified (function)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.CloseItemUpgrade

`C_ItemUpgrade.CloseItemUpgrade()`

- Status: ✅ verified (function)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetHighWatermarkForItem

`C_ItemUpgrade.GetHighWatermarkForItem(itemInfo: ItemInfo) → characterHighWatermark: number, accountHighWatermark: number`

- Status: ✅ verified (function)
- `itemInfo`: Item ID, Link, or Name
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetHighWatermarkForSlot

`C_ItemUpgrade.GetHighWatermarkForSlot(itemRedundancySlot: number) → characterHighWatermark: number, accountHighWatermark: number`

- Status: ✅ verified (function)
- `itemRedundancySlot`: Must be an Enum.ItemRedundancySlot value
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetHighWatermarkSlotForItem

`C_ItemUpgrade.GetHighWatermarkSlotForItem(itemInfo: ItemInfo) → itemRedundancySlot: number`

- Status: ✅ verified (function)
- `itemInfo`: Item ID, Link, or Name
- `itemRedundancySlot`: Enum.ItemRedundancySlot value
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetItemHyperlink

`C_ItemUpgrade.GetItemHyperlink() → link: cstring`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetItemUpgradeCurrentLevel

`C_ItemUpgrade.GetItemUpgradeCurrentLevel() → itemLevel: number, isPvpItemLevel: bool`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetItemUpgradeEffect

`C_ItemUpgrade.GetItemUpgradeEffect(effectIndex: number, numUpgradeLevels: number?) → outBaseEffect: string, outUpgradedEffect: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetItemUpgradeItemInfo

`C_ItemUpgrade.GetItemUpgradeItemInfo() → itemInfo: ItemUpgradeItemInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetItemUpgradePvpItemLevelDeltaValues

`C_ItemUpgrade.GetItemUpgradePvpItemLevelDeltaValues(numUpgradeLevels: number) → currentPvPItemLevel: number, upgradedPvPItemLevel: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetNumItemUpgradeEffects

`C_ItemUpgrade.GetNumItemUpgradeEffects() → numItemUpgradeEffects: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.IsItemBound

`C_ItemUpgrade.IsItemBound() → isBound: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.SetItemUpgradeFromCursorItem

`C_ItemUpgrade.SetItemUpgradeFromCursorItem()`

- Status: ✅ verified (function)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.SetItemUpgradeFromLocation

`C_ItemUpgrade.SetItemUpgradeFromLocation(itemToSet: ItemLocation)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.UpgradeItem

`C_ItemUpgrade.UpgradeItem(numUpgrades: number = 1)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

## Events

### ITEM_UPGRADE_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ITEM_UPGRADE_MASTER_SET_ITEM

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ITEM_UPGRADE_MASTER_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### ItemUpgradeCostDiscountInfo

- Structure
  - `isDiscounted`: bool
  - `discountHighWatermark`: number
  - `isPartialTwoHandDiscount`: bool
  - `isAccountWideDiscount`: bool
  - `doesCurrentCharacterMeetHighWatermark`: bool

### ItemUpgradeCurrencyCost

- Structure
  - `cost`: number
  - `currencyID`: number
  - `discountInfo`: ItemUpgradeCostDiscountInfo

### ItemUpgradeItemCost

- Structure
  - `cost`: number
  - `itemID`: number
  - `discountInfo`: ItemUpgradeCostDiscountInfo

### ItemUpgradeItemInfo

- Structure
  - `iconID`: number
  - `name`: string
  - `itemUpgradeable`: bool
  - `displayQuality`: number
  - `highWatermarkSlot`: number
  - `currUpgrade`: number
  - `maxUpgrade`: number
  - `minItemLevel`: number
  - `maxItemLevel`: number
  - `upgradeLevelInfos`: ItemUpgradeLevelInfo[]
  - `customUpgradeString`: string?
  - `upgradeCostTypesForSeason`: ItemUpgradeSeasonalCostType[]

### ItemUpgradeLevelInfo

- Structure
  - `upgradeLevel`: number
  - `displayQuality`: number
  - `itemLevelIncrement`: number
  - `levelStats`: ItemUpgradeStat[]
  - `currencyCostsToUpgrade`: ItemUpgradeCurrencyCost[]
  - `itemCostsToUpgrade`: ItemUpgradeItemCost[]
  - `moneyCost`: WOWMONEY?
  - `failureMessage`: string?

### ItemUpgradeSeasonalCostType

- Structure
- Blizzard: Costs are made up of either an Item OR a Currency, so either itemID or currencyID will be nil
  - `itemID`: number?
  - `currencyID`: number?
  - `orderIndex`: number
  - `sourceString`: string?

### ItemUpgradeStat

- Structure
  - `displayString`: string
  - `statValue`: number
  - `active`: bool
