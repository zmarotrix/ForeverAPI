# LossOfControl

Namespace: `C_LossOfControl`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_LossOfControl.GetActiveLossOfControlData](#c_lossofcontrolgetactivelossofcontroldata) |  |  |
| ❔ | [C_LossOfControl.GetActiveLossOfControlDataByUnit](#c_lossofcontrolgetactivelossofcontroldatabyunit) |  |  |
| ❔ | [C_LossOfControl.GetActiveLossOfControlDataCount](#c_lossofcontrolgetactivelossofcontroldatacount) |  |  |
| ❔ | [C_LossOfControl.GetActiveLossOfControlDataCountByUnit](#c_lossofcontrolgetactivelossofcontroldatacountbyunit) |  |  |
| ❔ | [C_LossOfControl.GetActiveLossOfControlDuration](#c_lossofcontrolgetactivelossofcontrolduration) |  |  |

### C_LossOfControl.GetActiveLossOfControlData

`C_LossOfControl.GetActiveLossOfControlData(index: luaIndex) → event: LossOfControlData?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenLossOfControlRestricted (Blizzard's docs; not checked in game)
- Source: client docs `LossOfControlDocumentation.lua`

### C_LossOfControl.GetActiveLossOfControlDataByUnit

`C_LossOfControl.GetActiveLossOfControlDataByUnit(unitToken: UnitToken, index: luaIndex) → event: LossOfControlData?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenLossOfControlRestricted (Blizzard's docs; not checked in game)
- Source: client docs `LossOfControlDocumentation.lua`

### C_LossOfControl.GetActiveLossOfControlDataCount

`C_LossOfControl.GetActiveLossOfControlDataCount() → count: number`

- Status: ❔ unverified
- Source: client docs `LossOfControlDocumentation.lua`

### C_LossOfControl.GetActiveLossOfControlDataCountByUnit

`C_LossOfControl.GetActiveLossOfControlDataCountByUnit(unitToken: UnitToken) → count: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LossOfControlDocumentation.lua`

### C_LossOfControl.GetActiveLossOfControlDuration

`C_LossOfControl.GetActiveLossOfControlDuration(unitToken: UnitToken, index: luaIndex) → duration: LuaDurationObject?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LossOfControlDocumentation.lua`

## Events

### LOSS_OF_CONTROL_ADDED

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`, `effectIndex: luaIndex`
- fires synchronously (Blizzard's docs)

### LOSS_OF_CONTROL_COMMENTATOR_ADDED

- Status: ❔ unverified
- Payload: `victim: WOWGUID`, `effectIndex: luaIndex`
- fires synchronously (Blizzard's docs)

### LOSS_OF_CONTROL_COMMENTATOR_UPDATE

- Status: ❔ unverified
- Payload: `victim: WOWGUID`
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### LOSS_OF_CONTROL_UPDATE

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### PLAYER_CONTROL_GAINED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_CONTROL_LOST

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### LossOfControlData

- Structure
  - `locType`: cstring
  - `spellID`: number
  - `displayText`: cstring
  - `iconTexture`: number
  - `startTime`: number?
  - `timeRemaining`: number?
  - `duration`: number?
  - `lockoutSchool`: number
  - `priority`: number
  - `displayType`: number
  - `auraInstanceID`: number?
