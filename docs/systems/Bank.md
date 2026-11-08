# Bank

Namespace: `C_Bank`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Bank.AreAnyBankTypesViewable](#c_bankareanybanktypesviewable) |  |  |
| ❔ | [C_Bank.AutoDepositItemsIntoBank](#c_bankautodeposititemsintobank) |  |  |
| ❔ | [C_Bank.BankBagTypeAndIDToInvSlot](#c_bankbankbagtypeandidtoinvslot) |  |  |
| ❔ | [C_Bank.CanDepositMoney](#c_bankcandepositmoney) |  |  |
| ❔ | [C_Bank.CanPurchaseBankTab](#c_bankcanpurchasebanktab) |  |  |
| ❔ | [C_Bank.CanUseBank](#c_bankcanusebank) |  |  |
| ❔ | [C_Bank.CanViewBank](#c_bankcanviewbank) |  |  |
| ❔ | [C_Bank.CanWithdrawMoney](#c_bankcanwithdrawmoney) |  |  |
| ❔ | [C_Bank.CloseBankFrame](#c_bankclosebankframe) |  |  |
| ❔ | [C_Bank.DepositMoney](#c_bankdepositmoney) |  |  |
| ❔ | [C_Bank.DoesBankTypeSupportAutoDeposit](#c_bankdoesbanktypesupportautodeposit) |  |  |
| ❔ | [C_Bank.DoesBankTypeSupportMoneyTransfer](#c_bankdoesbanktypesupportmoneytransfer) |  |  |
| ❔ | [C_Bank.FetchBankLockedReason](#c_bankfetchbanklockedreason) |  |  |
| ❔ | [C_Bank.FetchDepositedMoney](#c_bankfetchdepositedmoney) |  |  |
| ❔ | [C_Bank.FetchMaxNumBankTabs](#c_bankfetchmaxnumbanktabs) |  |  |
| ❔ | [C_Bank.FetchNextPurchasableBankTabData](#c_bankfetchnextpurchasablebanktabdata) |  |  |
| ❔ | [C_Bank.FetchNumPurchasedBankTabs](#c_bankfetchnumpurchasedbanktabs) |  |  |
| ❔ | [C_Bank.FetchPurchasedBankTabData](#c_bankfetchpurchasedbanktabdata) |  |  |
| ❔ | [C_Bank.FetchPurchasedBankTabIDs](#c_bankfetchpurchasedbanktabids) |  |  |
| ❔ | [C_Bank.FetchViewableBankTypes](#c_bankfetchviewablebanktypes) |  |  |
| ❔ | [C_Bank.HasMaxBankTabs](#c_bankhasmaxbanktabs) |  |  |
| ❔ | [C_Bank.IsItemAllowedInBankType](#c_bankisitemallowedinbanktype) |  |  |
| ❔ | [C_Bank.PurchaseBankTab](#c_bankpurchasebanktab) |  |  |
| ❔ | [C_Bank.ShouldUsePlayerBagsInBank](#c_bankshoulduseplayerbagsinbank) |  |  |
| ❔ | [C_Bank.UpdateBankTabSettings](#c_bankupdatebanktabsettings) |  |  |
| ❔ | [C_Bank.WithdrawMoney](#c_bankwithdrawmoney) |  |  |

### C_Bank.AreAnyBankTypesViewable

`C_Bank.AreAnyBankTypesViewable() → areAnyBankTypesViewable: bool`

- Status: ❔ unverified
- Source: client docs `BankDocumentation.lua`

### C_Bank.AutoDepositItemsIntoBank

`C_Bank.AutoDepositItemsIntoBank(bankType: BankType)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.BankBagTypeAndIDToInvSlot

`C_Bank.BankBagTypeAndIDToInvSlot(bankType: BankType, slotIndex: luaIndex) → slot: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.CanDepositMoney

`C_Bank.CanDepositMoney(bankType: BankType) → canDepositMoney: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.CanPurchaseBankTab

`C_Bank.CanPurchaseBankTab(bankType: BankType) → canPurchaseBankTab: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.CanUseBank

`C_Bank.CanUseBank(bankType: BankType) → canUseBank: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.CanViewBank

`C_Bank.CanViewBank(bankType: BankType) → canViewBank: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.CanWithdrawMoney

`C_Bank.CanWithdrawMoney(bankType: BankType) → canWithdrawMoney: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.CloseBankFrame

`C_Bank.CloseBankFrame()`

- Status: ❔ unverified
- Source: client docs `BankDocumentation.lua`

### C_Bank.DepositMoney

`C_Bank.DepositMoney(bankType: BankType, amount: WOWMONEY)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.DoesBankTypeSupportAutoDeposit

`C_Bank.DoesBankTypeSupportAutoDeposit(bankType: BankType) → doesBankTypeSupportAutoDeposit: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.DoesBankTypeSupportMoneyTransfer

`C_Bank.DoesBankTypeSupportMoneyTransfer(bankType: BankType) → doesBankTypeSupportMoneyTransfer: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.FetchBankLockedReason

`C_Bank.FetchBankLockedReason(bankType: BankType) → reason: BankLockedReason?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.FetchDepositedMoney

`C_Bank.FetchDepositedMoney(bankType: BankType) → amount: WOWMONEY`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.FetchMaxNumBankTabs

`C_Bank.FetchMaxNumBankTabs(bankType: BankType) → numPurchasedBankTabs: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.FetchNextPurchasableBankTabData

`C_Bank.FetchNextPurchasableBankTabData(bankType: BankType) → nextPurchasableTabData: PurchasableBankTabData?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.FetchNumPurchasedBankTabs

`C_Bank.FetchNumPurchasedBankTabs(bankType: BankType) → numPurchasedBankTabs: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.FetchPurchasedBankTabData

`C_Bank.FetchPurchasedBankTabData(bankType: BankType) → purchasedBankTabData: BankTabData[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.FetchPurchasedBankTabIDs

`C_Bank.FetchPurchasedBankTabIDs(bankType: BankType) → purchasedBankTabIDs: BagIndex[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.FetchViewableBankTypes

`C_Bank.FetchViewableBankTypes() → viewableBankTypes: BankType[]`

- Status: ❔ unverified
- Source: client docs `BankDocumentation.lua`

### C_Bank.HasMaxBankTabs

`C_Bank.HasMaxBankTabs(bankType: BankType) → hasMaxBankTabs: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.IsItemAllowedInBankType

`C_Bank.IsItemAllowedInBankType(bankType: BankType, itemLocation: ItemLocation) → isItemAllowedInBankType: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.PurchaseBankTab

`C_Bank.PurchaseBankTab(bankType: BankType)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.ShouldUsePlayerBagsInBank

`C_Bank.ShouldUsePlayerBagsInBank() → shouldUsePlayerBagsInBank: bool`

- Status: ❔ unverified
- Source: client docs `BankDocumentation.lua`

### C_Bank.UpdateBankTabSettings

`C_Bank.UpdateBankTabSettings(bankType: BankType, tabID: BagIndex, tabName: cstring, tabIcon: cstring, depositFlags: BagSlotFlags)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

### C_Bank.WithdrawMoney

`C_Bank.WithdrawMoney(bankType: BankType, amount: WOWMONEY)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BankDocumentation.lua`

## Events

### BANKFRAME_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### BANKFRAME_OPENED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### BANK_BAG_SLOT_FLAGS_UPDATED

- Status: ❔ unverified
- Payload: `slot: number`
- fires synchronously (Blizzard's docs)

### BANK_TABS_CHANGED

- Status: ❔ unverified
- Payload: `bankType: BankType`
- fires synchronously (Blizzard's docs)

### BANK_TAB_SETTINGS_UPDATED

- Status: ❔ unverified
- Payload: `bankType: BankType`
- fires synchronously (Blizzard's docs)

### PLAYERBANKSLOTS_CHANGED

- Status: ❔ unverified
- Payload: `slot: number`
- fires synchronously (Blizzard's docs)

### PLAYER_ACCOUNT_BANK_TAB_SLOTS_CHANGED

- Status: ❔ unverified
- Payload: `slot: number`
- fires synchronously (Blizzard's docs)

## Types

### BankLockedReason

- Enumeration — ❔ unverified
  - `None` = 0
  - `NoAccountInventoryLock` = 1
  - `BankDisabled` = 2
  - `BankConversionFailed` = 3

### BankTabData

- Structure
  - `ID`: number
  - `bankType`: BankType
  - `name`: cstring
  - `icon`: fileID
  - `depositFlags`: BagSlotFlags
  - `tabCleanupConfirmation`: cstring
  - `tabNameEditBoxHeader`: cstring

### PurchasableBankTabData

- Structure
  - `tabCost`: BigUInteger
  - `canAfford`: bool
  - `purchasePromptTitle`: cstring
  - `purchasePromptBody`: cstring
  - `purchasePromptConfirmation`: cstring
