# CatalogShop

Namespace: `C_CatalogShop`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_CatalogShop.BulkPurchaseProducts](#c_catalogshopbulkpurchaseproducts) |  |  |
| ❔ | [C_CatalogShop.BulkRefundDecors](#c_catalogshopbulkrefunddecors) |  |  |
| ❔ | [C_CatalogShop.CloseCatalogShopInteraction](#c_catalogshopclosecatalogshopinteraction) |  |  |
| ❔ | [C_CatalogShop.ConfirmHousingPurchase](#c_catalogshopconfirmhousingpurchase) |  |  |
| ❔ | [C_CatalogShop.FindBestCurrencyProductForNeededAmount](#c_catalogshopfindbestcurrencyproductforneededamount) |  |  |
| ❔ | [C_CatalogShop.GetAvailableCategoryIDs](#c_catalogshopgetavailablecategoryids) |  |  |
| ❔ | [C_CatalogShop.GetAvailableTransmogRaceInfos](#c_catalogshopgetavailabletransmograceinfos) |  |  |
| ❔ | [C_CatalogShop.GetCatalogShopProductDisplayInfo](#c_catalogshopgetcatalogshopproductdisplayinfo) |  |  |
| ❔ | [C_CatalogShop.GetCategoryInfo](#c_catalogshopgetcategoryinfo) |  |  |
| ❔ | [C_CatalogShop.GetCategorySectionInfo](#c_catalogshopgetcategorysectioninfo) |  |  |
| ❔ | [C_CatalogShop.GetFailureInfo](#c_catalogshopgetfailureinfo) |  |  |
| ❔ | [C_CatalogShop.GetFirstCategoryByProductID](#c_catalogshopgetfirstcategorybyproductid) |  |  |
| ❔ | [C_CatalogShop.GetNewProducts](#c_catalogshopgetnewproducts) |  |  |
| ❔ | [C_CatalogShop.GetProductAvailabilityTimeRemainingSecs](#c_catalogshopgetproductavailabilitytimeremainingsecs) |  |  |
| ❔ | [C_CatalogShop.GetProductIDsForBundle](#c_catalogshopgetproductidsforbundle) |  |  |
| ❔ | [C_CatalogShop.GetProductIDsForCategory](#c_catalogshopgetproductidsforcategory) |  |  |
| ❔ | [C_CatalogShop.GetProductIDsForCategorySection](#c_catalogshopgetproductidsforcategorysection) |  |  |
| ❔ | [C_CatalogShop.GetProductInfo](#c_catalogshopgetproductinfo) |  |  |
| ❔ | [C_CatalogShop.GetProductSortOrder](#c_catalogshopgetproductsortorder) |  |  |
| ❔ | [C_CatalogShop.GetRefundableDecors](#c_catalogshopgetrefundabledecors) |  |  |
| ❔ | [C_CatalogShop.GetSectionIDsForCategory](#c_catalogshopgetsectionidsforcategory) |  |  |
| ❔ | [C_CatalogShop.GetSpellVisualInfoForMount](#c_catalogshopgetspellvisualinfoformount) |  |  |
| ❔ | [C_CatalogShop.GetVCProductInfos](#c_catalogshopgetvcproductinfos) |  |  |
| ❔ | [C_CatalogShop.GetVirtualCurrencyBalance](#c_catalogshopgetvirtualcurrencybalance) |  |  |
| ❔ | [C_CatalogShop.HasNewProducts](#c_catalogshophasnewproducts) |  |  |
| ❔ | [C_CatalogShop.IsProductIncludedInAnyBundle](#c_catalogshopisproductincludedinanybundle) |  |  |
| ❔ | [C_CatalogShop.IsShop2Enabled](#c_catalogshopisshop2enabled) |  |  |
| ❔ | [C_CatalogShop.OnLegalDisclaimerClicked](#c_catalogshoponlegaldisclaimerclicked) |  |  |
| ❔ | [C_CatalogShop.OnLegalPersonalizedOptOutClicked](#c_catalogshoponlegalpersonalizedoptoutclicked) |  |  |
| ❔ | [C_CatalogShop.OpenCatalogShopInteractionFromHouse](#c_catalogshopopencatalogshopinteractionfromhouse) |  |  |
| ❔ | [C_CatalogShop.OpenCatalogShopInteractionFromShop](#c_catalogshopopencatalogshopinteractionfromshop) |  |  |
| ❔ | [C_CatalogShop.ProductDisplayedTelemetry](#c_catalogshopproductdisplayedtelemetry) |  |  |
| ❔ | [C_CatalogShop.ProductSelectedTelemetry](#c_catalogshopproductselectedtelemetry) |  |  |
| ❔ | [C_CatalogShop.PurchaseProduct](#c_catalogshoppurchaseproduct) |  |  |
| ❔ | [C_CatalogShop.RefreshRefundableDecors](#c_catalogshoprefreshrefundabledecors) |  |  |
| ❔ | [C_CatalogShop.RefreshVirtualCurrencyBalance](#c_catalogshoprefreshvirtualcurrencybalance) |  |  |
| ❔ | [C_CatalogShop.ShouldShowHousingWarning](#c_catalogshopshouldshowhousingwarning) |  |  |
| ❔ | [C_CatalogShop.StartHousingVCPurchaseConfirmation](#c_catalogshopstarthousingvcpurchaseconfirmation) |  |  |

### C_CatalogShop.BulkPurchaseProducts

`C_CatalogShop.BulkPurchaseProducts(productIDs: number[]) → canPurchaseProducts: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.BulkRefundDecors

`C_CatalogShop.BulkRefundDecors(decorGUIDs: WOWGUID[])`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.CloseCatalogShopInteraction

`C_CatalogShop.CloseCatalogShopInteraction()`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.ConfirmHousingPurchase

`C_CatalogShop.ConfirmHousingPurchase(productIDs: number[])`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.FindBestCurrencyProductForNeededAmount

`C_CatalogShop.FindBestCurrencyProductForNeededAmount(vcCurrencyCode: string, amountNeeded: number) → vcProductID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetAvailableCategoryIDs

`C_CatalogShop.GetAvailableCategoryIDs() → categoryIDs: number[]`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetAvailableTransmogRaceInfos

`C_CatalogShop.GetAvailableTransmogRaceInfos() → raceIDs: AvailableRaceInfo[]`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetCatalogShopProductDisplayInfo

`C_CatalogShop.GetCatalogShopProductDisplayInfo(catalogShopProductID: number) → item: CatalogShopProductDisplayInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetCategoryInfo

`C_CatalogShop.GetCategoryInfo(categoryID: number) → categoryInfo: CatalogShopCategoryInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetCategorySectionInfo

`C_CatalogShop.GetCategorySectionInfo(categoryID: number, sectionID: number) → sectionInfo: CatalogShopSectionInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetFailureInfo

`C_CatalogShop.GetFailureInfo() → errorResultEnum: StoreError?, errorResultRaw: number?`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetFirstCategoryByProductID

`C_CatalogShop.GetFirstCategoryByProductID(productID: number) → categoryInfo: CatalogShopCategoryInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetNewProducts

`C_CatalogShop.GetNewProducts() → newProducts: number[]`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductAvailabilityTimeRemainingSecs

`C_CatalogShop.GetProductAvailabilityTimeRemainingSecs(catalogShopProductID: number) → timeRemainingSecs: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductIDsForBundle

`C_CatalogShop.GetProductIDsForBundle(bundleProductID: number) → childIDs: CatalogShopBundleChildInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductIDsForCategory

`C_CatalogShop.GetProductIDsForCategory(categoryID: number) → productIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductIDsForCategorySection

`C_CatalogShop.GetProductIDsForCategorySection(categoryID: number, sectionID: number) → productIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductInfo

`C_CatalogShop.GetProductInfo(productID: number) → productInfo: CatalogShopProductInfo?`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetProductSortOrder

`C_CatalogShop.GetProductSortOrder(categoryID: number, sectionID: number, productID: number) → sortOrder: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetRefundableDecors

`C_CatalogShop.GetRefundableDecors(productIdFilterOpt: number?) → refundableDecorInfos: RefundableDecorInfo[], minTimeRemainingSeconds: time_t`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetSectionIDsForCategory

`C_CatalogShop.GetSectionIDsForCategory(categoryID: number) → sectionIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetSpellVisualInfoForMount

`C_CatalogShop.GetSpellVisualInfoForMount(spellVisualID: number) → spellVisualInfo: CatalogShopSpellVisualInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetVCProductInfos

`C_CatalogShop.GetVCProductInfos() → vcProductInfos: CatalogShopVCProductInfo[]`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.GetVirtualCurrencyBalance

`C_CatalogShop.GetVirtualCurrencyBalance(currencyCode: string) → balance: string?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.HasNewProducts

`C_CatalogShop.HasNewProducts() → hasNewProducts: bool`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.IsProductIncludedInAnyBundle

`C_CatalogShop.IsProductIncludedInAnyBundle(productID: number) → isIncludedInAnyBundle: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.IsShop2Enabled

`C_CatalogShop.IsShop2Enabled() → value: bool?`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.OnLegalDisclaimerClicked

`C_CatalogShop.OnLegalDisclaimerClicked(catalogShopProductID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.OnLegalPersonalizedOptOutClicked

`C_CatalogShop.OnLegalPersonalizedOptOutClicked()`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.OpenCatalogShopInteractionFromHouse

`C_CatalogShop.OpenCatalogShopInteractionFromHouse() → shoppingSessionUUIDStr: string`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.OpenCatalogShopInteractionFromShop

`C_CatalogShop.OpenCatalogShopInteractionFromShop() → shoppingSessionUUIDStr: string`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.ProductDisplayedTelemetry

`C_CatalogShop.ProductDisplayedTelemetry(categoryId: number, sectionId: number, catalogShopProductID: number)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.ProductSelectedTelemetry

`C_CatalogShop.ProductSelectedTelemetry(categoryId: number, sectionId: number, catalogShopProductID: number, wasCodeSelection: bool)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.PurchaseProduct

`C_CatalogShop.PurchaseProduct(productID: number) → canPurchase: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.RefreshRefundableDecors

`C_CatalogShop.RefreshRefundableDecors()`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.RefreshVirtualCurrencyBalance

`C_CatalogShop.RefreshVirtualCurrencyBalance(currencyCode: string)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.ShouldShowHousingWarning

`C_CatalogShop.ShouldShowHousingWarning() → shouldShowHousingWarning: bool`

- Status: ❔ unverified
- Source: client docs `CatalogShopDocumentation.lua`

### C_CatalogShop.StartHousingVCPurchaseConfirmation

`C_CatalogShop.StartHousingVCPurchaseConfirmation(productID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CatalogShopDocumentation.lua`

## Events

### BULK_PURCHASE_RESULT_RECEIVED

- Status: ❔ unverified
- Payload: `result: BulkPurchaseResult`, `productResults: BulkPurchaseIndividualProductResult[]`, `bestTopUpProductID: number?`, `totalCost: number?`
- fires synchronously (Blizzard's docs)

### BULK_REFUND_RESULT_RECEIVED

- Status: ❔ unverified
- Payload: `result: BulkRefundResult`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_ADD_PENDING_PRODUCT

- Status: ❔ unverified
- Payload: `productID: number`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_DATA_REFRESH

- Status: ❔ unverified
- Payload: `shoppingSessionUUIDStr: string?`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_DISABLED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_FETCH_FAILURE

- Status: ❔ unverified
- Payload: `shoppingSessionUUIDStr: string?`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_FETCH_SUCCESS

- Status: ❔ unverified
- Payload: `shoppingSessionUUIDStr: string?`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_OPEN_SIMPLE_CHECKOUT

- Status: ❔ unverified
- Payload: `checkoutID: number`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_PURCHASE_SUCCESS

- Status: ❔ unverified
- Payload: `productID: number`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_REBUILD_SCROLL_BOX

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_REFUNDABLE_DECORS_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_REMOVE_PENDING_PRODUCT

- Status: ❔ unverified
- Payload: `productID: number`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_RESULT_ERROR

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_SPECIFIC_PRODUCT_REFRESH

- Status: ❔ unverified
- Payload: `productID: number`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_VIRTUAL_CURRENCY_BALANCE_UPDATE

- Status: ❔ unverified
- Payload: `currencyCode: string`, `balance: string`
- fires synchronously (Blizzard's docs)

### CATALOG_SHOP_VIRTUAL_CURRENCY_BALANCE_UPDATE_FAILURE

- Status: ❔ unverified
- Payload: `currencyCode: string`
- fires synchronously (Blizzard's docs)

### SET_SEEN_PRODUCTS

- Status: ❔ unverified
- Payload: `productIds: number[]`
- fires synchronously (Blizzard's docs)

### SHOW_NEW_PRODUCT_NOTIFICATION

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

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
