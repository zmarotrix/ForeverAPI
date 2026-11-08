# PlayerScript

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [AcceptAreaSpiritHeal](#acceptareaspiritheal) |  |  |
| ✅ | [AcceptGuild](#acceptguild) |  |  |
| ✅ | [AcceptResurrect](#acceptresurrect) |  |  |
| ✅ | [Ambiguate](#ambiguate) |  |  |
| ✅ | [AutoEquipCursorItem](#autoequipcursoritem) |  |  |
| ✅ | [BeginTrade](#begintrade) |  |  |
| ✅ | [CanDualWield](#candualwield) | 1 value | 1 value |
| ✅ | [CanInspect](#caninspect) | 1 value | 1 value |
| ✅ | [CanLootUnit](#canlootunit) | 2 values | 2 values |
| ✅ | [CanPortGraveyard](#canportgraveyard) | 1 value | 1 value |
| ✅ | [CancelAreaSpiritHeal](#cancelareaspiritheal) |  |  |
| ✅ | [CancelPendingEquip](#cancelpendingequip) |  |  |
| ✅ | [CancelTrade](#canceltrade) |  |  |
| ✅ | [CheckInteractDistance](#checkinteractdistance) |  |  |
| ✅ | [CheckTalentMasterDist](#checktalentmasterdist) |  |  |
| ✅ | [ClearPendingBindConversionItem](#clearpendingbindconversionitem) |  |  |
| ✅ | [ConfirmTalentWipe](#confirmtalentwipe) |  |  |
| ✅ | [ConvertItemToBindToAccount](#convertitemtobindtoaccount) |  |  |
| ✅ | [DeclineGuild](#declineguild) |  |  |
| ✅ | [DeclineResurrect](#declineresurrect) |  |  |
| ✅ | [Dismount](#dismount) |  |  |
| ✅ | [EquipPendingItem](#equippendingitem) |  |  |
| ✅ | [FollowUnit](#followunit) |  |  |
| ✅ | [GetAllowLowLevelRaid](#getallowlowlevelraid) | 1 value | 1 value |
| ✅ | [GetAllowRecentAlliesSeeLocation](#getallowrecentalliesseelocation) | 1 value | 1 value |
| ✅ | [GetAreaSpiritHealerTime](#getareaspirithealertime) | 1 value | 1 value |
| ✅ | [GetArmorPenetration](#getarmorpenetration) | 1 value | secret |
| ✅ | [GetAttackPowerForStat](#getattackpowerforstat) |  |  |
| ✅ | [GetAutoDeclineGuildInvites](#getautodeclineguildinvites) | 1 value | 1 value |
| ✅ | [GetAutoDeclineNeighborhoodInvites](#getautodeclineneighborhoodinvites) | 1 value | 1 value |
| ✅ | [GetAvoidance](#getavoidance) | 1 value | secret |
| ✅ | [GetBindLocation](#getbindlocation) | 1 value | 1 value |
| ✅ | [GetBlockChance](#getblockchance) | 1 value | secret |
| ✅ | [GetCemeteryPreference](#getcemeterypreference) | 1 value | 1 value |
| ✅ | [GetCollapsingStarCost](#getcollapsingstarcost) | 1 value | 1 value |
| ✅ | [GetCombatRating](#getcombatrating) | 1 value | secret |
| ✅ | [GetCombatRatingBonus](#getcombatratingbonus) | 1 value | secret |
| ✅ | [GetCombatRatingBonusForCombatRatingValue](#getcombatratingbonusforcombatratingvalue) |  |  |
| ✅ | [GetCorpseRecoveryDelay](#getcorpserecoverydelay) | 1 value | 1 value |
| ✅ | [GetCorruption](#getcorruption) | 1 value | 1 value |
| ✅ | [GetCorruptionResistance](#getcorruptionresistance) | 1 value | 1 value |
| ✅ | [GetCritChance](#getcritchance) | 1 value | secret |
| ✅ | [GetCritChanceFromStat](#getcritchancefromstat) |  |  |
| ✅ | [GetCritChanceProvidesParryEffect](#getcritchanceprovidesparryeffect) | 1 value | 1 value |
| ✅ | [GetDodgeChance](#getdodgechance) | 1 value | secret |
| ✅ | [GetDodgeChanceFromAttribute](#getdodgechancefromattribute) | 1 value | secret |
| ✅ | [GetEvictionTimeRemaining](#getevictiontimeremaining) | 1 value | 1 value |
| ✅ | [GetExpertise](#getexpertise) | 3 values | secret |
| ✅ | [GetExpertisePercent](#getexpertisepercent) | 3 values | secret |
| ✅ | [GetGlancingBlowChance](#getglancingblowchance) |  |  |
| ✅ | [GetGlancingBlowPenalty](#getglancingblowpenalty) |  |  |
| ✅ | [GetHaste](#gethaste) | 1 value | secret |
| ✅ | [GetHealthRegen](#gethealthregen) | 2 values | 2 values |
| ✅ | [GetHealthRegenFromSpirit](#gethealthregenfromspirit) | 2 values | 2 values |
| ✅ | [GetHitModifier](#gethitmodifier) | 1 value | secret |
| ✅ | [GetJailersTowerLevel](#getjailerstowerlevel) | 1 value | 1 value |
| ✅ | [GetLifesteal](#getlifesteal) | 1 value | secret |
| ✅ | [GetLootSpecialization](#getlootspecialization) | 1 value | 1 value |
| ✅ | [GetManaRegen](#getmanaregen) | 2 values | secret |
| ✅ | [GetManaRegenFromSpirit](#getmanaregenfromspirit) | 2 values | 2 values |
| ✅ | [GetMastery](#getmastery) | 1 value | secret |
| ✅ | [GetMasteryEffect](#getmasteryeffect) | 2 values | secret |
| ✅ | [GetMaxPlayerLevel](#getmaxplayerlevel) | 1 value | 1 value |
| ✅ | [GetMeleeHaste](#getmeleehaste) | 1 value | secret |
| ✅ | [GetModResilienceDamageReduction](#getmodresiliencedamagereduction) | 1 value | secret |
| ✅ | [GetMoney](#getmoney) | 1 value | 1 value |
| ✅ | [GetNormalizedRealmName](#getnormalizedrealmname) | 1 value | 1 value |
| ✅ | [GetOffhandHitModifier](#getoffhandhitmodifier) | 1 value | secret |
| ✅ | [GetOverrideAPBySpellPower](#getoverrideapbyspellpower) | 1 value | secret |
| ✅ | [GetOverrideSpellPowerByAP](#getoverridespellpowerbyap) | 1 value | secret |
| ✅ | [GetPVPDesired](#getpvpdesired) | 1 value | 1 value |
| ✅ | [GetPVPGearStatRules](#getpvpgearstatrules) | 1 value | 1 value |
| ✅ | [GetPVPLifetimeStats](#getpvplifetimestats) | 2 values | 2 values |
| ✅ | [GetPVPSessionStats](#getpvpsessionstats) | 2 values | 2 values |
| ✅ | [GetPVPTimer](#getpvptimer) | 1 value | 1 value |
| ✅ | [GetPVPYesterdayStats](#getpvpyesterdaystats) | 2 values | 2 values |
| ✅ | [GetParryChance](#getparrychance) | 1 value | secret |
| ✅ | [GetParryChanceFromAttribute](#getparrychancefromattribute) | 1 value | secret |
| ✅ | [GetPetCritChance](#getpetcritchance) | 2 values | secret |
| ✅ | [GetPetDodgeChance](#getpetdodgechance) | 1 value | secret |
| ✅ | [GetPetHitChanceModifier](#getpethitchancemodifier) | 1 value | secret |
| ✅ | [GetPetMeleeHaste](#getpetmeleehaste) | 1 value | secret |
| ✅ | [GetPetSpellBonusDamage](#getpetspellbonusdamage) | 1 value | secret |
| ✅ | [GetPetSpellHitChanceModifier](#getpetspellhitchancemodifier) | 1 value | secret |
| ✅ | [GetPlayerFacing](#getplayerfacing) | 1 value | 1 value |
| ✅ | [GetPlayerInfoByGUID](#getplayerinfobyguid) | 8 values | 8 values |
| ✅ | [GetPowerRegen](#getpowerregen) | 2 values | secret |
| ✅ | [GetPowerRegenForPowerType](#getpowerregenforpowertype) |  |  |
| ✅ | [GetPvpPowerDamage](#getpvppowerdamage) | 1 value | secret |
| ✅ | [GetPvpPowerHealing](#getpvppowerhealing) | 1 value | secret |
| ✅ | [GetRangedAttackPowerForStat](#getrangedattackpowerforstat) |  |  |
| ✅ | [GetRangedCritChance](#getrangedcritchance) | 1 value | secret |
| ✅ | [GetRangedHaste](#getrangedhaste) | 2 values | secret |
| ✅ | [GetRangedHitModifier](#getrangedhitmodifier) | 1 value | secret |
| ✅ | [GetReleaseTimeRemaining](#getreleasetimeremaining) | 1 value | 1 value |
| ✅ | [GetResSicknessDuration](#getressicknessduration) | 1 value | 1 value |
| ✅ | [GetRestState](#getreststate) | 3 values | 3 values |
| ✅ | [GetRestrictedAccountData](#getrestrictedaccountdata) | 3 values | 3 values |
| ✅ | [GetRuneCooldown](#getrunecooldown) | 0 values | 0 values |
| ✅ | [GetRuneCount](#getrunecount) | 0 values | 0 values |
| ✅ | [GetSheathState](#getsheathstate) | 1 value | 1 value |
| ✅ | [GetShieldBlock](#getshieldblock) | 1 value | secret |
| ✅ | [GetSpeed](#getspeed) | 1 value | secret |
| ✅ | [GetSpellBonusDamage](#getspellbonusdamage) | 1 value | secret |
| ✅ | [GetSpellBonusHealing](#getspellbonushealing) | 1 value | secret |
| ✅ | [GetSpellCritChance](#getspellcritchance) | 1 value | secret |
| ✅ | [GetSpellCritChanceFromStat](#getspellcritchancefromstat) |  |  |
| ✅ | [GetSpellHitModifier](#getspellhitmodifier) | 1 value | secret |
| ✅ | [GetSpellPenetration](#getspellpenetration) | 1 value | secret |
| ✅ | [GetSturdiness](#getsturdiness) | 1 value | secret |
| ✅ | [GetTaxiBenchmarkMode](#gettaxibenchmarkmode) | 1 value | 1 value |
| ✅ | [GetVersatilityBonus](#getversatilitybonus) | 1 value | secret |
| ✅ | [GetXPExhaustion](#getxpexhaustion) | 1 value | 1 value |
| ✅ | [HasAPEffectsSpellPower](#hasapeffectsspellpower) | 1 value | 1 value |
| ✅ | [HasDualWieldPenalty](#hasdualwieldpenalty) | 1 value | 1 value |
| ✅ | [HasFullControl](#hasfullcontrol) | 1 value | 1 value |
| ✅ | [HasIgnoreDualWieldWeapon](#hasignoredualwieldweapon) | 1 value | 1 value |
| ✅ | [HasKey](#haskey) | 1 value | 1 value |
| ✅ | [HasNoReleaseAura](#hasnoreleaseaura) | 3 values | 3 values |
| ✅ | [HasSPEffectsAttackPower](#hasspeffectsattackpower) | 1 value | 1 value |
| ✅ | [InitiateTrade](#initiatetrade) |  |  |
| ✅ | [IsAccountSecured](#isaccountsecured) | 1 value | 1 value |
| ✅ | [IsAdvancedFlyableArea](#isadvancedflyablearea) | 1 value | 1 value |
| ✅ | [IsCemeterySelectionAvailable](#iscemeteryselectionavailable) | 1 value | 1 value |
| ✅ | [IsCharacterNewlyBoosted](#ischaracternewlyboosted) | 1 value | 1 value |
| ✅ | [IsDrivableArea](#isdrivablearea) | 1 value | 1 value |
| ✅ | [IsDualWielding](#isdualwielding) | 1 value | 1 value |
| ✅ | [IsFlyableArea](#isflyablearea) | 1 value | 1 value |
| ✅ | [IsGuildLeader](#isguildleader) | 1 value | 1 value |
| ✅ | [IsInGuild](#isinguild) | 1 value | 1 value |
| ✅ | [IsInJailersTower](#isinjailerstower) | 1 value | 1 value |
| ✅ | [IsIndoors](#isindoors) | 1 value | 1 value |
| ✅ | [IsInsane](#isinsane) | 1 value | 1 value |
| ✅ | [IsItemPreferredArmorType](#isitempreferredarmortype) | 1 value | 1 value |
| ✅ | [IsJailersTowerLayerTimeLocked](#isjailerstowerlayertimelocked) |  |  |
| ✅ | [IsLoggedIn](#isloggedin) | 1 value | 1 value |
| ✅ | [IsMounted](#ismounted) | 1 value | 1 value |
| ✅ | [IsOnGroundFloorInJailersTower](#isongroundfloorinjailerstower) | 1 value | 1 value |
| ✅ | [IsOutOfBounds](#isoutofbounds) | 1 value | 1 value |
| ✅ | [IsOutdoors](#isoutdoors) | 1 value | 1 value |
| ✅ | [IsPVPTimerRunning](#ispvptimerrunning) | 1 value | 1 value |
| ✅ | [IsPlayerInWorld](#isplayerinworld) | 1 value | 1 value |
| ✅ | [IsPlayerMoving](#isplayermoving) | 1 value | 1 value |
| ✅ | [IsRangedWeapon](#israngedweapon) | 1 value | 1 value |
| ✅ | [IsResting](#isresting) | 1 value | 1 value |
| ✅ | [IsRestrictedAccount](#isrestrictedaccount) | 1 value | 1 value |
| ✅ | [IsStealthed](#isstealthed) | 1 value | 1 value |
| ✅ | [IsXPUserDisabled](#isxpuserdisabled) | 1 value | 1 value |
| ✅ | [NoPlayTime](#noplaytime) |  |  |
| ✅ | [NotifyInspect](#notifyinspect) |  |  |
| ✅ | [PartialPlayTime](#partialplaytime) |  |  |
| ✅ | [PlayerCanTeleport](#playercanteleport) |  |  |
| ✅ | [PlayerEffectiveAttackPower](#playereffectiveattackpower) |  |  |
| ✅ | [PlayerGetTimerunningSeasonID](#playergettimerunningseasonid) |  |  |
| ✅ | [PlayerIsInCombat](#playerisincombat) |  |  |
| ✅ | [PlayerIsTimerunning](#playeristimerunning) |  |  |
| ✅ | [PortGraveyard](#portgraveyard) |  |  |
| ✅ | [RandomRoll](#randomroll) |  |  |
| ✅ | [ReagentsFromBankAllowed](#reagentsfrombankallowed) |  |  |
| ✅ | [RepopMe](#repopme) |  |  |
| ✅ | [RequestTimePlayed](#requesttimeplayed) |  |  |
| ✅ | [RespondInstanceLock](#respondinstancelock) |  |  |
| ✅ | [ResurrectGetOfferer](#resurrectgetofferer) |  |  |
| ✅ | [ResurrectHasSickness](#resurrecthassickness) |  |  |
| ✅ | [ResurrectHasTimer](#resurrecthastimer) |  |  |
| ✅ | [RetrieveCorpse](#retrievecorpse) |  |  |
| ✅ | [SetAllowLowLevelRaid](#setallowlowlevelraid) |  |  |
| ✅ | [SetAllowRecentAlliesSeeLocation](#setallowrecentalliesseelocation) |  |  |
| ✅ | [SetAutoDeclineGuildInvites](#setautodeclineguildinvites) |  |  |
| ✅ | [SetAutoDeclineNeighborhoodInvites](#setautodeclineneighborhoodinvites) |  |  |
| ✅ | [SetCemeteryPreference](#setcemeterypreference) |  |  |
| ✅ | [SetLootSpecialization](#setlootspecialization) |  |  |
| ✅ | [SetTaxiBenchmarkMode](#settaxibenchmarkmode) |  |  |
| ✅ | [ShouldDisplayRaidRolesInSocialFrame](#shoulddisplayraidrolesinsocialframe) | 1 value | 1 value |
| ✅ | [ShouldDisplayStoryModeTooltipInSocialFrame](#shoulddisplaystorymodetooltipinsocialframe) | 1 value | 1 value |
| ✅ | [ShouldShowIslandsWeeklyPOI](#shouldshowislandsweeklypoi) | 1 value | 1 value |
| ✅ | [ShouldShowSpecialSplashScreen](#shouldshowspecialsplashscreen) | 1 value | 1 value |
| ✅ | [ShowCloak](#showcloak) |  |  |
| ✅ | [ShowHelm](#showhelm) |  |  |
| ✅ | [ShowingCloak](#showingcloak) |  |  |
| ✅ | [ShowingHelm](#showinghelm) |  |  |
| ✅ | [SitStandOrDescendStart](#sitstandordescendstart) |  |  |
| ✅ | [SplashFrameCanBeShown](#splashframecanbeshown) |  |  |
| ✅ | [StartAttack](#startattack) |  |  |
| ✅ | [StopAttack](#stopattack) |  |  |
| ✅ | [Stuck](#stuck) |  |  |
| ✅ | [TimeoutResurrect](#timeoutresurrect) |  |  |
| ✅ | [ToggleSelfHighlight](#toggleselfhighlight) |  |  |
| ✅ | [ToggleSheath](#togglesheath) |  |  |
| ✅ | [ToggleSit](#togglesit) |  |  |

### AcceptAreaSpiritHeal

`AcceptAreaSpiritHeal()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### AcceptGuild

`AcceptGuild()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### AcceptResurrect

`AcceptResurrect()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### Ambiguate

`Ambiguate(fullName: cstring, context: cstring) → result: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### AutoEquipCursorItem

`AutoEquipCursorItem()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### BeginTrade

`BeginTrade()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### CanDualWield

`CanDualWield() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### CanInspect

`CanInspect(targetGUID: UnitToken) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `player`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### CanLootUnit

`CanLootUnit(targetUnit: WOWGUID) → hasLoot: bool, canLoot: bool`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 2 values: `boolean`, `boolean`
- Called in combat: returned 2 values: `boolean`, `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### CanPortGraveyard

`CanPortGraveyard() → canPortGraveyard: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### CancelAreaSpiritHeal

`CancelAreaSpiritHeal()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### CancelPendingEquip

`CancelPendingEquip(index: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### CancelTrade

`CancelTrade()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### CheckInteractDistance

`CheckInteractDistance(unitGUID: UnitToken, distIndex: luaIndex) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### CheckTalentMasterDist

`CheckTalentMasterDist() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### ClearPendingBindConversionItem

`ClearPendingBindConversionItem()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### ConfirmTalentWipe

`ConfirmTalentWipe()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### ConvertItemToBindToAccount

`ConvertItemToBindToAccount()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### DeclineGuild

`DeclineGuild()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### DeclineResurrect

`DeclineResurrect()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### Dismount

`Dismount()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### EquipPendingItem

`EquipPendingItem(index: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### FollowUnit

`FollowUnit(name: cstring = 0, exactMatch: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### GetAllowLowLevelRaid

`GetAllowLowLevelRaid() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetAllowRecentAlliesSeeLocation

`GetAllowRecentAlliesSeeLocation() → allowRecentAlliesSeeLocation: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetAreaSpiritHealerTime

`GetAreaSpiritHealerTime() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetArmorPenetration

`GetArmorPenetration() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetAttackPowerForStat

`GetAttackPowerForStat(stat: luaIndex, value: number) → result: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### GetAutoDeclineGuildInvites

`GetAutoDeclineGuildInvites() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetAutoDeclineNeighborhoodInvites

`GetAutoDeclineNeighborhoodInvites() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetAvoidance

`GetAvoidance() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetBindLocation

`GetBindLocation() → result: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetBlockChance

`GetBlockChance() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCemeteryPreference

`GetCemeteryPreference() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCollapsingStarCost

`GetCollapsingStarCost() → cost: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCombatRating

`GetCombatRating(ratingIndex: luaIndex) → result: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCombatRatingBonus

`GetCombatRatingBonus(ratingIndex: luaIndex) → result: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCombatRatingBonusForCombatRatingValue

`GetCombatRatingBonusForCombatRatingValue(ratingIndex: luaIndex, value: number) → result: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCorpseRecoveryDelay

`GetCorpseRecoveryDelay() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCorruption

`GetCorruption() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCorruptionResistance

`GetCorruptionResistance() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCritChance

`GetCritChance() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCritChanceFromStat

`GetCritChanceFromStat(stat: luaIndex, value: number) → critChance: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### GetCritChanceProvidesParryEffect

`GetCritChanceProvidesParryEffect() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetDodgeChance

`GetDodgeChance() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetDodgeChanceFromAttribute

`GetDodgeChanceFromAttribute() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetEvictionTimeRemaining

`GetEvictionTimeRemaining() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetExpertise

`GetExpertise() → mainhandExpertise: number, offhandExpertise: number, rangedExpertise: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 3 values: `number`, `number`, `number`
- Called in combat: returned 3 values: `secret:number`, `secret:number`, `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetExpertisePercent

`GetExpertisePercent() → mainhandExpertisePercent: number, offhandExpertisePercent: number, rangedExpertisePercent: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 3 values: `number`, `number`, `number`
- Called in combat: returned 3 values: `secret:number`, `secret:number`, `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetGlancingBlowChance

`GetGlancingBlowChance(playerWeaponSkill: number?, targetDefenseSkill: number) → result: number`

- Status: ✅ verified (function)
- Blizzard: If no playerWeaponSkill value is provided, uses the skill value for the player's main hand weapon/shapeshift form.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### GetGlancingBlowPenalty

`GetGlancingBlowPenalty(playerWeaponSkill: number?, targetDefenseSkill: number) → result: number`

- Status: ✅ verified (function)
- Blizzard: If no playerWeaponSkill value is provided, uses the skill value for the player's main hand weapon/shapeshift form.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### GetHaste

`GetHaste() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetHealthRegen

`GetHealthRegen() → healthRegen: number, combatHealthRegen: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetHealthRegenFromSpirit

`GetHealthRegenFromSpirit() → healthRegen: number, combatHealthRegen: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetHitModifier

`GetHitModifier() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetJailersTowerLevel

`GetJailersTowerLevel() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetLifesteal

`GetLifesteal() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetLootSpecialization

`GetLootSpecialization() → specializationID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetManaRegen

`GetManaRegen() → baseManaRegen: number, castingManaRegen: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `secret:number`, `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetManaRegenFromSpirit

`GetManaRegenFromSpirit() → powerRegen: number, combatPowerRegen: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetMastery

`GetMastery() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetMasteryEffect

`GetMasteryEffect() → masteryEffect: number, bonusCoefficient: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `secret:number`, `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetMaxPlayerLevel

`GetMaxPlayerLevel() → maxPlayerLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetMeleeHaste

`GetMeleeHaste() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetModResilienceDamageReduction

`GetModResilienceDamageReduction() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetMoney

`GetMoney() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetNormalizedRealmName

`GetNormalizedRealmName() → result: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetOffhandHitModifier

`GetOffhandHitModifier() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetOverrideAPBySpellPower

`GetOverrideAPBySpellPower() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetOverrideSpellPowerByAP

`GetOverrideSpellPowerByAP() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPVPDesired

`GetPVPDesired() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPVPGearStatRules

`GetPVPGearStatRules() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPVPLifetimeStats

`GetPVPLifetimeStats() → lifetimeHonorableKills: number, lifetimeMaxPVPRank: PvPRanks`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPVPSessionStats

`GetPVPSessionStats() → honorableKills: number, dishonorableKills: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPVPTimer

`GetPVPTimer() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPVPYesterdayStats

`GetPVPYesterdayStats() → honorableKills: number, dishonorableKills: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetParryChance

`GetParryChance() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetParryChanceFromAttribute

`GetParryChanceFromAttribute() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPetCritChance

`GetPetCritChance() → meleeCrit: number, spellCrit: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `secret:number`, `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPetDodgeChance

`GetPetDodgeChance() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPetHitChanceModifier

`GetPetHitChanceModifier() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPetMeleeHaste

`GetPetMeleeHaste() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPetSpellBonusDamage

`GetPetSpellBonusDamage() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPetSpellHitChanceModifier

`GetPetSpellHitChanceModifier() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPlayerFacing

`GetPlayerFacing() → result: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPlayerInfoByGUID

`GetPlayerInfoByGUID(guid: WOWGUID) → localizedClass: cstring, englishClass: cstring, localizedRace: cstring, englishRace: cstring, sex: number, name: string, realmName: cstring, level: number?`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 8 values: `string`, `string`, `string`, `string`, `number`, `string`, `string`, `number`
- Called in combat: returned 8 values: `string`, `string`, `string`, `string`, `number`, `string`, `string`, `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPowerRegen

`GetPowerRegen() → basePowerRegen: number, castingPowerRegen: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `secret:number`, `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPowerRegenForPowerType

`GetPowerRegenForPowerType(powerType: number) → basePowerRegen: number, castingPowerRegen: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPvpPowerDamage

`GetPvpPowerDamage() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetPvpPowerHealing

`GetPvpPowerHealing() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetRangedAttackPowerForStat

`GetRangedAttackPowerForStat(stat: luaIndex, value: number) → result: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### GetRangedCritChance

`GetRangedCritChance() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetRangedHaste

`GetRangedHaste() → result: number, quiverHaste: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `secret:number`, `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetRangedHitModifier

`GetRangedHitModifier() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetReleaseTimeRemaining

`GetReleaseTimeRemaining() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetResSicknessDuration

`GetResSicknessDuration() → result: string?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetRestState

`GetRestState() → exhaustionID: number, name: cstring, factor: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 3 values: `number`, `string`, `number`
- Called in combat: returned 3 values: `number`, `string`, `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetRestrictedAccountData

`GetRestrictedAccountData() → maxLevel: number, maxMoney: WOWMONEY, professionCap: number`

- Status: ✅ verified (function)
- Called out of combat: returned 3 values: `number`, `number`, `number`
- Called in combat: returned 3 values: `number`, `number`, `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetRuneCooldown

`GetRuneCooldown(runeIndex: luaIndex) → startTime: number, duration: number, isRuneReady: bool`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `PlayerScriptDocumentation.lua`

### GetRuneCount

`GetRuneCount(runeIndex: luaIndex) → result: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `PlayerScriptDocumentation.lua`

### GetSheathState

`GetSheathState() → result: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetShieldBlock

`GetShieldBlock() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetSpeed

`GetSpeed() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetSpellBonusDamage

`GetSpellBonusDamage(school: luaIndex) → result: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetSpellBonusHealing

`GetSpellBonusHealing() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetSpellCritChance

`GetSpellCritChance() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetSpellCritChanceFromStat

`GetSpellCritChanceFromStat(stat: luaIndex, value: number) → spellCritChance: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### GetSpellHitModifier

`GetSpellHitModifier() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetSpellPenetration

`GetSpellPenetration() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetSturdiness

`GetSturdiness() → result: number`

- Status: ✅ verified (function)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetTaxiBenchmarkMode

`GetTaxiBenchmarkMode() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetVersatilityBonus

`GetVersatilityBonus(combatRating: luaIndex) → result: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `secret:number`
- Source: client docs `PlayerScriptDocumentation.lua`

### GetXPExhaustion

`GetXPExhaustion() → result: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerScriptDocumentation.lua`

### HasAPEffectsSpellPower

`HasAPEffectsSpellPower() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### HasDualWieldPenalty

`HasDualWieldPenalty() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### HasFullControl

`HasFullControl() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### HasIgnoreDualWieldWeapon

`HasIgnoreDualWieldWeapon() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### HasKey

`HasKey() → hasKey: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### HasNoReleaseAura

`HasNoReleaseAura() → hasCannotReleaseEffect: bool, longestDuration: number, hasUntilCancelledDuration: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 3 values: `boolean`, `number`, `boolean`
- Called in combat: returned 3 values: `boolean`, `number`, `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### HasSPEffectsAttackPower

`HasSPEffectsAttackPower() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### InitiateTrade

`InitiateTrade(guid: UnitToken)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### IsAccountSecured

`IsAccountSecured() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsAdvancedFlyableArea

`IsAdvancedFlyableArea() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsCemeterySelectionAvailable

`IsCemeterySelectionAvailable() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsCharacterNewlyBoosted

`IsCharacterNewlyBoosted() → newlyBoosted: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsDrivableArea

`IsDrivableArea() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsDualWielding

`IsDualWielding() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsFlyableArea

`IsFlyableArea() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsGuildLeader

`IsGuildLeader() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsInGuild

`IsInGuild() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsInJailersTower

`IsInJailersTower() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsIndoors

`IsIndoors() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsInsane

`IsInsane() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsItemPreferredArmorType

`IsItemPreferredArmorType(itemLocation: ItemLocation) → isItemPreferredArmorType: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `itemloc`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsJailersTowerLayerTimeLocked

`IsJailersTowerLayerTimeLocked(layerLevel: number) → result: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### IsLoggedIn

`IsLoggedIn() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsMounted

`IsMounted() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsOnGroundFloorInJailersTower

`IsOnGroundFloorInJailersTower() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsOutOfBounds

`IsOutOfBounds() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsOutdoors

`IsOutdoors() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsPVPTimerRunning

`IsPVPTimerRunning() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsPlayerInWorld

`IsPlayerInWorld() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsPlayerMoving

`IsPlayerMoving() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsRangedWeapon

`IsRangedWeapon() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsResting

`IsResting() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsRestrictedAccount

`IsRestrictedAccount() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsStealthed

`IsStealthed() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### IsXPUserDisabled

`IsXPUserDisabled() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### NoPlayTime

`NoPlayTime() → result: bool?`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### NotifyInspect

`NotifyInspect(targetGUID: UnitToken)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### PartialPlayTime

`PartialPlayTime() → result: bool?`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### PlayerCanTeleport

`PlayerCanTeleport() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### PlayerEffectiveAttackPower

`PlayerEffectiveAttackPower() → mainHandAttackPower: number, offHandAttackPower: number, rangedAttackPower: number, baseAttackPower: number, baseRangedAttackPower: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret while unit stats are restricted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### PlayerGetTimerunningSeasonID

`PlayerGetTimerunningSeasonID() → timerunningSeasonID: number?`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### PlayerIsInCombat

`PlayerIsInCombat() → playerIsInCombat: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### PlayerIsTimerunning

`PlayerIsTimerunning() → playerIsTimerunning: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### PortGraveyard

`PortGraveyard()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### RandomRoll

`RandomRoll(min: number, max: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### ReagentsFromBankAllowed

`ReagentsFromBankAllowed() → allowed: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### RepopMe

`RepopMe()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### RequestTimePlayed

`RequestTimePlayed()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### RespondInstanceLock

`RespondInstanceLock(acceptLock: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### ResurrectGetOfferer

`ResurrectGetOfferer() → name: cstring`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### ResurrectHasSickness

`ResurrectHasSickness() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### ResurrectHasTimer

`ResurrectHasTimer() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### RetrieveCorpse

`RetrieveCorpse()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### SetAllowLowLevelRaid

`SetAllowLowLevelRaid(allow: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### SetAllowRecentAlliesSeeLocation

`SetAllowRecentAlliesSeeLocation(allowRecentAlliesSeeLocation: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### SetAutoDeclineGuildInvites

`SetAutoDeclineGuildInvites(allow: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### SetAutoDeclineNeighborhoodInvites

`SetAutoDeclineNeighborhoodInvites(allow: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### SetCemeteryPreference

`SetCemeteryPreference(cemetaryID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### SetLootSpecialization

`SetLootSpecialization(specializationID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### SetTaxiBenchmarkMode

`SetTaxiBenchmarkMode(enable: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### ShouldDisplayRaidRolesInSocialFrame

`ShouldDisplayRaidRolesInSocialFrame() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### ShouldDisplayStoryModeTooltipInSocialFrame

`ShouldDisplayStoryModeTooltipInSocialFrame() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### ShouldShowIslandsWeeklyPOI

`ShouldShowIslandsWeeklyPOI() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### ShouldShowSpecialSplashScreen

`ShouldShowSpecialSplashScreen() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerScriptDocumentation.lua`

### ShowCloak

`ShowCloak(show: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### ShowHelm

`ShowHelm(show: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### ShowingCloak

`ShowingCloak() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### ShowingHelm

`ShowingHelm() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### SitStandOrDescendStart

`SitStandOrDescendStart()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### SplashFrameCanBeShown

`SplashFrameCanBeShown() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### StartAttack

`StartAttack(name: cstring = 0, exactMatch: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

### StopAttack

`StopAttack()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### Stuck

`Stuck()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### TimeoutResurrect

`TimeoutResurrect()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### ToggleSelfHighlight

`ToggleSelfHighlight() → enabled: bool`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### ToggleSheath

`ToggleSheath()`

- Status: ✅ verified (function)
- Source: client docs `PlayerScriptDocumentation.lua`

### ToggleSit

`ToggleSit()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `PlayerScriptDocumentation.lua`

## Events

### PLAYER_IN_COMBAT_CHANGED

- Status: ✅ verified
- Payload: `inCombat: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 414 times (0 in combat); argument kinds: `b`

### PLAYER_TARGET_DIED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 372 times (371 in combat); argument kinds: ``

## Types

### PlayerAttackPowerInfo

- Structure
  - `mainHandAttackPower`: number
  - `offHandAttackPower`: number
  - `rangedAttackPower`: number
  - `baseAttackPower`: number
  - `baseRangedAttackPower`: number
