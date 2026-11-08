# WowTokenUI

Namespace: `C_WowTokenUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_WowTokenUI.ShouldDisplayInAuctionHouse](#c_wowtokenuishoulddisplayinauctionhouse) |  |  |
| ✅ | [C_WowTokenUI.StartTokenSell](#c_wowtokenuistarttokensell) |  |  |

### C_WowTokenUI.ShouldDisplayInAuctionHouse

`C_WowTokenUI.ShouldDisplayInAuctionHouse() → displayInAH: bool`

- Status: ✅ verified (function)
- Source: client docs `WowTokenUIDocumentation.lua`

### C_WowTokenUI.StartTokenSell

`C_WowTokenUI.StartTokenSell(tokenGUID: WOWGUID)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WowTokenUIDocumentation.lua`

## Events

### TOKEN_AUCTION_SOLD

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_BUY_CONFIRM_REQUIRED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_BUY_RESULT

- Status: ✅ verified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### TOKEN_CAN_VETERAN_BUY_UPDATE

- Status: ✅ verified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### TOKEN_DISTRIBUTIONS_UPDATED

- Status: ✅ verified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### TOKEN_MARKET_PRICE_UPDATED

- Status: ✅ verified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### TOKEN_REDEEM_BALANCE_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_REDEEM_CONFIRM_REQUIRED

- Status: ✅ verified
- Payload: `choiceType: luaIndex`
- fires synchronously (Blizzard's docs)

### TOKEN_REDEEM_FRAME_SHOW

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_REDEEM_GAME_TIME_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_REDEEM_RESULT

- Status: ✅ verified
- Payload: `result: luaIndex`, `choiceType: luaIndex`
- fires synchronously (Blizzard's docs)

### TOKEN_SELL_CONFIRMED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_SELL_CONFIRM_REQUIRED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_SELL_RESULT

- Status: ✅ verified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### TOKEN_STATUS_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
