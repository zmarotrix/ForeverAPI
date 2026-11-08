# UIEventToastManagerInfo

Namespace: `C_EventToastManager`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_EventToastManager.GetLevelUpDisplayToastsFromLevel](#c_eventtoastmanagergetlevelupdisplaytoastsfromlevel) | 1 value | 1 value |
| ✅ | [C_EventToastManager.GetNextToastToDisplay](#c_eventtoastmanagergetnexttoasttodisplay) | 0 values | 0 values |
| ✅ | [C_EventToastManager.RemoveCurrentToast](#c_eventtoastmanagerremovecurrenttoast) |  |  |

### C_EventToastManager.GetLevelUpDisplayToastsFromLevel

`C_EventToastManager.GetLevelUpDisplayToastsFromLevel(level: number) → toastInfo: EventToastInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:10`: returned 1 value: `table{[number]=table}`
- Called in combat: returned 1 value: `table{[number]=table}`
- Source: client docs `UIEventToastManagerDocumentation.lua`

### C_EventToastManager.GetNextToastToDisplay

`C_EventToastManager.GetNextToastToDisplay() → toastInfo: EventToastInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `UIEventToastManagerDocumentation.lua`

### C_EventToastManager.RemoveCurrentToast

`C_EventToastManager.RemoveCurrentToast()`

- Status: ✅ verified (function)
- Source: client docs `UIEventToastManagerDocumentation.lua`

## Events

### DISPLAY_EVENT_TOASTS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### DISPLAY_EVENT_TOAST_LINK

- Status: ✅ verified
- Payload: `link: string`
- fires synchronously (Blizzard's docs)

## Types

### EventToastInfo

- Structure
  - `eventToastID`: number
  - `title`: string
  - `subtitle`: string
  - `instructionText`: string
  - `iconFileID`: fileID
  - `subIcon`: textureAtlas?
  - `link`: string
  - `qualityString`: string?
  - `quality`: number?
  - `eventType`: EventToastEventType
  - `displayType`: EventToastDisplayType
  - `uiTextureKit`: textureKit
  - `sortOrder`: number
  - `time`: number?
  - `uiWidgetSetID`: number?
  - `extraUiWidgetSetID`: number?
  - `titleTooltip`: string?
  - `subtitleTooltip`: string?
  - `titleTooltipUiWidgetSetID`: number?
  - `subtitleTooltipUiWidgetSetID`: number?
  - `showSoundKitID`: number?
  - `hideSoundKitID`: number?
  - `colorTint`: colorRGB?
  - `flags`: number
