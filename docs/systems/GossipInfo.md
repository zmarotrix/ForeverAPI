# GossipInfo

Namespace: `C_GossipInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_GossipInfo.CloseGossip](#c_gossipinfoclosegossip) |  |  |
| ❔ | [C_GossipInfo.ForceGossip](#c_gossipinfoforcegossip) |  |  |
| ❔ | [C_GossipInfo.GetActiveQuests](#c_gossipinfogetactivequests) |  |  |
| ❔ | [C_GossipInfo.GetAvailableQuests](#c_gossipinfogetavailablequests) |  |  |
| ❔ | [C_GossipInfo.GetCompletedOptionDescriptionString](#c_gossipinfogetcompletedoptiondescriptionstring) |  |  |
| ❔ | [C_GossipInfo.GetCustomGossipDescriptionString](#c_gossipinfogetcustomgossipdescriptionstring) |  |  |
| ❔ | [C_GossipInfo.GetFriendshipReputation](#c_gossipinfogetfriendshipreputation) |  |  |
| ❔ | [C_GossipInfo.GetFriendshipReputationRanks](#c_gossipinfogetfriendshipreputationranks) |  |  |
| ❔ | [C_GossipInfo.GetNumActiveQuests](#c_gossipinfogetnumactivequests) |  |  |
| ❔ | [C_GossipInfo.GetNumAvailableQuests](#c_gossipinfogetnumavailablequests) |  |  |
| ❔ | [C_GossipInfo.GetOptionUIWidgetSetsAndTypesByOptionID](#c_gossipinfogetoptionuiwidgetsetsandtypesbyoptionid) |  |  |
| ❔ | [C_GossipInfo.GetOptions](#c_gossipinfogetoptions) |  |  |
| ❔ | [C_GossipInfo.GetPoiForUiMapID](#c_gossipinfogetpoiforuimapid) |  |  |
| ❔ | [C_GossipInfo.GetPoiInfo](#c_gossipinfogetpoiinfo) |  |  |
| ❔ | [C_GossipInfo.GetText](#c_gossipinfogettext) |  |  |
| ❔ | [C_GossipInfo.RefreshOptions](#c_gossipinforefreshoptions) |  |  |
| ❔ | [C_GossipInfo.SelectActiveQuest](#c_gossipinfoselectactivequest) |  |  |
| ❔ | [C_GossipInfo.SelectAvailableQuest](#c_gossipinfoselectavailablequest) |  |  |
| ❔ | [C_GossipInfo.SelectOption](#c_gossipinfoselectoption) |  |  |
| ❔ | [C_GossipInfo.SelectOptionByIndex](#c_gossipinfoselectoptionbyindex) |  |  |

### C_GossipInfo.CloseGossip

`C_GossipInfo.CloseGossip()`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.ForceGossip

`C_GossipInfo.ForceGossip() → forceGossip: bool`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetActiveQuests

`C_GossipInfo.GetActiveQuests() → info: GossipQuestUIInfo[]`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetAvailableQuests

`C_GossipInfo.GetAvailableQuests() → info: GossipQuestUIInfo[]`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetCompletedOptionDescriptionString

`C_GossipInfo.GetCompletedOptionDescriptionString() → description: string?`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetCustomGossipDescriptionString

`C_GossipInfo.GetCustomGossipDescriptionString() → description: string?`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetFriendshipReputation

`C_GossipInfo.GetFriendshipReputation(friendshipFactionID: number) → reputationInfo: FriendshipReputationInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetFriendshipReputationRanks

`C_GossipInfo.GetFriendshipReputationRanks(friendshipFactionID: number) → rankInfo: FriendshipReputationRankInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetNumActiveQuests

`C_GossipInfo.GetNumActiveQuests() → numQuests: number`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetNumAvailableQuests

`C_GossipInfo.GetNumAvailableQuests() → numQuests: number`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetOptionUIWidgetSetsAndTypesByOptionID

`C_GossipInfo.GetOptionUIWidgetSetsAndTypesByOptionID(gossipOptionID: number) → gossipOptionUIWidgetSetsAndTypes: GossipOptionUIWidgetSetAndType[]?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetOptions

`C_GossipInfo.GetOptions() → info: GossipOptionUIInfo[]`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetPoiForUiMapID

`C_GossipInfo.GetPoiForUiMapID(uiMapID: number) → gossipPoiID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetPoiInfo

`C_GossipInfo.GetPoiInfo(uiMapID: number, gossipPoiID: number) → gossipPoiInfo: GossipPoiInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.GetText

`C_GossipInfo.GetText() → gossipText: cstring`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.RefreshOptions

`C_GossipInfo.RefreshOptions()`

- Status: ❔ unverified
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.SelectActiveQuest

`C_GossipInfo.SelectActiveQuest(optionID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.SelectAvailableQuest

`C_GossipInfo.SelectAvailableQuest(optionID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.SelectOption

`C_GossipInfo.SelectOption(optionID: number, text: cstring?, confirmed: bool?)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GossipInfoDocumentation.lua`

### C_GossipInfo.SelectOptionByIndex

`C_GossipInfo.SelectOptionByIndex(optionID: number, text: cstring?, confirmed: bool?)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GossipInfoDocumentation.lua`

## Events

### DYNAMIC_GOSSIP_POI_UPDATED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### GOSSIP_CLOSED

- Status: ❔ unverified
- Payload: `interactionIsContinuing: bool`
- fires synchronously (Blizzard's docs)

### GOSSIP_CONFIRM

- Status: ❔ unverified
- Payload: `gossipID: number`, `text: string`, `cost: WOWMONEY`
- fires synchronously (Blizzard's docs)

### GOSSIP_CONFIRM_CANCEL

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GOSSIP_ENTER_CODE

- Status: ❔ unverified
- Payload: `gossipID: number`
- fires synchronously (Blizzard's docs)

### GOSSIP_OPTIONS_REFRESHED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GOSSIP_SHOW

- Status: ❔ unverified
- Payload: `uiTextureKit: textureKit?`
- fires synchronously (Blizzard's docs)

## Types

### FriendshipReputationInfo

- Structure
  - `friendshipFactionID`: number
  - `standing`: number
  - `maxRep`: number
  - `name`: string?
  - `text`: string
  - `texture`: number
  - `reaction`: string
  - `reactionThreshold`: number
  - `nextThreshold`: number?
  - `reversedColor`: bool
  - `overrideColor`: number?

### FriendshipReputationRankInfo

- Structure
  - `currentLevel`: number
  - `maxLevel`: number

### GossipOptionRewardInfo

- Structure
  - `id`: number
  - `quantity`: number
  - `rewardType`: GossipOptionRewardType
  - `context`: ItemCreationContext

### GossipOptionRewardType

- Enumeration — ❔ unverified
  - `Item` = 0
  - `Currency` = 1

### GossipOptionStatus

- Enumeration — ❔ unverified
  - `Available` = 0
  - `Unavailable` = 1
  - `Locked` = 2
  - `AlreadyComplete` = 3

### GossipOptionUIInfo

- Structure
  - `gossipOptionID`: number?
  - `name`: string
  - `icon`: fileID
  - `rewards`: GossipOptionRewardInfo[]
  - `status`: GossipOptionStatus
  - `spellID`: number?
  - `flags`: number
  - `overrideIconID`: fileID?
  - `selectOptionWhenOnlyOption`: bool
  - `orderIndex`: number
  - `failureDescription`: string?

### GossipOptionUIWidgetSetAndType

- Structure
  - `widgetType`: number
  - `uiWidgetSetID`: number

### GossipOptionUIWidgetSetTypes

- Enumeration — ❔ unverified
  - `Modifiers` = 0
  - `Background` = 1

### GossipPoiInfo

- Structure
  - `name`: string
  - `textureIndex`: number
  - `position`: vector2
  - `inBattleMap`: bool

### GossipQuestUIInfo

- Structure
  - `title`: string
  - `questLevel`: number
  - `isTrivial`: bool
  - `frequency`: number?
  - `repeatable`: bool?
  - `isComplete`: bool?
  - `isLegendary`: bool
  - `isIgnored`: bool
  - `questID`: number
  - `isImportant`: bool
  - `isMeta`: bool
  - `questInfoID`: number
