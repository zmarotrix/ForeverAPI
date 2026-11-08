# StableInfo

Namespace: `C_StableInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_StableInfo.BuyStableSlot](#c_stableinfobuystableslot) |  |  |
| ✅ | [C_StableInfo.ClosePetStables](#c_stableinfoclosepetstables) |  |  |
| ✅ | [C_StableInfo.GetActivePetList](#c_stableinfogetactivepetlist) | 1 value |  |
| ✅ | [C_StableInfo.GetAvailablePetSpecInfos](#c_stableinfogetavailablepetspecinfos) | 1 value |  |
| ✅ | [C_StableInfo.GetNextStableSlotCost](#c_stableinfogetnextstableslotcost) | 1 value |  |
| ✅ | [C_StableInfo.GetNumActivePets](#c_stableinfogetnumactivepets) | 1 value |  |
| ✅ | [C_StableInfo.GetNumStablePets](#c_stableinfogetnumstablepets) | 1 value |  |
| ✅ | [C_StableInfo.GetNumStableSlots](#c_stableinfogetnumstableslots) | 1 value |  |
| ✅ | [C_StableInfo.GetStablePetFoodTypes](#c_stableinfogetstablepetfoodtypes) |  |  |
| ✅ | [C_StableInfo.GetStablePetInfo](#c_stableinfogetstablepetinfo) |  |  |
| ✅ | [C_StableInfo.GetStabledPetList](#c_stableinfogetstabledpetlist) | 1 value |  |
| ✅ | [C_StableInfo.IsAtStableMaster](#c_stableinfoisatstablemaster) | 1 value |  |
| ✅ | [C_StableInfo.IsBonusPetSlotAvailable](#c_stableinfoisbonuspetslotavailable) | 1 value |  |
| ✅ | [C_StableInfo.IsPetFavorite](#c_stableinfoispetfavorite) |  |  |
| ✅ | [C_StableInfo.PickupStablePet](#c_stableinfopickupstablepet) |  |  |
| ✅ | [C_StableInfo.SetPetFavorite](#c_stableinfosetpetfavorite) |  |  |
| ✅ | [C_StableInfo.SetPetSlot](#c_stableinfosetpetslot) |  |  |

### C_StableInfo.BuyStableSlot

`C_StableInfo.BuyStableSlot()`

- Status: ✅ verified (function)
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.ClosePetStables

`C_StableInfo.ClosePetStables()`

- Status: ✅ verified (function)
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.GetActivePetList

`C_StableInfo.GetActivePetList() → activePets: PetInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.GetAvailablePetSpecInfos

`C_StableInfo.GetAvailablePetSpecInfos() → petSpecInfos: PetSpecInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=table}`
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.GetNextStableSlotCost

`C_StableInfo.GetNextStableSlotCost() → cost: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.GetNumActivePets

`C_StableInfo.GetNumActivePets() → numActivePets: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.GetNumStablePets

`C_StableInfo.GetNumStablePets() → numStablePets: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.GetNumStableSlots

`C_StableInfo.GetNumStableSlots() → numSlots: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.GetStablePetFoodTypes

`C_StableInfo.GetStablePetFoodTypes(index: luaIndex) → foodTypes: string[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.GetStablePetInfo

`C_StableInfo.GetStablePetInfo(index: luaIndex) → petInfo: PetInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.GetStabledPetList

`C_StableInfo.GetStabledPetList() → stabledPets: PetInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.IsAtStableMaster

`C_StableInfo.IsAtStableMaster() → isAtStableMaster: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.IsBonusPetSlotAvailable

`C_StableInfo.IsBonusPetSlotAvailable() → isAvailable: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.IsPetFavorite

`C_StableInfo.IsPetFavorite(slot: luaIndex) → isFavorite: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.PickupStablePet

`C_StableInfo.PickupStablePet(index: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.SetPetFavorite

`C_StableInfo.SetPetFavorite(slot: luaIndex, isFavorite: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `StableInfoDocumentation.lua`

### C_StableInfo.SetPetSlot

`C_StableInfo.SetPetSlot(index: luaIndex, slot: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `StableInfoDocumentation.lua`

## Events

### PET_INFO_UPDATE

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### PET_STABLE_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_STABLE_FAVORITES_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_STABLE_SHOW

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_STABLE_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### PetInfo

- Structure
  - `slotID`: number
  - `icon`: fileID
  - `name`: string
  - `level`: number
  - `familyName`: string
  - `specialization`: string
  - `type`: string
  - `petAbilities`: number[]
  - `specAbilities`: number[]
  - `displayID`: number
  - `isFavorite`: bool
  - `isExotic`: bool
  - `uiModelSceneID`: number
  - `petNumber`: number
  - `creatureID`: number
  - `specID`: number
  - `loyaltyLevel`: number
  - `loyaltyName`: string
  - `happinessLevel`: number
  - `experience`: number
  - `experienceNeeded`: number

### PetSpecInfo

- Structure
  - `specID`: number
  - `specIndex`: luaIndex
  - `specializationName`: string
