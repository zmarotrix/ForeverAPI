# Trainer

Namespace: `C_Trainer`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Trainer.GetCategorizeTrainerUI](#c_trainergetcategorizetrainerui) | 1 value | 1 value |
| ✅ | [C_Trainer.GetTrainerType](#c_trainergettrainertype) | 1 value | 1 value |
| ✅ | [C_Trainer.SetCategorizeTrainerUI](#c_trainersetcategorizetrainerui) |  |  |

### C_Trainer.GetCategorizeTrainerUI

`C_Trainer.GetCategorizeTrainerUI() → value: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `TrainerDocumentation.lua`

### C_Trainer.GetTrainerType

`C_Trainer.GetTrainerType() → trainerType: TrainerType`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `TrainerDocumentation.lua`

### C_Trainer.SetCategorizeTrainerUI

`C_Trainer.SetCategorizeTrainerUI(value: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TrainerDocumentation.lua`

## Events

### TRAINER_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRAINER_DESCRIPTION_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRAINER_SERVICE_INFO_NAME_UPDATE

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### TRAINER_SHOW

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRAINER_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
