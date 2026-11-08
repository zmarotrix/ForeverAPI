# AccountInfo

Namespace: `C_AccountInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AccountInfo.GetIDFromBattleNetAccountGUID](#c_accountinfogetidfrombattlenetaccountguid) | 1 value | 1 value |
| ✅ | [C_AccountInfo.IsGUIDBattleNetAccountType](#c_accountinfoisguidbattlenetaccounttype) | 1 value | 1 value |
| ✅ | [C_AccountInfo.IsGUIDRelatedToLocalAccount](#c_accountinfoisguidrelatedtolocalaccount) | 1 value | 1 value |

### C_AccountInfo.GetIDFromBattleNetAccountGUID

`C_AccountInfo.GetIDFromBattleNetAccountGUID(battleNetAccountGUID: WOWGUID) → battleNetAccountID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `AccountInfoDocumentation.lua`

### C_AccountInfo.IsGUIDBattleNetAccountType

`C_AccountInfo.IsGUIDBattleNetAccountType(guid: WOWGUID) → isBNet: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `AccountInfoDocumentation.lua`

### C_AccountInfo.IsGUIDRelatedToLocalAccount

`C_AccountInfo.IsGUIDRelatedToLocalAccount(guid: WOWGUID) → isLocalUser: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `AccountInfoDocumentation.lua`
