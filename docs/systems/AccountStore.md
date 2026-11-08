# AccountStore

Namespace: `C_AccountStore`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_AccountStore.BeginPurchase](#c_accountstorebeginpurchase) |  |  |
| ❔ | [C_AccountStore.GetCategories](#c_accountstoregetcategories) |  |  |
| ❔ | [C_AccountStore.GetCategoryInfo](#c_accountstoregetcategoryinfo) |  |  |
| ❔ | [C_AccountStore.GetCategoryItems](#c_accountstoregetcategoryitems) |  |  |
| ❔ | [C_AccountStore.GetCurrencyAvailable](#c_accountstoregetcurrencyavailable) |  |  |
| ❔ | [C_AccountStore.GetCurrencyIDForStore](#c_accountstoregetcurrencyidforstore) |  |  |
| ❔ | [C_AccountStore.GetCurrencyInfo](#c_accountstoregetcurrencyinfo) |  |  |
| ❔ | [C_AccountStore.GetItemInfo](#c_accountstoregetiteminfo) |  |  |
| ❔ | [C_AccountStore.GetStoreFrontState](#c_accountstoregetstorefrontstate) |  |  |
| ❔ | [C_AccountStore.RefundItem](#c_accountstorerefunditem) |  |  |
| ❔ | [C_AccountStore.RequestStoreFrontInfoUpdate](#c_accountstorerequeststorefrontinfoupdate) |  |  |

### C_AccountStore.BeginPurchase

`C_AccountStore.BeginPurchase(itemID: number) → purchaseStarted: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

### C_AccountStore.GetCategories

`C_AccountStore.GetCategories(storeFrontID: number) → categories: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

### C_AccountStore.GetCategoryInfo

`C_AccountStore.GetCategoryInfo(categoryID: number) → info: AccountStoreCategoryInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

### C_AccountStore.GetCategoryItems

`C_AccountStore.GetCategoryItems(categoryID: number) → itemIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

### C_AccountStore.GetCurrencyAvailable

`C_AccountStore.GetCurrencyAvailable(currencyID: number) → amount: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

### C_AccountStore.GetCurrencyIDForStore

`C_AccountStore.GetCurrencyIDForStore(storeFrontID: number) → currencyID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

### C_AccountStore.GetCurrencyInfo

`C_AccountStore.GetCurrencyInfo(currencyID: number) → info: AccountStoreCurrencyInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

### C_AccountStore.GetItemInfo

`C_AccountStore.GetItemInfo(itemID: number) → info: AccountStoreItemInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

### C_AccountStore.GetStoreFrontState

`C_AccountStore.GetStoreFrontState(storeFrontID: number) → state: AccountStoreState`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

### C_AccountStore.RefundItem

`C_AccountStore.RefundItem(itemID: number) → refundStarted: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

### C_AccountStore.RequestStoreFrontInfoUpdate

`C_AccountStore.RequestStoreFrontInfoUpdate(storeFrontID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountStoreDocumentation.lua`

## Events

### ACCOUNT_STORE_CURRENCY_AVAILABLE_UPDATED

- Status: ❔ unverified
- Payload: `currencyID: number`
- fires synchronously (Blizzard's docs)

### ACCOUNT_STORE_FRONT_UPDATED

- Status: ❔ unverified
- Payload: `storeFrontID: number`
- fires synchronously (Blizzard's docs)

### ACCOUNT_STORE_ITEM_INFO_UPDATED

- Status: ❔ unverified
- Payload: `itemID: number`
- fires synchronously (Blizzard's docs)

### ACCOUNT_STORE_TRANSACTION_ERROR

- Status: ❔ unverified
- Payload: `result: AccountStoreTransactionResult`
- fires synchronously (Blizzard's docs)

### STORE_FRONT_STATE_UPDATED

- Status: ❔ unverified
- Payload: `storeFrontID: number`
- fires synchronously (Blizzard's docs)

## Types

### AccountStoreCategoryInfo

- Structure
  - `id`: number
  - `name`: cstring
  - `type`: AccountStoreCategoryType
  - `icon`: fileID

### AccountStoreCurrencyInfo

- Structure
  - `id`: number
  - `amount`: number
  - `maxQuantity`: number?
  - `name`: cstring
  - `icon`: fileID

### AccountStoreItemInfo

- Structure
  - `id`: number
  - `status`: AccountStoreItemStatus
  - `mode`: AccountStoreItemMode
  - `currencyID`: number
  - `flags`: AccountStoreItemFlag
  - `customUIModelSceneID`: number?
  - `name`: cstring
  - `description`: cstring?
  - `price`: number
  - `nonrefundable`: bool
  - `creatureDisplayID`: number?
  - `transmogSetID`: number?
  - `displayIcon`: fileID?
  - `refundSecondsRemaining`: time_t?
