# Discord

Namespace: `C_Discord`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Discord.Authorize](#c_discordauthorize) |  |  |
| ✅ | [C_Discord.GetDiscordChannelName](#c_discordgetdiscordchannelname) |  |  |
| ✅ | [C_Discord.GetDiscordUserID](#c_discordgetdiscorduserid) | 💥 forbidden | 💥 forbidden |
| ✅ | [C_Discord.GetDiscordUserName](#c_discordgetdiscordusername) |  |  |
| ✅ | [C_Discord.GetDisplayNameType](#c_discordgetdisplaynametype) | 💥 forbidden | 💥 forbidden |
| ✅ | [C_Discord.GetGuildLinkStatus](#c_discordgetguildlinkstatus) | 💥 forbidden | 💥 forbidden |
| ✅ | [C_Discord.GetNumDiscordChannels](#c_discordgetnumdiscordchannels) |  |  |
| ✅ | [C_Discord.GetNumDiscordServers](#c_discordgetnumdiscordservers) | 💥 forbidden | 💥 forbidden |
| ✅ | [C_Discord.GetServerLinkableChannels](#c_discordgetserverlinkablechannels) |  |  |
| ✅ | [C_Discord.GetServerName](#c_discordgetservername) |  |  |
| ✅ | [C_Discord.GuildLink](#c_discordguildlink) |  |  |
| ✅ | [C_Discord.GuildUnlink](#c_discordguildunlink) |  |  |
| ✅ | [C_Discord.IsEnabled](#c_discordisenabled) | 1 value | 1 value |
| ✅ | [C_Discord.IsGuildChannelLinked](#c_discordisguildchannellinked) | 💥 forbidden | 💥 forbidden |
| ✅ | [C_Discord.IsGuildSettingSet](#c_discordisguildsettingset) |  |  |
| ✅ | [C_Discord.IsUserOAuthed](#c_discordisuseroauthed) | 💥 forbidden | 💥 forbidden |
| ✅ | [C_Discord.IsVoiceEnabled](#c_discordisvoiceenabled) | 1 value | 1 value |
| ✅ | [C_Discord.RefreshAuth](#c_discordrefreshauth) |  |  |
| ✅ | [C_Discord.SetGuildSetting](#c_discordsetguildsetting) |  |  |
| ✅ | [C_Discord.UpdateDiscordServers](#c_discordupdatediscordservers) |  |  |
| ✅ | [C_Discord.UpdateGuildLobby](#c_discordupdateguildlobby) |  |  |

### C_Discord.Authorize

`C_Discord.Authorize()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GetDiscordChannelName

`C_Discord.GetDiscordChannelName(serverIndex: luaIndex, channelIndex: luaIndex) → name: string`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GetDiscordUserID

`C_Discord.GetDiscordUserID() → userID: DiscordMemberOpaqueID`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Called out of combat: not called: forbidden
- Called in combat: not called: forbidden
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GetDiscordUserName

`C_Discord.GetDiscordUserName(userID: DiscordMemberOpaqueID) → userName: KStringDiscordUserName`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GetDisplayNameType

`C_Discord.GetDisplayNameType() → type: DiscordDisplayNameType`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Called out of combat: not called: forbidden
- Called in combat: not called: forbidden
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GetGuildLinkStatus

`C_Discord.GetGuildLinkStatus() → isFullyLinked: bool, linkedChannelName: string, linkedServerName: string`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Called out of combat: not called: forbidden
- Called in combat: not called: forbidden
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GetNumDiscordChannels

`C_Discord.GetNumDiscordChannels(serverIndex: luaIndex) → count: number, valid: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GetNumDiscordServers

`C_Discord.GetNumDiscordServers() → count: number`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Called out of combat: not called: forbidden
- Called in combat: not called: forbidden
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GetServerLinkableChannels

`C_Discord.GetServerLinkableChannels(index: luaIndex)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GetServerName

`C_Discord.GetServerName(index: luaIndex) → name: string`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GuildLink

`C_Discord.GuildLink(serverIndex: luaIndex, channelIndex: luaIndex)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.GuildUnlink

`C_Discord.GuildUnlink()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.IsEnabled

`C_Discord.IsEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.IsGuildChannelLinked

`C_Discord.IsGuildChannelLinked() → isLinked: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Called out of combat: not called: forbidden
- Called in combat: not called: forbidden
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.IsGuildSettingSet

`C_Discord.IsGuildSettingSet(setting: DiscordGuildSettings) → isSet: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.IsUserOAuthed

`C_Discord.IsUserOAuthed() → hasOAuth: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Called out of combat: not called: forbidden
- Called in combat: not called: forbidden
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.IsVoiceEnabled

`C_Discord.IsVoiceEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.RefreshAuth

`C_Discord.RefreshAuth()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.SetGuildSetting

`C_Discord.SetGuildSetting(setting: DiscordGuildSettings, set: bool)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.UpdateDiscordServers

`C_Discord.UpdateDiscordServers()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

### C_Discord.UpdateGuildLobby

`C_Discord.UpdateGuildLobby()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `DiscordDocumentation.lua`

## Events

### DISCORD_GUILD_ACHIEVEMENT

- Status: ✅ verified
- Payload: `achievementID: number`
- fires synchronously (Blizzard's docs)

### DISCORD_GUILD_LOBBY_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### DISCORD_GUILD_SETTINGS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### DISCORD_LINK_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### DISCORD_SERVER_LIST_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### DISCORD_STATUS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
