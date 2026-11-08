# CurrencySystem

Namespace: `C_CurrencyInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_CurrencyInfo.CanTransferCurrency](#c_currencyinfocantransfercurrency) |  |  |
| ✅ | [C_CurrencyInfo.DoesCurrentFilterRequireAccountCurrencyData](#c_currencyinfodoescurrentfilterrequireaccountcurrencydata) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.DoesWarModeBonusApply](#c_currencyinfodoeswarmodebonusapply) |  |  |
| ✅ | [C_CurrencyInfo.ExpandCurrencyList](#c_currencyinfoexpandcurrencylist) |  |  |
| ✅ | [C_CurrencyInfo.FetchCurrencyDataFromAccountCharacters](#c_currencyinfofetchcurrencydatafromaccountcharacters) |  |  |
| ✅ | [C_CurrencyInfo.FetchCurrencyTransferTransactions](#c_currencyinfofetchcurrencytransfertransactions) |  |  |
| ✅ | [C_CurrencyInfo.GetAzeriteCurrencyID](#c_currencyinfogetazeritecurrencyid) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.GetBackpackCurrencyInfo](#c_currencyinfogetbackpackcurrencyinfo) | 0 values | 0 values |
| ✅ | [C_CurrencyInfo.GetBasicCurrencyInfo](#c_currencyinfogetbasiccurrencyinfo) |  |  |
| ✅ | [C_CurrencyInfo.GetCoinIcon](#c_currencyinfogetcoinicon) |  |  |
| ✅ | [C_CurrencyInfo.GetCoinText](#c_currencyinfogetcointext) |  |  |
| ✅ | [C_CurrencyInfo.GetCoinTextureString](#c_currencyinfogetcointexturestring) |  |  |
| ✅ | [C_CurrencyInfo.GetCostToTransferCurrency](#c_currencyinfogetcosttotransfercurrency) |  |  |
| ✅ | [C_CurrencyInfo.GetCurrencyContainerInfo](#c_currencyinfogetcurrencycontainerinfo) |  |  |
| ✅ | [C_CurrencyInfo.GetCurrencyDescription](#c_currencyinfogetcurrencydescription) |  |  |
| ✅ | [C_CurrencyInfo.GetCurrencyFilter](#c_currencyinfogetcurrencyfilter) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.GetCurrencyIDFromLink](#c_currencyinfogetcurrencyidfromlink) |  |  |
| ✅ | [C_CurrencyInfo.GetCurrencyInfo](#c_currencyinfogetcurrencyinfo) |  |  |
| ✅ | [C_CurrencyInfo.GetCurrencyInfoFromLink](#c_currencyinfogetcurrencyinfofromlink) |  |  |
| ✅ | [C_CurrencyInfo.GetCurrencyLink](#c_currencyinfogetcurrencylink) |  |  |
| ✅ | [C_CurrencyInfo.GetCurrencyListInfo](#c_currencyinfogetcurrencylistinfo) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.GetCurrencyListLink](#c_currencyinfogetcurrencylistlink) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.GetCurrencyListSize](#c_currencyinfogetcurrencylistsize) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.GetDragonIslesSuppliesCurrencyID](#c_currencyinfogetdragonislessuppliescurrencyid) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.GetFactionGrantedByCurrency](#c_currencyinfogetfactiongrantedbycurrency) |  |  |
| ✅ | [C_CurrencyInfo.GetMaxTransferableAmountFromQuantity](#c_currencyinfogetmaxtransferableamountfromquantity) |  |  |
| ✅ | [C_CurrencyInfo.GetPlayerCurrencyCategoryInfo](#c_currencyinfogetplayercurrencycategoryinfo) |  |  |
| ✅ | [C_CurrencyInfo.GetWarResourcesCurrencyID](#c_currencyinfogetwarresourcescurrencyid) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.IsAccountCharacterCurrencyDataReady](#c_currencyinfoisaccountcharactercurrencydataready) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.IsAccountTransferableCurrency](#c_currencyinfoisaccounttransferablecurrency) |  |  |
| ✅ | [C_CurrencyInfo.IsAccountWideCurrency](#c_currencyinfoisaccountwidecurrency) |  |  |
| ✅ | [C_CurrencyInfo.IsCurrencyContainer](#c_currencyinfoiscurrencycontainer) |  |  |
| ✅ | [C_CurrencyInfo.IsCurrencyTransferInProgress](#c_currencyinfoiscurrencytransferinprogress) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.IsCurrencyTransferTransactionDataReady](#c_currencyinfoiscurrencytransfertransactiondataready) | 1 value | 1 value |
| ✅ | [C_CurrencyInfo.PickupCurrency](#c_currencyinfopickupcurrency) |  |  |
| ✅ | [C_CurrencyInfo.PlayerHasMaxQuantity](#c_currencyinfoplayerhasmaxquantity) |  |  |
| ✅ | [C_CurrencyInfo.PlayerHasMaxWeeklyQuantity](#c_currencyinfoplayerhasmaxweeklyquantity) |  |  |
| ✅ | [C_CurrencyInfo.RequestCurrencyDataForAccountCharacters](#c_currencyinforequestcurrencydataforaccountcharacters) |  |  |
| ✅ | [C_CurrencyInfo.RequestCurrencyFromAccountCharacter](#c_currencyinforequestcurrencyfromaccountcharacter) |  |  |
| ✅ | [C_CurrencyInfo.SetCurrencyBackpack](#c_currencyinfosetcurrencybackpack) |  |  |
| ✅ | [C_CurrencyInfo.SetCurrencyBackpackByID](#c_currencyinfosetcurrencybackpackbyid) |  |  |
| ✅ | [C_CurrencyInfo.SetCurrencyFilter](#c_currencyinfosetcurrencyfilter) |  |  |
| ✅ | [C_CurrencyInfo.SetCurrencyUnused](#c_currencyinfosetcurrencyunused) |  |  |

### C_CurrencyInfo.CanTransferCurrency

`C_CurrencyInfo.CanTransferCurrency(currencyID: number) → canTransferCurrency: bool, failureReason: AccountCurrencyTransferResult?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.DoesCurrentFilterRequireAccountCurrencyData

`C_CurrencyInfo.DoesCurrentFilterRequireAccountCurrencyData() → doesCurrentFilterRequireAccountCurrencyData: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.DoesWarModeBonusApply

`C_CurrencyInfo.DoesWarModeBonusApply(currencyID: number) → warModeApplies: bool?, limitOncePerTooltip: bool?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.ExpandCurrencyList

`C_CurrencyInfo.ExpandCurrencyList(index: luaIndex, expand: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.FetchCurrencyDataFromAccountCharacters

`C_CurrencyInfo.FetchCurrencyDataFromAccountCharacters(currencyID: number) → accountCurrencyData: CharacterCurrencyData[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.FetchCurrencyTransferTransactions

`C_CurrencyInfo.FetchCurrencyTransferTransactions() → currencyTransferTransactions: CurrencyTransferTransaction[]`

- Status: ✅ verified (function)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetAzeriteCurrencyID

`C_CurrencyInfo.GetAzeriteCurrencyID() → azeriteCurrencyID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetBackpackCurrencyInfo

`C_CurrencyInfo.GetBackpackCurrencyInfo(index: luaIndex) → info: BackpackCurrencyInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetBasicCurrencyInfo

`C_CurrencyInfo.GetBasicCurrencyInfo(currencyType: number, quantity: number?) → info: CurrencyDisplayInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCoinIcon

`C_CurrencyInfo.GetCoinIcon(amount: WOWMONEY) → result: fileID`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCoinText

`C_CurrencyInfo.GetCoinText(amount: WOWMONEY, separator: cstring = , ) → result: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCoinTextureString

`C_CurrencyInfo.GetCoinTextureString(amount: WOWMONEY, fontHeight: number = 14) → result: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCostToTransferCurrency

`C_CurrencyInfo.GetCostToTransferCurrency(currencyID: number, quantity: number) → totalQuantityConsumed: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCurrencyContainerInfo

`C_CurrencyInfo.GetCurrencyContainerInfo(currencyType: number, quantity: number) → info: CurrencyDisplayInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCurrencyDescription

`C_CurrencyInfo.GetCurrencyDescription(type: number) → description: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCurrencyFilter

`C_CurrencyInfo.GetCurrencyFilter() → filterType: CurrencyFilterType`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCurrencyIDFromLink

`C_CurrencyInfo.GetCurrencyIDFromLink(currencyLink: cstring) → currencyID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCurrencyInfo

`C_CurrencyInfo.GetCurrencyInfo(type: number) → info: CurrencyInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCurrencyInfoFromLink

`C_CurrencyInfo.GetCurrencyInfoFromLink(link: string) → info: CurrencyInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCurrencyLink

`C_CurrencyInfo.GetCurrencyLink(type: number, amount: number?) → link: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCurrencyListInfo

`C_CurrencyInfo.GetCurrencyListInfo(index: luaIndex) → info: CurrencyInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `table{canEarnPerWeek=boolean,currencyID=number,currencyListDepth=number,description=string,discovered=boolean,isAccountTransferable=boolean,isAccountWide=boolean,isHeader=boolean,isHeaderExpanded=boolean,isShowInBackpack=boolean,isTradeable=boolean,isTypeUnused=boolean,maxQuantity=number,maxWeeklyQuantity=number,name=string,quality=number,quantity=number,quantityEarnedThisWeek=number,rechargingAmountPerCycle=number,rechargingCycleDurationMS=number,totalEarned=number,trackedQuantity=number,useTotalEarnedForMaxQty=boolean}`
- Called in combat: returned 1 value: `table{canEarnPerWeek=boolean,currencyID=number,currencyListDepth=number,description=string,discovered=boolean,isAccountTransferable=boolean,isAccountWide=boolean,isHeader=boolean,isHeaderExpanded=boolean,isShowInBackpack=boolean,isTradeable=boolean,isTypeUnused=boolean,maxQuantity=number,maxWeeklyQuantity=number,name=string,quality=number,quantity=number,quantityEarnedThisWeek=number,rechargingAmountPerCycle=number,rechargingCycleDurationMS=number,totalEarned=number,trackedQuantity=number,useTotalEarnedForMaxQty=boolean}`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCurrencyListLink

`C_CurrencyInfo.GetCurrencyListLink(index: luaIndex) → link: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetCurrencyListSize

`C_CurrencyInfo.GetCurrencyListSize() → currencyListSize: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetDragonIslesSuppliesCurrencyID

`C_CurrencyInfo.GetDragonIslesSuppliesCurrencyID() → dragonIslesSuppliesCurrencyID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetFactionGrantedByCurrency

`C_CurrencyInfo.GetFactionGrantedByCurrency(currencyID: number) → factionID: number?`

- Status: ✅ verified (function)
- Blizzard: Gets the faction ID for currency that is immediately converted into reputation with that faction instead.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetMaxTransferableAmountFromQuantity

`C_CurrencyInfo.GetMaxTransferableAmountFromQuantity(currencyID: number, requestedQuantity: number) → maxTransferableAmount: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetPlayerCurrencyCategoryInfo

`C_CurrencyInfo.GetPlayerCurrencyCategoryInfo(categoryID: number, includeAccountWide: bool = True) → info: PlayerCurrencyCategoryInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.GetWarResourcesCurrencyID

`C_CurrencyInfo.GetWarResourcesCurrencyID() → warResourceCurrencyID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.IsAccountCharacterCurrencyDataReady

`C_CurrencyInfo.IsAccountCharacterCurrencyDataReady() → isReady: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.IsAccountTransferableCurrency

`C_CurrencyInfo.IsAccountTransferableCurrency(currencyID: number) → isAccountTransferableCurrency: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.IsAccountWideCurrency

`C_CurrencyInfo.IsAccountWideCurrency(currencyID: number) → isAccountWideCurrency: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.IsCurrencyContainer

`C_CurrencyInfo.IsCurrencyContainer(currencyID: number, quantity: number) → isCurrencyContainer: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.IsCurrencyTransferInProgress

`C_CurrencyInfo.IsCurrencyTransferInProgress() → currencyTransferInProgress: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.IsCurrencyTransferTransactionDataReady

`C_CurrencyInfo.IsCurrencyTransferTransactionDataReady() → isReady: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.PickupCurrency

`C_CurrencyInfo.PickupCurrency(type: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.PlayerHasMaxQuantity

`C_CurrencyInfo.PlayerHasMaxQuantity(currencyID: number) → hasMaxQuantity: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.PlayerHasMaxWeeklyQuantity

`C_CurrencyInfo.PlayerHasMaxWeeklyQuantity(currencyID: number) → hasMaxWeeklyQuantity: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.RequestCurrencyDataForAccountCharacters

`C_CurrencyInfo.RequestCurrencyDataForAccountCharacters()`

- Status: ✅ verified (function)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.RequestCurrencyFromAccountCharacter

`C_CurrencyInfo.RequestCurrencyFromAccountCharacter(sourceCharacterGUID: WOWGUID, currencyID: number, quantity: number)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.SetCurrencyBackpack

`C_CurrencyInfo.SetCurrencyBackpack(index: luaIndex, backpack: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.SetCurrencyBackpackByID

`C_CurrencyInfo.SetCurrencyBackpackByID(currencyType: number, backpack: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.SetCurrencyFilter

`C_CurrencyInfo.SetCurrencyFilter(filterType: CurrencyFilterType)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

### C_CurrencyInfo.SetCurrencyUnused

`C_CurrencyInfo.SetCurrencyUnused(index: luaIndex, unused: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurrencyInfoDocumentation.lua`

## Events

### ACCOUNT_CHARACTER_CURRENCY_DATA_RECEIVED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ACCOUNT_MONEY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CURRENCY_DISPLAY_UPDATE

- Status: ✅ verified
- Payload: `currencyType: number?`, `quantity: number?`, `quantityChange: number?`, `quantityGainSource: number?`, `destroyReason: number?`
- fires synchronously (Blizzard's docs)
- Seen firing 20 times (0 in combat); argument kinds: `-,-,-,-,-`

### CURRENCY_TRANSFER_FAILED

- Status: ✅ verified
- Payload: `failureReason: AccountCurrencyTransferResult`
- fires synchronously (Blizzard's docs)

### CURRENCY_TRANSFER_INITIATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CURRENCY_TRANSFER_LOG_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CURRENCY_TRANSFER_SUCCESS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_MONEY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 5 times (0 in combat); argument kinds: ``

## Types

### BackpackCurrencyInfo

- Structure
  - `name`: string
  - `quantity`: number
  - `iconFileID`: fileID
  - `currencyTypesID`: number

### CharacterCurrencyData

- Structure
  - `characterGUID`: WOWGUID
  - `characterName`: string
  - `fullCharacterName`: string
  - `currencyID`: number
  - `quantity`: number

### CurrencyDisplayInfo

- Structure
  - `name`: string
  - `description`: string
  - `icon`: number
  - `quality`: number
  - `displayAmount`: number
  - `actualAmount`: number

### CurrencyInfo

- Structure
  - `name`: cstring
  - `description`: cstring
  - `currencyID`: number
  - `isHeader`: bool
  - `isHeaderExpanded`: bool
  - `currencyListDepth`: number
  - `isTypeUnused`: bool
  - `isShowInBackpack`: bool
  - `quantity`: number
  - `trackedQuantity`: number
  - `iconFileID`: fileID
  - `maxQuantity`: number
  - `canEarnPerWeek`: bool
  - `quantityEarnedThisWeek`: number
  - `isTradeable`: bool
  - `quality`: ItemQuality
  - `maxWeeklyQuantity`: number
  - `totalEarned`: number
  - `discovered`: bool
  - `useTotalEarnedForMaxQty`: bool
  - `isAccountWide`: bool
  - `isAccountTransferable`: bool
  - `transferPercentage`: number?
  - `rechargingCycleDurationMS`: number
  - `rechargingAmountPerCycle`: number

### CurrencyTransferTransaction

- Structure
  - `sourceCharacterGUID`: WOWGUID
  - `sourceCharacterName`: string
  - `fullSourceCharacterName`: string
  - `destinationCharacterGUID`: WOWGUID
  - `destinationCharacterName`: string
  - `fullDestinationCharacterName`: string
  - `currencyType`: number
  - `quantityTransferred`: number
  - `totalQuantityConsumed`: number
  - `timestamp`: time_t

### PlayerCurrencyCategoryInfo

- Structure
  - `categoryName`: cstring
  - `currencyTypes`: number[]
  - `childCategories`: number[]
