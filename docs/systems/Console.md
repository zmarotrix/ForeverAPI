# Console

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [CalculateStringEditDistance](#calculatestringeditdistance) |  |  |
| ✅ | [ConsoleEcho](#consoleecho) |  |  |
| ✅ | [ConsoleExec](#consoleexec) |  |  |
| ✅ | [ConsoleGetAllCommands](#consolegetallcommands) |  |  |
| ✅ | [ConsoleGetColorFromType](#consolegetcolorfromtype) |  |  |
| ✅ | [ConsoleGetFontHeight](#consolegetfontheight) |  |  |
| ✅ | [ConsoleIsActive](#consoleisactive) |  |  |
| ✅ | [ConsolePrintAllMatchingCommands](#consoleprintallmatchingcommands) |  |  |
| ✅ | [ConsoleSetFontHeight](#consolesetfontheight) |  |  |
| ✅ | [SetConsoleKey](#setconsolekey) |  |  |

### CalculateStringEditDistance

`CalculateStringEditDistance(firstString: stringView, secondString: stringView) → distance: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleDocumentation.lua`

### ConsoleEcho

`ConsoleEcho(command: cstring, addToHistory: bool = False, prefix: cstring?) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleDocumentation.lua`

### ConsoleExec

`ConsoleExec(command: cstring, addToHistory: bool = False) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleDocumentation.lua`

### ConsoleGetAllCommands

`ConsoleGetAllCommands() → commands: ConsoleCommandInfo[]`

- Status: ✅ verified (function)
- Source: client docs `ConsoleDocumentation.lua`

### ConsoleGetColorFromType

`ConsoleGetColorFromType(colorType: ConsoleColorType) → color: colorRGB`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleDocumentation.lua`

### ConsoleGetFontHeight

`ConsoleGetFontHeight() → fontHeightInPixels: number`

- Status: ✅ verified (function)
- Source: client docs `ConsoleDocumentation.lua`

### ConsoleIsActive

`ConsoleIsActive() → consoleIsActive: bool`

- Status: ✅ verified (function)
- Source: client docs `ConsoleDocumentation.lua`

### ConsolePrintAllMatchingCommands

`ConsolePrintAllMatchingCommands(partialCommandText: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleDocumentation.lua`

### ConsoleSetFontHeight

`ConsoleSetFontHeight(fontHeightInPixels: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleDocumentation.lua`

### SetConsoleKey

`SetConsoleKey(keystring: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleDocumentation.lua`

## Events

### CONSOLE_CLEAR

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### CONSOLE_COLORS_CHANGED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### CONSOLE_FONT_SIZE_CHANGED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### CONSOLE_LOG

- Status: ✅ verified
- Payload: `message: cstring`
- fires synchronously (Blizzard's docs)

### CONSOLE_MESSAGE

- Status: ✅ verified
- Payload: `message: cstring`, `colorType: number`
- fires synchronously (Blizzard's docs)
- Seen firing 1098 times (22 in combat); argument kinds: `s,n`

### CVAR_UPDATE

- Status: ✅ verified
- Payload: `eventName: cstring`, `value: cstring`
- fires synchronously (Blizzard's docs)
- Seen firing 233 times (3 in combat); argument kinds: `s,s`

### TOGGLE_CONSOLE

- Status: ✅ verified
- Payload: `showConsole: bool?`
- fires synchronously (Blizzard's docs)

## Types

### ConsoleCategory

- Enumeration — ✅ verified
  - `Debug` = 0
  - `Graphics` = 1
  - `Console` = 2
  - `Combat` = 3
  - `Game` = 4
  - `Default` = 5
  - `Net` = 6
  - `Sound` = 7
  - `Gm` = 8
  - `Reveal` = 9
  - `None` = 10

### ConsoleColorType

- Enumeration — ✅ verified
  - `DefaultColor` = 0
  - `InputColor` = 1
  - `EchoColor` = 2
  - `ErrorColor` = 3
  - `WarningColor` = 4
  - `GlobalColor` = 5
  - `AdminColor` = 6
  - `HighlightColor` = 7
  - `BackgroundColor` = 8
  - `ClickbufferColor` = 9
  - `PrivateColor` = 10
  - `DefaultGreen` = 11

### ConsoleCommandInfo

- Structure
  - `command`: cstring
  - `help`: cstring
  - `category`: ConsoleCategory
  - `commandType`: ConsoleCommandType
  - `scriptContents`: cstring
  - `scriptParameters`: cstring

### ConsoleCommandType

- Enumeration — ✅ verified
  - `Cvar` = 0
  - `Command` = 1
  - `Macro` = 2
  - `Script` = 3
