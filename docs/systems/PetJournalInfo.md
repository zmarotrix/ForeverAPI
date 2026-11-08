# PetJournalInfo

Namespace: `C_PetJournal`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_PetJournal.ClearHoveredBattlePet](#c_petjournalclearhoveredbattlepet) |  |  |
| ❔ | [C_PetJournal.ClearSearchFilter](#c_petjournalclearsearchfilter) |  |  |
| ❔ | [C_PetJournal.DismissSummonedPet](#c_petjournaldismisssummonedpet) |  |  |
| ❔ | [C_PetJournal.GetDisplayIDByIndex](#c_petjournalgetdisplayidbyindex) |  |  |
| ❔ | [C_PetJournal.GetDisplayProbabilityByIndex](#c_petjournalgetdisplayprobabilitybyindex) |  |  |
| ❔ | [C_PetJournal.GetNonBattlePetLinkByIndex](#c_petjournalgetnonbattlepetlinkbyindex) |  |  |
| ❔ | [C_PetJournal.GetNumDisplays](#c_petjournalgetnumdisplays) |  |  |
| ❔ | [C_PetJournal.GetNumPetsInJournal](#c_petjournalgetnumpetsinjournal) |  |  |
| ❔ | [C_PetJournal.GetOwnedPetIDs](#c_petjournalgetownedpetids) |  |  |
| ❔ | [C_PetJournal.GetPetAbilityInfo](#c_petjournalgetpetabilityinfo) |  |  |
| ❔ | [C_PetJournal.GetPetAbilityListTable](#c_petjournalgetpetabilitylisttable) |  |  |
| ❔ | [C_PetJournal.GetPetInfoTableByPetID](#c_petjournalgetpetinfotablebypetid) |  |  |
| ❔ | [C_PetJournal.GetPetInfoTableBySpeciesID](#c_petjournalgetpetinfotablebyspeciesid) |  |  |
| ❔ | [C_PetJournal.GetPetLoadOutInfo](#c_petjournalgetpetloadoutinfo) |  |  |
| ❔ | [C_PetJournal.GetPetSummonInfo](#c_petjournalgetpetsummoninfo) |  |  |
| ❔ | [C_PetJournal.GetSearchFilter](#c_petjournalgetsearchfilter) |  |  |
| ❔ | [C_PetJournal.HasFavoritePets](#c_petjournalhasfavoritepets) |  |  |
| ❔ | [C_PetJournal.IsCurrentlySummoned](#c_petjournaliscurrentlysummoned) |  |  |
| ❔ | [C_PetJournal.IsUsingDefaultFilters](#c_petjournalisusingdefaultfilters) |  |  |
| ❔ | [C_PetJournal.PetIsSummonable](#c_petjournalpetissummonable) |  |  |
| ❔ | [C_PetJournal.PetUsesRandomDisplay](#c_petjournalpetusesrandomdisplay) |  |  |
| ❔ | [C_PetJournal.SetDefaultFilters](#c_petjournalsetdefaultfilters) |  |  |
| ❔ | [C_PetJournal.SetHoveredBattlePet](#c_petjournalsethoveredbattlepet) |  |  |
| ❔ | [C_PetJournal.SetSearchFilter](#c_petjournalsetsearchfilter) |  |  |
| ❔ | [C_PetJournal.SpellTargetBattlePet](#c_petjournalspelltargetbattlepet) |  |  |

### C_PetJournal.ClearHoveredBattlePet

`C_PetJournal.ClearHoveredBattlePet()`

- Status: ❔ unverified
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.ClearSearchFilter

`C_PetJournal.ClearSearchFilter()`

- Status: ❔ unverified
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.DismissSummonedPet

`C_PetJournal.DismissSummonedPet(petID: WOWGUID)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetDisplayIDByIndex

`C_PetJournal.GetDisplayIDByIndex(speciesID: number, index: luaIndex) → displayID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetDisplayProbabilityByIndex

`C_PetJournal.GetDisplayProbabilityByIndex(speciesID: number, index: luaIndex) → displayProbability: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetNonBattlePetLinkByIndex

`C_PetJournal.GetNonBattlePetLinkByIndex(index: luaIndex) → link: cstring`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetNumDisplays

`C_PetJournal.GetNumDisplays(speciesID: number) → numDisplays: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetNumPetsInJournal

`C_PetJournal.GetNumPetsInJournal(creatureID: number) → maxAllowed: number, numPets: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetOwnedPetIDs

`C_PetJournal.GetOwnedPetIDs() → ownedPetIDs: WOWGUID[]`

- Status: ❔ unverified
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetPetAbilityInfo

`C_PetJournal.GetPetAbilityInfo(abilityID: number) → name: string, icon: fileID, petType: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetPetAbilityListTable

`C_PetJournal.GetPetAbilityListTable(speciesID: number) → info: PetAbilityLevelInfo[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetPetInfoTableByPetID

`C_PetJournal.GetPetInfoTableByPetID(petID: WOWGUID) → info: PetJournalPetInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetPetInfoTableBySpeciesID

`C_PetJournal.GetPetInfoTableBySpeciesID(speciesID: number) → petInfo: PetJournalPetInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetPetLoadOutInfo

`C_PetJournal.GetPetLoadOutInfo(slot: luaIndex) → petID: WOWGUID?, ability1ID: number, ability2ID: number, ability3ID: number, locked: bool`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetPetSummonInfo

`C_PetJournal.GetPetSummonInfo(battlePetGUID: WOWGUID) → isSummonable: bool, error: PetJournalError, errorText: cstring`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.GetSearchFilter

`C_PetJournal.GetSearchFilter() → filterText: cstring`

- Status: ❔ unverified
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.HasFavoritePets

`C_PetJournal.HasFavoritePets() → hasFavorites: bool`

- Status: ❔ unverified
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.IsCurrentlySummoned

`C_PetJournal.IsCurrentlySummoned(petID: WOWGUID) → isSummoned: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.IsUsingDefaultFilters

`C_PetJournal.IsUsingDefaultFilters() → isUsingDefaultFilters: bool`

- Status: ❔ unverified
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.PetIsSummonable

`C_PetJournal.PetIsSummonable(battlePetGUID: WOWGUID) → isSummonable: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.PetUsesRandomDisplay

`C_PetJournal.PetUsesRandomDisplay(speciesID: number) → usesRandomDisplay: bool?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.SetDefaultFilters

`C_PetJournal.SetDefaultFilters()`

- Status: ❔ unverified
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.SetHoveredBattlePet

`C_PetJournal.SetHoveredBattlePet(battlePetGUID: WOWGUID)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.SetSearchFilter

`C_PetJournal.SetSearchFilter(filterText: cstring)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

### C_PetJournal.SpellTargetBattlePet

`C_PetJournal.SpellTargetBattlePet(battlePetGUID: WOWGUID)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetJournalInfoDocumentation.lua`

## Events

### BATTLEPET_FORCE_NAME_DECLENSION

- Status: ❔ unverified
- Payload: `name: cstring`, `battlePetGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### COMPANION_LEARNED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### COMPANION_UNLEARNED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### COMPANION_UPDATE

- Status: ❔ unverified
- Payload: `companionType: cstring?`
- fires synchronously (Blizzard's docs)

### NEW_PET_ADDED

- Status: ❔ unverified
- Payload: `battlePetGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### PET_JOURNAL_AUTO_SLOTTED_PET

- Status: ❔ unverified
- Payload: `slotIndex: number`, `battlePetGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### PET_JOURNAL_CAGE_FAILED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_JOURNAL_LIST_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### PET_JOURNAL_NEW_BATTLE_SLOT

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_JOURNAL_PETS_HEALED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_JOURNAL_PET_DELETED

- Status: ❔ unverified
- Payload: `battlePetGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### PET_JOURNAL_PET_RESTORED

- Status: ❔ unverified
- Payload: `battlePetGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### PET_JOURNAL_PET_REVOKED

- Status: ❔ unverified
- Payload: `battlePetGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

### PET_JOURNAL_TRAP_LEVEL_SET

- Status: ❔ unverified
- Payload: `trapLevel: number`
- fires synchronously (Blizzard's docs)

### UPDATE_SUMMONPETS_ACTION

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### PetAbilityLevelInfo

- Structure
  - `abilityID`: number
  - `level`: number

### PetJournalError

- Enumeration — ❔ unverified
  - `None` = 0
  - `PetIsDead` = 1
  - `JournalIsLocked` = 2
  - `InvalidFaction` = 3
  - `NoFavoritesToSummon` = 4
  - `NoValidRandomSummon` = 5

### PetJournalPetInfo

- Structure
  - `speciesID`: number
  - `customName`: cstring?
  - `petLevel`: number?
  - `xp`: number?
  - `maxXP`: number?
  - `displayID`: number?
  - `isFavorite`: bool?
  - `icon`: fileID
  - `petType`: luaIndex
  - `creatureID`: number
  - `name`: cstring?
  - `sourceText`: cstring
  - `description`: cstring
  - `isWild`: bool?
  - `canBattle`: bool
  - `tradable`: bool
  - `unique`: bool
  - `obtainable`: bool
  - `canAttachToDecor`: bool
  - `creatureModelScale`: number?
