# GenericWidgetDisplay

Namespace: `C_GenericWidgetDisplay`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_GenericWidgetDisplay.Acknowledge](#c_genericwidgetdisplayacknowledge) |  |  |
| ❔ | [C_GenericWidgetDisplay.Close](#c_genericwidgetdisplayclose) |  |  |

### C_GenericWidgetDisplay.Acknowledge

`C_GenericWidgetDisplay.Acknowledge()`

- Status: ❔ unverified
- Source: client docs `UIGenericWidgetDisplayDocumentation.lua`

### C_GenericWidgetDisplay.Close

`C_GenericWidgetDisplay.Close()`

- Status: ❔ unverified
- Source: client docs `UIGenericWidgetDisplayDocumentation.lua`

## Events

### GENERIC_WIDGET_DISPLAY_SHOW

- Status: ❔ unverified
- Payload: `info: GenericWidgetDisplayFrameInfo`
- fires synchronously (Blizzard's docs)

## Types

### GenericWidgetDisplayFrameInfo

- Structure
  - `uiWidgetSetID`: number?
  - `uiTextureKit`: textureKit?
  - `title`: string?
  - `frameWidth`: number
  - `frameHeight`: number
  - `extraButtonText`: string?
  - `closeButtonText`: string?
