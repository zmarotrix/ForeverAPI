# ChatInfo

Namespace: `C_ChatInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ChatInfo.AreOutgoingAddonChatMessagesRestricted](#c_chatinfoareoutgoingaddonchatmessagesrestricted) | 1 value | 1 value |
| ✅ | [C_ChatInfo.CanPlayerSpeakLanguage](#c_chatinfocanplayerspeaklanguage) |  |  |
| ✅ | [C_ChatInfo.CancelEmote](#c_chatinfocancelemote) |  |  |
| ✅ | [C_ChatInfo.DropCautionaryChatMessage](#c_chatinfodropcautionarychatmessage) |  |  |
| ✅ | [C_ChatInfo.GetChannelInfoFromIdentifier](#c_chatinfogetchannelinfofromidentifier) |  |  |
| ✅ | [C_ChatInfo.GetChannelRosterInfo](#c_chatinfogetchannelrosterinfo) | 0 values | 0 values |
| ✅ | [C_ChatInfo.GetChannelRuleset](#c_chatinfogetchannelruleset) | 1 value | 1 value |
| ✅ | [C_ChatInfo.GetChannelRulesetForChannelID](#c_chatinfogetchannelrulesetforchannelid) |  |  |
| ✅ | [C_ChatInfo.GetChannelShortcut](#c_chatinfogetchannelshortcut) | 1 value | 1 value |
| ✅ | [C_ChatInfo.GetChannelShortcutForChannelID](#c_chatinfogetchannelshortcutforchannelid) |  |  |
| ✅ | [C_ChatInfo.GetChatLineSenderGUID](#c_chatinfogetchatlinesenderguid) |  |  |
| ✅ | [C_ChatInfo.GetChatLineSenderName](#c_chatinfogetchatlinesendername) |  |  |
| ✅ | [C_ChatInfo.GetChatLineText](#c_chatinfogetchatlinetext) |  |  |
| ✅ | [C_ChatInfo.GetChatTypeName](#c_chatinfogetchattypename) |  |  |
| ✅ | [C_ChatInfo.GetClubStreamIDs](#c_chatinfogetclubstreamids) | 1 value | 1 value |
| ✅ | [C_ChatInfo.GetColorForChatType](#c_chatinfogetcolorforchattype) |  |  |
| ✅ | [C_ChatInfo.GetGeneralChannelID](#c_chatinfogetgeneralchannelid) | 1 value | 1 value |
| ✅ | [C_ChatInfo.GetGeneralChannelLocalID](#c_chatinfogetgeneralchannellocalid) | 1 value | 1 value |
| ✅ | [C_ChatInfo.GetMentorChannelID](#c_chatinfogetmentorchannelid) | 1 value | 1 value |
| ✅ | [C_ChatInfo.GetNumActiveChannels](#c_chatinfogetnumactivechannels) | 1 value | 1 value |
| ✅ | [C_ChatInfo.GetNumReservedChatWindows](#c_chatinfogetnumreservedchatwindows) | 1 value | 1 value |
| ✅ | [C_ChatInfo.GetRegisteredAddonMessagePrefixes](#c_chatinfogetregisteredaddonmessageprefixes) | 1 value | 1 value |
| ✅ | [C_ChatInfo.InChatMessagingLockdown](#c_chatinfoinchatmessaginglockdown) |  |  |
| ✅ | [C_ChatInfo.IsAddonMessagePrefixRegistered](#c_chatinfoisaddonmessageprefixregistered) |  |  |
| ✅ | [C_ChatInfo.IsChannelRegional](#c_chatinfoischannelregional) | 1 value | 1 value |
| ✅ | [C_ChatInfo.IsChannelRegionalForChannelID](#c_chatinfoischannelregionalforchannelid) |  |  |
| ✅ | [C_ChatInfo.IsChatLineCensored](#c_chatinfoischatlinecensored) |  |  |
| ✅ | [C_ChatInfo.IsLoggingChat](#c_chatinfoisloggingchat) | 1 value | 1 value |
| ✅ | [C_ChatInfo.IsLoggingCombat](#c_chatinfoisloggingcombat) | 2 values | 2 values |
| ✅ | [C_ChatInfo.IsPartyChannelType](#c_chatinfoispartychanneltype) | 1 value | 1 value |
| ✅ | [C_ChatInfo.IsRegionalServiceAvailable](#c_chatinfoisregionalserviceavailable) | 1 value | 1 value |
| ✅ | [C_ChatInfo.IsTimerunningPlayer](#c_chatinfoistimerunningplayer) | 1 value | 1 value |
| ✅ | [C_ChatInfo.IsValidChatLine](#c_chatinfoisvalidchatline) | 1 value | 1 value |
| ✅ | [C_ChatInfo.IsValidCombatFilterName](#c_chatinfoisvalidcombatfiltername) |  |  |
| ✅ | [C_ChatInfo.PerformEmote](#c_chatinfoperformemote) |  |  |
| ✅ | [C_ChatInfo.RegisterAddonMessagePrefix](#c_chatinforegisteraddonmessageprefix) |  |  |
| ✅ | [C_ChatInfo.ReplaceIconAndGroupExpressions](#c_chatinforeplaceiconandgroupexpressions) |  |  |
| ✅ | [C_ChatInfo.RequestCanLocalWhisperTarget](#c_chatinforequestcanlocalwhispertarget) |  |  |
| ✅ | [C_ChatInfo.ResetDefaultZoneChannels](#c_chatinforesetdefaultzonechannels) |  |  |
| ✅ | [C_ChatInfo.SendAddonMessage](#c_chatinfosendaddonmessage) |  |  |
| ✅ | [C_ChatInfo.SendAddonMessageLogged](#c_chatinfosendaddonmessagelogged) |  |  |
| ✅ | [C_ChatInfo.SendCautionaryChatMessage](#c_chatinfosendcautionarychatmessage) |  |  |
| ✅ | [C_ChatInfo.SendChatMessage](#c_chatinfosendchatmessage) |  |  |
| ✅ | [C_ChatInfo.SwapChatChannelsByChannelIndex](#c_chatinfoswapchatchannelsbychannelindex) |  |  |
| ✅ | [C_ChatInfo.UncensorChatLine](#c_chatinfouncensorchatline) |  |  |

### C_ChatInfo.AreOutgoingAddonChatMessagesRestricted

`C_ChatInfo.AreOutgoingAddonChatMessagesRestricted() → isRestricted: bool`

- Status: ✅ verified (function)
- Blizzard: Returns false if addons are allowed to send outgoing chat messages. This is controlled on a realm-by-realm basis (tournament realms allow it), and the ability for addons to receive comms is controlled separately.
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.CanPlayerSpeakLanguage

`C_ChatInfo.CanPlayerSpeakLanguage(languageId: number) → canSpeakLanguage: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.CancelEmote

`C_ChatInfo.CancelEmote()`

- Status: ✅ verified (function)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.DropCautionaryChatMessage

`C_ChatInfo.DropCautionaryChatMessage(confirmNumber: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelInfoFromIdentifier

`C_ChatInfo.GetChannelInfoFromIdentifier(channelIdentifier: cstring) → info: ChatChannelInfo?`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelRosterInfo

`C_ChatInfo.GetChannelRosterInfo(channelIndex: luaIndex, rosterIndex: luaIndex) → name: string, owner: bool, moderator: bool, guid: WOWGUID`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1,n:1`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelRuleset

`C_ChatInfo.GetChannelRuleset(channelIndex: luaIndex) → ruleset: ChatChannelRuleset`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelRulesetForChannelID

`C_ChatInfo.GetChannelRulesetForChannelID(channelID: number) → ruleset: ChatChannelRuleset`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelShortcut

`C_ChatInfo.GetChannelShortcut(channelIndex: luaIndex) → shortcut: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelShortcutForChannelID

`C_ChatInfo.GetChannelShortcutForChannelID(channelID: number) → shortcut: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChatLineSenderGUID

`C_ChatInfo.GetChatLineSenderGUID(chatLine: number) → guid: WOWGUID`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret during chat lockdown (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChatLineSenderName

`C_ChatInfo.GetChatLineSenderName(chatLine: number) → name: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret during chat lockdown (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChatLineText

`C_ChatInfo.GetChatLineText(chatLine: number) → text: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret during chat lockdown (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChatTypeName

`C_ChatInfo.GetChatTypeName(typeID: number) → name: string?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetClubStreamIDs

`C_ChatInfo.GetClubStreamIDs(clubID: ClubId) → ids: ClubStreamId[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `club`: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetColorForChatType

`C_ChatInfo.GetColorForChatType(chatType: cstring) → color: colorRGB?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetGeneralChannelID

`C_ChatInfo.GetGeneralChannelID() → channelID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetGeneralChannelLocalID

`C_ChatInfo.GetGeneralChannelLocalID() → localID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetMentorChannelID

`C_ChatInfo.GetMentorChannelID() → channelID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetNumActiveChannels

`C_ChatInfo.GetNumActiveChannels() → numChannels: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetNumReservedChatWindows

`C_ChatInfo.GetNumReservedChatWindows() → numReserved: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetRegisteredAddonMessagePrefixes

`C_ChatInfo.GetRegisteredAddonMessagePrefixes() → registeredPrefixes: cstring[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string}`
- Called in combat: returned 1 value: `table{[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string}`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.InChatMessagingLockdown

`C_ChatInfo.InChatMessagingLockdown() → isRestricted: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if API security restrictions regarding chat messaging are in effect.
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsAddonMessagePrefixRegistered

`C_ChatInfo.IsAddonMessagePrefixRegistered(prefix: cstring) → isRegistered: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsChannelRegional

`C_ChatInfo.IsChannelRegional(channelIndex: luaIndex) → isRegional: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsChannelRegionalForChannelID

`C_ChatInfo.IsChannelRegionalForChannelID(channelID: number) → isRegional: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsChatLineCensored

`C_ChatInfo.IsChatLineCensored(chatLine: number) → isCensored: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsLoggingChat

`C_ChatInfo.IsLoggingChat() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsLoggingCombat

`C_ChatInfo.IsLoggingCombat() → enabled: bool, advanced: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `boolean`
- Called in combat: returned 2 values: `boolean`, `boolean`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsPartyChannelType

`C_ChatInfo.IsPartyChannelType(channelType: ChatChannelType) → isPartyChannelType: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsRegionalServiceAvailable

`C_ChatInfo.IsRegionalServiceAvailable() → available: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsTimerunningPlayer

`C_ChatInfo.IsTimerunningPlayer(playerGUID: WOWGUID) → isTimerunning: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsValidChatLine

`C_ChatInfo.IsValidChatLine(chatLine: number?) → isValid: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsValidCombatFilterName

`C_ChatInfo.IsValidCombatFilterName(name: cstring) → isApproved: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.PerformEmote

`C_ChatInfo.PerformEmote(emoteName: cstring, targetName: cstring?, suppressMoveError: bool = False) → success: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.RegisterAddonMessagePrefix

`C_ChatInfo.RegisterAddonMessagePrefix(prefix: cstring) → result: RegisterAddonMessagePrefixResult`

- Status: ✅ verified (function)
- Blizzard: Registers interest in addon messages with this prefix, cannot be an empty string.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.ReplaceIconAndGroupExpressions

`C_ChatInfo.ReplaceIconAndGroupExpressions(input: string, noIconReplacement: bool?, noGroupReplacement: bool?) → output: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.RequestCanLocalWhisperTarget

`C_ChatInfo.RequestCanLocalWhisperTarget(whisperTarget: WOWGUID)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.ResetDefaultZoneChannels

`C_ChatInfo.ResetDefaultZoneChannels()`

- Status: ✅ verified (function)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.SendAddonMessage

`C_ChatInfo.SendAddonMessage(prefix: cstring, message: cstring, chatType: cstring?, target: cstring?) → result: SendAddonMessageResult`

- Status: ✅ verified (function)
- Blizzard: Sends a text payload to other clients specified by chatChannel and target which are registered to listen for prefix.
- `chatType`: ChatType, defaults to SLASH_CMD_PARTY.
- `target`: Only applies for targeted channels
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.SendAddonMessageLogged

`C_ChatInfo.SendAddonMessageLogged(prefix: cstring, message: cstring, chatType: cstring?, target: cstring?) → result: SendAddonMessageResult?`

- Status: ✅ verified (function)
- Blizzard: Sends a text payload to other clients specified by chatChannel and target which are registered to listen for prefix. Intended for plain text payloads; logged and throttled.
- `chatType`: ChatType, defaults to SLASH_CMD_PARTY.
- `target`: Only applies for targeted channels
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.SendCautionaryChatMessage

`C_ChatInfo.SendCautionaryChatMessage(confirmNumber: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.SendChatMessage

`C_ChatInfo.SendChatMessage(message: cstring, chatType: SendChatMessageType?, languageID: number?, target: cstring?)`

- Status: ✅ verified (function)
- `chatType`: Chat type string ('SAY', 'EMOTE', etc.). Defaults to 'SAY' if not specified.
- `languageID`: Language to send the message in.
- `target`: Name of the player to send a message to. Only applies to chat types that support targeted messages.
- restricted in some situations (Blizzard's docs; not checked in game)
- RestrictedForMacroChatMessages (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.SwapChatChannelsByChannelIndex

`C_ChatInfo.SwapChatChannelsByChannelIndex(firstChannelIndex: luaIndex, secondChannelIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.UncensorChatLine

`C_ChatInfo.UncensorChatLine(chatLine: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

## Events

### ALTERNATIVE_DEFAULT_LANGUAGE_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### BN_CHAT_MSG_ADDON

- Status: ✅ verified
- Payload: `prefix: cstring`, `text: cstring`, `channel: cstring`, `senderID: number`
- fires synchronously (Blizzard's docs)
- Seen firing 525 times (57 in combat); argument kinds: `s,s,s,n`

### CAN_LOCAL_WHISPER_TARGET_RESPONSE

- Status: ✅ verified
- Payload: `whisperTarget: WOWGUID`, `status: ChatWhisperTargetStatus`
- unique event (Blizzard's docs)

### CAN_PLAYER_SPEAK_LANGUAGE_CHANGED

- Status: ✅ verified
- Payload: `languageId: number`, `canSpeakLanguage: bool`
- unique event (Blizzard's docs)

### CAUTIONARY_CHANNEL_MESSAGE

- Status: ✅ verified
- Payload: `confirmNumber: number`
- fires synchronously (Blizzard's docs)

### CAUTIONARY_CHAT_MESSAGE

- Status: ✅ verified
- Payload: `chatLineID: number`, `confirmNumber: number`
- fires synchronously (Blizzard's docs)

### CHANNEL_COUNT_UPDATE

- Status: ✅ verified
- Payload: `displayIndex: number`, `count: number`
- fires synchronously (Blizzard's docs)

### CHANNEL_FLAGS_UPDATED

- Status: ✅ verified
- Payload: `displayIndex: number`
- fires synchronously (Blizzard's docs)

### CHANNEL_INVITE_REQUEST

- Status: ✅ verified
- Payload: `channelID: cstring`, `name: cstring`
- fires synchronously (Blizzard's docs)

### CHANNEL_LEFT

- Status: ✅ verified
- Payload: `chatChannelID: number`, `name: cstring`
- fires synchronously (Blizzard's docs)
- Seen firing 32 times (0 in combat); argument kinds: `n,s`

### CHANNEL_PASSWORD_REQUEST

- Status: ✅ verified
- Payload: `channelID: cstring`
- fires synchronously (Blizzard's docs)

### CHANNEL_ROSTER_UPDATE

- Status: ✅ verified
- Payload: `displayIndex: number`, `count: number`
- fires synchronously (Blizzard's docs)

### CHANNEL_UI_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 261 times (4 in combat); argument kinds: ``

### CHAT_COMBAT_MSG_ARENA_POINTS_GAIN

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_LOGGING_CHANGED

- Status: ✅ verified
- Payload: `whichLog: number`, `isEnabled: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 21 times (0 in combat); argument kinds: `n,b`

### CHAT_MSG_ACHIEVEMENT

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_ADDON

- Status: ✅ verified
- Payload: `prefix: cstring`, `text: cstring`, `channel: cstring`, `sender: cstring`, `target: cstring`, `zoneChannelID: number`, `localID: number`, `name: cstring`, `instanceID: number`
- fires synchronously (Blizzard's docs)
- Seen firing 2718 times (532 in combat); argument kinds: `s,s,s,s,s,n,n,s,n`

### CHAT_MSG_ADDON_LOGGED

- Status: ✅ verified
- Payload: `prefix: cstring`, `text: cstring`, `channel: cstring`, `sender: cstring`, `target: cstring`, `zoneChannelID: number`, `localID: number`, `name: cstring`, `instanceID: number`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_AFK

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BG_SYSTEM_ALLIANCE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BG_SYSTEM_HORDE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BG_SYSTEM_NEUTRAL

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_BN

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_INLINE_TOAST_ALERT

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 23 times (4 in combat); argument kinds: `S,S,s,s,S,s,n,n,s,n,n,-,S,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_BN_INLINE_TOAST_BROADCAST

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_INLINE_TOAST_BROADCAST_INFORM

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_INLINE_TOAST_CONVERSATION

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_WHISPER

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_BN_WHISPER_INFORM

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_WHISPER_PLAYER_OFFLINE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 430 times (1 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_MSG_CHANNEL_JOIN

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL_LEAVE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL_LEAVE_PREVENTED

- Status: ✅ verified
- Payload: `channelName: cstring`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL_LIST

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL_NOTICE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 225 times (2 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_CHANNEL_NOTICE_USER

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_COLLECTED_APPEARANCE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 37 times (6 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_COMBAT_FACTION_CHANGE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 223 times (212 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_COMBAT_HONOR_GAIN

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (1 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_COMBAT_MISC_INFO

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 3 times (2 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_COMBAT_XP_GAIN

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 515 times (488 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_COMMUNITIES_CHANNEL

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CURRENCY

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 7 times (1 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_DND

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_EMOTE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_FILTERED

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_GUILD

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 169 times (28 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_MSG_GUILD_ACHIEVEMENT

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_GUILD_DISCORD

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_GUILD_ITEM_LOOTED

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_IGNORED

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_INSTANCE_CHAT

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_INSTANCE_CHAT_LEADER

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_LOOT

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 1360 times (351 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_MSG_MONEY

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 315 times (107 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_MONSTER_EMOTE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 161 times (156 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_MONSTER_PARTY

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_MONSTER_SAY

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 12 times (0 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_MONSTER_WHISPER

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_MONSTER_YELL

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 46 times (23 in combat); argument kinds: `S,S,s,s,S,s,n,n,s,n,n,-,S,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_OFFICER

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 43 times (9 in combat); argument kinds: `S,S,s,s,S,s,n,n,s,n,n,S,S,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_MSG_OPENING

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 4 times (0 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_PARTY

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 530 times (102 in combat); argument kinds: `S,S,s,s,S,s,n,n,s,n,n,S,S,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_MSG_PARTY_LEADER

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 45 times (9 in combat); argument kinds: `S,S,s,s,S,s,n,n,s,n,n,S,S,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_MSG_PET_BATTLE_COMBAT_LOG

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_PET_BATTLE_INFO

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_PET_INFO

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)
- Seen firing 7 times (0 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_PING

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 27 times (9 in combat); argument kinds: `S,S,s,s,S,s,n,n,s,n,n,-,S,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_RAID

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RAID_BOSS_EMOTE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RAID_BOSS_WHISPER

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RAID_LEADER

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RAID_WARNING

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RESTRICTED

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_SAY

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 18 times (2 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_MSG_SKILL

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 35 times (32 in combat); argument kinds: `S,S,s,s,S,s,n,n,s,n,n,-,S,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_SYSTEM

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 328 times (27 in combat); argument kinds: `S,S,s,s,S,s,n,n,s,n,n,-,S,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_TARGETICONS

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 18 times (9 in combat); argument kinds: `S,S,s,s,S,s,n,n,s,n,n,-,S,b,b,b,b,t` / `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_TEXT_EMOTE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 20 times (4 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_MSG_TRADESKILLS

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 2310 times (9 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t`

### CHAT_MSG_VOICE_TEXT

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_WHISPER

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 16 times (3 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_MSG_WHISPER_INFORM

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 6 times (1 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_MSG_YELL

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t`

### CHAT_REGIONAL_SEND_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHAT_REGIONAL_STATUS_CHANGED

- Status: ✅ verified
- Payload: `isServiceAvailable: bool`
- fires synchronously (Blizzard's docs)

### CHAT_SERVER_DISCONNECTED

- Status: ✅ verified
- Payload: `isInitialMessage: bool?`
- fires synchronously (Blizzard's docs)

### CHAT_SERVER_RECONNECTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CLEAR_BOSS_EMOTES

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### DAILY_RESET_INSTANCE_WELCOME

- Status: ✅ verified
- Payload: `mapname: cstring`, `timeLeft: number`
- fires synchronously (Blizzard's docs)

### INSTANCE_RESET_WARNING

- Status: ✅ verified
- Payload: `warningMessage: cstring`, `timeLeft: number`
- fires synchronously (Blizzard's docs)

### LANGUAGE_LIST_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### NOTIFY_CHAT_SUPPRESSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### QUEST_BOSS_EMOTE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `displayTime: number`, `enableBossEmoteWarningSound: bool`
- fires synchronously (Blizzard's docs)

### RAID_BOSS_EMOTE

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `displayTime: number`, `enableBossEmoteWarningSound: bool`
- fires synchronously (Blizzard's docs)

### RAID_BOSS_WHISPER

- Status: ✅ verified
- Payload: `text: cstring`, `playerName: cstring`, `displayTime: number`, `enableBossEmoteWarningSound: bool`
- fires synchronously (Blizzard's docs)

### RAID_INSTANCE_WELCOME

- Status: ✅ verified
- Payload: `mapname: cstring`, `timeLeft: number`, `locked: number`, `extended: number`
- fires synchronously (Blizzard's docs)

### UPDATE_CHAT_COLOR

- Status: ✅ verified
- Payload: `name: cstring`, `r: number`, `g: number`, `b: number`
- fires synchronously (Blizzard's docs)
- Seen firing 3384 times (0 in combat); argument kinds: `s,n,n,n`

### UPDATE_CHAT_COLOR_NAME_BY_CLASS

- Status: ✅ verified
- Payload: `name: cstring`, `colorNameByClass: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 3384 times (0 in combat); argument kinds: `s,b`

### UPDATE_CHAT_WINDOWS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 108 times (0 in combat); argument kinds: ``

### UPDATE_FLOATING_CHAT_WINDOWS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 72 times (0 in combat); argument kinds: ``

## Types

### ChatMessageEventParams

- Structure
  - `text`: cstring
  - `playerName`: cstring
  - `languageName`: cstring
  - `channelName`: cstring
  - `playerName2`: cstring
  - `specialFlags`: cstring
  - `zoneChannelID`: number
  - `channelIndex`: number
  - `channelBaseName`: cstring
  - `languageID`: number
  - `lineID`: number
  - `guid`: WOWGUID
  - `bnSenderID`: number
  - `isMobile`: bool
  - `isSubtitle`: bool
  - `hideSenderInLetterbox`: bool
  - `suppressRaidIcons`: bool
  - `discordInfo`: DiscordChatInfo

### SendChatMessageParams

- Structure
  - `message`: cstring
  - `chatType`: SendChatMessageType?
  - `languageID`: number?
  - `target`: cstring?
