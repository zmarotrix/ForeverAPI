# PartyInfoSystemStatus

Namespace: `C_PartyInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PartyInfo.IsRaidListEnabled](#c_partyinfoisraidlistenabled) | 1 value | 1 value |
| ✅ | [C_PartyInfo.IsRaidListSupported](#c_partyinfoisraidlistsupported) | 1 value | 1 value |

### C_PartyInfo.IsRaidListEnabled

`C_PartyInfo.IsRaidListEnabled() → isRaidListEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PartyInfoSystemStatusDocumentation.lua`

### C_PartyInfo.IsRaidListSupported

`C_PartyInfo.IsRaidListSupported() → isRaidListSupported: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PartyInfoSystemStatusDocumentation.lua`

## Events

### SOCIAL_UI_RAID_LIST_SYSTEM_STATUS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
