# PlayerInteractionManager

Namespace: `C_PlayerInteractionManager`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PlayerInteractionManager.ClearInteraction](#c_playerinteractionmanagerclearinteraction) |  |  |
| ✅ | [C_PlayerInteractionManager.ConfirmationInteraction](#c_playerinteractionmanagerconfirmationinteraction) |  |  |
| ✅ | [C_PlayerInteractionManager.InteractUnit](#c_playerinteractionmanagerinteractunit) |  |  |
| ✅ | [C_PlayerInteractionManager.IsInteractingWithNpcOfType](#c_playerinteractionmanagerisinteractingwithnpcoftype) |  |  |
| ✅ | [C_PlayerInteractionManager.IsReplacingUnit](#c_playerinteractionmanagerisreplacingunit) | 1 value | 1 value |
| ✅ | [C_PlayerInteractionManager.IsValidNPCInteraction](#c_playerinteractionmanagerisvalidnpcinteraction) |  |  |
| ✅ | [C_PlayerInteractionManager.ReopenInteraction](#c_playerinteractionmanagerreopeninteraction) |  |  |
| ✅ | [C_PlayerInteractionManager.ShardTransferConfirm](#c_playerinteractionmanagershardtransferconfirm) |  |  |

### C_PlayerInteractionManager.ClearInteraction

`C_PlayerInteractionManager.ClearInteraction(type: PlayerInteractionType?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInteractionManagerDocumentation.lua`

### C_PlayerInteractionManager.ConfirmationInteraction

`C_PlayerInteractionManager.ConfirmationInteraction(type: PlayerInteractionType?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInteractionManagerDocumentation.lua`

### C_PlayerInteractionManager.InteractUnit

`C_PlayerInteractionManager.InteractUnit(unit: string, exactMatch: bool = False, looseTargeting: bool = True) → success: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInteractionManagerDocumentation.lua`

### C_PlayerInteractionManager.IsInteractingWithNpcOfType

`C_PlayerInteractionManager.IsInteractingWithNpcOfType(type: PlayerInteractionType) → interacting: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInteractionManagerDocumentation.lua`

### C_PlayerInteractionManager.IsReplacingUnit

`C_PlayerInteractionManager.IsReplacingUnit() → replacing: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInteractionManagerDocumentation.lua`

### C_PlayerInteractionManager.IsValidNPCInteraction

`C_PlayerInteractionManager.IsValidNPCInteraction(type: PlayerInteractionType) → isValidInteraction: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInteractionManagerDocumentation.lua`

### C_PlayerInteractionManager.ReopenInteraction

`C_PlayerInteractionManager.ReopenInteraction()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInteractionManagerDocumentation.lua`

### C_PlayerInteractionManager.ShardTransferConfirm

`C_PlayerInteractionManager.ShardTransferConfirm()`

- Status: ✅ verified (function)
- Source: client docs `PlayerInteractionManagerDocumentation.lua`

## Events

### PLAYER_INTERACTION_MANAGER_FRAME_HIDE

- Status: ✅ verified
- Payload: `type: PlayerInteractionType`
- fires synchronously (Blizzard's docs)

### PLAYER_INTERACTION_MANAGER_FRAME_SHOW

- Status: ✅ verified
- Payload: `type: PlayerInteractionType`
- fires synchronously (Blizzard's docs)
