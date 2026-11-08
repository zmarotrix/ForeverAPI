# ChatBubbles

Namespace: `C_ChatBubbles`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ChatBubbles.GetAllChatBubbles](#c_chatbubblesgetallchatbubbles) | 1 value | 1 value |

### C_ChatBubbles.GetAllChatBubbles

`C_ChatBubbles.GetAllChatBubbles(includeForbidden: bool = False) → chatBubbles: ChatBubbleFrame[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `ChatBubblesDocumentation.lua`
