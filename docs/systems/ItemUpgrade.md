# ItemUpgrade

Namespace: `C_ItemUpgrade`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ItemUpgrade.CanUpgradeItem](#c_itemupgradecanupgradeitem) |  |  |
| ❔ | [C_ItemUpgrade.ClearItemUpgrade](#c_itemupgradeclearitemupgrade) |  |  |
| ❔ | [C_ItemUpgrade.CloseItemUpgrade](#c_itemupgradecloseitemupgrade) |  |  |
| ❔ | [C_ItemUpgrade.GetHighWatermarkForItem](#c_itemupgradegethighwatermarkforitem) |  |  |
| ❔ | [C_ItemUpgrade.GetHighWatermarkForSlot](#c_itemupgradegethighwatermarkforslot) |  |  |
| ❔ | [C_ItemUpgrade.GetHighWatermarkSlotForItem](#c_itemupgradegethighwatermarkslotforitem) |  |  |
| ❔ | [C_ItemUpgrade.GetItemHyperlink](#c_itemupgradegetitemhyperlink) |  |  |
| ❔ | [C_ItemUpgrade.GetItemUpgradeCurrentLevel](#c_itemupgradegetitemupgradecurrentlevel) |  |  |
| ❔ | [C_ItemUpgrade.GetItemUpgradeEffect](#c_itemupgradegetitemupgradeeffect) |  |  |
| ❔ | [C_ItemUpgrade.GetItemUpgradeItemInfo](#c_itemupgradegetitemupgradeiteminfo) |  |  |
| ❔ | [C_ItemUpgrade.GetItemUpgradePvpItemLevelDeltaValues](#c_itemupgradegetitemupgradepvpitemleveldeltavalues) |  |  |
| ❔ | [C_ItemUpgrade.GetNumItemUpgradeEffects](#c_itemupgradegetnumitemupgradeeffects) |  |  |
| ❔ | [C_ItemUpgrade.IsItemBound](#c_itemupgradeisitembound) |  |  |
| ❔ | [C_ItemUpgrade.SetItemUpgradeFromCursorItem](#c_itemupgradesetitemupgradefromcursoritem) |  |  |
| ❔ | [C_ItemUpgrade.SetItemUpgradeFromLocation](#c_itemupgradesetitemupgradefromlocation) |  |  |
| ❔ | [C_ItemUpgrade.UpgradeItem](#c_itemupgradeupgradeitem) |  |  |

### C_ItemUpgrade.CanUpgradeItem

`C_ItemUpgrade.CanUpgradeItem(baseItem: ItemLocation) → isValid: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.ClearItemUpgrade

`C_ItemUpgrade.ClearItemUpgrade()`

- Status: ❔ unverified
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.CloseItemUpgrade

`C_ItemUpgrade.CloseItemUpgrade()`

- Status: ❔ unverified
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetHighWatermarkForItem

`C_ItemUpgrade.GetHighWatermarkForItem(itemInfo: ItemInfo) → characterHighWatermark: number, accountHighWatermark: number`

- Status: ❔ unverified
- `itemInfo`: Item ID, Link, or Name
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetHighWatermarkForSlot

`C_ItemUpgrade.GetHighWatermarkForSlot(itemRedundancySlot: number) → characterHighWatermark: number, accountHighWatermark: number`

- Status: ❔ unverified
- `itemRedundancySlot`: Must be an Enum.ItemRedundancySlot value
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetHighWatermarkSlotForItem

`C_ItemUpgrade.GetHighWatermarkSlotForItem(itemInfo: ItemInfo) → itemRedundancySlot: number`

- Status: ❔ unverified
- `itemInfo`: Item ID, Link, or Name
- `itemRedundancySlot`: Enum.ItemRedundancySlot value
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetItemHyperlink

`C_ItemUpgrade.GetItemHyperlink() → link: cstring`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetItemUpgradeCurrentLevel

`C_ItemUpgrade.GetItemUpgradeCurrentLevel() → itemLevel: number, isPvpItemLevel: bool`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetItemUpgradeEffect

`C_ItemUpgrade.GetItemUpgradeEffect(effectIndex: number, numUpgradeLevels: number?) → outBaseEffect: string, outUpgradedEffect: string`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetItemUpgradeItemInfo

`C_ItemUpgrade.GetItemUpgradeItemInfo() → itemInfo: ItemUpgradeItemInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetItemUpgradePvpItemLevelDeltaValues

`C_ItemUpgrade.GetItemUpgradePvpItemLevelDeltaValues(numUpgradeLevels: number) → currentPvPItemLevel: number, upgradedPvPItemLevel: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.GetNumItemUpgradeEffects

`C_ItemUpgrade.GetNumItemUpgradeEffects() → numItemUpgradeEffects: number`

- Status: ❔ unverified
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.IsItemBound

`C_ItemUpgrade.IsItemBound() → isBound: bool`

- Status: ❔ unverified
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.SetItemUpgradeFromCursorItem

`C_ItemUpgrade.SetItemUpgradeFromCursorItem()`

- Status: ❔ unverified
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.SetItemUpgradeFromLocation

`C_ItemUpgrade.SetItemUpgradeFromLocation(itemToSet: ItemLocation)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

### C_ItemUpgrade.UpgradeItem

`C_ItemUpgrade.UpgradeItem(numUpgrades: number = 1)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemUpgradeDocumentation.lua`

## Events

### ITEM_UPGRADE_FAILED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ITEM_UPGRADE_MASTER_SET_ITEM

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ITEM_UPGRADE_MASTER_UPDATE

- Status: ❔ unverified
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
