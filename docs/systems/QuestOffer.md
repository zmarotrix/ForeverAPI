# QuestOffer

Namespace: `C_QuestOffer`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_QuestOffer.GetHideRequiredItems](#c_questoffergethiderequireditems) | 1 value | 1 value |
| ✅ | [C_QuestOffer.GetQuestOfferMajorFactionReputationRewards](#c_questoffergetquestoffermajorfactionreputationrewards) |  |  |
| ✅ | [C_QuestOffer.GetQuestRequiredCurrencyInfo](#c_questoffergetquestrequiredcurrencyinfo) | 1 value | 1 value |
| ✅ | [C_QuestOffer.GetQuestRewardCurrencyInfo](#c_questoffergetquestrewardcurrencyinfo) |  |  |

### C_QuestOffer.GetHideRequiredItems

`C_QuestOffer.GetHideRequiredItems() → hideRequiredItems: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `QuestOfferDocumentation.lua`

### C_QuestOffer.GetQuestOfferMajorFactionReputationRewards

`C_QuestOffer.GetQuestOfferMajorFactionReputationRewards() → reputationRewards: QuestRewardReputationInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `QuestOfferDocumentation.lua`

### C_QuestOffer.GetQuestRequiredCurrencyInfo

`C_QuestOffer.GetQuestRequiredCurrencyInfo(questRewardIndex: luaIndex) → questRequiredCurrencyInfo: QuestRequiredCurrencyInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `QuestOfferDocumentation.lua`

### C_QuestOffer.GetQuestRewardCurrencyInfo

`C_QuestOffer.GetQuestRewardCurrencyInfo(questInfoType: cstring, questRewardIndex: luaIndex) → questRewardCurrencyInfo: QuestRewardCurrencyInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestOfferDocumentation.lua`

## Events

### QUEST_ACCEPT_CONFIRM

- Status: ✅ verified
- Payload: `name: cstring`, `questTitle: cstring`, `questID: number`
- fires synchronously (Blizzard's docs)

### QUEST_FINISHED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### QUEST_GREETING

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### QUEST_ITEM_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### QUEST_PROGRESS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### QuestRequiredCurrencyInfo

- Structure
  - `texture`: fileID
  - `name`: cstring
  - `currencyID`: number
  - `quality`: number
  - `requiredAmount`: number
