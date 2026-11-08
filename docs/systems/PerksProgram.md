# PerksProgram

Namespace: `C_PerksProgram`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_PerksProgram.ClearFrozenPerksVendorItem](#c_perksprogramclearfrozenperksvendoritem) |  |  |
| ❔ | [C_PerksProgram.CloseInteraction](#c_perksprogramcloseinteraction) |  |  |
| ❔ | [C_PerksProgram.GetAvailableCategoryIDs](#c_perksprogramgetavailablecategoryids) |  |  |
| ❔ | [C_PerksProgram.GetAvailableVendorItemIDs](#c_perksprogramgetavailablevendoritemids) |  |  |
| ❔ | [C_PerksProgram.GetCategoryInfo](#c_perksprogramgetcategoryinfo) |  |  |
| ❔ | [C_PerksProgram.GetCurrencyAmount](#c_perksprogramgetcurrencyamount) |  |  |
| ❔ | [C_PerksProgram.GetDraggedPerksVendorItem](#c_perksprogramgetdraggedperksvendoritem) |  |  |
| ❔ | [C_PerksProgram.GetFrozenPerksVendorItemInfo](#c_perksprogramgetfrozenperksvendoriteminfo) |  |  |
| ❔ | [C_PerksProgram.GetPendingChestRewards](#c_perksprogramgetpendingchestrewards) |  |  |
| ❔ | [C_PerksProgram.GetPerksProgramItemDisplayInfo](#c_perksprogramgetperksprogramitemdisplayinfo) |  |  |
| ❔ | [C_PerksProgram.GetTimeRemaining](#c_perksprogramgettimeremaining) |  |  |
| ❔ | [C_PerksProgram.GetVendorItemInfo](#c_perksprogramgetvendoriteminfo) |  |  |
| ❔ | [C_PerksProgram.GetVendorItemInfoRefundTimeLeft](#c_perksprogramgetvendoriteminforefundtimeleft) |  |  |
| ❔ | [C_PerksProgram.IsAttackAnimToggleEnabled](#c_perksprogramisattackanimtoggleenabled) |  |  |
| ❔ | [C_PerksProgram.IsFrozenPerksVendorItem](#c_perksprogramisfrozenperksvendoritem) |  |  |
| ❔ | [C_PerksProgram.IsMountSpecialAnimToggleEnabled](#c_perksprogramismountspecialanimtoggleenabled) |  |  |
| ❔ | [C_PerksProgram.ItemSelectedTelemetry](#c_perksprogramitemselectedtelemetry) |  |  |
| ❔ | [C_PerksProgram.PickupPerksVendorItem](#c_perksprogrampickupperksvendoritem) |  |  |
| ❔ | [C_PerksProgram.RequestCartCheckout](#c_perksprogramrequestcartcheckout) |  |  |
| ❔ | [C_PerksProgram.RequestPendingChestRewards](#c_perksprogramrequestpendingchestrewards) |  |  |
| ❔ | [C_PerksProgram.RequestPurchase](#c_perksprogramrequestpurchase) |  |  |
| ❔ | [C_PerksProgram.RequestRefund](#c_perksprogramrequestrefund) |  |  |
| ❔ | [C_PerksProgram.ResetHeldItemDragAndDrop](#c_perksprogramresethelditemdraganddrop) |  |  |
| ❔ | [C_PerksProgram.SetFrozenPerksVendorItem](#c_perksprogramsetfrozenperksvendoritem) |  |  |

### C_PerksProgram.ClearFrozenPerksVendorItem

`C_PerksProgram.ClearFrozenPerksVendorItem()`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.CloseInteraction

`C_PerksProgram.CloseInteraction()`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetAvailableCategoryIDs

`C_PerksProgram.GetAvailableCategoryIDs() → categoryIDs: number[]`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetAvailableVendorItemIDs

`C_PerksProgram.GetAvailableVendorItemIDs() → vendorItemIDs: number[]`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetCategoryInfo

`C_PerksProgram.GetCategoryInfo(categoryID: number) → categoryInfo: PerksVendorCategoryInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetCurrencyAmount

`C_PerksProgram.GetCurrencyAmount() → currencyAmount: number`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetDraggedPerksVendorItem

`C_PerksProgram.GetDraggedPerksVendorItem() → perksVendorItemID: number`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetFrozenPerksVendorItemInfo

`C_PerksProgram.GetFrozenPerksVendorItemInfo() → vendorItemInfo: PerksVendorItemInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetPendingChestRewards

`C_PerksProgram.GetPendingChestRewards() → pendingRewards: PerksProgramPendingChestRewards[]`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetPerksProgramItemDisplayInfo

`C_PerksProgram.GetPerksProgramItemDisplayInfo(id: number) → item: PerksProgramItemDisplayInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetTimeRemaining

`C_PerksProgram.GetTimeRemaining(vendorItemID: number) → timeRemaining: time_t`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetVendorItemInfo

`C_PerksProgram.GetVendorItemInfo(vendorItemID: number) → vendorItemInfo: PerksVendorItemInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.GetVendorItemInfoRefundTimeLeft

`C_PerksProgram.GetVendorItemInfoRefundTimeLeft(vendorItemID: number) → refundTimeRemaining: time_t`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.IsAttackAnimToggleEnabled

`C_PerksProgram.IsAttackAnimToggleEnabled() → isAttackAnimToggleEnabled: bool`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.IsFrozenPerksVendorItem

`C_PerksProgram.IsFrozenPerksVendorItem(perksVendorItemID: number) → isFrozen: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.IsMountSpecialAnimToggleEnabled

`C_PerksProgram.IsMountSpecialAnimToggleEnabled() → isMountSpecialAnimToggleEnabled: bool`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.ItemSelectedTelemetry

`C_PerksProgram.ItemSelectedTelemetry(perksVendorItemID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.PickupPerksVendorItem

`C_PerksProgram.PickupPerksVendorItem(perksVendorItemID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.RequestCartCheckout

`C_PerksProgram.RequestCartCheckout(perksVendorItemIDs: number[])`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.RequestPendingChestRewards

`C_PerksProgram.RequestPendingChestRewards()`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.RequestPurchase

`C_PerksProgram.RequestPurchase(perksVendorItemID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.RequestRefund

`C_PerksProgram.RequestRefund(perksVendorItemID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.ResetHeldItemDragAndDrop

`C_PerksProgram.ResetHeldItemDragAndDrop()`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

### C_PerksProgram.SetFrozenPerksVendorItem

`C_PerksProgram.SetFrozenPerksVendorItem()`

- Status: ❔ unverified
- Source: client docs `PerksProgramDocumentation.lua`

## Events

### CHEST_REWARDS_UPDATED_FROM_SERVER

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_ADD_PENDING_SHOP_ITEM

- Status: ❔ unverified
- Payload: `vendorItemID: number`
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_CLOSE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_CURRENCY_AWARDED

- Status: ❔ unverified
- Payload: `value: number`
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_CURRENCY_REFRESH

- Status: ❔ unverified
- Payload: `oldValue: number`, `newValue: number`
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_DATA_REFRESH

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_DATA_SPECIFIC_ITEM_REFRESH

- Status: ❔ unverified
- Payload: `vendorItemID: number`
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_DISABLED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_OPEN

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_PURCHASE_CART_SUCCESS

- Status: ❔ unverified
- Payload: `vendorItemIDs: number[]`
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_PURCHASE_SUCCESS

- Status: ❔ unverified
- Payload: `vendorItemID: number`
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_REFUND_SUCCESS

- Status: ❔ unverified
- Payload: `vendorItemID: number`
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_REMOVE_PENDING_SHOP_ITEM

- Status: ❔ unverified
- Payload: `vendorItemID: number`
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_RESULT_ERROR

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PERKS_PROGRAM_SET_FROZEN_ITEM

- Status: ❔ unverified
- Payload: `vendorItemID: number`
- fires synchronously (Blizzard's docs)

## Types

### PerksProgramItemDisplayInfo

- Structure
  - `overrideModelSceneID`: number?
  - `creatureDisplayInfoID`: number?
  - `mainHandItemModifiedAppearanceID`: number?
  - `offHandItemModifiedAppearanceID`: number?

### PerksProgramPendingChestRewards

- Structure
  - `rewardTypeID`: number
  - `perksVendorItemID`: number?
  - `rewardAmount`: number
  - `monthRewarded`: string?
  - `activityMonthID`: number
  - `thresholdOrderIndex`: number

### PerksVendorCategoryInfo

- Structure
  - `ID`: number
  - `displayName`: cstring
  - `defaultUIModelSceneID`: number

### PerksVendorItemInfo

- Structure
  - `name`: string
  - `perksVendorCategoryID`: number
  - `description`: string
  - `timeRemaining`: time_t
  - `purchased`: bool
  - `refundable`: bool
  - `subItemsLoaded`: bool
  - `isPurchasePending`: bool
  - `doesNotExpire`: bool
  - `price`: number
  - `originalPrice`: number?
  - `showSaleBanner`: bool
  - `perksVendorItemID`: number
  - `itemID`: number
  - `iconTexture`: string
  - `mountID`: number
  - `mountTypeName`: string
  - `speciesID`: number
  - `transmogSetID`: number
  - `itemModifiedAppearanceID`: number
  - `subItems`: PerksVendorSubItemInfo[]
  - `uiGroupInfo`: PerksVendorItemUIGroupInfo?
  - `invType`: string
  - `quality`: ItemQuality

### PerksVendorItemUIGroupInfo

- Structure
  - `ID`: number
  - `name`: cstring
  - `priority`: number

### PerksVendorSubItemInfo

- Structure
  - `name`: string
  - `itemID`: number
  - `itemModifiedAppearanceID`: number
  - `invType`: string
  - `quality`: ItemQuality
