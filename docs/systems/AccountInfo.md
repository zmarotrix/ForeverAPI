# AccountInfo

Namespace: `C_AccountInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AccountInfo.GetIDFromBattleNetAccountGUID](#c_accountinfogetidfrombattlenetaccountguid) |  |  |
| ✅ | [C_AccountInfo.IsGUIDBattleNetAccountType](#c_accountinfoisguidbattlenetaccounttype) |  |  |
| ✅ | [C_AccountInfo.IsGUIDRelatedToLocalAccount](#c_accountinfoisguidrelatedtolocalaccount) |  |  |

### C_AccountInfo.GetIDFromBattleNetAccountGUID

`C_AccountInfo.GetIDFromBattleNetAccountGUID(battleNetAccountGUID: WOWGUID) → battleNetAccountID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountInfoDocumentation.lua`

### C_AccountInfo.IsGUIDBattleNetAccountType

`C_AccountInfo.IsGUIDBattleNetAccountType(guid: WOWGUID) → isBNet: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountInfoDocumentation.lua`

### C_AccountInfo.IsGUIDRelatedToLocalAccount

`C_AccountInfo.IsGUIDRelatedToLocalAccount(guid: WOWGUID) → isLocalUser: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AccountInfoDocumentation.lua`
