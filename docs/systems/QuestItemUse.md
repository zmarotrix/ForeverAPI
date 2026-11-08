# QuestItemUse

Namespace: `C_QuestItemUse`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_QuestItemUse.CanUseQuestItemOnObject](#c_questitemusecanusequestitemonobject) | 1 value | 1 value |

### C_QuestItemUse.CanUseQuestItemOnObject

`C_QuestItemUse.CanUseQuestItemOnObject(item: ItemLocation, unit: UnitToken, checkRange: bool?) → canUse: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `itemloc,unit`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `QuestItemUseDocumentation.lua`
