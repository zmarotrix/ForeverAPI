# DeathInfo

Namespace: `C_DeathInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_DeathInfo.GetCorpseMapPosition](#c_deathinfogetcorpsemapposition) |  |  |
| ✅ | [C_DeathInfo.GetDeathReleasePosition](#c_deathinfogetdeathreleaseposition) |  |  |
| ✅ | [C_DeathInfo.GetGraveyardsForMap](#c_deathinfogetgraveyardsformap) |  |  |
| ✅ | [C_DeathInfo.GetSelfResurrectOptions](#c_deathinfogetselfresurrectoptions) | 0 values |  |
| ✅ | [C_DeathInfo.UseSelfResurrectOption](#c_deathinfouseselfresurrectoption) |  |  |

### C_DeathInfo.GetCorpseMapPosition

`C_DeathInfo.GetCorpseMapPosition(uiMapID: number) → position: vector2?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathInfoDocumentation.lua`

### C_DeathInfo.GetDeathReleasePosition

`C_DeathInfo.GetDeathReleasePosition(uiMapID: number) → position: vector2?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathInfoDocumentation.lua`

### C_DeathInfo.GetGraveyardsForMap

`C_DeathInfo.GetGraveyardsForMap(uiMapID: number) → graveyards: GraveyardMapInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathInfoDocumentation.lua`

### C_DeathInfo.GetSelfResurrectOptions

`C_DeathInfo.GetSelfResurrectOptions() → options: SelfResurrectOption[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `DeathInfoDocumentation.lua`

### C_DeathInfo.UseSelfResurrectOption

`C_DeathInfo.UseSelfResurrectOption(optionType: SelfResurrectOptionType, id: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DeathInfoDocumentation.lua`

## Events

### AREA_SPIRIT_HEALER_IN_RANGE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### AREA_SPIRIT_HEALER_OUT_OF_RANGE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### CEMETERY_PREFERENCE_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CONFIRM_XP_LOSS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CORPSE_IN_INSTANCE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CORPSE_IN_RANGE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CORPSE_OUT_OF_RANGE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_ALIVE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### PLAYER_DEAD

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_SKINNED

- Status: ✅ verified
- Payload: `hasFreeRepop: number`
- fires synchronously (Blizzard's docs)

### PLAYER_UNGHOST

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### REQUEST_CEMETERY_LIST_RESPONSE

- Status: ✅ verified
- Payload: `isGossipTriggered: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `b`

### RESURRECT_REQUEST

- Status: ✅ verified
- Payload: `inviter: cstring`
- fires synchronously (Blizzard's docs)

### SELF_RES_SPELL_CHANGED

- Status: ✅ verified
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

- Enumeration — ✅ verified
  - `Spell` = 0
  - `Item` = 1
