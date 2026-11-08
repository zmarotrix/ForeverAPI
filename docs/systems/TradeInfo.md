# TradeInfo

Namespace: `C_TradeInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_TradeInfo.AddTradeMoney](#c_tradeinfoaddtrademoney) |  |  |
| ❔ | [C_TradeInfo.PickupTradeMoney](#c_tradeinfopickuptrademoney) |  |  |
| ❔ | [C_TradeInfo.SetTradeMoney](#c_tradeinfosettrademoney) |  |  |
| ❔ | [C_TradeInfo.ShouldShowTradeOfferWarning](#c_tradeinfoshouldshowtradeofferwarning) |  |  |

### C_TradeInfo.AddTradeMoney

`C_TradeInfo.AddTradeMoney()`

- Status: ❔ unverified
- Blizzard: Adds any cursor-held money to the current trade offer.
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `TradeInfoDocumentation.lua`

### C_TradeInfo.PickupTradeMoney

`C_TradeInfo.PickupTradeMoney(amount: WOWMONEY)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TradeInfoDocumentation.lua`

### C_TradeInfo.SetTradeMoney

`C_TradeInfo.SetTradeMoney(amount: WOWMONEY)`

- Status: ❔ unverified
- Blizzard: Sets the amount of money in the current trade offer.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TradeInfoDocumentation.lua`

### C_TradeInfo.ShouldShowTradeOfferWarning

`C_TradeInfo.ShouldShowTradeOfferWarning() → shouldShow: bool`

- Status: ❔ unverified
- Source: client docs `TradeInfoDocumentation.lua`

## Events

### PLAYER_TRADE_CURRENCY

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_TRADE_MONEY

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRADE_ACCEPT_UPDATE

- Status: ❔ unverified
- Payload: `playerAccepted: number`, `targetAccepted: number`
- fires synchronously (Blizzard's docs)

### TRADE_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRADE_CURRENCY_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRADE_MONEY_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRADE_PLAYER_ITEM_CHANGED

- Status: ❔ unverified
- Payload: `tradeSlotIndex: number`
- fires synchronously (Blizzard's docs)

### TRADE_POTENTIAL_BIND_ENCHANT

- Status: ❔ unverified
- Payload: `canBecomeBoundForTrade: bool`
- fires synchronously (Blizzard's docs)

### TRADE_POTENTIAL_REMOVE_TRANSMOG

- Status: ❔ unverified
- Payload: `itemLink: cstring`, `tradeSlotIndex: number`
- fires synchronously (Blizzard's docs)

### TRADE_REQUEST

- Status: ❔ unverified
- Payload: `name: cstring`
- fires synchronously (Blizzard's docs)

### TRADE_REQUEST_CANCEL

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRADE_SHOW

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRADE_TARGET_ITEM_CHANGED

- Status: ❔ unverified
- Payload: `tradeSlotIndex: number`
- fires synchronously (Blizzard's docs)

### TRADE_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRADE_UPDATE_WARNINGS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
