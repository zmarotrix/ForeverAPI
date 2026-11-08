# TooltipComparison

Namespace: `C_TooltipComparison`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_TooltipComparison.CompareItem](#c_tooltipcomparisoncompareitem) |  |  |
| ❔ | [C_TooltipComparison.GetItemComparisonDelta](#c_tooltipcomparisongetitemcomparisondelta) |  |  |
| ❔ | [C_TooltipComparison.GetItemComparisonInfo](#c_tooltipcomparisongetitemcomparisoninfo) |  |  |

### C_TooltipComparison.CompareItem

`C_TooltipComparison.CompareItem(comparisonItem: TooltipComparisonItem, tooltip: Tooltip, anchorFrame: SimpleFrame?)`

- Status: ❔ unverified
- protected: only Blizzard's secure code may call it (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TooltipComparisonDocumentation.lua`

### C_TooltipComparison.GetItemComparisonDelta

`C_TooltipComparison.GetItemComparisonDelta(comparisonItem: TooltipComparisonItem, equippedItem: TooltipComparisonItem, pairedItem: TooltipComparisonItem?, addPairedStats: bool?) → lines: string[]`

- Status: ❔ unverified
- `addPairedStats`: Whether the paired item's stats are added or subtracted
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TooltipComparisonDocumentation.lua`

### C_TooltipComparison.GetItemComparisonInfo

`C_TooltipComparison.GetItemComparisonInfo(comparisonItem: TooltipComparisonItem) → info: TooltipItemComparisonInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TooltipComparisonDocumentation.lua`

## Events

### TOOLTIP_SHOW_ITEM_COMPARISON

- Status: ❔ unverified
- Payload: `comparisonItem: TooltipComparisonItem`, `tooltip: Tooltip`, `anchorFrame: SimpleFrame?`
- CallbackEvent (Blizzard's docs)

## Types

### TooltipComparisonMethod

- Enumeration — ❔ unverified
  - `Single` = 0
  - `WithBothHands` = 1
  - `WithBagMainHandItem` = 2
  - `WithBagOffHandItem` = 3

### TooltipItemComparisonInfo

- Structure
  - `method`: TooltipComparisonMethod
  - `item`: TooltipComparisonItem
  - `additionalItems`: TooltipComparisonItem[]
