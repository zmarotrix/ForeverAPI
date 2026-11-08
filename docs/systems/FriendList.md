# FriendList

Namespace: `C_FriendList`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_FriendList.AddFriend](#c_friendlistaddfriend) |  |  |
| ✅ | [C_FriendList.AddIgnore](#c_friendlistaddignore) |  |  |
| ✅ | [C_FriendList.AddOrDelIgnore](#c_friendlistaddordelignore) |  |  |
| ✅ | [C_FriendList.AddOrRemoveFriend](#c_friendlistaddorremovefriend) |  |  |
| ✅ | [C_FriendList.DelIgnore](#c_friendlistdelignore) |  |  |
| ✅ | [C_FriendList.DelIgnoreByIndex](#c_friendlistdelignorebyindex) |  |  |
| ✅ | [C_FriendList.GetFriendInfo](#c_friendlistgetfriendinfo) |  |  |
| ✅ | [C_FriendList.GetFriendInfoByIndex](#c_friendlistgetfriendinfobyindex) | 0 values | 0 values |
| ✅ | [C_FriendList.GetIgnoreName](#c_friendlistgetignorename) | 1 value | 1 value |
| ✅ | [C_FriendList.GetNumFriends](#c_friendlistgetnumfriends) | 1 value | 1 value |
| ✅ | [C_FriendList.GetNumIgnores](#c_friendlistgetnumignores) | 1 value | 1 value |
| ✅ | [C_FriendList.GetNumOnlineFriends](#c_friendlistgetnumonlinefriends) | 1 value | 1 value |
| ✅ | [C_FriendList.GetNumWhoResults](#c_friendlistgetnumwhoresults) | 2 values | 2 values |
| ✅ | [C_FriendList.GetSelectedFriend](#c_friendlistgetselectedfriend) | 1 value | 1 value |
| ✅ | [C_FriendList.GetSelectedIgnore](#c_friendlistgetselectedignore) | 1 value | 1 value |
| ✅ | [C_FriendList.GetWhoInfo](#c_friendlistgetwhoinfo) | 0 values | 0 values |
| ✅ | [C_FriendList.GetWhoRaceFilters](#c_friendlistgetwhoracefilters) | 1 value | 1 value |
| ✅ | [C_FriendList.IsFriend](#c_friendlistisfriend) | 1 value | 1 value |
| ✅ | [C_FriendList.IsIgnored](#c_friendlistisignored) |  |  |
| ✅ | [C_FriendList.IsIgnoredByGuid](#c_friendlistisignoredbyguid) | 1 value | 1 value |
| ✅ | [C_FriendList.IsLegacyFriendSystemEnabled](#c_friendlistislegacyfriendsystemenabled) | 1 value | 1 value |
| ✅ | [C_FriendList.IsOnIgnoredList](#c_friendlistisonignoredlist) |  |  |
| ✅ | [C_FriendList.RemoveFriend](#c_friendlistremovefriend) |  |  |
| ✅ | [C_FriendList.RemoveFriendByIndex](#c_friendlistremovefriendbyindex) |  |  |
| ✅ | [C_FriendList.SendWho](#c_friendlistsendwho) |  |  |
| ✅ | [C_FriendList.SetFriendNotes](#c_friendlistsetfriendnotes) |  |  |
| ✅ | [C_FriendList.SetFriendNotesByIndex](#c_friendlistsetfriendnotesbyindex) |  |  |
| ✅ | [C_FriendList.SetSelectedFriend](#c_friendlistsetselectedfriend) |  |  |
| ✅ | [C_FriendList.SetSelectedIgnore](#c_friendlistsetselectedignore) |  |  |
| ✅ | [C_FriendList.SetWhoToUi](#c_friendlistsetwhotoui) |  |  |
| ✅ | [C_FriendList.ShowFriends](#c_friendlistshowfriends) |  |  |
| ✅ | [C_FriendList.SortWho](#c_friendlistsortwho) |  |  |

### C_FriendList.AddFriend

`C_FriendList.AddFriend(name: cstring, notes: cstring?)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.AddIgnore

`C_FriendList.AddIgnore(name: cstring) → added: bool`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.AddOrDelIgnore

`C_FriendList.AddOrDelIgnore(name: cstring)`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.AddOrRemoveFriend

`C_FriendList.AddOrRemoveFriend(name: cstring, notes: cstring)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.DelIgnore

`C_FriendList.DelIgnore(name: cstring) → removed: bool`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.DelIgnoreByIndex

`C_FriendList.DelIgnoreByIndex(index: luaIndex)`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetFriendInfo

`C_FriendList.GetFriendInfo(name: cstring) → info: FriendInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetFriendInfoByIndex

`C_FriendList.GetFriendInfoByIndex(index: luaIndex) → info: FriendInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetIgnoreName

`C_FriendList.GetIgnoreName(index: luaIndex) → name: string?`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetNumFriends

`C_FriendList.GetNumFriends() → numFriends: number`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetNumIgnores

`C_FriendList.GetNumIgnores() → numIgnores: number`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetNumOnlineFriends

`C_FriendList.GetNumOnlineFriends() → numOnline: number`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetNumWhoResults

`C_FriendList.GetNumWhoResults() → numWhos: number, totalNumWhos: number`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetSelectedFriend

`C_FriendList.GetSelectedFriend() → index: luaIndex?`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetSelectedIgnore

`C_FriendList.GetSelectedIgnore() → index: luaIndex?`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetWhoInfo

`C_FriendList.GetWhoInfo(index: luaIndex) → info: WhoInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.GetWhoRaceFilters

`C_FriendList.GetWhoRaceFilters() → filters: WhoFilter[]`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table}`
- Called in combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table}`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.IsFriend

`C_FriendList.IsFriend(guid: WOWGUID) → isFriend: bool`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.IsIgnored

`C_FriendList.IsIgnored(token: cstring) → isIgnored: bool`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.IsIgnoredByGuid

`C_FriendList.IsIgnoredByGuid(guid: WOWGUID) → isIgnored: bool`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.IsLegacyFriendSystemEnabled

`C_FriendList.IsLegacyFriendSystemEnabled() → isLegacyFriendSystemEnabled: bool`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.IsOnIgnoredList

`C_FriendList.IsOnIgnoredList(token: cstring) → isIgnored: bool`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.RemoveFriend

`C_FriendList.RemoveFriend(name: cstring) → removed: bool`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.RemoveFriendByIndex

`C_FriendList.RemoveFriendByIndex(index: luaIndex)`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.SendWho

`C_FriendList.SendWho(filter: cstring, origin: number?, filters: SendWhoFilters?)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.SetFriendNotes

`C_FriendList.SetFriendNotes(name: cstring, notes: cstring) → found: bool`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.SetFriendNotesByIndex

`C_FriendList.SetFriendNotesByIndex(index: luaIndex, notes: cstring)`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.SetSelectedFriend

`C_FriendList.SetSelectedFriend(index: luaIndex)`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.SetSelectedIgnore

`C_FriendList.SetSelectedIgnore(index: luaIndex)`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.SetWhoToUi

`C_FriendList.SetWhoToUi(whoToUi: bool)`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.ShowFriends

`C_FriendList.ShowFriends()`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

### C_FriendList.SortWho

`C_FriendList.SortWho(sorting: cstring, ascending: bool?)`

- Status: ✅ verified (function)
- RequiresFriendList (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FriendListDocumentation.lua`

## Events

### BATTLE_NET_FRIEND_TAG_ENABLED_STATUS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BATTLE_NET_TITLE_FRIEND_CUSTOM_NAME_ENABLED_STATUS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BN_BLOCK_FAILED_TOO_MANY

- Status: ✅ verified
- Payload: `blockType: cstring`
- fires synchronously (Blizzard's docs)

### BN_BLOCK_LIST_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BN_CHAT_WHISPER_UNDELIVERABLE

- Status: ✅ verified
- Payload: `senderID: number`
- fires synchronously (Blizzard's docs)

### BN_CONNECTED

- Status: ✅ verified
- Payload: `suppressNotification: bool`
- fires synchronously (Blizzard's docs)

### BN_CUSTOM_MESSAGE_CHANGED

- Status: ✅ verified
- Payload: `id: number?`
- fires synchronously (Blizzard's docs)

### BN_CUSTOM_MESSAGE_LOADED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 3 times (0 in combat); argument kinds: ``

### BN_DISCONNECTED

- Status: ✅ verified
- Payload: `result: bool`, `suppressNotification: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `b,b`

### BN_FRIEND_ACCOUNT_OFFLINE

- Status: ✅ verified
- Payload: `friendId: number`, `isCompanionApp: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 13 times (2 in combat); argument kinds: `n,b`

### BN_FRIEND_ACCOUNT_ONLINE

- Status: ✅ verified
- Payload: `friendId: number`, `isCompanionApp: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 10 times (2 in combat); argument kinds: `n,b`

### BN_FRIEND_INFO_CHANGED

- Status: ✅ verified
- Payload: `friendIndex: luaIndex?`
- fires synchronously (Blizzard's docs)
- Seen firing 8249 times (949 in combat); argument kinds: `-` / `n`

### BN_FRIEND_INVITE_ADDED

- Status: ✅ verified
- Payload: `accountID: number`
- fires synchronously (Blizzard's docs)

### BN_FRIEND_INVITE_LIST_INITIALIZED

- Status: ✅ verified
- Payload: `listSize: number`
- fires synchronously (Blizzard's docs)

### BN_FRIEND_INVITE_REMOVED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BN_FRIEND_LIST_SIZE_CHANGED

- Status: ✅ verified
- Payload: `accountID: number?`
- fires synchronously (Blizzard's docs)

### BN_INFO_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 365 times (19 in combat); argument kinds: ``

### BN_REQUEST_FOF_SUCCEEDED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CONFIRM_BATTLE_NET_FRIEND_INVITE_SHOW

- Status: ✅ verified
- Payload: `name: cstring`, `friendLevel: BattleNetFriendLevel`
- fires synchronously (Blizzard's docs)

### FRIENDLIST_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### IGNORELIST_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LEGACY_FRIEND_SYSTEM_STATUS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### MUTELIST_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### NEW_MATCHMAKING_PARTY_INVITE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### REJECTED_MATCHMAKING_PARTY_INVITE

- Status: ✅ verified
- Payload: `name: cstring`
- fires synchronously (Blizzard's docs)

### SOCIAL_UI_FRIENDS_LIST_SYSTEM_STATUS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### WHO_LIST_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### FriendInfo

- Structure
  - `connected`: bool
  - `name`: string
  - `className`: string?
  - `area`: string?
  - `notes`: string?
  - `guid`: WOWGUID
  - `level`: number
  - `dnd`: bool
  - `afk`: bool
  - `rafLinkType`: RafLinkType

### SendWhoFilters

- Structure
  - `classIDs`: number[]
  - `raceIDs`: number[]
  - `uiMapIDs`: number[]

### WhoFilter

- Structure
  - `name`: string
  - `ID`: number

### WhoInfo

- Structure
  - `fullName`: string
  - `fullGuildName`: string
  - `level`: number
  - `raceStr`: string
  - `classStr`: string
  - `area`: string
  - `filename`: string?
  - `gender`: number
  - `timerunningSeasonID`: number?
