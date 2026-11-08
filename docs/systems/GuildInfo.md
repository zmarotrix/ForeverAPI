# GuildInfo

Namespace: `C_GuildInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_GuildInfo.AreGuildEventsEnabled](#c_guildinfoareguildeventsenabled) | 1 value | 1 value |
| ✅ | [C_GuildInfo.CanEditOfficerNote](#c_guildinfocaneditofficernote) | 1 value | 1 value |
| ✅ | [C_GuildInfo.CanSpeakInGuildChat](#c_guildinfocanspeakinguildchat) | 1 value | 1 value |
| ✅ | [C_GuildInfo.CanViewOfficerNote](#c_guildinfocanviewofficernote) | 1 value | 1 value |
| ✅ | [C_GuildInfo.Demote](#c_guildinfodemote) |  |  |
| ✅ | [C_GuildInfo.Disband](#c_guildinfodisband) |  |  |
| ✅ | [C_GuildInfo.GetGuildNewsInfo](#c_guildinfogetguildnewsinfo) |  |  |
| ✅ | [C_GuildInfo.GetGuildRankOrder](#c_guildinfogetguildrankorder) |  |  |
| ✅ | [C_GuildInfo.GetGuildTabardInfo](#c_guildinfogetguildtabardinfo) | 1 value | 1 value |
| ✅ | [C_GuildInfo.GetInfoText](#c_guildinfogetinfotext) | 💥 blocked | 💥 blocked |
| ✅ | [C_GuildInfo.GetMOTD](#c_guildinfogetmotd) | 💥 blocked | 💥 blocked |
| ✅ | [C_GuildInfo.GetPreferredPlaySettings](#c_guildinfogetpreferredplaysettings) | 6 values | 6 values |
| ✅ | [C_GuildInfo.GetPreferredPlaySettingsFeatures](#c_guildinfogetpreferredplaysettingsfeatures) | 2 values | 2 values |
| ✅ | [C_GuildInfo.GuildControlGetRankFlags](#c_guildinfoguildcontrolgetrankflags) |  |  |
| ✅ | [C_GuildInfo.GuildRoster](#c_guildinfoguildroster) |  |  |
| ✅ | [C_GuildInfo.Invite](#c_guildinfoinvite) |  |  |
| ✅ | [C_GuildInfo.IsDiscordStreamSeparate](#c_guildinfoisdiscordstreamseparate) | 1 value | 1 value |
| ✅ | [C_GuildInfo.IsEncounterGuildNewsEnabled](#c_guildinfoisencounterguildnewsenabled) | 1 value | 1 value |
| ✅ | [C_GuildInfo.IsGuildOfficer](#c_guildinfoisguildofficer) | 1 value | 1 value |
| ✅ | [C_GuildInfo.IsGuildRankAssignmentAllowed](#c_guildinfoisguildrankassignmentallowed) |  |  |
| ✅ | [C_GuildInfo.IsGuildReputationEnabled](#c_guildinfoisguildreputationenabled) | 1 value | 1 value |
| ✅ | [C_GuildInfo.Leave](#c_guildinfoleave) |  |  |
| ✅ | [C_GuildInfo.MemberExistsByName](#c_guildinfomemberexistsbyname) |  |  |
| ✅ | [C_GuildInfo.Promote](#c_guildinfopromote) |  |  |
| ✅ | [C_GuildInfo.QueryGuildMemberRecipes](#c_guildinfoqueryguildmemberrecipes) |  |  |
| ✅ | [C_GuildInfo.QueryGuildMembersForRecipe](#c_guildinfoqueryguildmembersforrecipe) |  |  |
| ✅ | [C_GuildInfo.RemoveFromGuild](#c_guildinforemovefromguild) |  |  |
| ✅ | [C_GuildInfo.RequestGuildRename](#c_guildinforequestguildrename) |  |  |
| ✅ | [C_GuildInfo.RequestGuildRenameRefund](#c_guildinforequestguildrenamerefund) |  |  |
| ✅ | [C_GuildInfo.RequestPreferredPlaySettings](#c_guildinforequestpreferredplaysettings) |  |  |
| ✅ | [C_GuildInfo.RequestRenameNameCheck](#c_guildinforequestrenamenamecheck) |  |  |
| ✅ | [C_GuildInfo.RequestRenameStatus](#c_guildinforequestrenamestatus) |  |  |
| ✅ | [C_GuildInfo.SetGuildRankOrder](#c_guildinfosetguildrankorder) |  |  |
| ✅ | [C_GuildInfo.SetInfoText](#c_guildinfosetinfotext) |  |  |
| ✅ | [C_GuildInfo.SetLeader](#c_guildinfosetleader) |  |  |
| ✅ | [C_GuildInfo.SetMOTD](#c_guildinfosetmotd) |  |  |
| ✅ | [C_GuildInfo.SetNote](#c_guildinfosetnote) |  |  |
| ✅ | [C_GuildInfo.SetPreferredPlaySettings](#c_guildinfosetpreferredplaysettings) |  |  |
| ✅ | [C_GuildInfo.Uninvite](#c_guildinfouninvite) |  |  |

### C_GuildInfo.AreGuildEventsEnabled

`C_GuildInfo.AreGuildEventsEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.CanEditOfficerNote

`C_GuildInfo.CanEditOfficerNote() → canEditOfficerNote: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.CanSpeakInGuildChat

`C_GuildInfo.CanSpeakInGuildChat() → canSpeakInGuildChat: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.CanViewOfficerNote

`C_GuildInfo.CanViewOfficerNote() → canViewOfficerNote: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.Demote

`C_GuildInfo.Demote(name: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.Disband

`C_GuildInfo.Disband()`

- Status: ✅ verified (function)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.GetGuildNewsInfo

`C_GuildInfo.GetGuildNewsInfo(index: luaIndex) → newsInfo: GuildNewsInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.GetGuildRankOrder

`C_GuildInfo.GetGuildRankOrder(guid: WOWGUID) → rankOrder: luaIndex`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.GetGuildTabardInfo

`C_GuildInfo.GetGuildTabardInfo(unit: UnitToken?) → tabardInfo: GuildTabardInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.GetInfoText

`C_GuildInfo.GetInfoText() → infoText: string`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Called out of combat: not called: blocked
- Called in combat: not called: blocked
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.GetMOTD

`C_GuildInfo.GetMOTD() → motd: string`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Called out of combat: not called: blocked
- Called in combat: not called: blocked
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.GetPreferredPlaySettings

`C_GuildInfo.GetPreferredPlaySettings() → loaded: bool, preferredLocaleID: number, preferredDatacenterLocalityID: number, lastPreferredLocaleChangeDate: time_t, lastPreferredDatacenterLocalityChangeDate: time_t, changeCooldownDays: number`

- Status: ✅ verified (function)
- Called out of combat: returned 6 values: `boolean`, `number`, `number`, `number`, `number`, `number`
- Called in combat: returned 6 values: `boolean`, `number`, `number`, `number`, `number`, `number`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.GetPreferredPlaySettingsFeatures

`C_GuildInfo.GetPreferredPlaySettingsFeatures() → canChangeLocale: bool, canChangeDatacenterLocality: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `boolean`
- Called in combat: returned 2 values: `boolean`, `boolean`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.GuildControlGetRankFlags

`C_GuildInfo.GuildControlGetRankFlags(rankOrder: luaIndex) → permissions: bool[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.GuildRoster

`C_GuildInfo.GuildRoster()`

- Status: ✅ verified (function)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.Invite

`C_GuildInfo.Invite(name: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.IsDiscordStreamSeparate

`C_GuildInfo.IsDiscordStreamSeparate() → separateStream: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.IsEncounterGuildNewsEnabled

`C_GuildInfo.IsEncounterGuildNewsEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.IsGuildOfficer

`C_GuildInfo.IsGuildOfficer() → isOfficer: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.IsGuildRankAssignmentAllowed

`C_GuildInfo.IsGuildRankAssignmentAllowed(guid: WOWGUID, rankOrder: luaIndex) → isGuildRankAssignmentAllowed: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.IsGuildReputationEnabled

`C_GuildInfo.IsGuildReputationEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.Leave

`C_GuildInfo.Leave()`

- Status: ✅ verified (function)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.MemberExistsByName

`C_GuildInfo.MemberExistsByName(name: cstring) → exists: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.Promote

`C_GuildInfo.Promote(name: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.QueryGuildMemberRecipes

`C_GuildInfo.QueryGuildMemberRecipes(guildMemberGUID: WOWGUID, skillLineID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.QueryGuildMembersForRecipe

`C_GuildInfo.QueryGuildMembersForRecipe(skillLineID: number, recipeSpellID: number, recipeLevel: luaIndex?) → updatedRecipeSpellID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.RemoveFromGuild

`C_GuildInfo.RemoveFromGuild(guid: WOWGUID)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.RequestGuildRename

`C_GuildInfo.RequestGuildRename(desiredName: cstring)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.RequestGuildRenameRefund

`C_GuildInfo.RequestGuildRenameRefund()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.RequestPreferredPlaySettings

`C_GuildInfo.RequestPreferredPlaySettings() → startedSuccessfully: bool`

- Status: ✅ verified (function)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.RequestRenameNameCheck

`C_GuildInfo.RequestRenameNameCheck(desiredName: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.RequestRenameStatus

`C_GuildInfo.RequestRenameStatus() → ableToRequest: bool`

- Status: ✅ verified (function)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.SetGuildRankOrder

`C_GuildInfo.SetGuildRankOrder(guid: WOWGUID, rankOrder: luaIndex)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.SetInfoText

`C_GuildInfo.SetInfoText(infoText: cstring)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.SetLeader

`C_GuildInfo.SetLeader(name: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.SetMOTD

`C_GuildInfo.SetMOTD(motd: cstring)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.SetNote

`C_GuildInfo.SetNote(guid: WOWGUID, note: cstring, isPublic: bool)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.SetPreferredPlaySettings

`C_GuildInfo.SetPreferredPlaySettings(preferredLocaleID: number = 0, preferredDatacenterLocalityID: number = 0) → startedSuccessfully: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

### C_GuildInfo.Uninvite

`C_GuildInfo.Uninvite(name: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GuildInfoDocumentation.lua`

## Events

### CLOSE_TABARD_FRAME

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### DISABLE_DECLINE_GUILD_INVITE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ENABLE_DECLINE_GUILD_INVITE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILDTABARD_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILD_CHALLENGE_COMPLETED

- Status: ✅ verified
- Payload: `challengeType: number`, `currentCount: number`, `maxCount: number`, `goldAwarded: number`
- fires synchronously (Blizzard's docs)

### GUILD_CHALLENGE_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 3 times (0 in combat); argument kinds: ``

### GUILD_EVENT_LOG_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILD_INVITE_CANCEL

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILD_INVITE_REQUEST

- Status: ✅ verified
- Payload: `inviter: cstring`, `guildName: cstring`, `guildAchievementPoints: number`, `oldGuildName: cstring`, `isNewGuild: bool?`, `tabardInfo: GuildTabardInfo?`
- fires synchronously (Blizzard's docs)

### GUILD_MOTD

- Status: ✅ verified
- Payload: `motdText: cstring`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### GUILD_NEWS_UPDATE

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### GUILD_PARTY_STATE_UPDATED

- Status: ✅ verified
- Payload: `inGuildParty: bool`
- fires synchronously (Blizzard's docs)

### GUILD_PREFERRED_PLAY_SETTINGS_UPDATED

- Status: ✅ verified
- Payload: `status: PreferredPlaySettingsStatus`, `preferredLocaleID: number`, `preferredDatacenterLocalityID: number`, `lastPreferredLocaleChangeDate: time_t`, `lastPreferredDatacenterLocalityChangeDate: time_t`
- fires synchronously (Blizzard's docs)

### GUILD_RANKS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 12 times (2 in combat); argument kinds: ``

### GUILD_RANKS_UPDATE_ACTIVE_PLAYER

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### GUILD_RECIPE_KNOWN_BY_MEMBERS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILD_REGISTRAR_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILD_REGISTRAR_SHOW

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILD_RENAME_NAME_CHECK

- Status: ✅ verified
- Payload: `desiredName: cstring`, `status: GuildErrorType`, `nameErrorToken: cstring?`
- fires synchronously (Blizzard's docs)

### GUILD_RENAME_REFUND_RESULT

- Status: ✅ verified
- Payload: `guildName: cstring`, `status: GuildErrorType`
- fires synchronously (Blizzard's docs)

### GUILD_RENAME_REQUIRED

- Status: ✅ verified
- Payload: `flagSet: bool`
- fires synchronously (Blizzard's docs)

### GUILD_RENAME_STATUS_UPDATE

- Status: ✅ verified
- Payload: `status: GuildRenameStatus`
- fires synchronously (Blizzard's docs)

### GUILD_REWARDS_LIST

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GUILD_REWARDS_LIST_UPDATE

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### GUILD_ROSTER_UPDATE

- Status: ✅ verified
- Payload: `canRequestRosterUpdate: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 33 times (9 in combat); argument kinds: `b`

### GUILD_TRADESKILL_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 15 times (3 in combat); argument kinds: ``

### OPEN_TABARD_FRAME

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_GUILD_UPDATE

- Status: ✅ verified
- Payload: `unitTarget: UnitTokenVariant`
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (0 in combat); argument kinds: `s`

### REQUESTED_GUILD_RENAME_RESULT

- Status: ✅ verified
- Payload: `newName: cstring`, `status: GuildErrorType`
- fires synchronously (Blizzard's docs)

### REQUIRED_GUILD_RENAME_RESULT

- Status: ✅ verified
- Payload: `success: bool`
- fires synchronously (Blizzard's docs)

### TABARD_CANSAVE_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### TABARD_SAVE_PENDING

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### UNIT_GUILD_LEVEL

- Status: ✅ verified
- Payload: `newLevel: number`
- fires synchronously (Blizzard's docs)

## Types

### GuildNewsInfo

- Structure
  - `isSticky`: bool
  - `isHeader`: bool
  - `newsType`: number
  - `whoText`: string?
  - `whatText`: string?
  - `newsDataID`: number
  - `data`: number[]
  - `weekday`: number
  - `day`: number
  - `month`: number
  - `year`: number
  - `guildMembersPresent`: number

### GuildRenameStatus

- Structure
  - `isNameChangeEnabled`: bool
  - `isPlayerGuildMaster`: bool
  - `refundEligibleEndTime`: time_t
  - `nextRenameTime`: time_t
  - `renamePrice`: WOWMONEY
  - `refundAmount`: WOWMONEY
  - `currentGuildMoney`: WOWMONEY
  - `result`: GuildErrorType
  - `oldGuildName`: cstring
  - `reservedName`: cstring
  - `reservedNameExpirationTime`: time_t
