# QuestInfoSystem

Namespace: `C_QuestInfoSystem`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_QuestInfoSystem.GetQuestClassification](#c_questinfosystemgetquestclassification) | 1 value | 1 value |
| ✅ | [C_QuestInfoSystem.GetQuestHasShortExpirationWarning](#c_questinfosystemgetquesthasshortexpirationwarning) | 1 value | 1 value |
| ✅ | [C_QuestInfoSystem.GetQuestLogRewardFavor](#c_questinfosystemgetquestlogrewardfavor) |  |  |
| ✅ | [C_QuestInfoSystem.GetQuestRewardCurrencies](#c_questinfosystemgetquestrewardcurrencies) |  |  |
| ✅ | [C_QuestInfoSystem.GetQuestRewardSpellInfo](#c_questinfosystemgetquestrewardspellinfo) |  |  |
| ✅ | [C_QuestInfoSystem.GetQuestRewardSpells](#c_questinfosystemgetquestrewardspells) |  |  |
| ✅ | [C_QuestInfoSystem.GetQuestShouldToastCompletion](#c_questinfosystemgetquestshouldtoastcompletion) | 1 value | 1 value |
| ✅ | [C_QuestInfoSystem.HasQuestRewardCurrencies](#c_questinfosystemhasquestrewardcurrencies) |  |  |
| ✅ | [C_QuestInfoSystem.HasQuestRewardSpells](#c_questinfosystemhasquestrewardspells) |  |  |

### C_QuestInfoSystem.GetQuestClassification

`C_QuestInfoSystem.GetQuestClassification(questID: number?, questInfoID: number?) → classification: QuestClassification`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `QuestInfoSystemDocumentation.lua`

### C_QuestInfoSystem.GetQuestHasShortExpirationWarning

`C_QuestInfoSystem.GetQuestHasShortExpirationWarning(questID: number?) → hasShortExpirationWarning: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `QuestInfoSystemDocumentation.lua`

### C_QuestInfoSystem.GetQuestLogRewardFavor

`C_QuestInfoSystem.GetQuestLogRewardFavor(questID: number?, clampFavorToCycleCap: bool?) → amount: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestInfoSystemDocumentation.lua`

### C_QuestInfoSystem.GetQuestRewardCurrencies

`C_QuestInfoSystem.GetQuestRewardCurrencies(questID: number?) → questRewardCurrencyInfo: QuestRewardCurrencyInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestInfoSystemDocumentation.lua`

### C_QuestInfoSystem.GetQuestRewardSpellInfo

`C_QuestInfoSystem.GetQuestRewardSpellInfo(questID: number?, spellID: number) → info: QuestRewardSpellInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestInfoSystemDocumentation.lua`

### C_QuestInfoSystem.GetQuestRewardSpells

`C_QuestInfoSystem.GetQuestRewardSpells(questID: number?) → spellIDs: number[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestInfoSystemDocumentation.lua`

### C_QuestInfoSystem.GetQuestShouldToastCompletion

`C_QuestInfoSystem.GetQuestShouldToastCompletion(questID: number?) → shouldToast: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `QuestInfoSystemDocumentation.lua`

### C_QuestInfoSystem.HasQuestRewardCurrencies

`C_QuestInfoSystem.HasQuestRewardCurrencies(questID: number?) → hasQuestRewardCurrencies: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestInfoSystemDocumentation.lua`

### C_QuestInfoSystem.HasQuestRewardSpells

`C_QuestInfoSystem.HasQuestRewardSpells(questID: number?) → hasRewardSpells: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestInfoSystemDocumentation.lua`
