# SecretUtil

Namespace: `C_Secrets`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Secrets.CanCompareUnitTokens](#c_secretscancompareunittokens) |  |  |
| ✅ | [C_Secrets.GetPowerTypeSecrecy](#c_secretsgetpowertypesecrecy) |  |  |
| ✅ | [C_Secrets.GetSpellAuraSecrecy](#c_secretsgetspellaurasecrecy) |  |  |
| ✅ | [C_Secrets.GetSpellCastSecrecy](#c_secretsgetspellcastsecrecy) |  |  |
| ✅ | [C_Secrets.GetSpellCooldownSecrecy](#c_secretsgetspellcooldownsecrecy) |  |  |
| ✅ | [C_Secrets.HasSecretRestrictions](#c_secretshassecretrestrictions) |  |  |
| ✅ | [C_Secrets.ShouldActionCooldownBeSecret](#c_secretsshouldactioncooldownbesecret) |  |  |
| ✅ | [C_Secrets.ShouldAurasBeSecret](#c_secretsshouldaurasbesecret) |  |  |
| ✅ | [C_Secrets.ShouldCooldownsBeSecret](#c_secretsshouldcooldownsbesecret) |  |  |
| ✅ | [C_Secrets.ShouldSpellAuraBeSecret](#c_secretsshouldspellaurabesecret) |  |  |
| ✅ | [C_Secrets.ShouldSpellBookItemCooldownBeSecret](#c_secretsshouldspellbookitemcooldownbesecret) |  |  |
| ✅ | [C_Secrets.ShouldSpellCooldownBeSecret](#c_secretsshouldspellcooldownbesecret) |  |  |
| ✅ | [C_Secrets.ShouldTotemSlotBeSecret](#c_secretsshouldtotemslotbesecret) |  |  |
| ✅ | [C_Secrets.ShouldTotemSpellBeSecret](#c_secretsshouldtotemspellbesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitAuraIndexBeSecret](#c_secretsshouldunitauraindexbesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitAuraInstanceBeSecret](#c_secretsshouldunitaurainstancebesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitAuraSlotBeSecret](#c_secretsshouldunitauraslotbesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitComparisonBeSecret](#c_secretsshouldunitcomparisonbesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitHealthMaxBeSecret](#c_secretsshouldunithealthmaxbesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitIdentityBeSecret](#c_secretsshouldunitidentitybesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitPowerBeSecret](#c_secretsshouldunitpowerbesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitPowerMaxBeSecret](#c_secretsshouldunitpowermaxbesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitSpellCastBeSecret](#c_secretsshouldunitspellcastbesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitSpellCastingBeSecret](#c_secretsshouldunitspellcastingbesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitStatsBeSecret](#c_secretsshouldunitstatsbesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitThreatStateBeSecret](#c_secretsshouldunitthreatstatebesecret) |  |  |
| ✅ | [C_Secrets.ShouldUnitThreatValuesBeSecret](#c_secretsshouldunitthreatvaluesbesecret) |  |  |

### C_Secrets.CanCompareUnitTokens

`C_Secrets.CanCompareUnitTokens(unit1: UnitToken, unit2: UnitToken) → isUnitComparisonPermitted: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries to compare two input unit tokens are permitted. If this returns false, APIs guarded by the RequiresComparableUnitTokens predicate will fail.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.GetPowerTypeSecrecy

`C_Secrets.GetPowerTypeSecrecy(powerType: PowerType) → secrecy: SecrecyLevel`

- Status: ✅ verified (function)
- Blizzard: Queries the base secrecy for a power type.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.GetSpellAuraSecrecy

`C_Secrets.GetSpellAuraSecrecy(spellIdentifier: SpellIdentifier) → secrecy: SecrecyLevel`

- Status: ✅ verified (function)
- Blizzard: Queries the base secrecy for a spell if queried as an aura.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.GetSpellCastSecrecy

`C_Secrets.GetSpellCastSecrecy(spellIdentifier: SpellIdentifier) → secrecy: SecrecyLevel`

- Status: ✅ verified (function)
- Blizzard: Queries the base secrecy for a spell if queried as a cast.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.GetSpellCooldownSecrecy

`C_Secrets.GetSpellCooldownSecrecy(spellIdentifier: SpellIdentifier) → secrecy: SecrecyLevel`

- Status: ✅ verified (function)
- Blizzard: Queries the base secrecy for a spell if queried as a cooldown.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.HasSecretRestrictions

`C_Secrets.HasSecretRestrictions() → hasSecretRestrictions: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if this client build has secret value restrictions enabled. If false, all APIs that are tagged as potentially returning secrets will never do so.
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldActionCooldownBeSecret

`C_Secrets.ShouldActionCooldownBeSecret(actionID: luaIndex) → isCooldownSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a given action bar slot ID will produce secret values for cooldowns if queried.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldAurasBeSecret

`C_Secrets.ShouldAurasBeSecret() → hasSecretAuras: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for aura data will generally produce secret values.
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldCooldownsBeSecret

`C_Secrets.ShouldCooldownsBeSecret() → hasSecretCooldowns: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for cooldown data will generally produce secret values.
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldSpellAuraBeSecret

`C_Secrets.ShouldSpellAuraBeSecret(spellIdentifier: SpellIdentifier) → isAuraSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a given spell identifier would, if applied as an aura, produce secret values when queried.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldSpellBookItemCooldownBeSecret

`C_Secrets.ShouldSpellBookItemCooldownBeSecret(spellBookItemSlotIndex: luaIndex, spellBookItemSpellBank: SpellBookSpellBank) → isCooldownSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a given spellbook item will produce secret values for cooldowns if queried.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldSpellCooldownBeSecret

`C_Secrets.ShouldSpellCooldownBeSecret(spellIdentifier: SpellIdentifier) → isCooldownSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a given spell identifier will produce secret values for cooldowns if queried.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldTotemSlotBeSecret

`C_Secrets.ShouldTotemSlotBeSecret(slot: luaIndex) → isTotemSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if information about a totem slot will produce secret values if queried.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldTotemSpellBeSecret

`C_Secrets.ShouldTotemSpellBeSecret(spellID: number) → isTotemSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if information about a spell when associated with a totem slot will produce secret values if queried.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitAuraIndexBeSecret

`C_Secrets.ShouldUnitAuraIndexBeSecret(unit: UnitToken, index: luaIndex, filter: AuraFilters?) → isAuraSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a given aura index will produce secret values if queried.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitAuraInstanceBeSecret

`C_Secrets.ShouldUnitAuraInstanceBeSecret(unit: UnitToken, auraInstanceID: number) → isAuraSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a given aura instance ID will produce secret values if queried.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitAuraSlotBeSecret

`C_Secrets.ShouldUnitAuraSlotBeSecret(unit: UnitToken, slot: number) → isAuraSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a given aura slot ID will produce secret values if queried.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitComparisonBeSecret

`C_Secrets.ShouldUnitComparisonBeSecret(unit1: UnitToken, unit2: UnitToken) → isUnitComparisonSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries that compare units will produce secret values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitHealthMaxBeSecret

`C_Secrets.ShouldUnitHealthMaxBeSecret(unit: UnitToken) → isUnitHealthMaxSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for maximum unit health will produce secret values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitIdentityBeSecret

`C_Secrets.ShouldUnitIdentityBeSecret(unit: UnitToken) → isUnitIdentitySecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for unit identity (such as name or GUID) will produce secret values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitPowerBeSecret

`C_Secrets.ShouldUnitPowerBeSecret(unit: UnitToken, powerType: PowerType?) → isUnitPowerSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for unit power will produce secret values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitPowerMaxBeSecret

`C_Secrets.ShouldUnitPowerMaxBeSecret(unit: UnitToken, powerType: PowerType?) → isUnitPowerMaxSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for maximum unit power will produce secret values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitSpellCastBeSecret

`C_Secrets.ShouldUnitSpellCastBeSecret(unit: UnitToken, spellIdentifier: SpellIdentifier) → isSpellCastSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for spell casting information for a unit would produce secret values when queried.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitSpellCastingBeSecret

`C_Secrets.ShouldUnitSpellCastingBeSecret(unit: UnitToken) → isSpellCastingSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for spell casting information for a specific unit will generally produce secret values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitStatsBeSecret

`C_Secrets.ShouldUnitStatsBeSecret() → hasSecretStats: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for unit statistics will produce secret values.
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitThreatStateBeSecret

`C_Secrets.ShouldUnitThreatStateBeSecret(unit: UnitToken, mobUnit: UnitToken?) → isUnitThreatSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for unit threat status will produce secret values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`

### C_Secrets.ShouldUnitThreatValuesBeSecret

`C_Secrets.ShouldUnitThreatValuesBeSecret(unit: UnitToken, mobUnit: UnitToken) → isUnitThreatSecret: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if queries for unit threat values will produce secret values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SecretPredicateAPIDocumentation.lua`
