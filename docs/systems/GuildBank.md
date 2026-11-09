# GuildBank

Namespace: `C_GuildBank`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_GuildBank.IsGuildBankEnabled](#c_guildbankisguildbankenabled) | 1 value | 1 value |

### C_GuildBank.IsGuildBankEnabled

`C_GuildBank.IsGuildBankEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GuildBankDocumentation.lua`

## Events

### GUILDBANKBAGSLOTS_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (0 in combat); argument kinds: ``

### GUILDBANKFRAME_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILDBANKFRAME_OPENED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILDBANKLOG_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILDBANK_ITEM_LOCK_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILDBANK_TEXT_CHANGED

- Status: ✅ verified
- Payload: `guildBankTab: luaIndex`
- fires synchronously (Blizzard's docs)

### GUILDBANK_UPDATE_MONEY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### GUILDBANK_UPDATE_TABS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILDBANK_UPDATE_TEXT

- Status: ✅ verified
- Payload: `guildBankTab: number`
- fires synchronously (Blizzard's docs)

### GUILDBANK_UPDATE_WITHDRAWMONEY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 101 times (5 in combat); argument kinds: ``
