# ItemInteractionUI

Namespace: `C_ItemInteraction`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ItemInteraction.ClearPendingItem](#c_iteminteractionclearpendingitem) |  |  |
| ✅ | [C_ItemInteraction.CloseUI](#c_iteminteractioncloseui) |  |  |
| ✅ | [C_ItemInteraction.GetChargeInfo](#c_iteminteractiongetchargeinfo) |  |  |
| ✅ | [C_ItemInteraction.GetItemConversionCurrencyCost](#c_iteminteractiongetitemconversioncurrencycost) |  |  |
| ✅ | [C_ItemInteraction.GetItemInteractionInfo](#c_iteminteractiongetiteminteractioninfo) |  |  |
| ✅ | [C_ItemInteraction.GetItemInteractionSpellId](#c_iteminteractiongetiteminteractionspellid) |  |  |
| ✅ | [C_ItemInteraction.InitializeFrame](#c_iteminteractioninitializeframe) |  |  |
| ✅ | [C_ItemInteraction.PerformItemInteraction](#c_iteminteractionperformiteminteraction) |  |  |
| ✅ | [C_ItemInteraction.Reset](#c_iteminteractionreset) |  |  |
| ✅ | [C_ItemInteraction.SetPendingItem](#c_iteminteractionsetpendingitem) |  |  |

### C_ItemInteraction.ClearPendingItem

`C_ItemInteraction.ClearPendingItem()`

- Status: ✅ verified (function)
- Source: client docs `ItemInteractionUIDocumentation.lua`

### C_ItemInteraction.CloseUI

`C_ItemInteraction.CloseUI()`

- Status: ✅ verified (function)
- Source: client docs `ItemInteractionUIDocumentation.lua`

### C_ItemInteraction.GetChargeInfo

`C_ItemInteraction.GetChargeInfo() → chargeInfo: ItemInteractionChargeInfo`

- Status: ✅ verified (function)
- Source: client docs `ItemInteractionUIDocumentation.lua`

### C_ItemInteraction.GetItemConversionCurrencyCost

`C_ItemInteraction.GetItemConversionCurrencyCost(item: ItemLocation) → conversionCost: ConversionCurrencyCost`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemInteractionUIDocumentation.lua`

### C_ItemInteraction.GetItemInteractionInfo

`C_ItemInteraction.GetItemInteractionInfo() → info: ItemInteractionFrameInfo?`

- Status: ✅ verified (function)
- Source: client docs `ItemInteractionUIDocumentation.lua`

### C_ItemInteraction.GetItemInteractionSpellId

`C_ItemInteraction.GetItemInteractionSpellId() → spellId: number`

- Status: ✅ verified (function)
- Source: client docs `ItemInteractionUIDocumentation.lua`

### C_ItemInteraction.InitializeFrame

`C_ItemInteraction.InitializeFrame()`

- Status: ✅ verified (function)
- Source: client docs `ItemInteractionUIDocumentation.lua`

### C_ItemInteraction.PerformItemInteraction

`C_ItemInteraction.PerformItemInteraction()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `ItemInteractionUIDocumentation.lua`

### C_ItemInteraction.Reset

`C_ItemInteraction.Reset()`

- Status: ✅ verified (function)
- Source: client docs `ItemInteractionUIDocumentation.lua`

### C_ItemInteraction.SetPendingItem

`C_ItemInteraction.SetPendingItem(item: ItemLocation?) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemInteractionUIDocumentation.lua`

## Events

### ITEM_INTERACTION_CHARGE_INFO_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ITEM_INTERACTION_ITEM_SELECTION_UPDATED

- Status: ✅ verified
- Payload: `itemLocation: ItemLocation?`
- fires synchronously (Blizzard's docs)

## Types

### ConversionCurrencyCost

- Structure
  - `currencyID`: number
  - `amount`: number

### ItemInteractionChargeInfo

- Structure
  - `newChargeAmount`: number
  - `rechargeRate`: number
  - `timeToNextCharge`: number

### ItemInteractionFrameInfo

- Structure
  - `textureKit`: textureKit
  - `openSoundKitID`: number
  - `closeSoundKitID`: number
  - `titleText`: string
  - `tutorialText`: string
  - `buttonText`: string
  - `interactionType`: UIItemInteractionType
  - `flags`: UIItemInteractionFlags
  - `description`: string?
  - `buttonTooltip`: string?
  - `confirmationDescription`: string?
  - `slotTooltip`: string?
  - `cost`: number?
  - `currencyTypeId`: number?
  - `dropInSlotSoundKitId`: number?
