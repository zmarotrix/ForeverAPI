# MerchantFrame

Namespace: `C_MerchantFrame`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_MerchantFrame.GetBuybackItemID](#c_merchantframegetbuybackitemid) | 1 value | 1 value |
| ✅ | [C_MerchantFrame.GetItemInfo](#c_merchantframegetiteminfo) | 0 values | 0 values |
| ✅ | [C_MerchantFrame.GetMerchantCurrencies](#c_merchantframegetmerchantcurrencies) | 1 value | 1 value |
| ✅ | [C_MerchantFrame.GetNumJunkItems](#c_merchantframegetnumjunkitems) | 1 value | 1 value |
| ✅ | [C_MerchantFrame.IsMerchantItemRefundable](#c_merchantframeismerchantitemrefundable) | 1 value | 1 value |
| ✅ | [C_MerchantFrame.IsSellAllJunkEnabled](#c_merchantframeissellalljunkenabled) | 1 value | 1 value |
| ✅ | [C_MerchantFrame.SellAllJunkItems](#c_merchantframesellalljunkitems) |  |  |

### C_MerchantFrame.GetBuybackItemID

`C_MerchantFrame.GetBuybackItemID(buybackSlotIndex: luaIndex) → buybackItemID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.GetItemInfo

`C_MerchantFrame.GetItemInfo(index: luaIndex) → info: MerchantItemInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.GetMerchantCurrencies

`C_MerchantFrame.GetMerchantCurrencies() → currencies: number[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.GetNumJunkItems

`C_MerchantFrame.GetNumJunkItems() → numJunkItems: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.IsMerchantItemRefundable

`C_MerchantFrame.IsMerchantItemRefundable(index: luaIndex) → refundable: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.IsSellAllJunkEnabled

`C_MerchantFrame.IsSellAllJunkEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.SellAllJunkItems

`C_MerchantFrame.SellAllJunkItems()`

- Status: ✅ verified (function)
- Source: client docs `MerchantFrameDocumentation.lua`

## Events

### MERCHANT_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 23 times (0 in combat); argument kinds: ``

### MERCHANT_FILTER_ITEM_UPDATE

- Status: ✅ verified
- Payload: `itemID: number`
- fires synchronously (Blizzard's docs)
- Seen firing 110 times (0 in combat); argument kinds: `n`

### MERCHANT_SHOW

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 11 times (0 in combat); argument kinds: ``

### MERCHANT_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 66 times (0 in combat); argument kinds: ``

## Types

### MerchantItemInfo

- Structure
  - `name`: string?
  - `texture`: fileID
  - `price`: number
  - `stackCount`: number
  - `numAvailable`: number
  - `isPurchasable`: bool
  - `isUsable`: bool
  - `hasExtendedCost`: bool
  - `currencyID`: number?
  - `spellID`: number?
  - `isQuestStartItem`: bool
