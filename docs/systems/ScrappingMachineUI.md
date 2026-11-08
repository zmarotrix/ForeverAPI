# ScrappingMachineUI

Namespace: `C_ScrappingMachineUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ScrappingMachineUI.CloseScrappingMachine](#c_scrappingmachineuiclosescrappingmachine) |  |  |
| ✅ | [C_ScrappingMachineUI.DropPendingScrapItemFromCursor](#c_scrappingmachineuidroppendingscrapitemfromcursor) |  |  |
| ✅ | [C_ScrappingMachineUI.GetCurrentPendingScrapItemLocationByIndex](#c_scrappingmachineuigetcurrentpendingscrapitemlocationbyindex) |  |  |
| ✅ | [C_ScrappingMachineUI.GetScrapSpellID](#c_scrappingmachineuigetscrapspellid) | 1 value |  |
| ✅ | [C_ScrappingMachineUI.GetScrappingMachineName](#c_scrappingmachineuigetscrappingmachinename) | 0 values |  |
| ✅ | [C_ScrappingMachineUI.HasScrappableItems](#c_scrappingmachineuihasscrappableitems) | 1 value |  |
| ✅ | [C_ScrappingMachineUI.RemoveAllScrapItems](#c_scrappingmachineuiremoveallscrapitems) |  |  |
| ✅ | [C_ScrappingMachineUI.RemoveCurrentScrappingItem](#c_scrappingmachineuiremovecurrentscrappingitem) |  |  |
| ✅ | [C_ScrappingMachineUI.RemoveItemToScrap](#c_scrappingmachineuiremoveitemtoscrap) |  |  |
| ✅ | [C_ScrappingMachineUI.ScrapItems](#c_scrappingmachineuiscrapitems) |  |  |
| ✅ | [C_ScrappingMachineUI.ValidateScrappingList](#c_scrappingmachineuivalidatescrappinglist) |  |  |

### C_ScrappingMachineUI.CloseScrappingMachine

`C_ScrappingMachineUI.CloseScrappingMachine()`

- Status: ✅ verified (function)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.DropPendingScrapItemFromCursor

`C_ScrappingMachineUI.DropPendingScrapItemFromCursor(index: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.GetCurrentPendingScrapItemLocationByIndex

`C_ScrappingMachineUI.GetCurrentPendingScrapItemLocationByIndex(index: number) → itemLoc: ItemLocation`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.GetScrapSpellID

`C_ScrappingMachineUI.GetScrapSpellID() → spellID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.GetScrappingMachineName

`C_ScrappingMachineUI.GetScrappingMachineName() → name: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.HasScrappableItems

`C_ScrappingMachineUI.HasScrappableItems() → hasScrappableItems: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.RemoveAllScrapItems

`C_ScrappingMachineUI.RemoveAllScrapItems()`

- Status: ✅ verified (function)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.RemoveCurrentScrappingItem

`C_ScrappingMachineUI.RemoveCurrentScrappingItem()`

- Status: ✅ verified (function)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.RemoveItemToScrap

`C_ScrappingMachineUI.RemoveItemToScrap(index: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.ScrapItems

`C_ScrappingMachineUI.ScrapItems()`

- Status: ✅ verified (function)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.ValidateScrappingList

`C_ScrappingMachineUI.ValidateScrappingList()`

- Status: ✅ verified (function)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

## Events

### SCRAPPING_MACHINE_ITEM_ADDED

- Status: ✅ verified
- Payload: `index: number`
- fires synchronously (Blizzard's docs)

### SCRAPPING_MACHINE_ITEM_REMOVED

- Status: ✅ verified
- Payload: `index: number`
- fires synchronously (Blizzard's docs)

### SCRAPPING_MACHINE_PENDING_ITEM_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SCRAPPING_MACHINE_SCRAPPING_FINISHED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
