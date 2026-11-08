# CreatureInfo

Namespace: `C_CreatureInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_CreatureInfo.GetClassInfo](#c_creatureinfogetclassinfo) |  |  |
| ✅ | [C_CreatureInfo.GetCreatureFamilyIDs](#c_creatureinfogetcreaturefamilyids) | 1 value | 1 value |
| ✅ | [C_CreatureInfo.GetCreatureFamilyInfo](#c_creatureinfogetcreaturefamilyinfo) |  |  |
| ✅ | [C_CreatureInfo.GetCreatureID](#c_creatureinfogetcreatureid) |  |  |
| ✅ | [C_CreatureInfo.GetCreatureTypeIDs](#c_creatureinfogetcreaturetypeids) | 1 value | 1 value |
| ✅ | [C_CreatureInfo.GetCreatureTypeInfo](#c_creatureinfogetcreaturetypeinfo) |  |  |
| ✅ | [C_CreatureInfo.GetFactionInfo](#c_creatureinfogetfactioninfo) |  |  |
| ✅ | [C_CreatureInfo.GetRaceInfo](#c_creatureinfogetraceinfo) |  |  |

### C_CreatureInfo.GetClassInfo

`C_CreatureInfo.GetClassInfo(classID: number) → classInfo: ClassInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CreatureInfoDocumentation.lua`

### C_CreatureInfo.GetCreatureFamilyIDs

`C_CreatureInfo.GetCreatureFamilyIDs() → creatureFamilyIDs: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number}`
- Called in combat: returned 1 value: `table{[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number}`
- Source: client docs `CreatureInfoDocumentation.lua`

### C_CreatureInfo.GetCreatureFamilyInfo

`C_CreatureInfo.GetCreatureFamilyInfo(creatureFamilyID: number) → creatureFamilyInfo: CreatureFamilyInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CreatureInfoDocumentation.lua`

### C_CreatureInfo.GetCreatureID

`C_CreatureInfo.GetCreatureID(creatureGUID: WOWGUID) → creatureID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CreatureInfoDocumentation.lua`

### C_CreatureInfo.GetCreatureTypeIDs

`C_CreatureInfo.GetCreatureTypeIDs() → creatureTypeIDs: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number}`
- Called in combat: returned 1 value: `table{[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number}`
- Source: client docs `CreatureInfoDocumentation.lua`

### C_CreatureInfo.GetCreatureTypeInfo

`C_CreatureInfo.GetCreatureTypeInfo(creatureTypeID: number) → creatureTypeInfo: CreatureTypeInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CreatureInfoDocumentation.lua`

### C_CreatureInfo.GetFactionInfo

`C_CreatureInfo.GetFactionInfo(raceID: number) → factionInfo: FactionInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CreatureInfoDocumentation.lua`

### C_CreatureInfo.GetRaceInfo

`C_CreatureInfo.GetRaceInfo(raceID: number) → raceInfo: RaceInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CreatureInfoDocumentation.lua`

## Types

### ClassInfo

- Structure
  - `className`: string
  - `classFile`: string
  - `classID`: number

### CreatureFamilyInfo

- Structure
  - `id`: number
  - `name`: cstring
  - `iconFile`: fileID?

### CreatureTypeInfo

- Structure
  - `id`: number
  - `name`: cstring

### FactionInfo

- Structure
  - `name`: cstring
  - `groupTag`: cstring

### RaceInfo

- Structure
  - `raceName`: string
  - `clientFileString`: string
  - `raceID`: number
