# WowTokenUI

Namespace: `C_WowTokenUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_WowTokenUI.ShouldDisplayInAuctionHouse](#c_wowtokenuishoulddisplayinauctionhouse) |  |  |
| ❔ | [C_WowTokenUI.StartTokenSell](#c_wowtokenuistarttokensell) |  |  |

### C_WowTokenUI.ShouldDisplayInAuctionHouse

`C_WowTokenUI.ShouldDisplayInAuctionHouse() → displayInAH: bool`

- Status: ❔ unverified
- Source: client docs `WowTokenUIDocumentation.lua`

### C_WowTokenUI.StartTokenSell

`C_WowTokenUI.StartTokenSell(tokenGUID: WOWGUID)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WowTokenUIDocumentation.lua`

## Events

### TOKEN_AUCTION_SOLD

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_BUY_CONFIRM_REQUIRED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_BUY_RESULT

- Status: ❔ unverified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### TOKEN_CAN_VETERAN_BUY_UPDATE

- Status: ❔ unverified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### TOKEN_DISTRIBUTIONS_UPDATED

- Status: ❔ unverified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### TOKEN_MARKET_PRICE_UPDATED

- Status: ❔ unverified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### TOKEN_REDEEM_BALANCE_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_REDEEM_CONFIRM_REQUIRED

- Status: ❔ unverified
- Payload: `choiceType: luaIndex`
- fires synchronously (Blizzard's docs)

### TOKEN_REDEEM_FRAME_SHOW

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_REDEEM_GAME_TIME_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_REDEEM_RESULT

- Status: ❔ unverified
- Payload: `result: luaIndex`, `choiceType: luaIndex`
- fires synchronously (Blizzard's docs)

### TOKEN_SELL_CONFIRMED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_SELL_CONFIRM_REQUIRED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### TOKEN_SELL_RESULT

- Status: ❔ unverified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### TOKEN_STATUS_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
