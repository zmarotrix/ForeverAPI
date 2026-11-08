# Container

Namespace: `C_Container`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Container.CalculateTotalNumberOfFreeBagSlots](#c_containercalculatetotalnumberoffreebagslots) |  |  |
| ✅ | [C_Container.ContainerIDToInventoryID](#c_containercontaineridtoinventoryid) |  |  |
| ✅ | [C_Container.ContainerRefundItemPurchase](#c_containercontainerrefunditempurchase) |  |  |
| ✅ | [C_Container.GetBackpackAutosortDisabled](#c_containergetbackpackautosortdisabled) | 1 value | 1 value |
| ✅ | [C_Container.GetBackpackSellJunkDisabled](#c_containergetbackpackselljunkdisabled) | 1 value | 1 value |
| ✅ | [C_Container.GetBagName](#c_containergetbagname) | 1 value | 1 value |
| ✅ | [C_Container.GetBagSlotFlag](#c_containergetbagslotflag) | 1 value | 1 value |
| ✅ | [C_Container.GetBankAutosortDisabled](#c_containergetbankautosortdisabled) | 1 value | 1 value |
| ✅ | [C_Container.GetContainerFreeSlots](#c_containergetcontainerfreeslots) | 1 value | 1 value |
| ✅ | [C_Container.GetContainerItemCooldown](#c_containergetcontaineritemcooldown) | 3 values | 3 values |
| ✅ | [C_Container.GetContainerItemDurability](#c_containergetcontaineritemdurability) | 0 values | 0 values |
| ✅ | [C_Container.GetContainerItemEquipmentSetInfo](#c_containergetcontaineritemequipmentsetinfo) | 2 values | 2 values |
| ✅ | [C_Container.GetContainerItemID](#c_containergetcontaineritemid) | 1 value | 1 value |
| ✅ | [C_Container.GetContainerItemInfo](#c_containergetcontaineriteminfo) | 1 value | 1 value |
| ✅ | [C_Container.GetContainerItemLink](#c_containergetcontaineritemlink) | 1 value | 1 value |
| ✅ | [C_Container.GetContainerItemPurchaseCurrency](#c_containergetcontaineritempurchasecurrency) | 0 values | 0 values |
| ✅ | [C_Container.GetContainerItemPurchaseInfo](#c_containergetcontaineritempurchaseinfo) | 0 values | 0 values |
| ✅ | [C_Container.GetContainerItemPurchaseItem](#c_containergetcontaineritempurchaseitem) | 0 values | 0 values |
| ✅ | [C_Container.GetContainerItemQuestInfo](#c_containergetcontaineritemquestinfo) | 1 value | 1 value |
| ✅ | [C_Container.GetContainerNumFreeSlots](#c_containergetcontainernumfreeslots) | 2 values | 2 values |
| ✅ | [C_Container.GetContainerNumSlots](#c_containergetcontainernumslots) | 1 value | 1 value |
| ✅ | [C_Container.GetInsertItemsLeftToRight](#c_containergetinsertitemslefttoright) | 1 value | 1 value |
| ✅ | [C_Container.GetItemCooldown](#c_containergetitemcooldown) | 3 values | 3 values |
| ✅ | [C_Container.GetMaxArenaCurrency](#c_containergetmaxarenacurrency) | 1 value | 1 value |
| ✅ | [C_Container.GetSortBagsRightToLeft](#c_containergetsortbagsrighttoleft) | 1 value | 1 value |
| ✅ | [C_Container.HasContainerItem](#c_containerhascontaineritem) | 1 value | 1 value |
| ✅ | [C_Container.IsBattlePayItem](#c_containerisbattlepayitem) | 1 value | 1 value |
| ✅ | [C_Container.IsContainerFiltered](#c_containeriscontainerfiltered) | 1 value | 1 value |
| ✅ | [C_Container.PickupContainerItem](#c_containerpickupcontaineritem) |  |  |
| ✅ | [C_Container.PlayerHasHearthstone](#c_containerplayerhashearthstone) |  |  |
| ✅ | [C_Container.SetBackpackAutosortDisabled](#c_containersetbackpackautosortdisabled) |  |  |
| ✅ | [C_Container.SetBackpackSellJunkDisabled](#c_containersetbackpackselljunkdisabled) |  |  |
| ✅ | [C_Container.SetBagPortraitTexture](#c_containersetbagportraittexture) |  |  |
| ✅ | [C_Container.SetBagSlotFlag](#c_containersetbagslotflag) |  |  |
| ✅ | [C_Container.SetBankAutosortDisabled](#c_containersetbankautosortdisabled) |  |  |
| ✅ | [C_Container.SetInsertItemsLeftToRight](#c_containersetinsertitemslefttoright) |  |  |
| ✅ | [C_Container.SetItemSearch](#c_containersetitemsearch) |  |  |
| ✅ | [C_Container.SetSortBagsRightToLeft](#c_containersetsortbagsrighttoleft) |  |  |
| ✅ | [C_Container.ShowContainerSellCursor](#c_containershowcontainersellcursor) |  |  |
| ✅ | [C_Container.SocketContainerItem](#c_containersocketcontaineritem) |  |  |
| ✅ | [C_Container.SortAccountBankBags](#c_containersortaccountbankbags) |  |  |
| ✅ | [C_Container.SortBags](#c_containersortbags) |  |  |
| ✅ | [C_Container.SortBank](#c_containersortbank) |  |  |
| ✅ | [C_Container.SortBankBags](#c_containersortbankbags) |  |  |
| ✅ | [C_Container.SplitContainerItem](#c_containersplitcontaineritem) |  |  |
| ✅ | [C_Container.UseContainerItem](#c_containerusecontaineritem) |  |  |
| ✅ | [C_Container.UseHearthstone](#c_containerusehearthstone) |  |  |

### C_Container.CalculateTotalNumberOfFreeBagSlots

`C_Container.CalculateTotalNumberOfFreeBagSlots() → totalFreeSlots: number`

- Status: ✅ verified (function)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.ContainerIDToInventoryID

`C_Container.ContainerIDToInventoryID(containerID: BagIndex) → inventoryID: luaIndex`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.ContainerRefundItemPurchase

`C_Container.ContainerRefundItemPurchase(containerIndex: BagIndex, slotIndex: luaIndex, isEquipped: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetBackpackAutosortDisabled

`C_Container.GetBackpackAutosortDisabled() → isDisabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetBackpackSellJunkDisabled

`C_Container.GetBackpackSellJunkDisabled() → isDisabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetBagName

`C_Container.GetBagName(bagIndex: BagIndex) → name: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetBagSlotFlag

`C_Container.GetBagSlotFlag(bagIndex: BagIndex, flag: BagSlotFlags) → isSet: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetBankAutosortDisabled

`C_Container.GetBankAutosortDisabled() → isDisabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerFreeSlots

`C_Container.GetContainerFreeSlots(containerIndex: BagIndex) → freeSlots: luaIndex[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `table{[number]=number,[number]=number,[number]=number,[number]=number}`
- Called in combat: returned 1 value: `table{[number]=number,[number]=number,[number]=number,[number]=number}`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerItemCooldown

`C_Container.GetContainerItemCooldown(containerIndex: BagIndex, slotIndex: luaIndex) → startTime: number, duration: number, enable: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1`: returned 3 values: `number`, `number`, `number`
- Called in combat: returned 3 values: `number`, `number`, `number`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerItemDurability

`C_Container.GetContainerItemDurability(containerIndex: BagIndex, slotIndex: luaIndex) → durability: number, maxDurability: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerItemEquipmentSetInfo

`C_Container.GetContainerItemEquipmentSetInfo(containerIndex: BagIndex, slotIndex: luaIndex) → inSet: bool, setList: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1`: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerItemID

`C_Container.GetContainerItemID(containerIndex: BagIndex, slotIndex: luaIndex) → containerID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerItemInfo

`C_Container.GetContainerItemInfo(containerIndex: BagIndex, slotIndex: luaIndex) → containerInfo: ContainerItemInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1`: returned 1 value: `table{hasLoot=boolean,hasNoValue=boolean,hyperlink=string,iconFileID=number,isBound=boolean,isFiltered=boolean,isLocked=boolean,isReadable=boolean,itemID=number,itemName=string,quality=number,stackCount=number}`
- Called in combat: returned 1 value: `table{hasLoot=boolean,hasNoValue=boolean,hyperlink=string,iconFileID=number,isBound=boolean,isFiltered=boolean,isLocked=boolean,isReadable=boolean,itemID=number,itemName=string,quality=number,stackCount=number}`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerItemLink

`C_Container.GetContainerItemLink(containerIndex: BagIndex, slotIndex: luaIndex) → itemLink: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1`: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerItemPurchaseCurrency

`C_Container.GetContainerItemPurchaseCurrency(containerIndex: BagIndex, slotIndex: luaIndex, itemIndex: luaIndex, isEquipped: bool) → currencyInfo: ItemPurchaseCurrency`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1,n:1,b:false`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerItemPurchaseInfo

`C_Container.GetContainerItemPurchaseInfo(containerIndex: BagIndex, slotIndex: luaIndex, isEquipped: bool) → info: ItemPurchaseInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1,b:false`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerItemPurchaseItem

`C_Container.GetContainerItemPurchaseItem(containerIndex: BagIndex, slotIndex: luaIndex, itemIndex: luaIndex, isEquipped: bool) → itemInfo: ItemPurchaseItem`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1,n:1,b:false`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerItemQuestInfo

`C_Container.GetContainerItemQuestInfo(containerIndex: BagIndex, slotIndex: luaIndex) → questInfo: ItemQuestInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1`: returned 1 value: `table{isActive=boolean,isQuestItem=boolean}`
- Called in combat: returned 1 value: `table{isActive=boolean,isQuestItem=boolean}`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerNumFreeSlots

`C_Container.GetContainerNumFreeSlots(bagIndex: BagIndex) → numFreeSlots: number, bagFamily: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetContainerNumSlots

`C_Container.GetContainerNumSlots(containerIndex: BagIndex) → numSlots: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetInsertItemsLeftToRight

`C_Container.GetInsertItemsLeftToRight() → isEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetItemCooldown

`C_Container.GetItemCooldown(itemID: number) → startTime: number, duration: number, enable: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `item`: returned 3 values: `number`, `number`, `number`
- Called in combat: returned 3 values: `number`, `number`, `number`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetMaxArenaCurrency

`C_Container.GetMaxArenaCurrency() → maxCurrency: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.GetSortBagsRightToLeft

`C_Container.GetSortBagsRightToLeft() → isEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.HasContainerItem

`C_Container.HasContainerItem(containerIndex: BagIndex, slotIndex: luaIndex) → hasItem: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.IsBattlePayItem

`C_Container.IsBattlePayItem(containerIndex: BagIndex, slotIndex: luaIndex) → isBattlePayItem: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:1`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.IsContainerFiltered

`C_Container.IsContainerFiltered(containerIndex: BagIndex) → isFiltered: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ContainerDocumentation.lua`

### C_Container.PickupContainerItem

`C_Container.PickupContainerItem(containerIndex: BagIndex, slotIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.PlayerHasHearthstone

`C_Container.PlayerHasHearthstone() → itemID: number?`

- Status: ✅ verified (function)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SetBackpackAutosortDisabled

`C_Container.SetBackpackAutosortDisabled(disable: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SetBackpackSellJunkDisabled

`C_Container.SetBackpackSellJunkDisabled(disable: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SetBagPortraitTexture

`C_Container.SetBagPortraitTexture(texture: SimpleTexture, bagIndex: BagIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SetBagSlotFlag

`C_Container.SetBagSlotFlag(bagIndex: BagIndex, flag: BagSlotFlags, isSet: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SetBankAutosortDisabled

`C_Container.SetBankAutosortDisabled(disable: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SetInsertItemsLeftToRight

`C_Container.SetInsertItemsLeftToRight(enable: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SetItemSearch

`C_Container.SetItemSearch(searchString: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SetSortBagsRightToLeft

`C_Container.SetSortBagsRightToLeft(enable: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.ShowContainerSellCursor

`C_Container.ShowContainerSellCursor(containerIndex: BagIndex, slotIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SocketContainerItem

`C_Container.SocketContainerItem(containerIndex: BagIndex, slotIndex: luaIndex) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SortAccountBankBags

`C_Container.SortAccountBankBags()`

- Status: ✅ verified (function)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SortBags

`C_Container.SortBags()`

- Status: ✅ verified (function)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SortBank

`C_Container.SortBank(bankType: BankType)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SortBankBags

`C_Container.SortBankBags()`

- Status: ✅ verified (function)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.SplitContainerItem

`C_Container.SplitContainerItem(containerIndex: BagIndex, slotIndex: luaIndex, amount: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.UseContainerItem

`C_Container.UseContainerItem(containerIndex: BagIndex, slotIndex: luaIndex, unitToken: UnitToken?, bankType: BankType?, reagentBankOpen: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ContainerDocumentation.lua`

### C_Container.UseHearthstone

`C_Container.UseHearthstone() → used: bool`

- Status: ✅ verified (function)
- Source: client docs `ContainerDocumentation.lua`

## Events

### BAG_CLOSED

- Status: ✅ verified
- Payload: `bagID: BagIndex`
- fires synchronously (Blizzard's docs)

### BAG_CONTAINER_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 103 times (0 in combat); argument kinds: ``

### BAG_NEW_ITEMS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 13 times (2 in combat); argument kinds: ``

### BAG_OPEN

- Status: ✅ verified
- Payload: `bagID: number`
- fires synchronously (Blizzard's docs)

### BAG_OVERFLOW_WITH_FULL_INVENTORY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BAG_SLOT_FLAGS_UPDATED

- Status: ✅ verified
- Payload: `slot: number`
- fires synchronously (Blizzard's docs)

### BAG_UPDATE

- Status: ✅ verified
- Payload: `bagID: BagIndex`
- fires synchronously (Blizzard's docs)
- Seen firing 2079 times (15 in combat); argument kinds: `n`

### BAG_UPDATE_COOLDOWN

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 1092 times (928 in combat); argument kinds: ``

### BAG_UPDATE_DELAYED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 104 times (11 in combat); argument kinds: ``

### EQUIP_BIND_REFUNDABLE_CONFIRM

- Status: ✅ verified
- Payload: `slot: number`, `itemLocation: ItemLocation`
- fires synchronously (Blizzard's docs)

### EQUIP_BIND_TRADEABLE_CONFIRM

- Status: ✅ verified
- Payload: `slot: number`, `itemLocation: ItemLocation`
- fires synchronously (Blizzard's docs)

### EXPAND_BAG_BAR_CHANGED

- Status: ✅ verified
- Payload: `expandBagBar: bool`
- fires synchronously (Blizzard's docs)

### INVENTORY_SEARCH_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ITEM_LOCKED

- Status: ✅ verified
- Payload: `bagOrSlotIndex: BagIndex`, `slotIndex: luaIndex?`
- fires synchronously (Blizzard's docs)
- Seen firing 27 times (0 in combat); argument kinds: `n,n`

### ITEM_LOCK_CHANGED

- Status: ✅ verified
- Payload: `bagOrSlotIndex: BagIndex`, `slotIndex: luaIndex?`
- fires synchronously (Blizzard's docs)
- Seen firing 46 times (0 in combat); argument kinds: `n,n`

### ITEM_UNLOCKED

- Status: ✅ verified
- Payload: `bagOrSlotIndex: BagIndex`, `slotIndex: luaIndex?`
- fires synchronously (Blizzard's docs)
- Seen firing 19 times (0 in combat); argument kinds: `n,n`

### USE_COMBINED_BAGS_CHANGED

- Status: ✅ verified
- Payload: `useCombinedBags: bool`
- fires synchronously (Blizzard's docs)

## Types

### ContainerItemInfo

- Structure
  - `iconFileID`: fileID
  - `stackCount`: number
  - `isLocked`: bool
  - `quality`: ItemQuality?
  - `isReadable`: bool
  - `hasLoot`: bool
  - `hyperlink`: string
  - `isFiltered`: bool
  - `hasNoValue`: bool
  - `itemID`: number
  - `isBound`: bool
  - `itemName`: string

### ItemPurchaseCurrency

- Structure
  - `iconFileID`: number?
  - `currencyCount`: number
  - `name`: cstring

### ItemPurchaseInfo

- Structure
  - `money`: WOWMONEY
  - `itemCount`: number
  - `refundSeconds`: time_t
  - `currencyCount`: number
  - `hasEnchants`: bool

### ItemPurchaseItem

- Structure
  - `iconFileID`: number?
  - `itemCount`: number
  - `hyperlink`: string

### ItemQuestInfo

- Structure
  - `isQuestItem`: bool
  - `questID`: number?
  - `isActive`: bool
