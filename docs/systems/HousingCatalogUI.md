# HousingCatalogUI

Namespace: `C_HousingCatalog`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| 🆕 | [C_HousingCatalog.CanDestroyEntry](#c_housingcatalogcandestroyentry) |  |  |
| ✅ | [C_HousingCatalog.CreateCatalogSearcher](#c_housingcatalogcreatecatalogsearcher) |  |  |
| ✅ | [C_HousingCatalog.DeletePreviewCartDecor](#c_housingcatalogdeletepreviewcartdecor) |  |  |
| ✅ | [C_HousingCatalog.DestroyEntry](#c_housingcatalogdestroyentry) |  |  |
| ✅ | [C_HousingCatalog.GetAllFilterTagGroups](#c_housingcataloggetallfiltertaggroups) | 1 value | 1 value |
| ✅ | [C_HousingCatalog.GetAllVariantInfosForEntry](#c_housingcataloggetallvariantinfosforentry) |  |  |
| ✅ | [C_HousingCatalog.GetBundleInfo](#c_housingcataloggetbundleinfo) |  |  |
| ✅ | [C_HousingCatalog.GetCartSizeLimit](#c_housingcataloggetcartsizelimit) | 1 value | 1 value |
| ✅ | [C_HousingCatalog.GetCatalogCategoryAndSubcategoryNames](#c_housingcataloggetcatalogcategoryandsubcategorynames) |  |  |
| ✅ | [C_HousingCatalog.GetCatalogCategoryInfo](#c_housingcataloggetcatalogcategoryinfo) |  |  |
| 🆕 | [C_HousingCatalog.GetCatalogEntryDebugInfoForID](#c_housingcataloggetcatalogentrydebuginfoforid) |  |  |
| ✅ | [C_HousingCatalog.GetCatalogEntryInfo](#c_housingcataloggetcatalogentryinfo) |  |  |
| ✅ | [C_HousingCatalog.GetCatalogEntryInfoByItem](#c_housingcataloggetcatalogentryinfobyitem) |  |  |
| ✅ | [C_HousingCatalog.GetCatalogEntryInfoByRecordID](#c_housingcataloggetcatalogentryinfobyrecordid) |  |  |
| ✅ | [C_HousingCatalog.GetCatalogEntryRefundTimeStampByRecordID](#c_housingcataloggetcatalogentryrefundtimestampbyrecordid) |  |  |
| ✅ | [C_HousingCatalog.GetCatalogEntryVariantInfo](#c_housingcataloggetcatalogentryvariantinfo) |  |  |
| ✅ | [C_HousingCatalog.GetCatalogSubcategoryInfo](#c_housingcataloggetcatalogsubcategoryinfo) |  |  |
| ✅ | [C_HousingCatalog.GetDecorMaxOwnedCount](#c_housingcataloggetdecormaxownedcount) | 1 value | 1 value |
| ✅ | [C_HousingCatalog.GetDecorTotalOwnedCount](#c_housingcataloggetdecortotalownedcount) | 2 values | 2 values |
| ✅ | [C_HousingCatalog.GetDestroyableInstanceCount](#c_housingcataloggetdestroyableinstancecount) |  |  |
| ✅ | [C_HousingCatalog.GetFeaturedBundles](#c_housingcataloggetfeaturedbundles) | 1 value | 1 value |
| 🆕 | [C_HousingCatalog.GetFeaturedDecor](#c_housingcataloggetfeatureddecor) |  |  |
| ✅ | [C_HousingCatalog.GetFeaturedSmallProducts](#c_housingcataloggetfeaturedsmallproducts) | 1 value | 1 value |
| ✅ | [C_HousingCatalog.GetMarketInfoForDecor](#c_housingcataloggetmarketinfofordecor) |  |  |
| ✅ | [C_HousingCatalog.HasFeaturedEntries](#c_housingcataloghasfeaturedentries) | 1 value | 1 value |
| ✅ | [C_HousingCatalog.HousingMarketActionAddToCart](#c_housingcataloghousingmarketactionaddtocart) |  |  |
| ✅ | [C_HousingCatalog.HousingMarketActionClearCart](#c_housingcataloghousingmarketactionclearcart) |  |  |
| ✅ | [C_HousingCatalog.HousingMarketActionRemoveFromCart](#c_housingcataloghousingmarketactionremovefromcart) |  |  |
| ✅ | [C_HousingCatalog.HousingMarketActionViewBundle](#c_housingcataloghousingmarketactionviewbundle) |  |  |
| ✅ | [C_HousingCatalog.HousingMarketActionViewInStore](#c_housingcataloghousingmarketactionviewinstore) |  |  |
| ✅ | [C_HousingCatalog.IsPreviewCartItemShown](#c_housingcatalogispreviewcartitemshown) |  |  |
| ✅ | [C_HousingCatalog.PromotePreviewDecor](#c_housingcatalogpromotepreviewdecor) |  |  |
| ✅ | [C_HousingCatalog.RequestHousingMarketInfoRefresh](#c_housingcatalogrequesthousingmarketinforefresh) |  |  |
| ✅ | [C_HousingCatalog.RequestHousingMarketRefundInfo](#c_housingcatalogrequesthousingmarketrefundinfo) |  |  |
| ✅ | [C_HousingCatalog.SearchCatalogCategories](#c_housingcatalogsearchcatalogcategories) |  |  |
| ✅ | [C_HousingCatalog.SearchCatalogSubcategories](#c_housingcatalogsearchcatalogsubcategories) |  |  |
| ✅ | [C_HousingCatalog.SetPreviewCartItemShown](#c_housingcatalogsetpreviewcartitemshown) |  |  |

### C_HousingCatalog.CanDestroyEntry

`C_HousingCatalog.CanDestroyEntry(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_HousingCatalog.CreateCatalogSearcher

`C_HousingCatalog.CreateCatalogSearcher() → searcher: HousingCatalogSearcher`

- Status: ✅ verified (function)
- Blizzard: Creates a new instance of a HousingCatalog searcher; This can be used to asynchronously search/filter the HousingCatalog without affecting/being restricted by the filter state of other Housing Catalog UI displays
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.DeletePreviewCartDecor

`C_HousingCatalog.DeletePreviewCartDecor(decorGUID: WOWGUID)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.DestroyEntry

`C_HousingCatalog.DestroyEntry(entryVariantID: HousingCatalogEntryVariantID, destroyAll: bool)`

- Status: ✅ verified (function)
- Blizzard: Attempt to delete the entry from storage
- `destroyAll`: If true, deletes all entries within the stack; If false, will only delete one
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetAllFilterTagGroups

`C_HousingCatalog.GetAllFilterTagGroups() → filterTagGroups: HousingCatalogFilterTagGroupInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetAllVariantInfosForEntry

`C_HousingCatalog.GetAllVariantInfosForEntry(entryID: HousingCatalogEntryID) → variantInfos: HousingCatalogEntryVariantInfo[]`

- Status: ✅ verified (function)
- Blizzard: Returns variant info for all variants of a given catalog entry; Variants represent different visual modifications of the same base entry (ex: dyed versions)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetBundleInfo

`C_HousingCatalog.GetBundleInfo(bundleCatalogShopProductID: number) → bundleInfo: HousingBundleInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetCartSizeLimit

`C_HousingCatalog.GetCartSizeLimit() → cartSizeLimit: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetCatalogCategoryAndSubcategoryNames

`C_HousingCatalog.GetCatalogCategoryAndSubcategoryNames(subcategoryID: number) → categoryName: string, subcategoryName: string`

- Status: ✅ verified (function)
- Blizzard: If found, returns the names of the parent category and the specified subcategory
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetCatalogCategoryInfo

`C_HousingCatalog.GetCatalogCategoryInfo(categoryID: number) → info: HousingCatalogCategoryInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetCatalogEntryDebugInfoForID

`C_HousingCatalog.GetCatalogEntryDebugInfoForID(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_HousingCatalog.GetCatalogEntryInfo

`C_HousingCatalog.GetCatalogEntryInfo(entryID: HousingCatalogEntryID) → info: HousingCatalogEntryInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetCatalogEntryInfoByItem

`C_HousingCatalog.GetCatalogEntryInfoByItem(itemInfo: ItemInfo) → info: HousingCatalogEntryInfo?`

- Status: ✅ verified (function)
- `itemInfo`: ItemID, name, or link of an item that grants/corresponds to a particular type of housing catalog object (ex: decor)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetCatalogEntryInfoByRecordID

`C_HousingCatalog.GetCatalogEntryInfoByRecordID(entryType: HousingCatalogEntryType, recordID: number) → info: HousingCatalogEntryInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetCatalogEntryRefundTimeStampByRecordID

`C_HousingCatalog.GetCatalogEntryRefundTimeStampByRecordID(entryType: HousingCatalogEntryType, recordID: number) → refundTimeStamp: time_t?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetCatalogEntryVariantInfo

`C_HousingCatalog.GetCatalogEntryVariantInfo(entryVariantID: HousingCatalogEntryVariantID) → info: HousingCatalogEntryVariantInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetCatalogSubcategoryInfo

`C_HousingCatalog.GetCatalogSubcategoryInfo(subcategoryID: number) → info: HousingCatalogSubcategoryInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetDecorMaxOwnedCount

`C_HousingCatalog.GetDecorMaxOwnedCount() → maxOwnedCount: number`

- Status: ✅ verified (function)
- Blizzard: Returns the maximum total number of decor that can be in storage/in the house chest; Note that not all decor entries in storage count towards this limit (see GetDecorTotalOwnedCount)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetDecorTotalOwnedCount

`C_HousingCatalog.GetDecorTotalOwnedCount() → totalOwnedCount: number, exemptDecorCount: number`

- Status: ✅ verified (function)
- `totalOwnedCount`: The total number of owned decor in storage, including both exempt and non-exempt decor
- `exemptDecorCount`: The number of decor that do not count against the max storage limit
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetDestroyableInstanceCount

`C_HousingCatalog.GetDestroyableInstanceCount(entryVariantID: HousingCatalogEntryVariantID) → destroyableInstanceCount: number`

- Status: ✅ verified (function)
- Blizzard: Returns the number of instances that can be to be destroyed in storage; These instances count towards the max storage limit
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetFeaturedBundles

`C_HousingCatalog.GetFeaturedBundles() → bundleInfos: HousingBundleInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetFeaturedDecor

`C_HousingCatalog.GetFeaturedDecor(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_HousingCatalog.GetFeaturedSmallProducts

`C_HousingCatalog.GetFeaturedSmallProducts() → infos: HousingFeaturedSmallProductInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.GetMarketInfoForDecor

`C_HousingCatalog.GetMarketInfoForDecor(decorID: number) → marketInfo: HousingMarketInfo?`

- Status: ✅ verified (function)
- Blizzard: Returns market info for a specific decor. This is decor-only for now but should be extended to support entry type and recordID generically
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.HasFeaturedEntries

`C_HousingCatalog.HasFeaturedEntries() → hasEntries: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.HousingMarketActionAddToCart

`C_HousingCatalog.HousingMarketActionAddToCart(productID: number, withPreview: bool)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.HousingMarketActionClearCart

`C_HousingCatalog.HousingMarketActionClearCart()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.HousingMarketActionRemoveFromCart

`C_HousingCatalog.HousingMarketActionRemoveFromCart(productID: number)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.HousingMarketActionViewBundle

`C_HousingCatalog.HousingMarketActionViewBundle(productID: number)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.HousingMarketActionViewInStore

`C_HousingCatalog.HousingMarketActionViewInStore(productID: number)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.IsPreviewCartItemShown

`C_HousingCatalog.IsPreviewCartItemShown(decorGUID: WOWGUID) → isShown: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.PromotePreviewDecor

`C_HousingCatalog.PromotePreviewDecor(decorID: number, previewDecorGUID: WOWGUID) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.RequestHousingMarketInfoRefresh

`C_HousingCatalog.RequestHousingMarketInfoRefresh()`

- Status: ✅ verified (function)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.RequestHousingMarketRefundInfo

`C_HousingCatalog.RequestHousingMarketRefundInfo()`

- Status: ✅ verified (function)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.SearchCatalogCategories

`C_HousingCatalog.SearchCatalogCategories(searchParams: HousingCategorySearchInfo) → categoryIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.SearchCatalogSubcategories

`C_HousingCatalog.SearchCatalogSubcategories(searchParams: HousingCategorySearchInfo) → subcategoryIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

### C_HousingCatalog.SetPreviewCartItemShown

`C_HousingCatalog.SetPreviewCartItemShown(decorGUID: WOWGUID, shown: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingCatalogUIDocumentation.lua`

## Events

### HOUSING_CATALOG_CATEGORY_UPDATED

- Status: ✅ verified
- Payload: `categoryID: number`
- unique event (Blizzard's docs)

### HOUSING_CATALOG_SUBCATEGORY_UPDATED

- Status: ✅ verified
- Payload: `subcategoryID: number`
- unique event (Blizzard's docs)

### HOUSING_DECOR_ADD_TO_PREVIEW_LIST

- Status: ✅ verified
- Payload: `previewItemData: HousingPreviewItemData`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_PREVIEW_LIST_REMOVE_FROM_WORLD

- Status: ✅ verified
- Payload: `decorGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### HOUSING_DECOR_PREVIEW_LIST_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_REFUND_LIST_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_STORAGE_ENTRY_UPDATED

- Status: ✅ verified
- Payload: `entryVariantID: HousingCatalogEntryVariantID`
- unique event (Blizzard's docs)

### HOUSING_STORAGE_UPDATED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

## Types

### HousingBundleDecorEntryInfo

- Structure
  - `decorID`: number
  - `quantity`: number

### HousingBundleInfo

- Structure
  - `productID`: number
  - `price`: number
  - `originalPrice`: number?
  - `nonDecorProducts`: number[]
  - `decorEntries`: HousingBundleDecorEntryInfo[]
  - `canPreview`: bool

### HousingCatalogCategoryInfo

- Structure
  - `ID`: number
  - `orderIndex`: number
  - `name`: cstring?
  - `icon`: textureAtlas?
  - `subcategoryIDs`: number[]
  - `anyStoredEntries`: bool

### HousingCatalogEntryInfo

- Structure
- Blizzard: Base information about an object in the Catalog; For info for a specific owned stack of this object, see HousingCatalogEntryVariantInfo
  - `recordID`: number
  - `entryType`: HousingCatalogEntryType
  - `itemID`: number?
  - `name`: cstring
  - `asset`: ModelAsset?
  - `iconTexture`: FileAsset?
  - `iconAtlas`: textureAtlas?
  - `uiModelSceneID`: number?
  - `categoryIDs`: number[]
  - `subcategoryIDs`: number[]
  - `dataTagsByID`: LuaValueVariant
  - `size`: HousingCatalogEntrySize
  - `placementCost`: number
  - `totalNumStored`: number
  - `remainingRedeemable`: number
  - `totalNumPlaced`: number
  - `destroyableInstanceCount`: number
  - `isUniqueTrophy`: bool
  - `isAllowedOutdoors`: bool
  - `isAllowedIndoors`: bool
  - `canCustomize`: bool
  - `isPrefab`: bool
  - `quality`: ItemQuality?
  - `firstAcquisitionBonus`: number
  - `sourceText`: cstring

### HousingCatalogEntryVariantInfo

- Structure
- Blizzard: Represents a single stack of instances of an object in the Catalog, that are all of a specific variation; For example, a stack of undyed chairs, or blue-dyed tables
  - `entryVariantID`: HousingCatalogEntryVariantID
  - `numStored`: number
  - `dyeSlots`: HousingDecorDyeSlot[]

### HousingCatalogSubcategoryInfo

- Structure
  - `ID`: number
  - `orderIndex`: number
  - `parentCategoryID`: number
  - `name`: cstring?
  - `icon`: textureAtlas?
  - `anyStoredEntries`: bool

### HousingCategorySearchInfo

- Structure
  - `withStoredEntriesOnly`: bool
  - `includeFeaturedCategory`: bool
  - `editorModeContext`: HouseEditorMode?

### HousingFeaturedSmallProductInfo

- Structure
  - `entryVariantID`: HousingCatalogEntryVariantID?
  - `productID`: number
  - `price`: number
  - `originalPrice`: number?
  - `canPreview`: bool

### HousingMarketInfo

- Structure
  - `price`: number
  - `productID`: number
  - `bundleIDs`: number[]

### HousingPreviewItemData

- Structure
  - `decorGUID`: WOWGUID?
  - `productID`: number?
  - `bundleCatalogShopProductID`: number?
  - `isBundleParent`: bool
  - `isBundleChild`: bool
  - `id`: number
  - `decorID`: number
  - `name`: string
  - `icon`: number
  - `price`: number
  - `salePrice`: number?
