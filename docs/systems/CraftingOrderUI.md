# CraftingOrderUI

Namespace: `C_CraftingOrders`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_CraftingOrders.AreOrderNotesDisabled](#c_craftingordersareordernotesdisabled) |  |  |
| ❔ | [C_CraftingOrders.CalculateCraftingOrderPostingFee](#c_craftingorderscalculatecraftingorderpostingfee) |  |  |
| ❔ | [C_CraftingOrders.CanOrderSkillAbility](#c_craftingorderscanorderskillability) |  |  |
| ❔ | [C_CraftingOrders.CancelOrder](#c_craftingorderscancelorder) |  |  |
| ❔ | [C_CraftingOrders.ClaimOrder](#c_craftingordersclaimorder) |  |  |
| ❔ | [C_CraftingOrders.CloseCrafterCraftingOrders](#c_craftingordersclosecraftercraftingorders) |  |  |
| ❔ | [C_CraftingOrders.CloseCustomerCraftingOrders](#c_craftingordersclosecustomercraftingorders) |  |  |
| ❔ | [C_CraftingOrders.FulfillOrder](#c_craftingordersfulfillorder) |  |  |
| ❔ | [C_CraftingOrders.GetClaimedOrder](#c_craftingordersgetclaimedorder) |  |  |
| ❔ | [C_CraftingOrders.GetCrafterBuckets](#c_craftingordersgetcrafterbuckets) |  |  |
| ❔ | [C_CraftingOrders.GetCrafterOrders](#c_craftingordersgetcrafterorders) |  |  |
| ❔ | [C_CraftingOrders.GetCraftingOrderTime](#c_craftingordersgetcraftingordertime) |  |  |
| ❔ | [C_CraftingOrders.GetCustomerCategories](#c_craftingordersgetcustomercategories) |  |  |
| ❔ | [C_CraftingOrders.GetCustomerOptions](#c_craftingordersgetcustomeroptions) |  |  |
| ❔ | [C_CraftingOrders.GetCustomerOrders](#c_craftingordersgetcustomerorders) |  |  |
| ❔ | [C_CraftingOrders.GetDefaultOrdersSkillLine](#c_craftingordersgetdefaultordersskillline) |  |  |
| ❔ | [C_CraftingOrders.GetMyOrders](#c_craftingordersgetmyorders) |  |  |
| ❔ | [C_CraftingOrders.GetNumFavoriteCustomerOptions](#c_craftingordersgetnumfavoritecustomeroptions) |  |  |
| ❔ | [C_CraftingOrders.GetOrderClaimInfo](#c_craftingordersgetorderclaiminfo) |  |  |
| ❔ | [C_CraftingOrders.GetPersonalOrdersInfo](#c_craftingordersgetpersonalordersinfo) |  |  |
| ❔ | [C_CraftingOrders.HasFavoriteCustomerOptions](#c_craftingordershasfavoritecustomeroptions) |  |  |
| ❔ | [C_CraftingOrders.IsCustomerOptionFavorited](#c_craftingordersiscustomeroptionfavorited) |  |  |
| ❔ | [C_CraftingOrders.ListMyOrders](#c_craftingorderslistmyorders) |  |  |
| ❔ | [C_CraftingOrders.OpenCrafterCraftingOrders](#c_craftingordersopencraftercraftingorders) |  |  |
| ❔ | [C_CraftingOrders.OpenCustomerCraftingOrders](#c_craftingordersopencustomercraftingorders) |  |  |
| ❔ | [C_CraftingOrders.OrderCanBeRecrafted](#c_craftingordersordercanberecrafted) |  |  |
| ❔ | [C_CraftingOrders.ParseCustomerOptions](#c_craftingordersparsecustomeroptions) |  |  |
| ❔ | [C_CraftingOrders.PlaceNewOrder](#c_craftingordersplaceneworder) |  |  |
| ❔ | [C_CraftingOrders.RejectOrder](#c_craftingordersrejectorder) |  |  |
| ❔ | [C_CraftingOrders.ReleaseOrder](#c_craftingordersreleaseorder) |  |  |
| ❔ | [C_CraftingOrders.RequestCrafterOrders](#c_craftingordersrequestcrafterorders) |  |  |
| ❔ | [C_CraftingOrders.RequestCustomerOrders](#c_craftingordersrequestcustomerorders) |  |  |
| ❔ | [C_CraftingOrders.SetCustomerOptionFavorited](#c_craftingorderssetcustomeroptionfavorited) |  |  |
| ❔ | [C_CraftingOrders.ShouldShowCraftingOrderTab](#c_craftingordersshouldshowcraftingordertab) |  |  |
| ❔ | [C_CraftingOrders.SkillLineHasOrders](#c_craftingordersskilllinehasorders) |  |  |
| ❔ | [C_CraftingOrders.UpdateIgnoreList](#c_craftingordersupdateignorelist) |  |  |

### C_CraftingOrders.AreOrderNotesDisabled

`C_CraftingOrders.AreOrderNotesDisabled() → areNotesDisabled: bool`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.CalculateCraftingOrderPostingFee

`C_CraftingOrders.CalculateCraftingOrderPostingFee(skillLineAbilityID: number, orderType: CraftingOrderType, orderDuration: CraftingOrderDuration) → deposit: WOWMONEY`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.CanOrderSkillAbility

`C_CraftingOrders.CanOrderSkillAbility(skillLineAbilityID: number) → canOrder: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.CancelOrder

`C_CraftingOrders.CancelOrder(orderID: BigUInteger)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.ClaimOrder

`C_CraftingOrders.ClaimOrder(orderID: BigUInteger, profession: Profession)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.CloseCrafterCraftingOrders

`C_CraftingOrders.CloseCrafterCraftingOrders()`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.CloseCustomerCraftingOrders

`C_CraftingOrders.CloseCustomerCraftingOrders()`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.FulfillOrder

`C_CraftingOrders.FulfillOrder(orderID: BigUInteger, crafterNote: string, profession: Profession)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetClaimedOrder

`C_CraftingOrders.GetClaimedOrder() → order: CraftingOrderInfo?`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCrafterBuckets

`C_CraftingOrders.GetCrafterBuckets() → buckets: CraftingOrderBucketInfo[]`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCrafterOrders

`C_CraftingOrders.GetCrafterOrders() → orders: CraftingOrderInfo[]`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCraftingOrderTime

`C_CraftingOrders.GetCraftingOrderTime() → time: BigUInteger`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCustomerCategories

`C_CraftingOrders.GetCustomerCategories() → categories: CraftingOrderCustomerCategory[]`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCustomerOptions

`C_CraftingOrders.GetCustomerOptions(params: CraftingOrderCustomerSearchParams) → results: CraftingOrderCustomerSearchResults`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetCustomerOrders

`C_CraftingOrders.GetCustomerOrders() → customerOrders: CraftingOrderInfo[]`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetDefaultOrdersSkillLine

`C_CraftingOrders.GetDefaultOrdersSkillLine() → skillLineID: number?`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetMyOrders

`C_CraftingOrders.GetMyOrders() → myOrders: CraftingOrderInfo[]`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetNumFavoriteCustomerOptions

`C_CraftingOrders.GetNumFavoriteCustomerOptions() → numFavorites: BigUInteger`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetOrderClaimInfo

`C_CraftingOrders.GetOrderClaimInfo(profession: Profession) → claimInfo: CraftingOrderClaimsRemainingInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.GetPersonalOrdersInfo

`C_CraftingOrders.GetPersonalOrdersInfo() → infos: CraftingOrderPersonalOrdersInfo[]`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.HasFavoriteCustomerOptions

`C_CraftingOrders.HasFavoriteCustomerOptions() → hasFavorites: bool`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.IsCustomerOptionFavorited

`C_CraftingOrders.IsCustomerOptionFavorited(recipeID: number) → favorited: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.ListMyOrders

`C_CraftingOrders.ListMyOrders(request: CraftingOrderRequestMyOrdersInfo)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.OpenCrafterCraftingOrders

`C_CraftingOrders.OpenCrafterCraftingOrders()`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.OpenCustomerCraftingOrders

`C_CraftingOrders.OpenCustomerCraftingOrders()`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.OrderCanBeRecrafted

`C_CraftingOrders.OrderCanBeRecrafted(orderID: BigUInteger) → recraftable: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.ParseCustomerOptions

`C_CraftingOrders.ParseCustomerOptions()`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.PlaceNewOrder

`C_CraftingOrders.PlaceNewOrder(orderInfo: NewCraftingOrderInfo)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.RejectOrder

`C_CraftingOrders.RejectOrder(orderID: BigUInteger, crafterNote: string, profession: Profession)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.ReleaseOrder

`C_CraftingOrders.ReleaseOrder(orderID: BigUInteger, profession: Profession)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.RequestCrafterOrders

`C_CraftingOrders.RequestCrafterOrders(request: CraftingOrderRequestInfo)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.RequestCustomerOrders

`C_CraftingOrders.RequestCustomerOrders(request: CraftingOrderRequestInfo)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.SetCustomerOptionFavorited

`C_CraftingOrders.SetCustomerOptionFavorited(recipeID: number, favorited: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.ShouldShowCraftingOrderTab

`C_CraftingOrders.ShouldShowCraftingOrderTab() → showTab: bool`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.SkillLineHasOrders

`C_CraftingOrders.SkillLineHasOrders(skillLineID: number) → hasOrders: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CraftingOrderUIDocumentation.lua`

### C_CraftingOrders.UpdateIgnoreList

`C_CraftingOrders.UpdateIgnoreList()`

- Status: ❔ unverified
- Source: client docs `CraftingOrderUIDocumentation.lua`

## Events

### CRAFTINGORDERS_CAN_REQUEST

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CLAIMED_ORDER_ADDED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CLAIMED_ORDER_REMOVED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CLAIMED_ORDER_UPDATED

- Status: ❔ unverified
- Payload: `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CLAIM_ORDER_RESPONSE

- Status: ❔ unverified
- Payload: `result: CraftingOrderResult`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CRAFT_ORDER_RESPONSE

- Status: ❔ unverified
- Payload: `result: CraftingOrderResult`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CUSTOMER_FAVORITES_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_CUSTOMER_OPTIONS_PARSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_DISPLAY_CRAFTER_FULFILLED_MSG

- Status: ❔ unverified
- Payload: `orderTypeString: cstring`, `itemNameString: cstring`, `playerNameString: cstring`, `tipAmount: WOWMONEY`, `quantityCrafted: number`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_FULFILL_ORDER_RESPONSE

- Status: ❔ unverified
- Payload: `result: CraftingOrderResult`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_HIDE_CRAFTER

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_HIDE_CUSTOMER

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_ORDER_CANCEL_RESPONSE

- Status: ❔ unverified
- Payload: `result: CraftingOrderResult`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_ORDER_PLACEMENT_RESPONSE

- Status: ❔ unverified
- Payload: `result: CraftingOrderResult`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_REJECT_ORDER_RESPONSE

- Status: ❔ unverified
- Payload: `result: CraftingOrderResult`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_RELEASE_ORDER_RESPONSE

- Status: ❔ unverified
- Payload: `result: CraftingOrderResult`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_SHOW_CRAFTER

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_SHOW_CUSTOMER

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_UNEXPECTED_ERROR

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_UPDATE_CUSTOMER_NAME

- Status: ❔ unverified
- Payload: `customerName: cstring`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_UPDATE_ORDER_COUNT

- Status: ❔ unverified
- Payload: `orderType: CraftingOrderType`, `numOrders: number`
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_UPDATE_PERSONAL_ORDER_COUNTS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CRAFTINGORDERS_UPDATE_REWARDS

- Status: ❔ unverified
- Payload: `npcOrderRewards: CraftingOrderRewardInfo[]`, `orderID: BigUInteger`
- fires synchronously (Blizzard's docs)

### CRAFTING_HOUSE_DISABLED

- Status: ❔ unverified
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
