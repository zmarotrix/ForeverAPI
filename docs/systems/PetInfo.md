# PetInfo

Namespace: `C_PetInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PetInfo.CanPetEatItem](#c_petinfocanpeteatitem) | 1 value | 1 value |
| ✅ | [C_PetInfo.GetPetFoodTypes](#c_petinfogetpetfoodtypes) | 1 value | 1 value |
| ✅ | [C_PetInfo.GetPetHappiness](#c_petinfogetpethappiness) | 0 values | 0 values |
| ✅ | [C_PetInfo.GetPetLoyalty](#c_petinfogetpetloyalty) | 0 values | 0 values |
| ✅ | [C_PetInfo.GetPetTalentTree](#c_petinfogetpettalenttree) | 0 values | 0 values |
| ✅ | [C_PetInfo.GetPetTamersForMap](#c_petinfogetpettamersformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_PetInfo.GetPetTrainingPoints](#c_petinfogetpettrainingpoints) | 2 values | 2 values |
| ✅ | [C_PetInfo.GetPetUIModelSceneID](#c_petinfogetpetuimodelsceneid) | 1 value | 1 value |
| ✅ | [C_PetInfo.GetSpellForPetAction](#c_petinfogetspellforpetaction) |  |  |
| ✅ | [C_PetInfo.IsPetActionPassive](#c_petinfoispetactionpassive) |  |  |
| ✅ | [C_PetInfo.IsPetOrderMoveToPending](#c_petinfoispetordermovetopending) | 1 value | 1 value |
| ✅ | [C_PetInfo.PetAbandon](#c_petinfopetabandon) |  |  |
| ✅ | [C_PetInfo.PetAssistMode](#c_petinfopetassistmode) |  |  |
| ✅ | [C_PetInfo.PetRename](#c_petinfopetrename) |  |  |

### C_PetInfo.CanPetEatItem

`C_PetInfo.CanPetEatItem(itemID: number) → canEat: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `item`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetFoodTypes

`C_PetInfo.GetPetFoodTypes() → foodTypes: string[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetHappiness

`C_PetInfo.GetPetHappiness() → happiness: number, damagePercentage: number, loyaltyRate: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetLoyalty

`C_PetInfo.GetPetLoyalty() → loyaltyName: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetTalentTree

`C_PetInfo.GetPetTalentTree() → talentTreeName: stringView`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetTamersForMap

`C_PetInfo.GetPetTamersForMap(uiMapID: number) → petTamers: PetTamerMapInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetTrainingPoints

`C_PetInfo.GetPetTrainingPoints() → totalPoints: number, usedPoints: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetUIModelSceneID

`C_PetInfo.GetPetUIModelSceneID() → modelSceneID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetSpellForPetAction

`C_PetInfo.GetSpellForPetAction(actionID: number) → spellID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.IsPetActionPassive

`C_PetInfo.IsPetActionPassive(actionID: number) → isPassive: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.IsPetOrderMoveToPending

`C_PetInfo.IsPetOrderMoveToPending() → isPetOrderMoveToPending: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.PetAbandon

`C_PetInfo.PetAbandon(petNumber: number?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.PetAssistMode

`C_PetInfo.PetAssistMode()`

- Status: ✅ verified (function)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.PetRename

`C_PetInfo.PetRename(name: cstring, petNumber: number?, declensions: cstring[]?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

## Events

### PET_ATTACK_START

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_ATTACK_STOP

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BAR_HIDEGRID

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BAR_SHOWGRID

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BAR_UPDATE_COOLDOWN

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 88 times (1 in combat); argument kinds: ``

### PET_DISMISS_START

- Status: ✅ verified
- Payload: `delay: number`
- fires synchronously (Blizzard's docs)

### PET_FORCE_NAME_DECLENSION

- Status: ✅ verified
- Payload: `name: cstring`, `petNumber: number?`, `declinedName1: cstring?`, `declinedName2: cstring?`, `declinedName3: cstring?`, `declinedName4: cstring?`, `declinedName5: cstring?`
- fires synchronously (Blizzard's docs)

### PET_ORDER_MOVE_TO_PENDING_CHANGED

- Status: ✅ verified
- Payload: `isPetOrderMoveToPending: bool`
- fires synchronously (Blizzard's docs)

### PET_UI_CLOSE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### RAISED_AS_GHOUL

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_POSSESS_BAR

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_VEHICLE_ACTIONBAR

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 61 times (0 in combat); argument kinds: ``

## Types

### PetTamerMapInfo

- Structure
  - `areaPoiID`: number
  - `position`: vector2
  - `name`: cstring
  - `atlasName`: string?
  - `textureIndex`: number?
