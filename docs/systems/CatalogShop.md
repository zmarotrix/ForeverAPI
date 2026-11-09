# CatalogShop

Namespace: `C_CatalogShop`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_CatalogShop.BulkPurchaseProducts](#c_catalogshopbulkpurchaseproducts) |  |  |
| ✅ | [C_CatalogShop.BulkRefundDecors](#c_catalogshopbulkrefunddecors) |  |  |
| ✅ | [C_CatalogShop.CloseCatalogShopInteraction](#c_catalogshopclosecatalogshopinteraction) |  |  |
| ✅ | [C_CatalogShop.ConfirmHousingPurchase](#c_catalogshopconfirmhousingpurchase) |  |  |
| ✅ | [C_CatalogShop.FindBestCurrencyProductForNeededAmount](#c_catalogshopfindbestcurrencyproductforneededamount) |  |  |
| ✅ | [C_CatalogShop.GetAvailableCategoryIDs](#c_catalogshopgetavailablecategoryids) | 1 value | 1 value |
| ✅ | [C_CatalogShop.GetAvailableTransmogRaceInfos](#c_catalogshopgetavailabletransmograceinfos) | 1 value | 1 value |
| ✅ | [C_CatalogShop.GetCatalogShopProductDisplayInfo](#c_catalogshopgetcatalogshopproductdisplayinfo) |  |  |
| ✅ | [C_CatalogShop.GetCategoryInfo](#c_catalogshopgetcategoryinfo) |  |  |
| ✅ | [C_CatalogShop.GetCategorySectionInfo](#c_catalogshopgetcategorysectioninfo) |  |  |
| ✅ | [C_CatalogShop.GetFailureInfo](#c_catalogshopgetfailureinfo) | 2 values | 2 values |
| ✅ | [C_CatalogShop.GetFirstCategoryByProductID](#c_catalogshopgetfirstcategorybyproductid) |  |  |
| ✅ | [C_CatalogShop.GetNewProducts](#c_catalogshopgetnewproducts) | 1 value | 1 value |
| ✅ | [C_CatalogShop.GetProductAvailabilityTimeRemainingSecs](#c_catalogshopgetproductavailabilitytimeremainingsecs) |  |  |
| ✅ | [C_CatalogShop.GetProductIDsForBundle](#c_catalogshopgetproductidsforbundle) |  |  |
| ✅ | [C_CatalogShop.GetProductIDsForCategory](#c_catalogshopgetproductidsforcategory) |  |  |
| ✅ | [C_CatalogShop.GetProductIDsForCategorySection](#c_catalogshopgetproductidsforcategorysection) |  |  |
| ✅ | [C_CatalogShop.GetProductInfo](#c_catalogshopgetproductinfo) |  |  |
| ✅ | [C_CatalogShop.GetProductSortOrder](#c_catalogshopgetproductsortorder) |  |  |
| ✅ | [C_CatalogShop.GetRefundableDecors](#c_catalogshopgetrefundabledecors) | 2 values | 2 values |
| ✅ | [C_CatalogShop.GetSectionIDsForCategory](#c_catalogshopgetsectionidsforcategory) |  |  |
| ✅ | [C_CatalogShop.GetSpellVisualInfoForMount](#c_catalogshopgetspellvisualinfoformount) |  |  |
| ✅ | [C_CatalogShop.GetVCProductInfos](#c_catalogshopgetvcproductinfos) | 1 value | 1 value |
| ✅ | [C_CatalogShop.GetVirtualCurrencyBalance](#c_catalogshopgetvirtualcurrencybalance) |  |  |
| ✅ | [C_CatalogShop.HasNewProducts](#c_catalogshophasnewproducts) | 1 value | 1 value |
| ✅ | [C_CatalogShop.IsProductIncludedInAnyBundle](#c_catalogshopisproductincludedinanybundle) |  |  |
| ✅ | [C_CatalogShop.IsShop2Enabled](#c_catalogshopisshop2enabled) | 1 value | 1 value |
| ✅ | [C_CatalogShop.OnLegalDisclaimerClicked](#c_catalogshoponlegaldisclaimerclicked) |  |  |
| ✅ | [C_CatalogShop.OnLegalPersonalizedOptOutClicked](#c_catalogshoponlegalpersonalizedoptoutclicked) |  |  |
| ✅ | [C_CatalogShop.OpenCatalogShopInteractionFromHouse](#c_catalogshopopencatalogshopinteractionfromhouse) |  |  |
| ✅ | [C_CatalogShop.OpenCatalogShopInteractionFromShop](#c_catalogshopopencatalogshopinteractionfromshop) |  |  |
| ✅ | [C_CatalogShop.ProductDisplayedTelemetry](#c_catalogshopproductdisplayedtelemetry) |  |  |
| ✅ | [C_CatalogShop.ProductSelectedTelemetry](#c_catalogshopproductselectedtelemetry) |  |  |
| ✅ | [C_CatalogShop.PurchaseProduct](#c_catalogshoppurchaseproduct) |  |  |
| ✅ | [C_CatalogShop.RefreshRefundableDecors](#c_catalogshoprefreshrefundabledecors) |  |  |
| ✅ | [C_CatalogShop.RefreshVirtualCurrencyBalance](#c_catalogshoprefreshvirtualcurrencybalance) |  |  |
| ✅ | [C_CatalogShop.ShouldShowHousingWarning](#c_catalogshopshouldshowhousingwarning) | 1 value | 1 value |
| ✅ | [C_CatalogShop.StartHousingVCPurchaseConfirmation](#c_catalogshopstarthousingvcpurchaseconfirmation) |  |  |

### C_CatalogShop.BulkPurchaseProducts

`C_CatalogShop.BulkPurchaseProducts(productIDs: number[]) → canPurchaseProducts: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.BulkRefundDecors

`C_CatalogShop.BulkRefundDecors(decorGUIDs: WOWGUID[])`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.CloseCatalogShopInteraction

`C_CatalogShop.CloseCatalogShopInteraction()`

- Status: ✅ verified (function)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.ConfirmHousingPurchase

`C_CatalogShop.ConfirmHousingPurchase(productIDs: number[])`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.FindBestCurrencyProductForNeededAmount

`C_CatalogShop.FindBestCurrencyProductForNeededAmount(vcCurrencyCode: string, amountNeeded: number) → vcProductID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetAvailableCategoryIDs

`C_CatalogShop.GetAvailableCategoryIDs() → categoryIDs: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetAvailableTransmogRaceInfos

`C_CatalogShop.GetAvailableTransmogRaceInfos() → raceIDs: AvailableRaceInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table}`
- Called in combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table}`
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetCatalogShopProductDisplayInfo

`C_CatalogShop.GetCatalogShopProductDisplayInfo(catalogShopProductID: number) → item: CatalogShopProductDisplayInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetCategoryInfo

`C_CatalogShop.GetCategoryInfo(categoryID: number) → categoryInfo: CatalogShopCategoryInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetCategorySectionInfo

`C_CatalogShop.GetCategorySectionInfo(categoryID: number, sectionID: number) → sectionInfo: CatalogShopSectionInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetFailureInfo

`C_CatalogShop.GetFailureInfo() → errorResultEnum: StoreError?, errorResultRaw: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `nil`
- Called in combat: returned 2 values: `number`, `nil`
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetFirstCategoryByProductID

`C_CatalogShop.GetFirstCategoryByProductID(productID: number) → categoryInfo: CatalogShopCategoryInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetNewProducts

`C_CatalogShop.GetNewProducts() → newProducts: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductAvailabilityTimeRemainingSecs

`C_CatalogShop.GetProductAvailabilityTimeRemainingSecs(catalogShopProductID: number) → timeRemainingSecs: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductIDsForBundle

`C_CatalogShop.GetProductIDsForBundle(bundleProductID: number) → childIDs: CatalogShopBundleChildInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductIDsForCategory

`C_CatalogShop.GetProductIDsForCategory(categoryID: number) → productIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductIDsForCategorySection

`C_CatalogShop.GetProductIDsForCategorySection(categoryID: number, sectionID: number) → productIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductInfo

`C_CatalogShop.GetProductInfo(productID: number) → productInfo: CatalogShopProductInfo?`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductSortOrder

`C_CatalogShop.GetProductSortOrder(categoryID: number, sectionID: number, productID: number) → sortOrder: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetRefundableDecors

`C_CatalogShop.GetRefundableDecors(productIdFilterOpt: number?) → refundableDecorInfos: RefundableDecorInfo[], minTimeRemainingSeconds: time_t`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 2 values: `table{}`, `number`
- Called in combat: returned 2 values: `table{}`, `number`
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetSectionIDsForCategory

`C_CatalogShop.GetSectionIDsForCategory(categoryID: number) → sectionIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetSpellVisualInfoForMount

`C_CatalogShop.GetSpellVisualInfoForMount(spellVisualID: number) → spellVisualInfo: CatalogShopSpellVisualInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetVCProductInfos

`C_CatalogShop.GetVCProductInfos() → vcProductInfos: CatalogShopVCProductInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetVirtualCurrencyBalance

`C_CatalogShop.GetVirtualCurrencyBalance(currencyCode: string) → balance: string?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.HasNewProducts

`C_CatalogShop.HasNewProducts() → hasNewProducts: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.IsProductIncludedInAnyBundle

`C_CatalogShop.IsProductIncludedInAnyBundle(productID: number) → isIncludedInAnyBundle: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.IsShop2Enabled

`C_CatalogShop.IsShop2Enabled() → value: bool?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.OnLegalDisclaimerClicked

`C_CatalogShop.OnLegalDisclaimerClicked(catalogShopProductID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.OnLegalPersonalizedOptOutClicked

`C_CatalogShop.OnLegalPersonalizedOptOutClicked()`

- Status: ✅ verified (function)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.OpenCatalogShopInteractionFromHouse

`C_CatalogShop.OpenCatalogShopInteractionFromHouse() → shoppingSessionUUIDStr: string`

- Status: ✅ verified (function)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.OpenCatalogShopInteractionFromShop

`C_CatalogShop.OpenCatalogShopInteractionFromShop() → shoppingSessionUUIDStr: string`

- Status: ✅ verified (function)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.ProductDisplayedTelemetry

`C_CatalogShop.ProductDisplayedTelemetry(categoryId: number, sectionId: number, catalogShopProductID: number)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.ProductSelectedTelemetry

`C_CatalogShop.ProductSelectedTelemetry(categoryId: number, sectionId: number, catalogShopProductID: number, wasCodeSelection: bool)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.PurchaseProduct

`C_CatalogShop.PurchaseProduct(productID: number) → canPurchase: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.RefreshRefundableDecors

`C_CatalogShop.RefreshRefundableDecors()`

- Status: ✅ verified (function)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.RefreshVirtualCurrencyBalance

`C_CatalogShop.RefreshVirtualCurrencyBalance(currencyCode: string)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.ShouldShowHousingWarning

`C_CatalogShop.ShouldShowHousingWarning() → shouldShowHousingWarning: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.StartHousingVCPurchaseConfirmation

`C_CatalogShop.StartHousingVCPurchaseConfirmation(productID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

## Events

### BULK_PURCHASE_RESULT_RECEIVED

- Status: ✅ verified
- Payload: `result: BulkPurchaseResult`, `productResults: BulkPurchaseIndividualProductResult[]`, `bestTopUpProductID: number?`, `totalCost: number?`
- fires synchronously (Blizzard's docs)

### BULK_REFUND_RESULT_RECEIVED

- Status: ✅ verified
- Payload: `result: BulkRefundResult`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_ADD_PENDING_PRODUCT

- Status: ✅ verified
- Payload: `productID: number`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_DATA_REFRESH

- Status: ✅ verified
- Payload: `shoppingSessionUUIDStr: string?`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `s`

### CATALOG_SHOP_DISABLED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_FETCH_FAILURE

- Status: ✅ verified
- Payload: `shoppingSessionUUIDStr: string?`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_FETCH_SUCCESS

- Status: ✅ verified
- Payload: `shoppingSessionUUIDStr: string?`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `s`

### CATALOG_SHOP_OPEN_SIMPLE_CHECKOUT

- Status: ✅ verified
- Payload: `checkoutID: number`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_PURCHASE_SUCCESS

- Status: ✅ verified
- Payload: `productID: number`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_REBUILD_SCROLL_BOX

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_REFUNDABLE_DECORS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### CATALOG_SHOP_REMOVE_PENDING_PRODUCT

- Status: ✅ verified
- Payload: `productID: number`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_RESULT_ERROR

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_SPECIFIC_PRODUCT_REFRESH

- Status: ✅ verified
- Payload: `productID: number`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_VIRTUAL_CURRENCY_BALANCE_UPDATE

- Status: ✅ verified
- Payload: `currencyCode: string`, `balance: string`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_VIRTUAL_CURRENCY_BALANCE_UPDATE_FAILURE

- Status: ✅ verified
- Payload: `currencyCode: string`
- fires synchronously (Blizzard's docs)

### SET_SEEN_PRODUCTS

- Status: ✅ verified
- Payload: `productIds: number[]`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `t`

### SHOW_NEW_PRODUCT_NOTIFICATION

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (0 in combat); argument kinds: ``

## Types

### AvailableRaceInfo

- Structure
  - `raceID`: number
  - `displayName`: string

### BulkPurchaseIndividualProductResult

- Structure
  - `recordId`: number
  - `parentProductId`: number?
  - `entitlementId`: string
  - `externalTransactionId`: string
  - `status`: SimpleOrderStatus

### CatalogShopBundleChildInfo

- Structure
  - `childProductID`: number
  - `displayOrder`: number
  - `quantityInBundle`: number

### CatalogShopCategoryInfo

- Structure
  - `ID`: number
  - `displayName`: string
  - `iconTexture`: string
  - `linkTag`: string
  - `isDisabled`: bool
  - `showPersistentRefundButton`: bool

### CatalogShopProductDisplayInfo

- Structure
  - `defaultPreviewModelSceneID`: number
  - `defaultCardModelSceneID`: number
  - `defaultWideCardModelSceneID`: number
  - `itemID`: number
  - `overridePreviewModelSceneID`: number?
  - `overrideCardModelSceneID`: number?
  - `overrideWideCardModelSceneID`: number?
  - `creatureDisplayInfoIDs`: number[]
  - `spellVisualIDs`: number[]
  - `mainHandItemModifiedAppearanceID`: number?
  - `offHandItemModifiedAppearanceID`: number?
  - `itemModifiedAppearanceIDs`: number[]
  - `iconFileDataID`: number?
  - `iconTextureKit`: textureKit?
  - `productType`: string?
  - `itemDescription`: string?
  - `hasUnknownLicense`: bool
  - `productPMTURL`: string?
  - `additionalProductPMTURLs`: string[]
  - `otherProductImageAtlasName`: string?
  - `otherProductGameTitleBaseTag`: string?
  - `otherProductGameType`: string?
  - `customLoopingSoundStart`: number?
  - `customLoopingSoundMiddle`: number?
  - `customLoopingSoundEnd`: number?
  - `specialActorID_1`: string?
  - `specialActorID_2`: string?
  - `specialActorID_3`: string?
  - `specialActorID_4`: string?
  - `specialActorID_5`: string?
  - `gameFlavorID`: number?
  - `decorFileDataID`: number?
  - `quantity`: number?
  - `houseTextureAtlas`: textureAtlas?

### CatalogShopProductInfo

- Structure
  - `catalogShopProductID`: number
  - `name`: string
  - `type`: string?
  - `description`: string
  - `iconTexture`: string
  - `isFullyOwned`: bool
  - `isPurchasePending`: bool
  - `refundable`: bool
  - `price`: string
  - `originalPrice`: string
  - `discountPercentage`: number
  - `itemID`: number
  - `mountID`: number
  - `mountTypeName`: string
  - `speciesID`: number
  - `transmogSetID`: number
  - `itemModifiedAppearanceID`: number
  - `subItems`: CatalogShopSubItemInfo[]
  - `subItemsLoaded`: bool
  - `backgroundTexture`: string
  - `foregroundTexture`: string?
  - `smallCardBGTexture`: string?
  - `smallCardFGTexture`: string?
  - `wideCardBGTexture`: string?
  - `wideCardFGTexture`: string?
  - `previewIconTexture`: string?
  - `optionalWideCardBackgroundTexture`: string?
  - `isBundle`: bool
  - `bundleChildrenSize`: number
  - `licenseTermType`: number
  - `licenseTermDuration`: number
  - `virtualCurrencies`: CatalogShopVirtualCurrency[]
  - `isHidden`: bool
  - `isMystery`: bool
  - `hasPendingOrders`: bool
  - `numBundleDetailCards`: number
  - `isDynamicallyDiscounted`: bool
  - `shouldShowOriginalPrice`: bool
  - `wideCardBGOverrideProductURL`: string?
  - `previewBGOverrideProductURL`: string?
  - `previewSmallBGOverrideProductURL`: string?
  - `decorQuantity`: DecorQuantity?
  - `isVCProduct`: bool
  - `containsHousingItem`: bool
  - `deferredGameTimeDays`: number

### CatalogShopSectionInfo

- Structure
  - `ID`: number
  - `displayName`: string
  - `parentCatalogShopCategoryInfoID`: number?
  - `cardType`: string?
  - `scrollGridSize`: number?
  - `shouldShowRecommendationOptOutDisclaimer`: bool

### CatalogShopSpellVisualInfo

- Structure
  - `animID`: number?
  - `spellVisualKitID`: number?

### CatalogShopSubItemInfo

- Structure
  - `name`: string
  - `itemID`: number
  - `itemAppearanceID`: number
  - `invType`: string
  - `quality`: ItemQuality

### CatalogShopVCProductInfo

- Structure
  - `vcProductID`: number

### CatalogShopVirtualCurrency

- Structure
  - `amount`: number
  - `currencyCode`: string

### DecorQuantity

- Structure
  - `placedQuantity`: number
  - `storedQuantity`: number

### RefundableDecorInfo

- Structure
  - `decorGUID`: WOWGUID
  - `timeRemainingSeconds`: time_t
  - `name`: string
  - `price`: string
