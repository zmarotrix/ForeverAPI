# SummonInfo

Namespace: `C_SummonInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SummonInfo.CancelSummon](#c_summoninfocancelsummon) | 0 values |  |
| ✅ | [C_SummonInfo.ConfirmSummon](#c_summoninfoconfirmsummon) |  |  |
| ✅ | [C_SummonInfo.GetSummonConfirmAreaName](#c_summoninfogetsummonconfirmareaname) | 1 value |  |
| ✅ | [C_SummonInfo.GetSummonConfirmSummoner](#c_summoninfogetsummonconfirmsummoner) | 1 value |  |
| ✅ | [C_SummonInfo.GetSummonConfirmTimeLeft](#c_summoninfogetsummonconfirmtimeleft) | 1 value |  |
| ✅ | [C_SummonInfo.GetSummonReason](#c_summoninfogetsummonreason) | 1 value |  |
| ✅ | [C_SummonInfo.IsSummonSkippingStartExperience](#c_summoninfoissummonskippingstartexperience) | 1 value |  |

### C_SummonInfo.CancelSummon

`C_SummonInfo.CancelSummon()`

- Status: ✅ verified (function)
- Called out of combat: returned 0 values
- Source: client docs `SummonInfoDocumentation.lua`

### C_SummonInfo.ConfirmSummon

`C_SummonInfo.ConfirmSummon()`

- Status: ✅ verified (function)
- Source: client docs `SummonInfoDocumentation.lua`

### C_SummonInfo.GetSummonConfirmAreaName

`C_SummonInfo.GetSummonConfirmAreaName() → areaName: string`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Source: client docs `SummonInfoDocumentation.lua`

### C_SummonInfo.GetSummonConfirmSummoner

`C_SummonInfo.GetSummonConfirmSummoner() → summoner: string?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Source: client docs `SummonInfoDocumentation.lua`

### C_SummonInfo.GetSummonConfirmTimeLeft

`C_SummonInfo.GetSummonConfirmTimeLeft() → timeLeft: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `SummonInfoDocumentation.lua`

### C_SummonInfo.GetSummonReason

`C_SummonInfo.GetSummonReason() → summonReason: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `SummonInfoDocumentation.lua`

### C_SummonInfo.IsSummonSkippingStartExperience

`C_SummonInfo.IsSummonSkippingStartExperience() → isSummonSkippingStartExperience: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `SummonInfoDocumentation.lua`
