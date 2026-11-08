# PlayerChoice

Namespace: `C_PlayerChoice`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_PlayerChoice.GetCurrentPlayerChoiceInfo](#c_playerchoicegetcurrentplayerchoiceinfo) |  |  |
| ❔ | [C_PlayerChoice.GetNumRerolls](#c_playerchoicegetnumrerolls) |  |  |
| ❔ | [C_PlayerChoice.GetRemainingTime](#c_playerchoicegetremainingtime) |  |  |
| ❔ | [C_PlayerChoice.IsWaitingForPlayerChoiceResponse](#c_playerchoiceiswaitingforplayerchoiceresponse) |  |  |
| ❔ | [C_PlayerChoice.OnUIClosed](#c_playerchoiceonuiclosed) |  |  |
| ❔ | [C_PlayerChoice.RequestRerollPlayerChoice](#c_playerchoicerequestrerollplayerchoice) |  |  |
| ❔ | [C_PlayerChoice.SendPlayerChoiceResponse](#c_playerchoicesendplayerchoiceresponse) |  |  |

### C_PlayerChoice.GetCurrentPlayerChoiceInfo

`C_PlayerChoice.GetCurrentPlayerChoiceInfo() → choiceInfo: PlayerChoiceInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `PlayerChoiceDocumentation.lua`

### C_PlayerChoice.GetNumRerolls

`C_PlayerChoice.GetNumRerolls() → numRerolls: number`

- Status: ❔ unverified
- Source: client docs `PlayerChoiceDocumentation.lua`

### C_PlayerChoice.GetRemainingTime

`C_PlayerChoice.GetRemainingTime() → remainingTime: number?`

- Status: ❔ unverified
- Source: client docs `PlayerChoiceDocumentation.lua`

### C_PlayerChoice.IsWaitingForPlayerChoiceResponse

`C_PlayerChoice.IsWaitingForPlayerChoiceResponse() → isWaitingForResponse: bool`

- Status: ❔ unverified
- Source: client docs `PlayerChoiceDocumentation.lua`

### C_PlayerChoice.OnUIClosed

`C_PlayerChoice.OnUIClosed()`

- Status: ❔ unverified
- Source: client docs `PlayerChoiceDocumentation.lua`

### C_PlayerChoice.RequestRerollPlayerChoice

`C_PlayerChoice.RequestRerollPlayerChoice()`

- Status: ❔ unverified
- Source: client docs `PlayerChoiceDocumentation.lua`

### C_PlayerChoice.SendPlayerChoiceResponse

`C_PlayerChoice.SendPlayerChoiceResponse(responseID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerChoiceDocumentation.lua`

## Events

### PLAYER_CHOICE_CLOSE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_CHOICE_UPDATE

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

## Types

### PlayerChoiceInfo

- Structure
  - `objectGUID`: WOWGUID
  - `choiceID`: number
  - `questionText`: string
  - `pendingChoiceText`: string
  - `uiTextureKit`: textureKit
  - `hideWarboardHeader`: bool
  - `keepOpenAfterChoice`: bool
  - `requiresSelection`: bool
  - `hideAnswerArt`: bool
  - `playerChoiceLayout`: PlayerChoiceLayout
  - `options`: PlayerChoiceOptionInfo[]
  - `soundKitID`: number?
  - `closeUISoundKitID`: number?

### PlayerChoiceOptionButtonInfo

- Structure
  - `id`: number
  - `text`: string
  - `disabled`: bool
  - `showCheckmark`: bool
  - `hideButtonShowText`: bool
  - `selected`: bool
  - `confirmation`: string?
  - `tooltip`: string?
  - `rewardQuestID`: number?
  - `soundKitID`: number?
  - `listText`: string?

### PlayerChoiceOptionInfo

- Structure
  - `id`: number
  - `description`: string
  - `header`: string
  - `choiceArtID`: number
  - `desaturatedArt`: bool
  - `disabledOption`: bool
  - `hasRewards`: bool
  - `rewardInfo`: PlayerChoiceOptionRewardInfo
  - `uiTextureKit`: textureKit
  - `maxStacks`: number
  - `buttons`: PlayerChoiceOptionButtonInfo[]
  - `widgetSetID`: number?
  - `spellID`: number?
  - `rarity`: PlayerChoiceRarity?
  - `typeArtID`: number?
  - `headerIconAtlasElement`: string?
  - `subHeader`: string?
  - `consolidateWidgets`: bool

### PlayerChoiceOptionRewardInfo

- Structure
  - `currencyRewards`: PlayerChoiceRewardCurrencyInfo[]
  - `itemRewards`: PlayerChoiceRewardItemInfo[]
  - `repRewards`: PlayerChoiceRewardReputationInfo[]

### PlayerChoiceRarity

- Enumeration — ❔ unverified
  - `Common` = 0
  - `Uncommon` = 1
  - `Rare` = 2
  - `Epic` = 3

### PlayerChoiceRewardCurrencyInfo

- Structure
  - `currencyId`: number
  - `name`: string
  - `currencyTexture`: number
  - `quantity`: number
  - `isCurrencyContainer`: bool

### PlayerChoiceRewardItemInfo

- Structure
  - `itemId`: number
  - `name`: string
  - `quantity`: number

### PlayerChoiceRewardReputationInfo

- Structure
  - `factionId`: number
  - `quantity`: number
