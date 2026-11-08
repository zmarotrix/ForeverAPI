# XMLUtil

Namespace: `C_XMLUtil`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_XMLUtil.GetTemplateInfo](#c_xmlutilgettemplateinfo) |  |  |
| ✅ | [C_XMLUtil.GetTemplates](#c_xmlutilgettemplates) | 1 value | 1 value |

### C_XMLUtil.GetTemplateInfo

`C_XMLUtil.GetTemplateInfo(name: cstring) → info: XMLTemplateInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `XMLUtilDocumentation.lua`

### C_XMLUtil.GetTemplates

`C_XMLUtil.GetTemplates() → templates: XMLTemplateListInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,...(2615)}`
- Called in combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,...(2615)}`
- Source: client docs `XMLUtilDocumentation.lua`

## Types

### XMLTemplateInfo

- Structure
  - `type`: cstring
  - `width`: number
  - `height`: number
  - `keyValues`: XMLTemplateKeyValue[]
  - `inherits`: cstring?
  - `sourceLocation`: string

### XMLTemplateKeyValue

- Structure
  - `key`: cstring
  - `keyType`: cstring
  - `type`: cstring
  - `value`: cstring

### XMLTemplateListInfo

- Structure
  - `name`: cstring
  - `type`: cstring
