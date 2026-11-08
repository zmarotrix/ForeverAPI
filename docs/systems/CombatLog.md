# CombatLog

Namespace: `C_CombatLog`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_CombatLog.ApplyFilterSettings](#c_combatlogapplyfiltersettings) |  |  |
| ✅ | [C_CombatLog.AreFilteredEventsEnabled](#c_combatlogarefilteredeventsenabled) |  |  |
| ✅ | [C_CombatLog.ClearEntries](#c_combatlogclearentries) |  |  |
| ✅ | [C_CombatLog.DoesObjectMatchFilter](#c_combatlogdoesobjectmatchfilter) |  |  |
| ✅ | [C_CombatLog.GetEntryRetentionTime](#c_combatloggetentryretentiontime) |  |  |
| ✅ | [C_CombatLog.GetMessageLimit](#c_combatloggetmessagelimit) |  |  |
| ✅ | [C_CombatLog.IsCombatLogRestricted](#c_combatlogiscombatlogrestricted) |  |  |
| ✅ | [C_CombatLog.RefilterEntries](#c_combatlogrefilterentries) |  |  |
| ✅ | [C_CombatLog.SetEntryRetentionTime](#c_combatlogsetentryretentiontime) |  |  |
| ✅ | [C_CombatLog.SetFilteredEventsEnabled](#c_combatlogsetfilteredeventsenabled) |  |  |
| ✅ | [C_CombatLog.SetMessageLimit](#c_combatlogsetmessagelimit) |  |  |

### C_CombatLog.ApplyFilterSettings

`C_CombatLog.ApplyFilterSettings(filterSettings: LuaValueVariant)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogDocumentation.lua`

### C_CombatLog.AreFilteredEventsEnabled

`C_CombatLog.AreFilteredEventsEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Source: client docs `CombatLogDocumentation.lua`

### C_CombatLog.ClearEntries

`C_CombatLog.ClearEntries()`

- Status: ✅ verified (function)
- Source: client docs `CombatLogDocumentation.lua`

### C_CombatLog.DoesObjectMatchFilter

`C_CombatLog.DoesObjectMatchFilter(mask: CombatLogObject, flags: CombatLogObject) → matches: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogDocumentation.lua`

### C_CombatLog.GetEntryRetentionTime

`C_CombatLog.GetEntryRetentionTime() → retentionTime: number`

- Status: ✅ verified (function)
- Source: client docs `CombatLogDocumentation.lua`

### C_CombatLog.GetMessageLimit

`C_CombatLog.GetMessageLimit() → messageLimit: number`

- Status: ✅ verified (function)
- Source: client docs `CombatLogDocumentation.lua`

### C_CombatLog.IsCombatLogRestricted

`C_CombatLog.IsCombatLogRestricted() → restricted: bool`

- Status: ✅ verified (function)
- Source: client docs `CombatLogDocumentation.lua`

### C_CombatLog.RefilterEntries

`C_CombatLog.RefilterEntries()`

- Status: ✅ verified (function)
- Source: client docs `CombatLogDocumentation.lua`

### C_CombatLog.SetEntryRetentionTime

`C_CombatLog.SetEntryRetentionTime(retentionTime: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogDocumentation.lua`

### C_CombatLog.SetFilteredEventsEnabled

`C_CombatLog.SetFilteredEventsEnabled(enabled: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogDocumentation.lua`

### C_CombatLog.SetMessageLimit

`C_CombatLog.SetMessageLimit(messageLimit: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatLogDocumentation.lua`

## Events

### COMBAT_LOG_ENTRIES_CLEARED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### COMBAT_LOG_EVENT

- Status: ✅ verified
- Payload: none
- CallbackEvent (Blizzard's docs)
- restricted in some situations (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### COMBAT_LOG_EVENT_UNFILTERED

- Status: ✅ verified
- Payload: none
- CallbackEvent (Blizzard's docs)
- restricted in some situations (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### COMBAT_LOG_MESSAGE_LIMIT_CHANGED

- Status: ✅ verified
- Payload: `messageLimit: number`
- fires synchronously (Blizzard's docs)
