# CovenantCallings

Namespace: `C_CovenantCallings`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_CovenantCallings.AreCallingsUnlocked](#c_covenantcallingsarecallingsunlocked) | 1 value | 1 value |
| ✅ | [C_CovenantCallings.RequestCallings](#c_covenantcallingsrequestcallings) |  |  |

### C_CovenantCallings.AreCallingsUnlocked

`C_CovenantCallings.AreCallingsUnlocked() → unlocked: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CovenantCallingsDocumentation.lua`

### C_CovenantCallings.RequestCallings

`C_CovenantCallings.RequestCallings()`

- Status: ✅ verified (function)
- Source: client docs `CovenantCallingsDocumentation.lua`

## Events

### COVENANT_CALLINGS_UPDATED

- Status: ✅ verified
- Payload: `callings: BountyInfo[]`
- fires synchronously (Blizzard's docs)
- Seen firing 5 times (0 in combat); argument kinds: `t`
