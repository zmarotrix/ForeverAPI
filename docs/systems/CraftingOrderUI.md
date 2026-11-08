# CraftingOrderUI

Namespace: `C_CraftingOrders`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_CraftingOrders.AreOrderNotesDisabled](#c_craftingordersareordernotesdisabled) |  |  |
| ✅ | [C_CraftingOrders.CalculateCraftingOrderPostingFee](#c_craftingorderscalculatecraftingorderpostingfee) |  |  |
| ✅ | [C_CraftingOrders.CanOrderSkillAbility](#c_craftingorderscanorderskillability) |  |  |
| ✅ | [C_CraftingOrders.CancelOrder](#c_craftingorderscancelorder) |  |  |
| ✅ | [C_CraftingOrders.ClaimOrder](#c_craftingordersclaimorder) |  |  |
| ✅ | [C_CraftingOrders.CloseCrafterCraftingOrders](#c_craftingordersclosecraftercraftingorders) |  |  |
| ✅ | [C_CraftingOrders.CloseCustomerCraftingOrders](#c_craftingordersclosecustomercraftingorders) |  |  |
| ✅ | [C_CraftingOrders.FulfillOrder](#c_craftingordersfulfillorder) |  |  |
| ✅ | [C_CraftingOrders.GetClaimedOrder](#c_craftingordersgetclaimedorder) |  |  |
| ✅ | [C_CraftingOrders.GetCrafterBuckets](#c_craftingordersgetcrafterbuckets) |  |  |
| ✅ | [C_CraftingOrders.GetCrafterOrders](#c_craftingordersgetcrafterorders) |  |  |
| ✅ | [C_CraftingOrders.GetCraftingOrderTime](#c_craftingordersgetcraftingordertime) |  |  |
| ✅ | [C_CraftingOrders.GetCustomerCategories](#c_craftingordersgetcustomercategories) |  |  |
| ✅ | [C_CraftingOrders.GetCustomerOptions](#c_craftingordersgetcustomeroptions) |  |  |
| ✅ | [C_CraftingOrders.GetCustomerOrders](#c_craftingordersgetcustomerorders) |  |  |
| ✅ | [C_CraftingOrders.GetDefaultOrdersSkillLine](#c_craftingordersgetdefaultordersskillline) |  |  |
| ✅ | [C_CraftingOrders.GetMyOrders](#c_craftingordersgetmyorders) |  |  |
| ✅ | [C_CraftingOrders.GetNumFavoriteCustomerOptions](#c_craftingordersgetnumfavoritecustomeroptions) |  |  |
| ✅ | [C_CraftingOrders.GetOrderClaimInfo](#c_craftingordersgetorderclaiminfo) |  |  |
| ✅ | [C_CraftingOrders.GetPersonalOrdersInfo](#c_craftingordersgetpersonalordersinfo) |  |  |
| ✅ | [C_CraftingOrders.HasFavoriteCustomerOptions](#c_craftingordershasfavoritecustomeroptions) |  |  |
| ✅ | [C_CraftingOrders.IsCustomerOptionFavorited](#c_craftingordersiscustomeroptionfavorited) |  |  |
| ✅ | [C_CraftingOrders.ListMyOrders](#c_craftingorderslistmyorders) |  |  |
| ✅ | [C_CraftingOrders.OpenCrafterCraftingOrders](#c_craftingordersopencraftercraftingorders) |  |  |
| ✅ | [C_CraftingOrders.OpenCustomerCraftingOrders](#c_craftingordersopencustomercraftingorders) |  |  |
| ✅ | [C_CraftingOrders.OrderCanBeRecrafted](#c_craftingordersordercanberecrafted) |  |  |
| ✅ | [C_CraftingOrders.ParseCustomerOptions](#c_craftingordersparsecustomeroptions) |  |  |
| ✅ | [C_CraftingOrders.PlaceNewOrder](#c_craftingordersplaceneworder) |  |  |
| ✅ | [C_CraftingOrders.RejectOrder](#c_craftingordersrejectorder) |  |  |
| ✅ | [C_CraftingOrders.ReleaseOrder](#c_craftingordersreleaseorder) |  |  |
| ✅ | [C_CraftingOrders.RequestCrafterOrders](#c_craftingordersrequestcrafterorders) |  |  |
| ✅ | [C_CraftingOrders.RequestCustomerOrders](#c_craftingordersrequestcustomerorders) |  |  |
| ✅ | [C_CraftingOrders.SetCustomerOptionFavorited](#c_craftingorderssetcustomeroptionfavorited) |  |  |
| ✅ | [C_CraftingOrders.ShouldShowCraftingOrderTab](#c_craftingordersshouldshowcraftingordertab) |  |  |
| ✅ | [C_CraftingOrders.SkillLineHasOrders](#c_craftingordersskilllinehasorders) |  |  |
| ✅ | [C_CraftingOrders.UpdateIgnoreList](#c_craftingordersupdateignorelist) |  |  |

### C_CraftingOrders.AreOrderNotesDisabled

`C_CraftingOrders.AreOrderNotesDisabled() → areNotesDisabled: bool`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.CalculateCraftingOrderPostingFee

`C_CraftingOrders.CalculateCraftingOrderPostingFee(skillLineAbilityID: number, orderType: CraftingOrderType, orderDuration: CraftingOrderDuration) → deposit: WOWMONEY`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.CanOrderSkillAbility

`C_CraftingOrders.CanOrderSkillAbility(skillLineAbilityID: number) → canOrder: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.CancelOrder

`C_CraftingOrders.CancelOrder(orderID: BigUInteger)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.ClaimOrder

`C_CraftingOrders.ClaimOrder(orderID: BigUInteger, profession: Profession)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.CloseCrafterCraftingOrders

`C_CraftingOrders.CloseCrafterCraftingOrders()`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.CloseCustomerCraftingOrders

`C_CraftingOrders.CloseCustomerCraftingOrders()`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.FulfillOrder

`C_CraftingOrders.FulfillOrder(orderID: BigUInteger, crafterNote: string, profession: Profession)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetClaimedOrder

`C_CraftingOrders.GetClaimedOrder() → order: CraftingOrderInfo?`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCrafterBuckets

`C_CraftingOrders.GetCrafterBuckets() → buckets: CraftingOrderBucketInfo[]`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCrafterOrders

`C_CraftingOrders.GetCrafterOrders() → orders: CraftingOrderInfo[]`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCraftingOrderTime

`C_CraftingOrders.GetCraftingOrderTime() → time: BigUInteger`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCustomerCategories

`C_CraftingOrders.GetCustomerCategories() → categories: CraftingOrderCustomerCategory[]`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCustomerOptions

`C_CraftingOrders.GetCustomerOptions(params: CraftingOrderCustomerSearchParams) → results: CraftingOrderCustomerSearchResults`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCustomerOrders

`C_CraftingOrders.GetCustomerOrders() → customerOrders: CraftingOrderInfo[]`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetDefaultOrdersSkillLine

`C_CraftingOrders.GetDefaultOrdersSkillLine() → skillLineID: number?`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetMyOrders

`C_CraftingOrders.GetMyOrders() → myOrders: CraftingOrderInfo[]`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetNumFavoriteCustomerOptions

`C_CraftingOrders.GetNumFavoriteCustomerOptions() → numFavorites: BigUInteger`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetOrderClaimInfo

`C_CraftingOrders.GetOrderClaimInfo(profession: Profession) → claimInfo: CraftingOrderClaimsRemainingInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetPersonalOrdersInfo

`C_CraftingOrders.GetPersonalOrdersInfo() → infos: CraftingOrderPersonalOrdersInfo[]`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.HasFavoriteCustomerOptions

`C_CraftingOrders.HasFavoriteCustomerOptions() → hasFavorites: bool`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.IsCustomerOptionFavorited

`C_CraftingOrders.IsCustomerOptionFavorited(recipeID: number) → favorited: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.ListMyOrders

`C_CraftingOrders.ListMyOrders(request: CraftingOrderRequestMyOrdersInfo)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.OpenCrafterCraftingOrders

`C_CraftingOrders.OpenCrafterCraftingOrders()`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.OpenCustomerCraftingOrders

`C_CraftingOrders.OpenCustomerCraftingOrders()`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.OrderCanBeRecrafted

`C_CraftingOrders.OrderCanBeRecrafted(orderID: BigUInteger) → recraftable: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.ParseCustomerOptions

`C_CraftingOrders.ParseCustomerOptions()`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.PlaceNewOrder

`C_CraftingOrders.PlaceNewOrder(orderInfo: NewCraftingOrderInfo)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.RejectOrder

`C_CraftingOrders.RejectOrder(orderID: BigUInteger, crafterNote: string, profession: Profession)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.ReleaseOrder

`C_CraftingOrders.ReleaseOrder(orderID: BigUInteger, profession: Profession)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.RequestCrafterOrders

`C_CraftingOrders.RequestCrafterOrders(request: CraftingOrderRequestInfo)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.RequestCustomerOrders

`C_CraftingOrders.RequestCustomerOrders(request: CraftingOrderRequestInfo)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.SetCustomerOptionFavorited

`C_CraftingOrders.SetCustomerOptionFavorited(recipeID: number, favorited: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.ShouldShowCraftingOrderTab

`C_CraftingOrders.ShouldShowCraftingOrderTab() → showTab: bool`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.SkillLineHasOrders

`C_CraftingOrders.SkillLineHasOrders(skillLineID: number) → hasOrders: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.UpdateIgnoreList

`C_CraftingOrders.UpdateIgnoreList()`

- Status: ✅ verified (function)
- Source: client docs `CraftingOrderUIDocumentation.lua`

## Events

### CRAFTINGORDERS_CAN_REQUEST

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CLAIMED_ORDER_ADDED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CLAIMED_ORDER_REMOVED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CLAIMED_ORDER_UPDATED

- Status: ✅ verified
- Payload: `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CLAIM_ORDER_RESPONSE

- Status: ✅ verified
- Payload: `result: CraftingOrderResult`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CRAFT_ORDER_RESPONSE

- Status: ✅ verified
- Payload: `result: CraftingOrderResult`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CUSTOMER_FAVORITES_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CUSTOMER_OPTIONS_PARSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_DISPLAY_CRAFTER_FULFILLED_MSG

- Status: ✅ verified
- Payload: `orderTypeString: cstring`, `itemNameString: cstring`, `playerNameString: cstring`, `tipAmount: WOWMONEY`, `quantityCrafted: number`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_FULFILL_ORDER_RESPONSE

- Status: ✅ verified
- Payload: `result: CraftingOrderResult`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_HIDE_CRAFTER

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_HIDE_CUSTOMER

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_ORDER_CANCEL_RESPONSE

- Status: ✅ verified
- Payload: `result: CraftingOrderResult`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_ORDER_PLACEMENT_RESPONSE

- Status: ✅ verified
- Payload: `result: CraftingOrderResult`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_REJECT_ORDER_RESPONSE

- Status: ✅ verified
- Payload: `result: CraftingOrderResult`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_RELEASE_ORDER_RESPONSE

- Status: ✅ verified
- Payload: `result: CraftingOrderResult`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_SHOW_CRAFTER

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_SHOW_CUSTOMER

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_UNEXPECTED_ERROR

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_UPDATE_CUSTOMER_NAME

- Status: ✅ verified
- Payload: `customerName: cstring`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_UPDATE_ORDER_COUNT

- Status: ✅ verified
- Payload: `orderType: CraftingOrderType`, `numOrders: number`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_UPDATE_PERSONAL_ORDER_COUNTS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_UPDATE_REWARDS

- Status: ✅ verified
- Payload: `npcOrderRewards: CraftingOrderRewardInfo[]`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTING_HOUSE_DISABLED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### CraftingOrderRequestInfo

- Structure
  - `orderType`: CraftingOrderType
  - `selectedSkillLineAbility`: number?
  - `searchFavorites`: bool
  - `initialNonPublicSearch`: bool
  - `primarySort`: CraftingOrderSortInfo
  - `secondarySort`: CraftingOrderSortInfo
  - `forCrafter`: bool
  - `offset`: number
  - `callback`: CraftingOrderRequestCallback
  - `profession`: Profession?

### CraftingOrderRequestMyOrdersInfo

- Structure
  - `primarySort`: CraftingOrderSortInfo
  - `secondarySort`: CraftingOrderSortInfo
  - `offset`: number
  - `callback`: CraftingOrderRequestMyOrdersCallback
