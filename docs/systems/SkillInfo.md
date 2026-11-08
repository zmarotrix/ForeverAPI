# SkillInfo

Namespace: `C_SkillInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SkillInfo.AbandonSkill](#c_skillinfoabandonskill) |  |  |
| ✅ | [C_SkillInfo.CollapseSkillHeader](#c_skillinfocollapseskillheader) |  |  |
| ✅ | [C_SkillInfo.ExpandSkillHeader](#c_skillinfoexpandskillheader) |  |  |
| ✅ | [C_SkillInfo.GetNumSkillLines](#c_skillinfogetnumskilllines) | 1 value | 1 value |
| ✅ | [C_SkillInfo.GetSelectedSkill](#c_skillinfogetselectedskill) | 1 value | 1 value |
| ✅ | [C_SkillInfo.GetSkillLineInfo](#c_skillinfogetskilllineinfo) | 1 value | 1 value |
| ✅ | [C_SkillInfo.GetSkillLineInfoByID](#c_skillinfogetskilllineinfobyid) |  |  |
| ✅ | [C_SkillInfo.SetSelectedSkill](#c_skillinfosetselectedskill) |  |  |

### C_SkillInfo.AbandonSkill

`C_SkillInfo.AbandonSkill(skillLineID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SkillInfoDocumentation.lua`

### C_SkillInfo.CollapseSkillHeader

`C_SkillInfo.CollapseSkillHeader(index: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SkillInfoDocumentation.lua`

### C_SkillInfo.ExpandSkillHeader

`C_SkillInfo.ExpandSkillHeader(index: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SkillInfoDocumentation.lua`

### C_SkillInfo.GetNumSkillLines

`C_SkillInfo.GetNumSkillLines() → numSkillLines: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `SkillInfoDocumentation.lua`

### C_SkillInfo.GetSelectedSkill

`C_SkillInfo.GetSelectedSkill() → index: luaIndex`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `SkillInfoDocumentation.lua`

### C_SkillInfo.GetSkillLineInfo

`C_SkillInfo.GetSkillLineInfo(index: luaIndex) → skillLineAttributes: SkillLineAttributes?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `table{costType=number,description=string,isAbandonable=boolean,isCollapsed=boolean,isHeader=boolean,maxRank=number,minLevel=number,modifier=number,name=string,parentSkillLineID=number,rank=number,rankCost=number,skillID=number,skillLineCategoryID=number,stepCost=number,tempPoints=number}`
- Called in combat: returned 1 value: `table{costType=number,description=string,isAbandonable=boolean,isCollapsed=boolean,isHeader=boolean,maxRank=number,minLevel=number,modifier=number,name=string,parentSkillLineID=number,rank=number,rankCost=number,skillID=number,skillLineCategoryID=number,stepCost=number,tempPoints=number}`
- Source: client docs `SkillInfoDocumentation.lua`

### C_SkillInfo.GetSkillLineInfoByID

`C_SkillInfo.GetSkillLineInfoByID(ID: number) → skillLineAttributes: SkillLineAttributes?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SkillInfoDocumentation.lua`

### C_SkillInfo.SetSelectedSkill

`C_SkillInfo.SetSelectedSkill(index: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SkillInfoDocumentation.lua`

## Events

### SKILL_LINES_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 115 times (47 in combat); argument kinds: ``

## Types

### SkillLineAttributes

- Structure
  - `skillID`: number
  - `name`: cstring
  - `isHeader`: bool
  - `isCollapsed`: bool
  - `rank`: number
  - `tempPoints`: number
  - `modifier`: number
  - `maxRank`: number
  - `isAbandonable`: bool
  - `stepCost`: number
  - `rankCost`: number
  - `minLevel`: number
  - `costType`: number
  - `parentSkillLineID`: number
  - `skillLineCategoryID`: number
  - `description`: cstring
