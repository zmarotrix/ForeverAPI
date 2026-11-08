# DeathRecap

Namespace: `C_DeathRecap`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_DeathRecap.GetRecapEvents](#c_deathrecapgetrecapevents) |  |  |
| ✅ | [C_DeathRecap.GetRecapLink](#c_deathrecapgetrecaplink) |  |  |
| ✅ | [C_DeathRecap.GetRecapMaxHealth](#c_deathrecapgetrecapmaxhealth) |  |  |
| ✅ | [C_DeathRecap.HasRecapEvents](#c_deathrecaphasrecapevents) |  |  |

### C_DeathRecap.GetRecapEvents

`C_DeathRecap.GetRecapEvents(recapID: number?) → events: DeathRecapEventInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathRecapDocumentation.lua`

### C_DeathRecap.GetRecapLink

`C_DeathRecap.GetRecapLink(recapID: number?) → link: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathRecapDocumentation.lua`

### C_DeathRecap.GetRecapMaxHealth

`C_DeathRecap.GetRecapMaxHealth(recapID: number?) → maxHealth: number`

- Status: ✅ verified (function)
- Blizzard: Returns the max health for the unit that died in the provided death recap.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathRecapDocumentation.lua`

### C_DeathRecap.HasRecapEvents

`C_DeathRecap.HasRecapEvents(recapID: number?) → hasEvents: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathRecapDocumentation.lua`

## Types

### DeathRecapEventInfo

- Structure
