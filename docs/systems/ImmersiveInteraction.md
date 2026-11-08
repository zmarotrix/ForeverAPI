# ImmersiveInteraction

Namespace: `C_ImmersiveInteraction`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ImmersiveInteraction.HasImmersiveInteraction](#c_immersiveinteractionhasimmersiveinteraction) | 1 value | 1 value |

### C_ImmersiveInteraction.HasImmersiveInteraction

`C_ImmersiveInteraction.HasImmersiveInteraction() → immersiveInteraction: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ImmersiveInteractionManagerDocumentation.lua`

## Events

### IMMERSIVE_INTERACTION_BEGIN

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### IMMERSIVE_INTERACTION_END

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
