# HousingBlueprintUI

Namespace: `C_HousingBlueprint`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_HousingBlueprint.CanExportRoom](#c_housingblueprintcanexportroom) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HousingBlueprint.CanExportTypeFromCurrentLocation](#c_housingblueprintcanexporttypefromcurrentlocation) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HousingBlueprint.CanImportTypeFromCurrentLocation](#c_housingblueprintcanimporttypefromcurrentlocation) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HousingBlueprint.DeleteBlueprint](#c_housingblueprintdeleteblueprint) |  |  |
| ✅ | [C_HousingBlueprint.ExportBlueprint](#c_housingblueprintexportblueprint) |  |  |
| ✅ | [C_HousingBlueprint.ExportRoomBlueprint](#c_housingblueprintexportroomblueprint) |  |  |
| ✅ | [C_HousingBlueprint.GetBlueprintHyperlink](#c_housingblueprintgetblueprinthyperlink) |  |  |
| ✅ | [C_HousingBlueprint.GetBlueprintTypeForCode](#c_housingblueprintgetblueprinttypeforcode) |  |  |
| ✅ | [C_HousingBlueprint.GetExportAvailability](#c_housingblueprintgetexportavailability) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HousingBlueprint.GetFeatureAvailability](#c_housingblueprintgetfeatureavailability) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HousingBlueprint.GetImportAvailability](#c_housingblueprintgetimportavailability) | 💥 crashed the client (whole namespace skipped) | 💥 crashed the client (whole namespace skipped) |
| ✅ | [C_HousingBlueprint.ImportBlueprint](#c_housingblueprintimportblueprint) |  |  |
| ✅ | [C_HousingBlueprint.IsShareCodeValid](#c_housingblueprintissharecodevalid) |  |  |
| ✅ | [C_HousingBlueprint.RenameBlueprint](#c_housingblueprintrenameblueprint) |  |  |
| ✅ | [C_HousingBlueprint.RequestBlueprintCollection](#c_housingblueprintrequestblueprintcollection) |  |  |
| ✅ | [C_HousingBlueprint.RequestBlueprintContents](#c_housingblueprintrequestblueprintcontents) |  |  |
| ✅ | [C_HousingBlueprint.RequestBlueprintContentsForContext](#c_housingblueprintrequestblueprintcontentsforcontext) |  |  |
| ✅ | [C_HousingBlueprint.StartImportRoomBlueprint](#c_housingblueprintstartimportroomblueprint) |  |  |
| ✅ | [C_HousingBlueprint.UpdateBlueprintStringFromInput](#c_housingblueprintupdateblueprintstringfrominput) |  |  |

### C_HousingBlueprint.CanExportRoom

`C_HousingBlueprint.CanExportRoom(roomGUID: WOWGUID) → canExport: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the specific room is allowed to be exported
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.CanExportTypeFromCurrentLocation

`C_HousingBlueprint.CanExportTypeFromCurrentLocation(type: HousingBlueprintType) → locationValid: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the player's current location is a valid place to attempt to export a specific kind of blueprint
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.CanImportTypeFromCurrentLocation

`C_HousingBlueprint.CanImportTypeFromCurrentLocation(type: HousingBlueprintType) → locationValid: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the player's current location is a valid place to attempt to import a specific kind of blueprint
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.DeleteBlueprint

`C_HousingBlueprint.DeleteBlueprint(blueprintID: BigUInteger)`

- Status: ✅ verified (function)
- Blizzard: Delete the specified owned blueprint; Listen for HousingBlueprintDeleteSuccess and HousingBlueprintDeleteFailure for results
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.ExportBlueprint

`C_HousingBlueprint.ExportBlueprint(type: HousingBlueprintType, name: cstring)`

- Status: ✅ verified (function)
- Blizzard: Saves out a new Blueprint of the specified type, using the specified name, if available, based on where the player is currently standing (see GetExportAvailability); Listen for HousingBlueprintExportSuccess and HousingBlueprintExportFailure for results
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.ExportRoomBlueprint

`C_HousingBlueprint.ExportRoomBlueprint(name: cstring, roomGUID: WOWGUID)`

- Status: ✅ verified (function)
- Blizzard: Saves out a new Blueprint of the specified room, using the specified name, if available (see GetExportAvailability); Listen for HousingBlueprintExportSuccess and HousingBlueprintExportFailure for results
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.GetBlueprintHyperlink

`C_HousingBlueprint.GetBlueprintHyperlink(blueprintShareCode: cstring) → hyperLink: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.GetBlueprintTypeForCode

`C_HousingBlueprint.GetBlueprintTypeForCode(shareCode: cstring) → type: HousingBlueprintType`

- Status: ✅ verified (function)
- Blizzard: Returns what type of Blueprint the specified code is for; Will return HousingBlueprintType.None if code is invalid; Does NOT check whether the shareCode actually matches up to a real valid Blueprint
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.GetExportAvailability

`C_HousingBlueprint.GetExportAvailability() → availability: HousingResult`

- Status: ✅ verified (function)
- Blizzard: Returns success if the player can currently export Blueprints, or a specific error type (ex: invalid location or permissions)
- Called out of combat: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.GetFeatureAvailability

`C_HousingBlueprint.GetFeatureAvailability() → blueprintsAvailability: HousingResult`

- Status: ✅ verified (function)
- Blizzard: Returns success if Blueprints as a feature is currently enabled and available
- Called out of combat: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.GetImportAvailability

`C_HousingBlueprint.GetImportAvailability() → availability: HousingResult`

- Status: ✅ verified (function)
- Blizzard: Returns success if the player can currently import Blueprints, or a specific error type (ex: invalid location or permissions)
- Called out of combat: 💥 not called: crashed the client (whole namespace skipped)
- Called in combat: 💥 not called: crashed the client (whole namespace skipped)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.ImportBlueprint

`C_HousingBlueprint.ImportBlueprint(shareCode: cstring)`

- Status: ✅ verified (function)
- Blizzard: Imports the specified blueprint, if available (see GetImportAvailability and CanImportTypeFromCurrentLocation); Listen for HousingBlueprintImportSuccess and HousingBlueprintImportFailure for results
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.IsShareCodeValid

`C_HousingBlueprint.IsShareCodeValid(shareCode: cstring) → isValid: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the string matches the valid expected format for a Blueprint Share Code; Does NOT check whether the shareCode actually matches up to a real valid Blueprint
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.RenameBlueprint

`C_HousingBlueprint.RenameBlueprint(blueprintID: BigUInteger, newName: cstring)`

- Status: ✅ verified (function)
- Blizzard: Rename the specified owned blueprint to the specified name; Listen for HousingBlueprintRenameSuccess and HousingBlueprintRenameFailure for results
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.RequestBlueprintCollection

`C_HousingBlueprint.RequestBlueprintCollection()`

- Status: ✅ verified (function)
- Blizzard: Request the full list of all of the player's Blueprints; This is async, either the HOUSING_BLUEPRINT_COLLECTION_RECEIVED or HOUSING_BLUEPRINT_COLLECTION_FAILURE event will eventually be fired as a result
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.RequestBlueprintContents

`C_HousingBlueprint.RequestBlueprintContents(shareCode: cstring)`

- Status: ✅ verified (function)
- Blizzard: Request the full contents of a specific Blueprint, in context of the current owned plot or house (if any); This is async as content info includes dynamic data from the server, either the HOUSING_BLUEPRINT_CONTENTS_RECEIVED or HOUSING_BLUEPRINT_CONTENTS_FAILURE event will eventually be fired as a result; Calling this again before a prior request has finished will cancel the prior request
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.RequestBlueprintContentsForContext

`C_HousingBlueprint.RequestBlueprintContentsForContext(shareCode: cstring, optionalHouseGUID: WOWGUID?)`

- Status: ✅ verified (function)
- Blizzard: Request the full contents of a specific Blueprint, either in context of a specific owned House or plot, or explicitly outside of any specific context; Typically used to update missing requirement info from previously-retrieved contents; See RequestBlueprintContents for other notes
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.StartImportRoomBlueprint

`C_HousingBlueprint.StartImportRoomBlueprint(shareCode: cstring)`

- Status: ✅ verified (function)
- Blizzard: Start the process of importing a Room Blueprint. This will lead to Layout Mode being opened, so the player can then select an available door to attach the room to
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

### C_HousingBlueprint.UpdateBlueprintStringFromInput

`C_HousingBlueprint.UpdateBlueprintStringFromInput(inputShareCode: cstring) → updatedShareCode: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingBlueprintUIDocumentation.lua`

## Events

### HOUSING_BLUEPRINTS_AVAILABILITY_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_COLLECTION_FAILURE

- Status: ✅ verified
- Payload: `result: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_COLLECTION_RECEIVED

- Status: ✅ verified
- Payload: `collection: HousingBlueprintCollection`
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_CONTENTS_FAILURE

- Status: ✅ verified
- Payload: `blueprintShareCode: string`, `result: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_CONTENTS_RECEIVED

- Status: ✅ verified
- Payload: `contentInfo: HousingBlueprintContentInfo`
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_DELETE_FAILURE

- Status: ✅ verified
- Payload: `blueprintID: BigUInteger`, `result: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_DELETE_SUCCESS

- Status: ✅ verified
- Payload: `blueprintID: BigUInteger`
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_EXPORT_FAILURE

- Status: ✅ verified
- Payload: `result: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_EXPORT_SUCCESS

- Status: ✅ verified
- Payload: `blueprintShareCode: string`
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_IMPORT_FAILURE

- Status: ✅ verified
- Payload: `result: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_IMPORT_STARTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_IMPORT_SUCCESS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_RENAME_FAILURE

- Status: ✅ verified
- Payload: `blueprintID: BigUInteger`, `result: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_BLUEPRINT_RENAME_SUCCESS

- Status: ✅ verified
- Payload: `blueprintID: BigUInteger`, `name: string`
- fires synchronously (Blizzard's docs)
