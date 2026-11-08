# GMTicketInfo

## Events

### GM_PLAYER_INFO

- Status: ✅ verified
- Payload: `name: cstring`, `info: cstring`
- fires synchronously (Blizzard's docs)

### ITEM_RESTORATION_BUTTON_STATUS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 3 times (0 in combat); argument kinds: ``

### PETITION_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PETITION_SHOW

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_REPORT_SUBMITTED

- Status: ✅ verified
- Payload: `invitedByGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### QUICK_TICKET_SYSTEM_STATUS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 29 times (12 in combat); argument kinds: ``

### QUICK_TICKET_THROTTLE_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 16 times (7 in combat); argument kinds: ``

### UPDATE_WEB_TICKET

- Status: ✅ verified
- Payload: `hasTicket: bool`, `numTickets: number?`, `ticketStatus: number?`, `caseIndex: number?`, `waitTimeMinutes: number?`, `waitMessage: cstring?`, `caseTitle: cstring?`, `caseDescription: cstring?`
- fires synchronously (Blizzard's docs)
- Seen firing 6 times (3 in combat); argument kinds: `b,-,-,-,-,-,-,-`
