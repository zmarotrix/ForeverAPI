# StorePublic

Namespace: `C_StorePublic`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_StorePublic.DoesGroupHavePurchaseableProducts](#c_storepublicdoesgrouphavepurchaseableproducts) |  |  |
| ✅ | [C_StorePublic.EventStoreUISetShown](#c_storepubliceventstoreuisetshown) |  |  |
| ✅ | [C_StorePublic.IsEnabled](#c_storepublicisenabled) |  |  |

### C_StorePublic.DoesGroupHavePurchaseableProducts

`C_StorePublic.DoesGroupHavePurchaseableProducts(groupID: number) → hasPurchaseableProducts: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `StorePublicUIDocumentation.lua`

### C_StorePublic.EventStoreUISetShown

`C_StorePublic.EventStoreUISetShown(newShown: bool, contextKey: string?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `StorePublicUIDocumentation.lua`

### C_StorePublic.IsEnabled

`C_StorePublic.IsEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Source: client docs `StorePublicUIDocumentation.lua`
