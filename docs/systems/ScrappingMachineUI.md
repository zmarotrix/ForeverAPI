# ScrappingMachineUI

Namespace: `C_ScrappingMachineUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ScrappingMachineUI.CloseScrappingMachine](#c_scrappingmachineuiclosescrappingmachine) |  |  |
| ❔ | [C_ScrappingMachineUI.DropPendingScrapItemFromCursor](#c_scrappingmachineuidroppendingscrapitemfromcursor) |  |  |
| ❔ | [C_ScrappingMachineUI.GetCurrentPendingScrapItemLocationByIndex](#c_scrappingmachineuigetcurrentpendingscrapitemlocationbyindex) |  |  |
| ❔ | [C_ScrappingMachineUI.GetScrapSpellID](#c_scrappingmachineuigetscrapspellid) |  |  |
| ❔ | [C_ScrappingMachineUI.GetScrappingMachineName](#c_scrappingmachineuigetscrappingmachinename) |  |  |
| ❔ | [C_ScrappingMachineUI.HasScrappableItems](#c_scrappingmachineuihasscrappableitems) |  |  |
| ❔ | [C_ScrappingMachineUI.RemoveAllScrapItems](#c_scrappingmachineuiremoveallscrapitems) |  |  |
| ❔ | [C_ScrappingMachineUI.RemoveCurrentScrappingItem](#c_scrappingmachineuiremovecurrentscrappingitem) |  |  |
| ❔ | [C_ScrappingMachineUI.RemoveItemToScrap](#c_scrappingmachineuiremoveitemtoscrap) |  |  |
| ❔ | [C_ScrappingMachineUI.ScrapItems](#c_scrappingmachineuiscrapitems) |  |  |
| ❔ | [C_ScrappingMachineUI.ValidateScrappingList](#c_scrappingmachineuivalidatescrappinglist) |  |  |

### C_ScrappingMachineUI.CloseScrappingMachine

`C_ScrappingMachineUI.CloseScrappingMachine()`

- Status: ❔ unverified
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.DropPendingScrapItemFromCursor

`C_ScrappingMachineUI.DropPendingScrapItemFromCursor(index: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.GetCurrentPendingScrapItemLocationByIndex

`C_ScrappingMachineUI.GetCurrentPendingScrapItemLocationByIndex(index: number) → itemLoc: ItemLocation`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.GetScrapSpellID

`C_ScrappingMachineUI.GetScrapSpellID() → spellID: number`

- Status: ❔ unverified
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.GetScrappingMachineName

`C_ScrappingMachineUI.GetScrappingMachineName() → name: string`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.HasScrappableItems

`C_ScrappingMachineUI.HasScrappableItems() → hasScrappableItems: bool`

- Status: ❔ unverified
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.RemoveAllScrapItems

`C_ScrappingMachineUI.RemoveAllScrapItems()`

- Status: ❔ unverified
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.RemoveCurrentScrappingItem

`C_ScrappingMachineUI.RemoveCurrentScrappingItem()`

- Status: ❔ unverified
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.RemoveItemToScrap

`C_ScrappingMachineUI.RemoveItemToScrap(index: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.ScrapItems

`C_ScrappingMachineUI.ScrapItems()`

- Status: ❔ unverified
- Source: client docs `ScrappingMachineUIDocumentation.lua`

### C_ScrappingMachineUI.ValidateScrappingList

`C_ScrappingMachineUI.ValidateScrappingList()`

- Status: ❔ unverified
- Source: client docs `ScrappingMachineUIDocumentation.lua`

## Events

### SCRAPPING_MACHINE_ITEM_ADDED

- Status: ❔ unverified
- Payload: `index: number`
- fires synchronously (Blizzard's docs)

### SCRAPPING_MACHINE_ITEM_REMOVED

- Status: ❔ unverified
- Payload: `index: number`
- fires synchronously (Blizzard's docs)

### SCRAPPING_MACHINE_PENDING_ITEM_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SCRAPPING_MACHINE_SCRAPPING_FINISHED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
