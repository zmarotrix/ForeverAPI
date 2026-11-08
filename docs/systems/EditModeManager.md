# EditModeManager

Namespace: `C_EditMode`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_EditMode.ConvertLayoutInfoToString](#c_editmodeconvertlayoutinfotostring) |  |  |
| ❔ | [C_EditMode.ConvertStringToLayoutInfo](#c_editmodeconvertstringtolayoutinfo) |  |  |
| ❔ | [C_EditMode.GetAccountSettings](#c_editmodegetaccountsettings) |  |  |
| ❔ | [C_EditMode.GetEditModeDefaultLayout](#c_editmodegeteditmodedefaultlayout) |  |  |
| ❔ | [C_EditMode.GetLayouts](#c_editmodegetlayouts) |  |  |
| ❔ | [C_EditMode.IsValidLayoutName](#c_editmodeisvalidlayoutname) |  |  |
| ❔ | [C_EditMode.OnEditModeExit](#c_editmodeoneditmodeexit) |  |  |
| ❔ | [C_EditMode.OnLayoutAdded](#c_editmodeonlayoutadded) |  |  |
| ❔ | [C_EditMode.OnLayoutDeleted](#c_editmodeonlayoutdeleted) |  |  |
| ❔ | [C_EditMode.SaveLayouts](#c_editmodesavelayouts) |  |  |
| ❔ | [C_EditMode.SetAccountSetting](#c_editmodesetaccountsetting) |  |  |
| ❔ | [C_EditMode.SetActiveLayout](#c_editmodesetactivelayout) |  |  |

### C_EditMode.ConvertLayoutInfoToString

`C_EditMode.ConvertLayoutInfoToString(layoutInfo: EditModeLayoutInfo) → layoutInfoAsString: string`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.ConvertStringToLayoutInfo

`C_EditMode.ConvertStringToLayoutInfo(layoutInfoAsString: string) → layoutInfo: EditModeLayoutInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.GetAccountSettings

`C_EditMode.GetAccountSettings() → accountSettings: EditModeSettingInfo[]`

- Status: ❔ unverified
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.GetEditModeDefaultLayout

`C_EditMode.GetEditModeDefaultLayout() → defaultLayout: number`

- Status: ❔ unverified
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.GetLayouts

`C_EditMode.GetLayouts() → layoutInfo: EditModeLayouts`

- Status: ❔ unverified
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.IsValidLayoutName

`C_EditMode.IsValidLayoutName(name: cstring) → isApproved: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.OnEditModeExit

`C_EditMode.OnEditModeExit()`

- Status: ❔ unverified
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.OnLayoutAdded

`C_EditMode.OnLayoutAdded(addedLayoutIndex: luaIndex, activateNewLayout: bool, isLayoutImported: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.OnLayoutDeleted

`C_EditMode.OnLayoutDeleted(deletedLayoutIndex: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.SaveLayouts

`C_EditMode.SaveLayouts(saveInfo: EditModeLayouts)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.SetAccountSetting

`C_EditMode.SetAccountSetting(setting: EditModeAccountSetting, value: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EditModeManagerDocumentation.lua`

### C_EditMode.SetActiveLayout

`C_EditMode.SetActiveLayout(activeLayout: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EditModeManagerDocumentation.lua`

## Events

### EDIT_MODE_LAYOUTS_UPDATED

- Status: ❔ unverified
- Payload: `layoutInfo: EditModeLayouts`, `reconcileLayouts: bool`
- fires synchronously (Blizzard's docs)

## Types

### EditModeAnchorInfo

- Structure
  - `point`: FramePoint
  - `relativeTo`: string
  - `relativePoint`: FramePoint
  - `offsetX`: number
  - `offsetY`: number

### EditModeLayoutInfo

- Structure
  - `layoutName`: string
  - `layoutType`: EditModeLayoutType
  - `interfaceStyle`: InputDeviceInterfaceType?
  - `systems`: EditModeSystemInfo[]

### EditModeLayouts

- Structure
  - `layouts`: EditModeLayoutInfo[]
  - `activeLayout`: luaIndex

### EditModeSettingInfo

- Structure
  - `setting`: number
  - `value`: number

### EditModeSystemInfo

- Structure
  - `system`: EditModeSystem
  - `systemIndex`: luaIndex?
  - `anchorInfo`: EditModeAnchorInfo
  - `anchorInfo2`: EditModeAnchorInfo?
  - `settings`: EditModeSettingInfo[]
  - `isInDefaultPosition`: bool
