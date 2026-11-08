# DeathRecap

Namespace: `C_DeathRecap`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_DeathRecap.GetRecapEvents](#c_deathrecapgetrecapevents) | 0 values |  |
| ✅ | [C_DeathRecap.GetRecapLink](#c_deathrecapgetrecaplink) | 1 value |  |
| ✅ | [C_DeathRecap.GetRecapMaxHealth](#c_deathrecapgetrecapmaxhealth) | 1 value |  |
| ✅ | [C_DeathRecap.HasRecapEvents](#c_deathrecaphasrecapevents) | 1 value |  |

### C_DeathRecap.GetRecapEvents

`C_DeathRecap.GetRecapEvents(recapID: number?) → events: DeathRecapEventInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `DeathRecapDocumentation.lua`

### C_DeathRecap.GetRecapLink

`C_DeathRecap.GetRecapLink(recapID: number?) → link: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `string`
- Source: client docs `DeathRecapDocumentation.lua`

### C_DeathRecap.GetRecapMaxHealth

`C_DeathRecap.GetRecapMaxHealth(recapID: number?) → maxHealth: number`

- Status: ✅ verified (function)
- Blizzard: Returns the max health for the unit that died in the provided death recap.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Source: client docs `DeathRecapDocumentation.lua`

### C_DeathRecap.HasRecapEvents

`C_DeathRecap.HasRecapEvents(recapID: number?) → hasEvents: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `DeathRecapDocumentation.lua`

## Types

### DeathRecapEventInfo

- Structure
