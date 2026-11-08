# DeathInfo

Namespace: `C_DeathInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_DeathInfo.GetCorpseMapPosition](#c_deathinfogetcorpsemapposition) |  |  |
| ❔ | [C_DeathInfo.GetDeathReleasePosition](#c_deathinfogetdeathreleaseposition) |  |  |
| ❔ | [C_DeathInfo.GetGraveyardsForMap](#c_deathinfogetgraveyardsformap) |  |  |
| ❔ | [C_DeathInfo.GetSelfResurrectOptions](#c_deathinfogetselfresurrectoptions) |  |  |
| ❔ | [C_DeathInfo.UseSelfResurrectOption](#c_deathinfouseselfresurrectoption) |  |  |

### C_DeathInfo.GetCorpseMapPosition

`C_DeathInfo.GetCorpseMapPosition(uiMapID: number) → position: vector2?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathInfoDocumentation.lua`

### C_DeathInfo.GetDeathReleasePosition

`C_DeathInfo.GetDeathReleasePosition(uiMapID: number) → position: vector2?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathInfoDocumentation.lua`

### C_DeathInfo.GetGraveyardsForMap

`C_DeathInfo.GetGraveyardsForMap(uiMapID: number) → graveyards: GraveyardMapInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathInfoDocumentation.lua`

### C_DeathInfo.GetSelfResurrectOptions

`C_DeathInfo.GetSelfResurrectOptions() → options: SelfResurrectOption[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `DeathInfoDocumentation.lua`

### C_DeathInfo.UseSelfResurrectOption

`C_DeathInfo.UseSelfResurrectOption(optionType: SelfResurrectOptionType, id: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathInfoDocumentation.lua`

## Events

### AREA_SPIRIT_HEALER_IN_RANGE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### AREA_SPIRIT_HEALER_OUT_OF_RANGE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CEMETERY_PREFERENCE_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CONFIRM_XP_LOSS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CORPSE_IN_INSTANCE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CORPSE_IN_RANGE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CORPSE_OUT_OF_RANGE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_ALIVE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_DEAD

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_SKINNED

- Status: ❔ unverified
- Payload: `hasFreeRepop: number`
- fires synchronously (Blizzard's docs)

### PLAYER_UNGHOST

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### REQUEST_CEMETERY_LIST_RESPONSE

- Status: ❔ unverified
- Payload: `isGossipTriggered: bool`
- fires synchronously (Blizzard's docs)

### RESURRECT_REQUEST

- Status: ❔ unverified
- Payload: `inviter: cstring`
- fires synchronously (Blizzard's docs)

### SELF_RES_SPELL_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### GraveyardMapInfo

- Structure
  - `areaPoiID`: number
  - `position`: vector2
  - `name`: cstring
  - `textureIndex`: number
  - `graveyardID`: number
  - `isGraveyardSelectable`: bool

### SelfResurrectOption

- Structure
  - `name`: string
  - `optionType`: SelfResurrectOptionType
  - `id`: number
  - `canUse`: bool
  - `isLimited`: bool
  - `priority`: number

### SelfResurrectOptionType

- Enumeration — ❔ unverified
  - `Spell` = 0
  - `Item` = 1
