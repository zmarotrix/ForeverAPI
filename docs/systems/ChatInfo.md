# ChatInfo

Namespace: `C_ChatInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ChatInfo.AreOutgoingAddonChatMessagesRestricted](#c_chatinfoareoutgoingaddonchatmessagesrestricted) |  |  |
| ❔ | [C_ChatInfo.CanPlayerSpeakLanguage](#c_chatinfocanplayerspeaklanguage) |  |  |
| ❔ | [C_ChatInfo.CancelEmote](#c_chatinfocancelemote) |  |  |
| ❔ | [C_ChatInfo.DropCautionaryChatMessage](#c_chatinfodropcautionarychatmessage) |  |  |
| ❔ | [C_ChatInfo.GetChannelInfoFromIdentifier](#c_chatinfogetchannelinfofromidentifier) |  |  |
| ❔ | [C_ChatInfo.GetChannelRosterInfo](#c_chatinfogetchannelrosterinfo) |  |  |
| ❔ | [C_ChatInfo.GetChannelRuleset](#c_chatinfogetchannelruleset) |  |  |
| ❔ | [C_ChatInfo.GetChannelRulesetForChannelID](#c_chatinfogetchannelrulesetforchannelid) |  |  |
| ❔ | [C_ChatInfo.GetChannelShortcut](#c_chatinfogetchannelshortcut) |  |  |
| ❔ | [C_ChatInfo.GetChannelShortcutForChannelID](#c_chatinfogetchannelshortcutforchannelid) |  |  |
| ❔ | [C_ChatInfo.GetChatLineSenderGUID](#c_chatinfogetchatlinesenderguid) |  |  |
| ❔ | [C_ChatInfo.GetChatLineSenderName](#c_chatinfogetchatlinesendername) |  |  |
| ❔ | [C_ChatInfo.GetChatLineText](#c_chatinfogetchatlinetext) |  |  |
| ❔ | [C_ChatInfo.GetChatTypeName](#c_chatinfogetchattypename) |  |  |
| ❔ | [C_ChatInfo.GetClubStreamIDs](#c_chatinfogetclubstreamids) |  |  |
| ❔ | [C_ChatInfo.GetColorForChatType](#c_chatinfogetcolorforchattype) |  |  |
| ❔ | [C_ChatInfo.GetGeneralChannelID](#c_chatinfogetgeneralchannelid) |  |  |
| ❔ | [C_ChatInfo.GetGeneralChannelLocalID](#c_chatinfogetgeneralchannellocalid) |  |  |
| ❔ | [C_ChatInfo.GetMentorChannelID](#c_chatinfogetmentorchannelid) |  |  |
| ❔ | [C_ChatInfo.GetNumActiveChannels](#c_chatinfogetnumactivechannels) |  |  |
| ❔ | [C_ChatInfo.GetNumReservedChatWindows](#c_chatinfogetnumreservedchatwindows) |  |  |
| ❔ | [C_ChatInfo.GetRegisteredAddonMessagePrefixes](#c_chatinfogetregisteredaddonmessageprefixes) |  |  |
| ❔ | [C_ChatInfo.InChatMessagingLockdown](#c_chatinfoinchatmessaginglockdown) |  |  |
| ❔ | [C_ChatInfo.IsAddonMessagePrefixRegistered](#c_chatinfoisaddonmessageprefixregistered) |  |  |
| ❔ | [C_ChatInfo.IsChannelRegional](#c_chatinfoischannelregional) |  |  |
| ❔ | [C_ChatInfo.IsChannelRegionalForChannelID](#c_chatinfoischannelregionalforchannelid) |  |  |
| ❔ | [C_ChatInfo.IsChatLineCensored](#c_chatinfoischatlinecensored) |  |  |
| ❔ | [C_ChatInfo.IsLoggingChat](#c_chatinfoisloggingchat) |  |  |
| ❔ | [C_ChatInfo.IsLoggingCombat](#c_chatinfoisloggingcombat) |  |  |
| ❔ | [C_ChatInfo.IsPartyChannelType](#c_chatinfoispartychanneltype) |  |  |
| ❔ | [C_ChatInfo.IsRegionalServiceAvailable](#c_chatinfoisregionalserviceavailable) |  |  |
| ❔ | [C_ChatInfo.IsTimerunningPlayer](#c_chatinfoistimerunningplayer) |  |  |
| ❔ | [C_ChatInfo.IsValidChatLine](#c_chatinfoisvalidchatline) |  |  |
| ❔ | [C_ChatInfo.IsValidCombatFilterName](#c_chatinfoisvalidcombatfiltername) |  |  |
| ❔ | [C_ChatInfo.PerformEmote](#c_chatinfoperformemote) |  |  |
| ❔ | [C_ChatInfo.RegisterAddonMessagePrefix](#c_chatinforegisteraddonmessageprefix) |  |  |
| ❔ | [C_ChatInfo.ReplaceIconAndGroupExpressions](#c_chatinforeplaceiconandgroupexpressions) |  |  |
| ❔ | [C_ChatInfo.RequestCanLocalWhisperTarget](#c_chatinforequestcanlocalwhispertarget) |  |  |
| ❔ | [C_ChatInfo.ResetDefaultZoneChannels](#c_chatinforesetdefaultzonechannels) |  |  |
| ❔ | [C_ChatInfo.SendAddonMessage](#c_chatinfosendaddonmessage) |  |  |
| ❔ | [C_ChatInfo.SendAddonMessageLogged](#c_chatinfosendaddonmessagelogged) |  |  |
| ❔ | [C_ChatInfo.SendCautionaryChatMessage](#c_chatinfosendcautionarychatmessage) |  |  |
| ❔ | [C_ChatInfo.SendChatMessage](#c_chatinfosendchatmessage) |  |  |
| ❔ | [C_ChatInfo.SwapChatChannelsByChannelIndex](#c_chatinfoswapchatchannelsbychannelindex) |  |  |
| ❔ | [C_ChatInfo.UncensorChatLine](#c_chatinfouncensorchatline) |  |  |

### C_ChatInfo.AreOutgoingAddonChatMessagesRestricted

`C_ChatInfo.AreOutgoingAddonChatMessagesRestricted() → isRestricted: bool`

- Status: ❔ unverified
- Blizzard: Returns false if addons are allowed to send outgoing chat messages. This is controlled on a realm-by-realm basis (tournament realms allow it), and the ability for addons to receive comms is controlled separately.
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.CanPlayerSpeakLanguage

`C_ChatInfo.CanPlayerSpeakLanguage(languageId: number) → canSpeakLanguage: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.CancelEmote

`C_ChatInfo.CancelEmote()`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.DropCautionaryChatMessage

`C_ChatInfo.DropCautionaryChatMessage(confirmNumber: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelInfoFromIdentifier

`C_ChatInfo.GetChannelInfoFromIdentifier(channelIdentifier: cstring) → info: ChatChannelInfo?`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelRosterInfo

`C_ChatInfo.GetChannelRosterInfo(channelIndex: luaIndex, rosterIndex: luaIndex) → name: string, owner: bool, moderator: bool, guid: WOWGUID`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelRuleset

`C_ChatInfo.GetChannelRuleset(channelIndex: luaIndex) → ruleset: ChatChannelRuleset`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelRulesetForChannelID

`C_ChatInfo.GetChannelRulesetForChannelID(channelID: number) → ruleset: ChatChannelRuleset`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelShortcut

`C_ChatInfo.GetChannelShortcut(channelIndex: luaIndex) → shortcut: cstring`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChannelShortcutForChannelID

`C_ChatInfo.GetChannelShortcutForChannelID(channelID: number) → shortcut: cstring`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChatLineSenderGUID

`C_ChatInfo.GetChatLineSenderGUID(chatLine: number) → guid: WOWGUID`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret during chat lockdown (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChatLineSenderName

`C_ChatInfo.GetChatLineSenderName(chatLine: number) → name: string`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret during chat lockdown (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChatLineText

`C_ChatInfo.GetChatLineText(chatLine: number) → text: string`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret during chat lockdown (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetChatTypeName

`C_ChatInfo.GetChatTypeName(typeID: number) → name: string?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetClubStreamIDs

`C_ChatInfo.GetClubStreamIDs(clubID: ClubId) → ids: ClubStreamId[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetColorForChatType

`C_ChatInfo.GetColorForChatType(chatType: cstring) → color: colorRGB?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetGeneralChannelID

`C_ChatInfo.GetGeneralChannelID() → channelID: number`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetGeneralChannelLocalID

`C_ChatInfo.GetGeneralChannelLocalID() → localID: number?`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetMentorChannelID

`C_ChatInfo.GetMentorChannelID() → channelID: number`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetNumActiveChannels

`C_ChatInfo.GetNumActiveChannels() → numChannels: number`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetNumReservedChatWindows

`C_ChatInfo.GetNumReservedChatWindows() → numReserved: number`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.GetRegisteredAddonMessagePrefixes

`C_ChatInfo.GetRegisteredAddonMessagePrefixes() → registeredPrefixes: cstring[]`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.InChatMessagingLockdown

`C_ChatInfo.InChatMessagingLockdown() → isRestricted: bool`

- Status: ❔ unverified
- Blizzard: Returns true if API security restrictions regarding chat messaging are in effect.
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsAddonMessagePrefixRegistered

`C_ChatInfo.IsAddonMessagePrefixRegistered(prefix: cstring) → isRegistered: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsChannelRegional

`C_ChatInfo.IsChannelRegional(channelIndex: luaIndex) → isRegional: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsChannelRegionalForChannelID

`C_ChatInfo.IsChannelRegionalForChannelID(channelID: number) → isRegional: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsChatLineCensored

`C_ChatInfo.IsChatLineCensored(chatLine: number) → isCensored: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsLoggingChat

`C_ChatInfo.IsLoggingChat() → enabled: bool`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsLoggingCombat

`C_ChatInfo.IsLoggingCombat() → enabled: bool, advanced: bool`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsPartyChannelType

`C_ChatInfo.IsPartyChannelType(channelType: ChatChannelType) → isPartyChannelType: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsRegionalServiceAvailable

`C_ChatInfo.IsRegionalServiceAvailable() → available: bool`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsTimerunningPlayer

`C_ChatInfo.IsTimerunningPlayer(playerGUID: WOWGUID) → isTimerunning: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsValidChatLine

`C_ChatInfo.IsValidChatLine(chatLine: number?) → isValid: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.IsValidCombatFilterName

`C_ChatInfo.IsValidCombatFilterName(name: cstring) → isApproved: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.PerformEmote

`C_ChatInfo.PerformEmote(emoteName: cstring, targetName: cstring?, suppressMoveError: bool = False) → success: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.RegisterAddonMessagePrefix

`C_ChatInfo.RegisterAddonMessagePrefix(prefix: cstring) → result: RegisterAddonMessagePrefixResult`

- Status: ❔ unverified
- Blizzard: Registers interest in addon messages with this prefix, cannot be an empty string.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.ReplaceIconAndGroupExpressions

`C_ChatInfo.ReplaceIconAndGroupExpressions(input: string, noIconReplacement: bool?, noGroupReplacement: bool?) → output: string`

- Status: ❔ unverified
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.RequestCanLocalWhisperTarget

`C_ChatInfo.RequestCanLocalWhisperTarget(whisperTarget: WOWGUID)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.ResetDefaultZoneChannels

`C_ChatInfo.ResetDefaultZoneChannels()`

- Status: ❔ unverified
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.SendAddonMessage

`C_ChatInfo.SendAddonMessage(prefix: cstring, message: cstring, chatType: cstring?, target: cstring?) → result: SendAddonMessageResult`

- Status: ❔ unverified
- Blizzard: Sends a text payload to other clients specified by chatChannel and target which are registered to listen for prefix.
- `chatType`: ChatType, defaults to SLASH_CMD_PARTY.
- `target`: Only applies for targeted channels
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.SendAddonMessageLogged

`C_ChatInfo.SendAddonMessageLogged(prefix: cstring, message: cstring, chatType: cstring?, target: cstring?) → result: SendAddonMessageResult?`

- Status: ❔ unverified
- Blizzard: Sends a text payload to other clients specified by chatChannel and target which are registered to listen for prefix. Intended for plain text payloads; logged and throttled.
- `chatType`: ChatType, defaults to SLASH_CMD_PARTY.
- `target`: Only applies for targeted channels
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.SendCautionaryChatMessage

`C_ChatInfo.SendCautionaryChatMessage(confirmNumber: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.SendChatMessage

`C_ChatInfo.SendChatMessage(message: cstring, chatType: SendChatMessageType?, languageID: number?, target: cstring?)`

- Status: ❔ unverified
- `chatType`: Chat type string ('SAY', 'EMOTE', etc.). Defaults to 'SAY' if not specified.
- `languageID`: Language to send the message in.
- `target`: Name of the player to send a message to. Only applies to chat types that support targeted messages.
- restricted in some situations (Blizzard's docs; not checked in game)
- RestrictedForMacroChatMessages (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.SwapChatChannelsByChannelIndex

`C_ChatInfo.SwapChatChannelsByChannelIndex(firstChannelIndex: luaIndex, secondChannelIndex: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

### C_ChatInfo.UncensorChatLine

`C_ChatInfo.UncensorChatLine(chatLine: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChatInfoDocumentation.lua`

## Events

### ALTERNATIVE_DEFAULT_LANGUAGE_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### BN_CHAT_MSG_ADDON

- Status: ❔ unverified
- Payload: `prefix: cstring`, `text: cstring`, `channel: cstring`, `senderID: number`
- fires synchronously (Blizzard's docs)

### CAN_LOCAL_WHISPER_TARGET_RESPONSE

- Status: ❔ unverified
- Payload: `whisperTarget: WOWGUID`, `status: ChatWhisperTargetStatus`
- unique event (Blizzard's docs)

### CAN_PLAYER_SPEAK_LANGUAGE_CHANGED

- Status: ❔ unverified
- Payload: `languageId: number`, `canSpeakLanguage: bool`
- unique event (Blizzard's docs)

### CAUTIONARY_CHANNEL_MESSAGE

- Status: ❔ unverified
- Payload: `confirmNumber: number`
- fires synchronously (Blizzard's docs)

### CAUTIONARY_CHAT_MESSAGE

- Status: ❔ unverified
- Payload: `chatLineID: number`, `confirmNumber: number`
- fires synchronously (Blizzard's docs)

### CHANNEL_COUNT_UPDATE

- Status: ❔ unverified
- Payload: `displayIndex: number`, `count: number`
- fires synchronously (Blizzard's docs)

### CHANNEL_FLAGS_UPDATED

- Status: ❔ unverified
- Payload: `displayIndex: number`
- fires synchronously (Blizzard's docs)

### CHANNEL_INVITE_REQUEST

- Status: ❔ unverified
- Payload: `channelID: cstring`, `name: cstring`
- fires synchronously (Blizzard's docs)

### CHANNEL_LEFT

- Status: ❔ unverified
- Payload: `chatChannelID: number`, `name: cstring`
- fires synchronously (Blizzard's docs)

### CHANNEL_PASSWORD_REQUEST

- Status: ❔ unverified
- Payload: `channelID: cstring`
- fires synchronously (Blizzard's docs)

### CHANNEL_ROSTER_UPDATE

- Status: ❔ unverified
- Payload: `displayIndex: number`, `count: number`
- fires synchronously (Blizzard's docs)

### CHANNEL_UI_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHAT_COMBAT_MSG_ARENA_POINTS_GAIN

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_LOGGING_CHANGED

- Status: ❔ unverified
- Payload: `whichLog: number`, `isEnabled: bool`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_ACHIEVEMENT

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_ADDON

- Status: ❔ unverified
- Payload: `prefix: cstring`, `text: cstring`, `channel: cstring`, `sender: cstring`, `target: cstring`, `zoneChannelID: number`, `localID: number`, `name: cstring`, `instanceID: number`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_ADDON_LOGGED

- Status: ❔ unverified
- Payload: `prefix: cstring`, `text: cstring`, `channel: cstring`, `sender: cstring`, `target: cstring`, `zoneChannelID: number`, `localID: number`, `name: cstring`, `instanceID: number`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_AFK

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BG_SYSTEM_ALLIANCE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BG_SYSTEM_HORDE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BG_SYSTEM_NEUTRAL

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_INLINE_TOAST_ALERT

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_INLINE_TOAST_BROADCAST

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_INLINE_TOAST_BROADCAST_INFORM

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_INLINE_TOAST_CONVERSATION

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_WHISPER

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_WHISPER_INFORM

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_BN_WHISPER_PLAYER_OFFLINE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL_JOIN

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL_LEAVE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL_LEAVE_PREVENTED

- Status: ❔ unverified
- Payload: `channelName: cstring`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL_LIST

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL_NOTICE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CHANNEL_NOTICE_USER

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_COLLECTED_APPEARANCE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_COMBAT_FACTION_CHANGE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_COMBAT_HONOR_GAIN

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_COMBAT_MISC_INFO

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_COMBAT_XP_GAIN

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_COMMUNITIES_CHANNEL

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_CURRENCY

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_DND

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_EMOTE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_FILTERED

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_GUILD

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_GUILD_ACHIEVEMENT

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_GUILD_DISCORD

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_GUILD_ITEM_LOOTED

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_IGNORED

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_INSTANCE_CHAT

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_INSTANCE_CHAT_LEADER

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_LOOT

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_MONEY

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_MONSTER_EMOTE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_MONSTER_PARTY

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_MONSTER_SAY

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_MONSTER_WHISPER

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_MONSTER_YELL

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_OFFICER

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_OPENING

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_PARTY

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_PARTY_LEADER

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_PET_BATTLE_COMBAT_LOG

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_PET_BATTLE_INFO

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_PET_INFO

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_PING

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RAID

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RAID_BOSS_EMOTE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RAID_BOSS_WHISPER

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RAID_LEADER

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RAID_WARNING

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_RESTRICTED

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- fires synchronously (Blizzard's docs)

### CHAT_MSG_SAY

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_SKILL

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_SYSTEM

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_TARGETICONS

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_TEXT_EMOTE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_TRADESKILLS

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_VOICE_TEXT

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_WHISPER

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_WHISPER_INFORM

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_MSG_YELL

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `languageName: cstring`, `channelName: cstring`, `playerName2: cstring`, `specialFlags: cstring`, `zoneChannelID: number`, `channelIndex: number`, `channelBaseName: cstring`, `languageID: number`, `lineID: number`, `guid: WOWGUID`, `bnSenderID: number`, `isMobile: bool`, `isSubtitle: bool`, `hideSenderInLetterbox: bool`, `suppressRaidIcons: bool`, `discordInfo: DiscordChatInfo`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### CHAT_REGIONAL_SEND_FAILED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHAT_REGIONAL_STATUS_CHANGED

- Status: ❔ unverified
- Payload: `isServiceAvailable: bool`
- fires synchronously (Blizzard's docs)

### CHAT_SERVER_DISCONNECTED

- Status: ❔ unverified
- Payload: `isInitialMessage: bool?`
- fires synchronously (Blizzard's docs)

### CHAT_SERVER_RECONNECTED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CLEAR_BOSS_EMOTES

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### DAILY_RESET_INSTANCE_WELCOME

- Status: ❔ unverified
- Payload: `mapname: cstring`, `timeLeft: number`
- fires synchronously (Blizzard's docs)

### INSTANCE_RESET_WARNING

- Status: ❔ unverified
- Payload: `warningMessage: cstring`, `timeLeft: number`
- fires synchronously (Blizzard's docs)

### LANGUAGE_LIST_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### NOTIFY_CHAT_SUPPRESSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### QUEST_BOSS_EMOTE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `displayTime: number`, `enableBossEmoteWarningSound: bool`
- fires synchronously (Blizzard's docs)

### RAID_BOSS_EMOTE

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `displayTime: number`, `enableBossEmoteWarningSound: bool`
- fires synchronously (Blizzard's docs)

### RAID_BOSS_WHISPER

- Status: ❔ unverified
- Payload: `text: cstring`, `playerName: cstring`, `displayTime: number`, `enableBossEmoteWarningSound: bool`
- fires synchronously (Blizzard's docs)

### RAID_INSTANCE_WELCOME

- Status: ❔ unverified
- Payload: `mapname: cstring`, `timeLeft: number`, `locked: number`, `extended: number`
- fires synchronously (Blizzard's docs)

### UPDATE_CHAT_COLOR

- Status: ❔ unverified
- Payload: `name: cstring`, `r: number`, `g: number`, `b: number`
- fires synchronously (Blizzard's docs)

### UPDATE_CHAT_COLOR_NAME_BY_CLASS

- Status: ❔ unverified
- Payload: `name: cstring`, `colorNameByClass: bool`
- fires synchronously (Blizzard's docs)

### UPDATE_CHAT_WINDOWS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_FLOATING_CHAT_WINDOWS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

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
