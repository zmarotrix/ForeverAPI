# UnitAuras

Namespace: `C_UnitAuras`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_UnitAuras.AddAuraSound](#c_unitaurasaddaurasound) |  |  |
| ❔ | [C_UnitAuras.AddBlockedAura](#c_unitaurasaddblockedaura) |  |  |
| ❔ | [C_UnitAuras.AddPrivateAuraAnchor](#c_unitaurasaddprivateauraanchor) |  |  |
| ❔ | [C_UnitAuras.AuraIsBigDefensive](#c_unitaurasauraisbigdefensive) |  |  |
| ❔ | [C_UnitAuras.AuraIsPrivate](#c_unitaurasauraisprivate) |  |  |
| ❔ | [C_UnitAuras.CancelAuraByInstanceID](#c_unitaurascancelaurabyinstanceid) |  |  |
| ❔ | [C_UnitAuras.ClearBlockedAuras](#c_unitaurasclearblockedauras) |  |  |
| ❔ | [C_UnitAuras.DoesAuraHaveExpirationTime](#c_unitaurasdoesaurahaveexpirationtime) |  |  |
| ❔ | [C_UnitAuras.GetAuraApplicationDisplayCount](#c_unitaurasgetauraapplicationdisplaycount) |  |  |
| ❔ | [C_UnitAuras.GetAuraBaseDuration](#c_unitaurasgetaurabaseduration) |  |  |
| ❔ | [C_UnitAuras.GetAuraCasterGUID](#c_unitaurasgetauracasterguid) |  |  |
| ❔ | [C_UnitAuras.GetAuraDataByAuraInstanceID](#c_unitaurasgetauradatabyaurainstanceid) |  |  |
| ❔ | [C_UnitAuras.GetAuraDataByIndex](#c_unitaurasgetauradatabyindex) |  |  |
| ❔ | [C_UnitAuras.GetAuraDataBySlot](#c_unitaurasgetauradatabyslot) |  |  |
| ❔ | [C_UnitAuras.GetAuraDataBySpellName](#c_unitaurasgetauradatabyspellname) |  |  |
| ❔ | [C_UnitAuras.GetAuraDispelTypeColor](#c_unitaurasgetauradispeltypecolor) |  |  |
| ❔ | [C_UnitAuras.GetAuraDuration](#c_unitaurasgetauraduration) |  |  |
| ❔ | [C_UnitAuras.GetAuraSlots](#c_unitaurasgetauraslots) |  |  |
| ❔ | [C_UnitAuras.GetBuffDataByIndex](#c_unitaurasgetbuffdatabyindex) |  |  |
| ❔ | [C_UnitAuras.GetCooldownAuraBySpellID](#c_unitaurasgetcooldownaurabyspellid) |  |  |
| ❔ | [C_UnitAuras.GetDebuffDataByIndex](#c_unitaurasgetdebuffdatabyindex) |  |  |
| ❔ | [C_UnitAuras.GetGroupBuffVisualAlerts](#c_unitaurasgetgroupbuffvisualalerts) |  |  |
| ❔ | [C_UnitAuras.GetHiddenGroupBuffs](#c_unitaurasgethiddengroupbuffs) |  |  |
| ❔ | [C_UnitAuras.GetPlayerAuraBySpellID](#c_unitaurasgetplayeraurabyspellid) |  |  |
| ❔ | [C_UnitAuras.GetRefreshCarryOverDuration](#c_unitaurasgetrefreshcarryoverduration) |  |  |
| ❔ | [C_UnitAuras.GetRefreshExtendedDuration](#c_unitaurasgetrefreshextendedduration) |  |  |
| ❔ | [C_UnitAuras.GetUnitAuraBySpellID](#c_unitaurasgetunitaurabyspellid) |  |  |
| ❔ | [C_UnitAuras.GetUnitAuraInstanceIDs](#c_unitaurasgetunitaurainstanceids) |  |  |
| ❔ | [C_UnitAuras.GetUnitAuras](#c_unitaurasgetunitauras) |  |  |
| ❔ | [C_UnitAuras.IsAuraFilteredOutByInstanceID](#c_unitaurasisaurafilteredoutbyinstanceid) |  |  |
| ❔ | [C_UnitAuras.RemoveAuraSound](#c_unitaurasremoveaurasound) |  |  |
| ❔ | [C_UnitAuras.RemovePrivateAuraAnchor](#c_unitaurasremoveprivateauraanchor) |  |  |
| ❔ | [C_UnitAuras.ResetAuraDataProvider](#c_unitaurasresetauradataprovider) |  |  |
| ❔ | [C_UnitAuras.SetGroupBuffVisualAlerts](#c_unitaurassetgroupbuffvisualalerts) |  |  |
| ❔ | [C_UnitAuras.SetHiddenGroupBuffs](#c_unitaurassethiddengroupbuffs) |  |  |
| ❔ | [C_UnitAuras.SetPrivateWarningTextAnchor](#c_unitaurassetprivatewarningtextanchor) |  |  |
| ❔ | [C_UnitAuras.SwitchAuraDataProvider](#c_unitaurasswitchauradataprovider) |  |  |
| ❔ | [C_UnitAuras.WantsAlteredForm](#c_unitauraswantsalteredform) |  |  |

### C_UnitAuras.AddAuraSound

`C_UnitAuras.AddAuraSound(trigger: UnitAuraSoundTrigger, sound: UnitAuraSoundInfo) → auraSoundID: number?`

- Status: ❔ unverified
- Blizzard: Registers a sound for an aura event. The sound is stopped after five seconds of playback. The throttleSeconds value must be between 0 and 5 seconds, inclusive.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.AddBlockedAura

`C_UnitAuras.AddBlockedAura(unit: UnitTokenRestrictedForAddOns, auraInstanceID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.AddPrivateAuraAnchor

`C_UnitAuras.AddPrivateAuraAnchor(args: AddPrivateAuraAnchorArgs) → anchorID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.AuraIsBigDefensive

`C_UnitAuras.AuraIsBigDefensive(spellID: SpellIdentifier) → isBigDefensive: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.AuraIsPrivate

`C_UnitAuras.AuraIsPrivate(spellID: SpellIdentifier) → isPrivate: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.CancelAuraByInstanceID

`C_UnitAuras.CancelAuraByInstanceID(unit: UnitTokenRestrictedForAddOns, auraInstanceID: number)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.ClearBlockedAuras

`C_UnitAuras.ClearBlockedAuras(unit: UnitTokenRestrictedForAddOns)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.DoesAuraHaveExpirationTime

`C_UnitAuras.DoesAuraHaveExpirationTime(auraInstanceUnit: UnitToken, auraInstanceID: number) → hasExpirationTime: bool`

- Status: ❔ unverified
- Blizzard: Returns true if an aura instance will expire after a certain amount of time.
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- RequiresValidUnitAuraInstance (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetAuraApplicationDisplayCount

`C_UnitAuras.GetAuraApplicationDisplayCount(auraInstanceUnit: UnitToken, auraInstanceID: number, minDisplayCount: number = 2, maxDisplayCount: number?) → count: string`

- Status: ❔ unverified
- Blizzard: Formats a string for displaying the number of applications an aura has present.
- `minDisplayCount`: Minimum number of applications required; if the application count is below this figure an empty string will be returned.
- `maxDisplayCount`: Maximum number of applications allowed; if the application count is above this figure then the string '*' will be returned.
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- RequiresValidUnitAuraInstance (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetAuraBaseDuration

`C_UnitAuras.GetAuraBaseDuration(auraInstanceUnit: UnitToken, auraInstanceID: number, spellID: SpellIdentifier?) → newDuration: number?`

- Status: ❔ unverified
- Blizzard: Returns the base duration of the given spell (or aura). Takes an optional spellID to use as the new duration if that cannot be derived from the aura, if that value isn't supplied the aura's spellID will be used
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- RequiresValidUnitAuraInstance (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetAuraCasterGUID

`C_UnitAuras.GetAuraCasterGUID(auraInstanceUnit: UnitToken, auraInstanceID: number) → casterGUID: WOWGUID?`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- RequiresValidUnitAuraInstance (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetAuraDataByAuraInstanceID

`C_UnitAuras.GetAuraDataByAuraInstanceID(unit: UnitTokenRestrictedForAddOns, auraInstanceID: number) → aura: AuraData?`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetAuraDataByIndex

`C_UnitAuras.GetAuraDataByIndex(unit: UnitTokenRestrictedForAddOns, index: luaIndex, filter: AuraFilters?) → aura: AuraData?`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetAuraDataBySlot

`C_UnitAuras.GetAuraDataBySlot(unit: UnitTokenRestrictedForAddOns, slot: number) → aura: AuraData?`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetAuraDataBySpellName

`C_UnitAuras.GetAuraDataBySpellName(unit: UnitTokenRestrictedForAddOns, spellName: cstring, filter: AuraFilters?) → aura: AuraData?`

- Status: ❔ unverified
- RequiresNonSecretAura (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetAuraDispelTypeColor

`C_UnitAuras.GetAuraDispelTypeColor(auraInstanceUnit: UnitToken, auraInstanceID: number, curve: LuaColorCurveObject) → dispelTypeColor: colorRGBA`

- Status: ❔ unverified
- Blizzard: Queries the dispel type associated with an aura instance and remaps it to a color via a curve, with the dispel type ID used as the 'x' value.
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- RequiresValidUnitAuraInstance (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenCurveSecret (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetAuraDuration

`C_UnitAuras.GetAuraDuration(auraInstanceUnit: UnitToken, auraInstanceID: number) → duration: LuaDurationObject`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- RequiresValidUnitAuraInstance (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetAuraSlots

`C_UnitAuras.GetAuraSlots(unit: UnitTokenRestrictedForAddOns, filter: AuraFilters?, maxSlots: number?, continuationToken: number?) → outContinuationToken: number?, slots: number`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetBuffDataByIndex

`C_UnitAuras.GetBuffDataByIndex(unit: UnitTokenRestrictedForAddOns, index: luaIndex, filter: AuraFilters?) → aura: AuraData?`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetCooldownAuraBySpellID

`C_UnitAuras.GetCooldownAuraBySpellID(spellID: SpellIdentifier) → cooldownSpellID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetDebuffDataByIndex

`C_UnitAuras.GetDebuffDataByIndex(unit: UnitTokenRestrictedForAddOns, index: luaIndex, filter: AuraFilters?) → aura: AuraData?`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetGroupBuffVisualAlerts

`C_UnitAuras.GetGroupBuffVisualAlerts() → visualAlerts: GroupBuffVisualAlertInfo[]`

- Status: ❔ unverified
- Blizzard: Returns the alerts passed to SetGroupBuffVisualAlerts plus an entry for every linked rank spell of those group buffs.
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetHiddenGroupBuffs

`C_UnitAuras.GetHiddenGroupBuffs() → spellIDs: number[]`

- Status: ❔ unverified
- Blizzard: Returns the spell IDs passed to SetHiddenGroupBuffs plus every linked rank spell of those group buffs.
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetPlayerAuraBySpellID

`C_UnitAuras.GetPlayerAuraBySpellID(spellID: SpellIdentifier) → aura: AuraData?`

- Status: ❔ unverified
- RequiresNonSecretAura (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetRefreshCarryOverDuration

`C_UnitAuras.GetRefreshCarryOverDuration(auraInstanceUnit: UnitToken, auraInstanceID: number, spellID: SpellIdentifier?) → newDuration: number?`

- Status: ❔ unverified
- Blizzard: Returns the client-predicted amount of time that a new spellcast of the same spell would carry over to the new application of that aura. Takes an optional spellID to use as the new duration if that cannot be derived from the aura, if that value isn't supplied the aura's spellID will be used
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- RequiresValidUnitAuraInstance (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetRefreshExtendedDuration

`C_UnitAuras.GetRefreshExtendedDuration(auraInstanceUnit: UnitToken, auraInstanceID: number, spellID: SpellIdentifier?) → newDuration: number?`

- Status: ❔ unverified
- Blizzard: Returns the client-predicted new duration of this aura if it were cast again right now. Takes an optional spellID to use as the new duration if that cannot be derived from the aura, if that value isn't supplied the aura's spellID will be used
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- RequiresValidUnitAuraInstance (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetUnitAuraBySpellID

`C_UnitAuras.GetUnitAuraBySpellID(unit: UnitTokenRestrictedForAddOns, spellID: SpellIdentifier) → aura: AuraData?`

- Status: ❔ unverified
- Blizzard: Returns the first instance of an aura on a unit matching a given spell ID. Returns nil if no such aura is found. Additionally can return nil if querying a unit that is not visible (eg. party members on other maps).
- RequiresNonSecretAura (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- secret while unit auras are restricted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetUnitAuraInstanceIDs

`C_UnitAuras.GetUnitAuraInstanceIDs(unit: UnitTokenRestrictedForAddOns, filter: AuraFilters, maxCount: number?, sortRule: UnitAuraSortRule = Unsorted, sortDirection: UnitAuraSortDirection = Normal) → auraInstanceIDs: number[]`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.GetUnitAuras

`C_UnitAuras.GetUnitAuras(unit: UnitTokenRestrictedForAddOns, filter: AuraFilters, maxCount: number?, sortRule: UnitAuraSortRule = Unsorted, sortDirection: UnitAuraSortDirection = Normal) → auras: AuraData[]`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.IsAuraFilteredOutByInstanceID

`C_UnitAuras.IsAuraFilteredOutByInstanceID(unit: UnitTokenRestrictedForAddOns, auraInstanceID: number, filter: AuraFilters) → isFiltered: bool`

- Status: ❔ unverified
- RequiresUnitAuraAccess (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.RemoveAuraSound

`C_UnitAuras.RemoveAuraSound(auraSoundID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.RemovePrivateAuraAnchor

`C_UnitAuras.RemovePrivateAuraAnchor(anchorID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.ResetAuraDataProvider

`C_UnitAuras.ResetAuraDataProvider()`

- Status: ❔ unverified
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.SetGroupBuffVisualAlerts

`C_UnitAuras.SetGroupBuffVisualAlerts(visualAlerts: GroupBuffVisualAlertInfo[])`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.SetHiddenGroupBuffs

`C_UnitAuras.SetHiddenGroupBuffs(spellIDs: number[])`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.SetPrivateWarningTextAnchor

`C_UnitAuras.SetPrivateWarningTextAnchor(parent: SimpleFrame, anchor: AnchorBinding?)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.SwitchAuraDataProvider

`C_UnitAuras.SwitchAuraDataProvider()`

- Status: ❔ unverified
- Source: client docs `UnitAuraDocumentation.lua`

### C_UnitAuras.WantsAlteredForm

`C_UnitAuras.WantsAlteredForm(unit: UnitToken) → wantsAlteredForm: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UnitAuraDocumentation.lua`

## Events

### AURA_DATA_PROVIDER_SWITCH

- Status: ❔ unverified
- Payload: `useRealDataProvider: bool`
- fires synchronously (Blizzard's docs)

### GROUP_BUFF_VISUAL_ALERTS_CHANGED

- Status: ❔ unverified
- Payload: `visualAlerts: GroupBuffVisualAlertInfo[]`
- Blizzard: The payload matches GetGroupBuffVisualAlerts, including linked rank spells.
- fires synchronously (Blizzard's docs)

### HIDDEN_GROUP_BUFFS_CHANGED

- Status: ❔ unverified
- Payload: `spellIDs: number[]`
- Blizzard: The payload matches GetHiddenGroupBuffs, including linked rank spells.
- fires synchronously (Blizzard's docs)

### UNIT_AURA

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`, `updateInfo: UnitAuraUpdateInfo`
- SecretWhenAurasRestricted (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### UNIT_AURA_BLOCKED

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`, `auraInstanceID: number`
- fires synchronously (Blizzard's docs)

### UNIT_AURA_BLOCK_LIST_CLEARED

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`
- fires synchronously (Blizzard's docs)
