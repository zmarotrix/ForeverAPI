# ItemSocketInfo

Namespace: `C_ItemSocketInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ItemSocketInfo.AcceptSockets](#c_itemsocketinfoacceptsockets) |  |  |
| ✅ | [C_ItemSocketInfo.ClickSocketButton](#c_itemsocketinfoclicksocketbutton) |  |  |
| ✅ | [C_ItemSocketInfo.CloseSocketInfo](#c_itemsocketinfoclosesocketinfo) |  |  |
| ✅ | [C_ItemSocketInfo.CompleteSocketing](#c_itemsocketinfocompletesocketing) |  |  |
| ✅ | [C_ItemSocketInfo.GetCurrUIType](#c_itemsocketinfogetcurruitype) | 1 value | 1 value |
| ✅ | [C_ItemSocketInfo.GetExistingSocketInfo](#c_itemsocketinfogetexistingsocketinfo) |  |  |
| ✅ | [C_ItemSocketInfo.GetExistingSocketLink](#c_itemsocketinfogetexistingsocketlink) |  |  |
| ✅ | [C_ItemSocketInfo.GetNewSocketInfo](#c_itemsocketinfogetnewsocketinfo) |  |  |
| ✅ | [C_ItemSocketInfo.GetNewSocketLink](#c_itemsocketinfogetnewsocketlink) |  |  |
| ✅ | [C_ItemSocketInfo.GetNumSockets](#c_itemsocketinfogetnumsockets) | 1 value | 1 value |
| ✅ | [C_ItemSocketInfo.GetSocketItemBoundTradeable](#c_itemsocketinfogetsocketitemboundtradeable) | 1 value | 1 value |
| ✅ | [C_ItemSocketInfo.GetSocketItemInfo](#c_itemsocketinfogetsocketiteminfo) | 3 values | 3 values |
| ✅ | [C_ItemSocketInfo.GetSocketItemRefundable](#c_itemsocketinfogetsocketitemrefundable) | 1 value | 1 value |
| ✅ | [C_ItemSocketInfo.GetSocketTypes](#c_itemsocketinfogetsockettypes) |  |  |
| ✅ | [C_ItemSocketInfo.HasBoundGemProposed](#c_itemsocketinfohasboundgemproposed) | 1 value | 1 value |
| ✅ | [C_ItemSocketInfo.IsArtifactRelicItem](#c_itemsocketinfoisartifactrelicitem) |  |  |

### C_ItemSocketInfo.AcceptSockets

`C_ItemSocketInfo.AcceptSockets()`

- Status: ✅ verified (function)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.ClickSocketButton

`C_ItemSocketInfo.ClickSocketButton(index: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.CloseSocketInfo

`C_ItemSocketInfo.CloseSocketInfo()`

- Status: ✅ verified (function)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.CompleteSocketing

`C_ItemSocketInfo.CompleteSocketing()`

- Status: ✅ verified (function)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetCurrUIType

`C_ItemSocketInfo.GetCurrUIType() → uiType: ItemSocketInfoUIType`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetExistingSocketInfo

`C_ItemSocketInfo.GetExistingSocketInfo(index: luaIndex) → name: string?, icon: fileID?, gemMatchesSocket: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetExistingSocketLink

`C_ItemSocketInfo.GetExistingSocketLink(index: luaIndex) → existingSocketLink: string?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetNewSocketInfo

`C_ItemSocketInfo.GetNewSocketInfo(index: luaIndex) → name: string?, icon: fileID?, gemMatchesSocket: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetNewSocketLink

`C_ItemSocketInfo.GetNewSocketLink(index: luaIndex) → newSocketLink: string?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetNumSockets

`C_ItemSocketInfo.GetNumSockets() → numSockets: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetSocketItemBoundTradeable

`C_ItemSocketInfo.GetSocketItemBoundTradeable() → socketItemTradeable: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetSocketItemInfo

`C_ItemSocketInfo.GetSocketItemInfo() → name: string?, icon: fileID?, quality: ItemQuality`

- Status: ✅ verified (function)
- Called out of combat: returned 3 values: `nil`, `nil`, `number`
- Called in combat: returned 3 values: `nil`, `nil`, `number`
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetSocketItemRefundable

`C_ItemSocketInfo.GetSocketItemRefundable() → socketItemRefundable: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetSocketTypes

`C_ItemSocketInfo.GetSocketTypes(index: luaIndex) → socketType: string?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.HasBoundGemProposed

`C_ItemSocketInfo.HasBoundGemProposed() → hasBoundGemProposed: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.IsArtifactRelicItem

`C_ItemSocketInfo.IsArtifactRelicItem(info: ItemInfo) → isArtifactRelicItem: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

## Events

### SOCKET_INFO_ACCEPT

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_BIND_CONFIRM

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_CLOSE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 4 times (0 in combat); argument kinds: ``

### SOCKET_INFO_FAILURE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_REFUNDABLE_CONFIRM

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_SUCCESS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_UI_EVENT_REGISTRATION_UPDATE

- Status: ✅ verified
- Payload: `uiType: ItemSocketInfoUIType`
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### ItemSocketInfoUIType

- Enumeration — ✅ verified
  - `Default` = 0

### SocketInfo

- Structure
  - `name`: string?
  - `icon`: fileID?
  - `gemMatchesSocket`: bool

### SocketItemInfo

- Structure
  - `name`: string?
  - `icon`: fileID?
  - `quality`: ItemQuality
