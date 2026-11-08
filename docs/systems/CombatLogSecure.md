# CombatLogSecure

Namespace: `C_CombatLogSecure`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_CombatLogSecure.AddEventFilter](#c_combatlogsecureaddeventfilter) |  |  |
| ❔ | [C_CombatLogSecure.ClearEventFilters](#c_combatlogsecurecleareventfilters) |  |  |
| ❔ | [C_CombatLogSecure.CreateCombatLogMessage](#c_combatlogsecurecreatecombatlogmessage) |  |  |
| ❔ | [C_CombatLogSecure.GetCurrentEntryInfo](#c_combatlogsecuregetcurrententryinfo) |  |  |
| ❔ | [C_CombatLogSecure.GetCurrentEventInfo](#c_combatlogsecuregetcurrenteventinfo) |  |  |
| ❔ | [C_CombatLogSecure.GetEntryCount](#c_combatlogsecuregetentrycount) |  |  |
| ❔ | [C_CombatLogSecure.SeekToNewestEntry](#c_combatlogsecureseektonewestentry) |  |  |
| ❔ | [C_CombatLogSecure.SeekToPreviousEntry](#c_combatlogsecureseektopreviousentry) |  |  |
| ❔ | [C_CombatLogSecure.ShouldShowCurrentEntry](#c_combatlogsecureshouldshowcurrententry) |  |  |

### C_CombatLogSecure.AddEventFilter

`C_CombatLogSecure.AddEventFilter()`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogSecureDocumentation.lua`

### C_CombatLogSecure.ClearEventFilters

`C_CombatLogSecure.ClearEventFilters()`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogSecureDocumentation.lua`

### C_CombatLogSecure.CreateCombatLogMessage

`C_CombatLogSecure.CreateCombatLogMessage(message: string, colorR: number, colorG: number, colorB: number, order: CombatLogMessageOrder)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogSecureDocumentation.lua`

### C_CombatLogSecure.GetCurrentEntryInfo

`C_CombatLogSecure.GetCurrentEntryInfo()`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogSecureDocumentation.lua`

### C_CombatLogSecure.GetCurrentEventInfo

`C_CombatLogSecure.GetCurrentEventInfo()`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogSecureDocumentation.lua`

### C_CombatLogSecure.GetEntryCount

`C_CombatLogSecure.GetEntryCount(ignoreFilter: bool = False) → count: number`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogSecureDocumentation.lua`

### C_CombatLogSecure.SeekToNewestEntry

`C_CombatLogSecure.SeekToNewestEntry(ignoreFilter: bool = False) → isValidEntry: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogSecureDocumentation.lua`

### C_CombatLogSecure.SeekToPreviousEntry

`C_CombatLogSecure.SeekToPreviousEntry(ignoreFilter: bool = False) → isValidEntry: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogSecureDocumentation.lua`

### C_CombatLogSecure.ShouldShowCurrentEntry

`C_CombatLogSecure.ShouldShowCurrentEntry() → shouldShow: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogSecureDocumentation.lua`

## Events

### COMBAT_LOG_APPLY_FILTER_SETTINGS

- Status: ❔ unverified
- Payload: `filterSettings: LuaValueVariant`
- CallbackEvent (Blizzard's docs)
- restricted in some situations (Blizzard's docs)

### COMBAT_LOG_MESSAGE

- Status: ❔ unverified
- Payload: `message: string`, `colorR: number`, `colorG: number`, `colorB: number`, `order: CombatLogMessageOrder`
- fires synchronously (Blizzard's docs)

### COMBAT_LOG_REFILTER_ENTRIES

- Status: ❔ unverified
- Payload: none
- CallbackEvent (Blizzard's docs)
- restricted in some situations (Blizzard's docs)
