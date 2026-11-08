# MerchantFrame

Namespace: `C_MerchantFrame`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_MerchantFrame.GetBuybackItemID](#c_merchantframegetbuybackitemid) |  |  |
| ✅ | [C_MerchantFrame.GetItemInfo](#c_merchantframegetiteminfo) |  |  |
| ✅ | [C_MerchantFrame.GetMerchantCurrencies](#c_merchantframegetmerchantcurrencies) |  |  |
| ✅ | [C_MerchantFrame.GetNumJunkItems](#c_merchantframegetnumjunkitems) |  |  |
| ✅ | [C_MerchantFrame.IsMerchantItemRefundable](#c_merchantframeismerchantitemrefundable) |  |  |
| ✅ | [C_MerchantFrame.IsSellAllJunkEnabled](#c_merchantframeissellalljunkenabled) |  |  |
| ✅ | [C_MerchantFrame.SellAllJunkItems](#c_merchantframesellalljunkitems) |  |  |

### C_MerchantFrame.GetBuybackItemID

`C_MerchantFrame.GetBuybackItemID(buybackSlotIndex: luaIndex) → buybackItemID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.GetItemInfo

`C_MerchantFrame.GetItemInfo(index: luaIndex) → info: MerchantItemInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.GetMerchantCurrencies

`C_MerchantFrame.GetMerchantCurrencies() → currencies: number[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.GetNumJunkItems

`C_MerchantFrame.GetNumJunkItems() → numJunkItems: number`

- Status: ✅ verified (function)
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.IsMerchantItemRefundable

`C_MerchantFrame.IsMerchantItemRefundable(index: luaIndex) → refundable: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MerchantFrameDocumentation.lua`

### C_MerchantFrame.IsSellAllJunkEnabled

`C_MerchantFrame.IsSellAllJunkEnabled() → enabled: bool`

- Status: ✅ verified (function)
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

### MERCHANT_FILTER_ITEM_UPDATE

- Status: ✅ verified
- Payload: `itemID: number`
- fires synchronously (Blizzard's docs)

### MERCHANT_SHOW

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### MERCHANT_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

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
