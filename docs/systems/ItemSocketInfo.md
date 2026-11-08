# ItemSocketInfo

Namespace: `C_ItemSocketInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ItemSocketInfo.AcceptSockets](#c_itemsocketinfoacceptsockets) |  |  |
| ❔ | [C_ItemSocketInfo.ClickSocketButton](#c_itemsocketinfoclicksocketbutton) |  |  |
| ❔ | [C_ItemSocketInfo.CloseSocketInfo](#c_itemsocketinfoclosesocketinfo) |  |  |
| ❔ | [C_ItemSocketInfo.CompleteSocketing](#c_itemsocketinfocompletesocketing) |  |  |
| ❔ | [C_ItemSocketInfo.GetCurrUIType](#c_itemsocketinfogetcurruitype) |  |  |
| ❔ | [C_ItemSocketInfo.GetExistingSocketInfo](#c_itemsocketinfogetexistingsocketinfo) |  |  |
| ❔ | [C_ItemSocketInfo.GetExistingSocketLink](#c_itemsocketinfogetexistingsocketlink) |  |  |
| ❔ | [C_ItemSocketInfo.GetNewSocketInfo](#c_itemsocketinfogetnewsocketinfo) |  |  |
| ❔ | [C_ItemSocketInfo.GetNewSocketLink](#c_itemsocketinfogetnewsocketlink) |  |  |
| ❔ | [C_ItemSocketInfo.GetNumSockets](#c_itemsocketinfogetnumsockets) |  |  |
| ❔ | [C_ItemSocketInfo.GetSocketItemBoundTradeable](#c_itemsocketinfogetsocketitemboundtradeable) |  |  |
| ❔ | [C_ItemSocketInfo.GetSocketItemInfo](#c_itemsocketinfogetsocketiteminfo) |  |  |
| ❔ | [C_ItemSocketInfo.GetSocketItemRefundable](#c_itemsocketinfogetsocketitemrefundable) |  |  |
| ❔ | [C_ItemSocketInfo.GetSocketTypes](#c_itemsocketinfogetsockettypes) |  |  |
| ❔ | [C_ItemSocketInfo.HasBoundGemProposed](#c_itemsocketinfohasboundgemproposed) |  |  |
| ❔ | [C_ItemSocketInfo.IsArtifactRelicItem](#c_itemsocketinfoisartifactrelicitem) |  |  |

### C_ItemSocketInfo.AcceptSockets

`C_ItemSocketInfo.AcceptSockets()`

- Status: ❔ unverified
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.ClickSocketButton

`C_ItemSocketInfo.ClickSocketButton(index: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.CloseSocketInfo

`C_ItemSocketInfo.CloseSocketInfo()`

- Status: ❔ unverified
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.CompleteSocketing

`C_ItemSocketInfo.CompleteSocketing()`

- Status: ❔ unverified
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetCurrUIType

`C_ItemSocketInfo.GetCurrUIType() → uiType: ItemSocketInfoUIType`

- Status: ❔ unverified
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetExistingSocketInfo

`C_ItemSocketInfo.GetExistingSocketInfo(index: luaIndex) → name: string?, icon: fileID?, gemMatchesSocket: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetExistingSocketLink

`C_ItemSocketInfo.GetExistingSocketLink(index: luaIndex) → existingSocketLink: string?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetNewSocketInfo

`C_ItemSocketInfo.GetNewSocketInfo(index: luaIndex) → name: string?, icon: fileID?, gemMatchesSocket: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetNewSocketLink

`C_ItemSocketInfo.GetNewSocketLink(index: luaIndex) → newSocketLink: string?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetNumSockets

`C_ItemSocketInfo.GetNumSockets() → numSockets: number`

- Status: ❔ unverified
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetSocketItemBoundTradeable

`C_ItemSocketInfo.GetSocketItemBoundTradeable() → socketItemTradeable: bool`

- Status: ❔ unverified
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetSocketItemInfo

`C_ItemSocketInfo.GetSocketItemInfo() → name: string?, icon: fileID?, quality: ItemQuality`

- Status: ❔ unverified
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetSocketItemRefundable

`C_ItemSocketInfo.GetSocketItemRefundable() → socketItemRefundable: bool`

- Status: ❔ unverified
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.GetSocketTypes

`C_ItemSocketInfo.GetSocketTypes(index: luaIndex) → socketType: string?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.HasBoundGemProposed

`C_ItemSocketInfo.HasBoundGemProposed() → hasBoundGemProposed: bool`

- Status: ❔ unverified
- Source: client docs `ItemSocketInfoDocumentation.lua`

### C_ItemSocketInfo.IsArtifactRelicItem

`C_ItemSocketInfo.IsArtifactRelicItem(info: ItemInfo) → isArtifactRelicItem: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ItemSocketInfoDocumentation.lua`

## Events

### SOCKET_INFO_ACCEPT

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_BIND_CONFIRM

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_CLOSE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_FAILURE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_REFUNDABLE_CONFIRM

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_SUCCESS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_UI_EVENT_REGISTRATION_UPDATE

- Status: ❔ unverified
- Payload: `uiType: ItemSocketInfoUIType`
- fires synchronously (Blizzard's docs)

### SOCKET_INFO_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### ItemSocketInfoUIType

- Enumeration — ❔ unverified
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
