# ConsoleScriptCollection

Namespace: `C_ConsoleScriptCollection`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ConsoleScriptCollection.GetCollectionDataByID](#c_consolescriptcollectiongetcollectiondatabyid) |  |  |
| ✅ | [C_ConsoleScriptCollection.GetCollectionDataByTag](#c_consolescriptcollectiongetcollectiondatabytag) |  |  |
| ✅ | [C_ConsoleScriptCollection.GetElements](#c_consolescriptcollectiongetelements) |  |  |
| ✅ | [C_ConsoleScriptCollection.GetScriptData](#c_consolescriptcollectiongetscriptdata) |  |  |

### C_ConsoleScriptCollection.GetCollectionDataByID

`C_ConsoleScriptCollection.GetCollectionDataByID(collectionID: number) → data: ConsoleScriptCollectionData?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleScriptCollectionDocumentation.lua`

### C_ConsoleScriptCollection.GetCollectionDataByTag

`C_ConsoleScriptCollection.GetCollectionDataByTag(collectionTag: string) → data: ConsoleScriptCollectionData?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleScriptCollectionDocumentation.lua`

### C_ConsoleScriptCollection.GetElements

`C_ConsoleScriptCollection.GetElements(collectionID: number) → elementIDs: ConsoleScriptCollectionElementData[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleScriptCollectionDocumentation.lua`

### C_ConsoleScriptCollection.GetScriptData

`C_ConsoleScriptCollection.GetScriptData(consoleScriptID: number) → data: ConsoleScriptData`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConsoleScriptCollectionDocumentation.lua`

## Types

### ConsoleScriptCollectionData

- Structure
  - `ID`: number
  - `name`: cstring

### ConsoleScriptCollectionElementData

- Structure
  - `collectionID`: number?
  - `consoleScriptID`: number?

### ConsoleScriptData

- Structure
  - `ID`: number
  - `name`: cstring
  - `help`: cstring
  - `script`: cstring
  - `params`: cstring
  - `isLuaScript`: bool

### ConsoleScriptParameter

- Structure
  - `name`: string
  - `description`: string
