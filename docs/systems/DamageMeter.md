# DamageMeter

Namespace: `C_DamageMeter`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_DamageMeter.GetAvailableCombatSessions](#c_damagemetergetavailablecombatsessions) | 1 value | 1 value |
| ✅ | [C_DamageMeter.GetCombatSessionFromID](#c_damagemetergetcombatsessionfromid) |  |  |
| ✅ | [C_DamageMeter.GetCombatSessionFromType](#c_damagemetergetcombatsessionfromtype) | 1 value | 1 value |
| ✅ | [C_DamageMeter.GetCombatSessionSourceFromID](#c_damagemetergetcombatsessionsourcefromid) |  |  |
| ✅ | [C_DamageMeter.GetCombatSessionSourceFromType](#c_damagemetergetcombatsessionsourcefromtype) | 1 value | 1 value |
| ✅ | [C_DamageMeter.GetSessionDurationSeconds](#c_damagemetergetsessiondurationseconds) | 1 value | 1 value |
| ✅ | [C_DamageMeter.IsDamageMeterAvailable](#c_damagemeterisdamagemeteravailable) | 2 values | 2 values |
| ✅ | [C_DamageMeter.ResetAllCombatSessions](#c_damagemeterresetallcombatsessions) |  |  |

### C_DamageMeter.GetAvailableCombatSessions

`C_DamageMeter.GetAvailableCombatSessions() → availableSessions: DamageMeterAvailableCombatSession[]`

- Status: ✅ verified (function)
- Blizzard: Returns a list of combat sessions currently being tracked.
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{[number]=table}`
- Source: client docs `DamageMeterDocumentation.lua`

### C_DamageMeter.GetCombatSessionFromID

`C_DamageMeter.GetCombatSessionFromID(sessionID: number, type: DamageMeterType) → session: DamageMeterCombatSession`

- Status: ✅ verified (function)
- Blizzard: Returns the data for the player's combat session with the specified ID.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- returns secrets in combat (Blizzard's docs; not checked in game)
- Source: client docs `DamageMeterDocumentation.lua`

### C_DamageMeter.GetCombatSessionFromType

`C_DamageMeter.GetCombatSessionFromType(sessionType: DamageMeterSessionType, type: DamageMeterType) → session: DamageMeterCombatSession`

- Status: ✅ verified (function)
- Blizzard: Returns the data for the player's current combat session.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- returns secrets in combat (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:0`: returned 1 value: `table{combatSources=table,maxAmount=number,totalAmount=number}`
- Called in combat: returned 1 value: `table{combatSources=table,maxAmount=secret,totalAmount=secret}`
- Source: client docs `DamageMeterDocumentation.lua`

### C_DamageMeter.GetCombatSessionSourceFromID

`C_DamageMeter.GetCombatSessionSourceFromID(sessionID: number, type: DamageMeterType, sourceGUID: WOWGUID?, sourceCreatureID: number?) → sessionSource: DamageMeterCombatSessionSource`

- Status: ✅ verified (function)
- Blizzard: Returns the data for a single source (unit) in the player's current combat session with the specified ID.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- returns secrets in combat (Blizzard's docs; not checked in game)
- Source: client docs `DamageMeterDocumentation.lua`

### C_DamageMeter.GetCombatSessionSourceFromType

`C_DamageMeter.GetCombatSessionSourceFromType(sessionType: DamageMeterSessionType, type: DamageMeterType, sourceGUID: WOWGUID?, sourceCreatureID: number?) → sessionSource: DamageMeterCombatSessionSource`

- Status: ✅ verified (function)
- Blizzard: Returns the data for a single source (unit) in the player's current combat session.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- returns secrets in combat (Blizzard's docs; not checked in game)
- Called out of combat with `n:0,n:0`: returned 1 value: `table{combatSpells=table,maxAmount=number,totalAmount=number}`
- Called in combat: returned 1 value: `table{combatSpells=table,maxAmount=secret,totalAmount=secret}`
- Source: client docs `DamageMeterDocumentation.lua`

### C_DamageMeter.GetSessionDurationSeconds

`C_DamageMeter.GetSessionDurationSeconds(sessionType: DamageMeterSessionType) → durationSeconds: number?`

- Status: ✅ verified (function)
- Blizzard: Returns the amount of time a combat session has lasted
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `DamageMeterDocumentation.lua`

### C_DamageMeter.IsDamageMeterAvailable

`C_DamageMeter.IsDamageMeterAvailable() → isAvailable: bool, failureReason: string`

- Status: ✅ verified (function)
- Blizzard: Returns whether the player can enable and use the Damage Meter.
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `DamageMeterDocumentation.lua`

### C_DamageMeter.ResetAllCombatSessions

`C_DamageMeter.ResetAllCombatSessions()`

- Status: ✅ verified (function)
- Blizzard: Clears the data for all the player's combat sessions.
- Source: client docs `DamageMeterDocumentation.lua`

## Events

### DAMAGE_METER_COMBAT_SESSION_UPDATED

- Status: ✅ verified
- Payload: `type: DamageMeterType`, `sessionID: number`
- unique event (Blizzard's docs)
- Seen firing 273246 times (261838 in combat); argument kinds: `n,n`

### DAMAGE_METER_CURRENT_SESSION_UPDATED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 451 times (276 in combat); argument kinds: ``

### DAMAGE_METER_RESET

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 18 times (2 in combat); argument kinds: ``

## Types

### DamageMeterAvailableCombatSession

- Structure
- Blizzard: Data for a combat session currently being tracked.
  - `sessionID`: number
  - `name`: cstring
  - `durationSeconds`: number?

### DamageMeterCombatSession

- Structure
- Blizzard: Aggregated data for all sources (units) in a damage meter combat session.
  - `combatSources`: DamageMeterCombatSource[]
  - `maxAmount`: number
  - `totalAmount`: number
  - `durationSeconds`: number?

### DamageMeterCombatSessionSource

- Structure
- Blizzard: Data for a single source (unit) in a combat session.
  - `combatSpells`: DamageMeterCombatSpell[]
  - `maxAmount`: number
  - `totalAmount`: number

### DamageMeterCombatSource

- Structure
- Blizzard: Aggregated data for a single source (unit) in a damage meter combat session.
  - `sourceGUID`: WOWGUID?
  - `sourceCreatureID`: number?
  - `name`: cstring
  - `classFilename`: cstring
  - `specIconID`: fileID
  - `totalAmount`: number
  - `amountPerSecond`: number
  - `isLocalPlayer`: bool
  - `deathRecapID`: number
  - `deathTimeSeconds`: number
  - `classification`: cstring
  - `sourceDisplayType`: DamageMeterSourceDisplayType
  - `factionGroup`: cstring?

### DamageMeterCombatSpell

- Structure
- Blizzard: Aggregated data for all spells of the same ID cast by a single source (unit) in a combat session.
  - `spellID`: number
  - `totalAmount`: number
  - `amountPerSecond`: number
  - `creatureName`: cstring
  - `overkillAmount`: number
  - `isAvoidable`: bool
  - `isDeadly`: bool
  - `combatSpellDetails`: DamageMeterCombatSpellUnitDetails

### DamageMeterCombatSpellUnitDetails

- Structure
- Blizzard: Amount for a single target for all casts of the same spellID by a single source (unit) in a combat session.
  - `unitName`: cstring
  - `unitClassFilename`: cstring
  - `classification`: cstring
  - `isPet`: bool
  - `isMob`: bool
  - `amount`: number
  - `specIconID`: fileID
