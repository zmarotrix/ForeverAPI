# MailInfo

Namespace: `C_Mail`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Mail.CanCheckInbox](#c_mailcancheckinbox) |  |  |
| ❔ | [C_Mail.GetCraftingOrderMailInfo](#c_mailgetcraftingordermailinfo) |  |  |
| ❔ | [C_Mail.HasInboxMoney](#c_mailhasinboxmoney) |  |  |
| ❔ | [C_Mail.IsCommandPending](#c_mailiscommandpending) |  |  |
| ❔ | [C_Mail.SetOpeningAll](#c_mailsetopeningall) |  |  |

### C_Mail.CanCheckInbox

`C_Mail.CanCheckInbox() → canCheckInbox: bool, secondsUntilAllowed: number`

- Status: ❔ unverified
- Source: client docs `MailInfoDocumentation.lua`

### C_Mail.GetCraftingOrderMailInfo

`C_Mail.GetCraftingOrderMailInfo(inboxIndex: luaIndex) → info: CraftingOrderMailInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MailInfoDocumentation.lua`

### C_Mail.HasInboxMoney

`C_Mail.HasInboxMoney(inboxIndex: luaIndex) → inboxItemHasMoneyAttached: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MailInfoDocumentation.lua`

### C_Mail.IsCommandPending

`C_Mail.IsCommandPending() → isCommandPending: bool`

- Status: ❔ unverified
- Source: client docs `MailInfoDocumentation.lua`

### C_Mail.SetOpeningAll

`C_Mail.SetOpeningAll(openingAll: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MailInfoDocumentation.lua`

## Events

### CLOSE_INBOX_ITEM

- Status: ❔ unverified
- Payload: `mailIndex: luaIndex`
- fires synchronously (Blizzard's docs)

### MAIL_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### MAIL_FAILED

- Status: ❔ unverified
- Payload: `itemID: number?`
- fires synchronously (Blizzard's docs)

### MAIL_INBOX_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### MAIL_LOCK_SEND_ITEMS

- Status: ❔ unverified
- Payload: `attachSlot: luaIndex`, `itemLink: cstring`
- fires synchronously (Blizzard's docs)

### MAIL_OPEN_ALL_CANCELED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### MAIL_SEND_INFO_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### MAIL_SEND_SUCCESS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### MAIL_SHOW

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### MAIL_SUCCESS

- Status: ❔ unverified
- Payload: `itemID: number?`
- fires synchronously (Blizzard's docs)

### MAIL_UNLOCK_SEND_ITEMS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SEND_MAIL_COD_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SEND_MAIL_MONEY_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_PENDING_MAIL

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
