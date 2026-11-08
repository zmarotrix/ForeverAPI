# PetInfo

Namespace: `C_PetInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_PetInfo.CanPetEatItem](#c_petinfocanpeteatitem) |  |  |
| ❔ | [C_PetInfo.GetPetFoodTypes](#c_petinfogetpetfoodtypes) |  |  |
| ❔ | [C_PetInfo.GetPetHappiness](#c_petinfogetpethappiness) |  |  |
| ❔ | [C_PetInfo.GetPetLoyalty](#c_petinfogetpetloyalty) |  |  |
| ❔ | [C_PetInfo.GetPetTalentTree](#c_petinfogetpettalenttree) |  |  |
| ❔ | [C_PetInfo.GetPetTamersForMap](#c_petinfogetpettamersformap) |  |  |
| ❔ | [C_PetInfo.GetPetTrainingPoints](#c_petinfogetpettrainingpoints) |  |  |
| ❔ | [C_PetInfo.GetPetUIModelSceneID](#c_petinfogetpetuimodelsceneid) |  |  |
| ❔ | [C_PetInfo.GetSpellForPetAction](#c_petinfogetspellforpetaction) |  |  |
| ❔ | [C_PetInfo.IsPetActionPassive](#c_petinfoispetactionpassive) |  |  |
| ❔ | [C_PetInfo.IsPetOrderMoveToPending](#c_petinfoispetordermovetopending) |  |  |
| ❔ | [C_PetInfo.PetAbandon](#c_petinfopetabandon) |  |  |
| ❔ | [C_PetInfo.PetAssistMode](#c_petinfopetassistmode) |  |  |
| ❔ | [C_PetInfo.PetRename](#c_petinfopetrename) |  |  |

### C_PetInfo.CanPetEatItem

`C_PetInfo.CanPetEatItem(itemID: number) → canEat: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetFoodTypes

`C_PetInfo.GetPetFoodTypes() → foodTypes: string[]`

- Status: ❔ unverified
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetHappiness

`C_PetInfo.GetPetHappiness() → happiness: number, damagePercentage: number, loyaltyRate: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetLoyalty

`C_PetInfo.GetPetLoyalty() → loyaltyName: string`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetTalentTree

`C_PetInfo.GetPetTalentTree() → talentTreeName: stringView`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetTamersForMap

`C_PetInfo.GetPetTamersForMap(uiMapID: number) → petTamers: PetTamerMapInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetTrainingPoints

`C_PetInfo.GetPetTrainingPoints() → totalPoints: number, usedPoints: number`

- Status: ❔ unverified
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetPetUIModelSceneID

`C_PetInfo.GetPetUIModelSceneID() → modelSceneID: number`

- Status: ❔ unverified
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.GetSpellForPetAction

`C_PetInfo.GetSpellForPetAction(actionID: number) → spellID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.IsPetActionPassive

`C_PetInfo.IsPetActionPassive(actionID: number) → isPassive: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.IsPetOrderMoveToPending

`C_PetInfo.IsPetOrderMoveToPending() → isPetOrderMoveToPending: bool`

- Status: ❔ unverified
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.PetAbandon

`C_PetInfo.PetAbandon(petNumber: number?)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.PetAssistMode

`C_PetInfo.PetAssistMode()`

- Status: ❔ unverified
- Source: client docs `PetInfoDocumentation.lua`

### C_PetInfo.PetRename

`C_PetInfo.PetRename(name: cstring, petNumber: number?, declensions: cstring[]?)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetInfoDocumentation.lua`

## Events

### PET_ATTACK_START

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_ATTACK_STOP

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BAR_HIDEGRID

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BAR_SHOWGRID

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BAR_UPDATE_COOLDOWN

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_DISMISS_START

- Status: ❔ unverified
- Payload: `delay: number`
- fires synchronously (Blizzard's docs)

### PET_FORCE_NAME_DECLENSION

- Status: ❔ unverified
- Payload: `name: cstring`, `petNumber: number?`, `declinedName1: cstring?`, `declinedName2: cstring?`, `declinedName3: cstring?`, `declinedName4: cstring?`, `declinedName5: cstring?`
- fires synchronously (Blizzard's docs)

### PET_ORDER_MOVE_TO_PENDING_CHANGED

- Status: ❔ unverified
- Payload: `isPetOrderMoveToPending: bool`
- fires synchronously (Blizzard's docs)

### PET_UI_CLOSE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### RAISED_AS_GHOUL

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_POSSESS_BAR

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_VEHICLE_ACTIONBAR

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### PetTamerMapInfo

- Structure
  - `areaPoiID`: number
  - `position`: vector2
  - `name`: cstring
  - `atlasName`: string?
  - `textureIndex`: number?
