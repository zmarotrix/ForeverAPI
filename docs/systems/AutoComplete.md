# AutoComplete

Namespace: `C_AutoComplete`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_AutoComplete.GetAutoCompletePresenceID](#c_autocompletegetautocompletepresenceid) |  |  |
| ❔ | [C_AutoComplete.GetAutoCompleteRealms](#c_autocompletegetautocompleterealms) |  |  |
| ❔ | [C_AutoComplete.GetAutoCompleteResults](#c_autocompletegetautocompleteresults) |  |  |
| ❔ | [C_AutoComplete.IsRecognizedName](#c_autocompleteisrecognizedname) |  |  |

### C_AutoComplete.GetAutoCompletePresenceID

`C_AutoComplete.GetAutoCompletePresenceID(name: cstring) → presenceID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AutoCompleteDocumentation.lua`

### C_AutoComplete.GetAutoCompleteRealms

`C_AutoComplete.GetAutoCompleteRealms() → realms: string[]`

- Status: ❔ unverified
- Source: client docs `AutoCompleteDocumentation.lua`

### C_AutoComplete.GetAutoCompleteResults

`C_AutoComplete.GetAutoCompleteResults(name: cstring, numResults: number, cursorPosition: number, allowFullMatch: bool, includeFlags: number, excludeFlags: number) → results: AutoCompleteResult[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AutoCompleteDocumentation.lua`

### C_AutoComplete.IsRecognizedName

`C_AutoComplete.IsRecognizedName(name: cstring, includeFlags: number, excludeFlags: number) → isRecognizedName: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AutoCompleteDocumentation.lua`

## Types

### AutoCompleteResult

- Structure
  - `name`: string
  - `priority`: AutoCompletePriority
  - `bnetID`: number
