# AdventureMap

Namespace: `C_AdventureMap`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_AdventureMap.GetAdventureMapTextureKit](#c_adventuremapgetadventuremaptexturekit) |  |  |
| ❔ | [C_AdventureMap.GetNumMapInsets](#c_adventuremapgetnummapinsets) |  |  |
| ❔ | [C_AdventureMap.GetNumQuestOffers](#c_adventuremapgetnumquestoffers) |  |  |
| ❔ | [C_AdventureMap.GetNumZoneChoices](#c_adventuremapgetnumzonechoices) |  |  |
| ❔ | [C_AdventureMap.GetQuestPortraitInfo](#c_adventuremapgetquestportraitinfo) |  |  |

### C_AdventureMap.GetAdventureMapTextureKit

`C_AdventureMap.GetAdventureMapTextureKit() → adventureMapTextureKit: textureKit`

- Status: ❔ unverified
- Source: client docs `AdventureMapDocumentation.lua`

### C_AdventureMap.GetNumMapInsets

`C_AdventureMap.GetNumMapInsets() → numMapInsets: number`

- Status: ❔ unverified
- Source: client docs `AdventureMapDocumentation.lua`

### C_AdventureMap.GetNumQuestOffers

`C_AdventureMap.GetNumQuestOffers() → numQuestOffers: number`

- Status: ❔ unverified
- Source: client docs `AdventureMapDocumentation.lua`

### C_AdventureMap.GetNumZoneChoices

`C_AdventureMap.GetNumZoneChoices() → numZoneChoices: number`

- Status: ❔ unverified
- Source: client docs `AdventureMapDocumentation.lua`

### C_AdventureMap.GetQuestPortraitInfo

`C_AdventureMap.GetQuestPortraitInfo(questID: number) → info: AdventureMapQuestPortraitInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AdventureMapDocumentation.lua`

## Events

### ADVENTURE_MAP_CLOSE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ADVENTURE_MAP_OPEN

- Status: ❔ unverified
- Payload: `followerTypeID: number`
- fires synchronously (Blizzard's docs)

### ADVENTURE_MAP_QUEST_UPDATE

- Status: ❔ unverified
- Payload: `questID: number`
- fires synchronously (Blizzard's docs)

### ADVENTURE_MAP_UPDATE_INSETS

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### ADVENTURE_MAP_UPDATE_POIS

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

## Types

### AdventureMapQuestPortraitInfo

- Structure
  - `portraitDisplayID`: number
  - `mountPortraitDisplayID`: number
  - `name`: string
  - `text`: string
  - `modelSceneID`: number?
