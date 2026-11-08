# ConnectionScript

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [CancelLogout](#cancellogout) | 💥 blocked | 💥 blocked |
| ✅ | [ForceLogout](#forcelogout) |  |  |
| ✅ | [ForceQuit](#forcequit) |  |  |
| ✅ | [GetNativeRealmID](#getnativerealmid) | 1 value | 1 value |
| ✅ | [GetNetIpTypes](#getnetiptypes) | 2 values | 2 values |
| ✅ | [GetNetStats](#getnetstats) | 4 values | 4 values |
| ✅ | [GetProtocolTypes](#getprotocoltypes) | 2 values | 2 values |
| ✅ | [GetRealmID](#getrealmid) | 1 value | 1 value |
| ✅ | [GetRealmName](#getrealmname) | 1 value | 1 value |
| ✅ | [IsOnTournamentRealm](#isontournamentrealm) | 1 value | 1 value |
| ✅ | [Logout](#logout) |  |  |
| ✅ | [Quit](#quit) |  |  |
| ✅ | [SelectedRealmName](#selectedrealmname) |  |  |

### CancelLogout

`CancelLogout()`

- Status: ✅ verified (function)
- Called out of combat: 💥 not called: blocked
- Called in combat: 💥 not called: blocked
- Source: client docs `ConnectionDocumentation.lua`

### ForceLogout

`ForceLogout()`

- Status: ✅ verified (function)
- Source: client docs `ConnectionDocumentation.lua`

### ForceQuit

`ForceQuit()`

- Status: ✅ verified (function)
- Source: client docs `ConnectionDocumentation.lua`

### GetNativeRealmID

`GetNativeRealmID() → nativeRealmID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ConnectionDocumentation.lua`

### GetNetIpTypes

`GetNetIpTypes() → ipTypes: ConnectionIptype`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `ConnectionDocumentation.lua`

### GetNetStats

`GetNetStats() → in: number, out: number, latencyList: number`

- Status: ✅ verified (function)
- Called out of combat: returned 4 values: `number`, `number`, `number`, `number`
- Called in combat: returned 4 values: `number`, `number`, `number`, `number`
- Source: client docs `ConnectionDocumentation.lua`

### GetProtocolTypes

`GetProtocolTypes() → protocolTypes: ConnectionProtocol`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `ConnectionDocumentation.lua`

### GetRealmID

`GetRealmID() → realmID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ConnectionDocumentation.lua`

### GetRealmName

`GetRealmName() → realmName: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `ConnectionDocumentation.lua`

### IsOnTournamentRealm

`IsOnTournamentRealm() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ConnectionDocumentation.lua`

### Logout

`Logout()`

- Status: ✅ verified (function)
- Source: client docs `ConnectionDocumentation.lua`

### Quit

`Quit()`

- Status: ✅ verified (function)
- Source: client docs `ConnectionDocumentation.lua`

### SelectedRealmName

`SelectedRealmName() → selectedRealmName: cstring`

- Status: ✅ verified (function)
- Source: client docs `ConnectionDocumentation.lua`
