# HouseEditorUI

Namespace: `C_HouseEditor`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_HouseEditor.ActivateHouseEditorMode](#c_houseeditoractivatehouseeditormode) |  |  |
| ✅ | [C_HouseEditor.EnterHouseEditor](#c_houseeditorenterhouseeditor) |  |  |
| ✅ | [C_HouseEditor.GetActiveHouseEditorMode](#c_houseeditorgetactivehouseeditormode) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HouseEditor.GetHouseEditorAvailability](#c_houseeditorgethouseeditoravailability) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HouseEditor.GetHouseEditorModeAvailability](#c_houseeditorgethouseeditormodeavailability) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HouseEditor.GetHouseEditorPlayerType](#c_houseeditorgethouseeditorplayertype) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HouseEditor.IsHouseEditorActive](#c_houseeditorishouseeditoractive) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HouseEditor.IsHouseEditorModeActive](#c_houseeditorishouseeditormodeactive) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HouseEditor.IsHouseEditorStatusAvailable](#c_houseeditorishouseeditorstatusavailable) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HouseEditor.LeaveHouseEditor](#c_houseeditorleavehouseeditor) |  |  |

### C_HouseEditor.ActivateHouseEditorMode

`C_HouseEditor.ActivateHouseEditorMode(editMode: HouseEditorMode) → result: HousingResult`

- Status: ✅ verified (function)
- Blizzard: Attempts switch the House Editor to a specific House Editor mode
- `result`: The initial result of the attempt to activate the mode; If Success, mode is either already active, or we've succesfully started making required requests to server; Listen for MODE_CHANGED or MODE_CHANGE_FAILURE events for ultimate end result after server calls
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HouseEditorUIDocumentation.lua`

### C_HouseEditor.EnterHouseEditor

`C_HouseEditor.EnterHouseEditor() → result: HousingResult`

- Status: ✅ verified (function)
- Blizzard: Attempts to open the House Editor to the default House Editor mode
- `result`: The initial result of the attempt to open the Editor; If Success, Editor is either already active, or we've succesfully started making required requests to server; Listen for MODE_CHANGED or MODE_CHANGE_FAILURE events for ultimate end result after server calls
- Source: client docs `HouseEditorUIDocumentation.lua`

### C_HouseEditor.GetActiveHouseEditorMode

`C_HouseEditor.GetActiveHouseEditorMode() → editMode: HouseEditorMode`

- Status: ✅ verified (function)
- Called out of combat: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HouseEditorUIDocumentation.lua`

### C_HouseEditor.GetHouseEditorAvailability

`C_HouseEditor.GetHouseEditorAvailability() → result: HousingResult`

- Status: ✅ verified (function)
- Blizzard: Returns the availability state of the House Editor overall
- Called out of combat: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HouseEditorUIDocumentation.lua`

### C_HouseEditor.GetHouseEditorModeAvailability

`C_HouseEditor.GetHouseEditorModeAvailability(editMode: HouseEditorMode) → result: HousingResult`

- Status: ✅ verified (function)
- Blizzard: Returns the availability of a specific House Editor mode
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HouseEditorUIDocumentation.lua`

### C_HouseEditor.GetHouseEditorPlayerType

`C_HouseEditor.GetHouseEditorPlayerType() → playerType: HouseEditorPlayerType`

- Status: ✅ verified (function)
- Called out of combat: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HouseEditorUIDocumentation.lua`

### C_HouseEditor.IsHouseEditorActive

`C_HouseEditor.IsHouseEditorActive() → isEditorActive: bool`

- Status: ✅ verified (function)
- Blizzard: Returns whether the House Editor is active, in any mode
- Called out of combat: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HouseEditorUIDocumentation.lua`

### C_HouseEditor.IsHouseEditorModeActive

`C_HouseEditor.IsHouseEditorModeActive(editMode: HouseEditorMode) → isModeActive: bool`

- Status: ✅ verified (function)
- Blizzard: Returns whether the specific House Editor mode is active
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HouseEditorUIDocumentation.lua`

### C_HouseEditor.IsHouseEditorStatusAvailable

`C_HouseEditor.IsHouseEditorStatusAvailable() → editorStatusAvailable: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the HouseEditor currently able process mode availability and switching; May be false if not in a house or plot, or while waiting to get house settings back from the server
- Called out of combat: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HouseEditorUIDocumentation.lua`

### C_HouseEditor.LeaveHouseEditor

`C_HouseEditor.LeaveHouseEditor()`

- Status: ✅ verified (function)
- Source: client docs `HouseEditorUIDocumentation.lua`

## Events

### HOUSE_EDITOR_AVAILABILITY_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSE_EDITOR_MODE_CHANGED

- Status: ✅ verified
- Payload: `currentEditMode: HouseEditorMode`
- fires synchronously (Blizzard's docs)

### HOUSE_EDITOR_MODE_CHANGE_FAILURE

- Status: ✅ verified
- Payload: `result: HousingResult`
- fires synchronously (Blizzard's docs)

## Types

### HouseEditorPlayerType

- Enumeration — ✅ verified
  - `None` = 0
  - `Owner` = 1
  - `Visitor` = 2
