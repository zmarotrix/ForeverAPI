# AdventureMap

Namespace: `C_AdventureMap`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| 🆕 | [C_AdventureMap.Close](#c_adventuremapclose) |  |  |
| ✅ | [C_AdventureMap.GetAdventureMapTextureKit](#c_adventuremapgetadventuremaptexturekit) |  |  |
| 🆕 | [C_AdventureMap.GetMapID](#c_adventuremapgetmapid) |  |  |
| 🆕 | [C_AdventureMap.GetMapInsetDetailTileInfo](#c_adventuremapgetmapinsetdetailtileinfo) |  |  |
| 🆕 | [C_AdventureMap.GetMapInsetInfo](#c_adventuremapgetmapinsetinfo) |  |  |
| ✅ | [C_AdventureMap.GetNumMapInsets](#c_adventuremapgetnummapinsets) |  |  |
| ✅ | [C_AdventureMap.GetNumQuestOffers](#c_adventuremapgetnumquestoffers) |  |  |
| ✅ | [C_AdventureMap.GetNumZoneChoices](#c_adventuremapgetnumzonechoices) |  |  |
| 🆕 | [C_AdventureMap.GetQuestInfo](#c_adventuremapgetquestinfo) |  |  |
| 🆕 | [C_AdventureMap.GetQuestOfferInfo](#c_adventuremapgetquestofferinfo) |  |  |
| ✅ | [C_AdventureMap.GetQuestPortraitInfo](#c_adventuremapgetquestportraitinfo) |  |  |
| 🆕 | [C_AdventureMap.GetZoneChoiceInfo](#c_adventuremapgetzonechoiceinfo) |  |  |
| 🆕 | [C_AdventureMap.StartQuest](#c_adventuremapstartquest) |  |  |

### C_AdventureMap.Close

`C_AdventureMap.Close(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_AdventureMap.GetAdventureMapTextureKit

`C_AdventureMap.GetAdventureMapTextureKit() → adventureMapTextureKit: textureKit`

- Status: ✅ verified (function)
- Source: client docs `AdventureMapDocumentation.lua`

### C_AdventureMap.GetMapID

`C_AdventureMap.GetMapID(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_AdventureMap.GetMapInsetDetailTileInfo

`C_AdventureMap.GetMapInsetDetailTileInfo(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_AdventureMap.GetMapInsetInfo

`C_AdventureMap.GetMapInsetInfo(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_AdventureMap.GetNumMapInsets

`C_AdventureMap.GetNumMapInsets() → numMapInsets: number`

- Status: ✅ verified (function)
- Source: client docs `AdventureMapDocumentation.lua`

### C_AdventureMap.GetNumQuestOffers

`C_AdventureMap.GetNumQuestOffers() → numQuestOffers: number`

- Status: ✅ verified (function)
- Source: client docs `AdventureMapDocumentation.lua`

### C_AdventureMap.GetNumZoneChoices

`C_AdventureMap.GetNumZoneChoices() → numZoneChoices: number`

- Status: ✅ verified (function)
- Source: client docs `AdventureMapDocumentation.lua`

### C_AdventureMap.GetQuestInfo

`C_AdventureMap.GetQuestInfo(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_AdventureMap.GetQuestOfferInfo

`C_AdventureMap.GetQuestOfferInfo(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_AdventureMap.GetQuestPortraitInfo

`C_AdventureMap.GetQuestPortraitInfo(questID: number) → info: AdventureMapQuestPortraitInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AdventureMapDocumentation.lua`

### C_AdventureMap.GetZoneChoiceInfo

`C_AdventureMap.GetZoneChoiceInfo(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_AdventureMap.StartQuest

`C_AdventureMap.StartQuest(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

## Events

### ADVENTURE_MAP_CLOSE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ADVENTURE_MAP_OPEN

- Status: ✅ verified
- Payload: `followerTypeID: number`
- fires synchronously (Blizzard's docs)

### ADVENTURE_MAP_QUEST_UPDATE

- Status: ✅ verified
- Payload: `questID: number`
- fires synchronously (Blizzard's docs)

### ADVENTURE_MAP_UPDATE_INSETS

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### ADVENTURE_MAP_UPDATE_POIS

- Status: ✅ verified
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
