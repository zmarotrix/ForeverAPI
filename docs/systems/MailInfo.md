# MailInfo

Namespace: `C_Mail`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Mail.CanCheckInbox](#c_mailcancheckinbox) | 2 values |  |
| ✅ | [C_Mail.GetCraftingOrderMailInfo](#c_mailgetcraftingordermailinfo) |  |  |
| ✅ | [C_Mail.HasInboxMoney](#c_mailhasinboxmoney) |  |  |
| ✅ | [C_Mail.IsCommandPending](#c_mailiscommandpending) | 1 value |  |
| ✅ | [C_Mail.SetOpeningAll](#c_mailsetopeningall) |  |  |

### C_Mail.CanCheckInbox

`C_Mail.CanCheckInbox() → canCheckInbox: bool, secondsUntilAllowed: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `number`
- Source: client docs `MailInfoDocumentation.lua`

### C_Mail.GetCraftingOrderMailInfo

`C_Mail.GetCraftingOrderMailInfo(inboxIndex: luaIndex) → info: CraftingOrderMailInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MailInfoDocumentation.lua`

### C_Mail.HasInboxMoney

`C_Mail.HasInboxMoney(inboxIndex: luaIndex) → inboxItemHasMoneyAttached: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MailInfoDocumentation.lua`

### C_Mail.IsCommandPending

`C_Mail.IsCommandPending() → isCommandPending: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `MailInfoDocumentation.lua`

### C_Mail.SetOpeningAll

`C_Mail.SetOpeningAll(openingAll: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MailInfoDocumentation.lua`

## Events

### CLOSE_INBOX_ITEM

- Status: ✅ verified
- Payload: `mailIndex: luaIndex`
- fires synchronously (Blizzard's docs)

### MAIL_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### MAIL_FAILED

- Status: ✅ verified
- Payload: `itemID: number?`
- fires synchronously (Blizzard's docs)

### MAIL_INBOX_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### MAIL_LOCK_SEND_ITEMS

- Status: ✅ verified
- Payload: `attachSlot: luaIndex`, `itemLink: cstring`
- fires synchronously (Blizzard's docs)

### MAIL_OPEN_ALL_CANCELED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### MAIL_SEND_INFO_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### MAIL_SEND_SUCCESS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### MAIL_SHOW

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### MAIL_SUCCESS

- Status: ✅ verified
- Payload: `itemID: number?`
- fires synchronously (Blizzard's docs)

### MAIL_UNLOCK_SEND_ITEMS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SEND_MAIL_COD_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SEND_MAIL_MONEY_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_PENDING_MAIL

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 4 times (0 in combat); argument kinds: ``
