# UIModifiedInstance

Namespace: `C_ModifiedInstance`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ModifiedInstance.GetModifiedInstanceInfoFromMapID](#c_modifiedinstancegetmodifiedinstanceinfofrommapid) | 💥 no sample for map | 💥 no sample for map |

### C_ModifiedInstance.GetModifiedInstanceInfoFromMapID

`C_ModifiedInstance.GetModifiedInstanceInfoFromMapID(mapID: number) → info: ModifiedInstanceInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `UIModifiedInstanceDocumentation.lua`

## Types

### ModifiedInstanceInfo

- Structure
  - `lfrItemLevel`: number?
  - `normalItemLevel`: number?
  - `heroicItemLevel`: number?
  - `mythicItemLevel`: number?
  - `uiTextureKit`: textureKit
  - `description`: string
