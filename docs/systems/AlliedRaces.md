# AlliedRaces

Namespace: `C_AlliedRaces`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_AlliedRaces.GetAllRacialAbilitiesFromID](#c_alliedracesgetallracialabilitiesfromid) |  |  |
| ❔ | [C_AlliedRaces.GetRaceInfoByID](#c_alliedracesgetraceinfobyid) |  |  |

### C_AlliedRaces.GetAllRacialAbilitiesFromID

`C_AlliedRaces.GetAllRacialAbilitiesFromID(raceID: number) → allDisplayInfo: AlliedRaceRacialAbility[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AlliedRacesFrameDocumentation.lua`

### C_AlliedRaces.GetRaceInfoByID

`C_AlliedRaces.GetRaceInfoByID(raceID: number) → info: AlliedRaceInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AlliedRacesFrameDocumentation.lua`

## Events

### ALLIED_RACE_CLOSE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ALLIED_RACE_OPEN

- Status: ❔ unverified
- Payload: `raceID: number`
- fires synchronously (Blizzard's docs)

## Types

### AlliedRaceInfo

- Structure
  - `raceID`: number
  - `maleModelID`: number
  - `femaleModelID`: number
  - `achievementIds`: number[]
  - `maleName`: cstring
  - `femaleName`: cstring
  - `description`: cstring
  - `raceFileString`: cstring
  - `crestAtlas`: textureAtlas
  - `modelBackgroundAtlas`: textureAtlas
  - `bannerColor`: colorRGB

### AlliedRaceRacialAbility

- Structure
  - `description`: cstring
  - `name`: cstring
  - `icon`: fileID
