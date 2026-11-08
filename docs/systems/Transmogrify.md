# Transmogrify

Namespace: `C_Transmog`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Transmog.CanHaveSecondaryAppearanceForSlotID](#c_transmogcanhavesecondaryappearanceforslotid) |  |  |
| ✅ | [C_Transmog.ExtractTransmogIDList](#c_transmogextracttransmogidlist) |  |  |
| ✅ | [C_Transmog.GetAllSetAppearancesByID](#c_transmoggetallsetappearancesbyid) |  |  |
| ✅ | [C_Transmog.GetItemIDForSource](#c_transmoggetitemidforsource) |  |  |
| ✅ | [C_Transmog.GetSlotForInventoryType](#c_transmoggetslotforinventorytype) |  |  |
| ✅ | [C_Transmog.GetSlotVisualInfo](#c_transmoggetslotvisualinfo) |  |  |
| ✅ | [C_Transmog.IsAtTransmogNPC](#c_transmogisattransmognpc) |  |  |

### C_Transmog.CanHaveSecondaryAppearanceForSlotID

`C_Transmog.CanHaveSecondaryAppearanceForSlotID(slotID: luaIndex) → canHaveSecondaryAppearance: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogDocumentation.lua`

### C_Transmog.ExtractTransmogIDList

`C_Transmog.ExtractTransmogIDList(input: cstring) → transmogIDList: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogDocumentation.lua`

### C_Transmog.GetAllSetAppearancesByID

`C_Transmog.GetAllSetAppearancesByID(setID: number) → setItems: TransmogSetItemInfo[]?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogDocumentation.lua`

### C_Transmog.GetItemIDForSource

`C_Transmog.GetItemIDForSource(itemModifiedAppearanceID: number) → itemID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogDocumentation.lua`

### C_Transmog.GetSlotForInventoryType

`C_Transmog.GetSlotForInventoryType(inventoryType: luaIndex) → slot: luaIndex`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogDocumentation.lua`

### C_Transmog.GetSlotVisualInfo

`C_Transmog.GetSlotVisualInfo(transmogLocation: TransmogLocation) → slotVisualInfo: TransmogSlotVisualInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogDocumentation.lua`

### C_Transmog.IsAtTransmogNPC

`C_Transmog.IsAtTransmogNPC() → isAtNPC: bool`

- Status: ✅ verified (function)
- Source: client docs `TransmogDocumentation.lua`

## Events

### TRANSMOGRIFY_CLOSE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRANSMOGRIFY_ITEM_UPDATE

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### TRANSMOGRIFY_OPEN

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRANSMOGRIFY_SUCCESS

- Status: ✅ verified
- Payload: `transmogLocation: TransmogLocation`
- fires synchronously (Blizzard's docs)

### TRANSMOGRIFY_UPDATE

- Status: ✅ verified
- Payload: `transmogLocation: TransmogLocation?`, `action: cstring?`
- fires synchronously (Blizzard's docs)

### TRANSMOG_COLLECTION_CAMERA_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRANSMOG_COLLECTION_ITEM_FAVORITE_UPDATE

- Status: ✅ verified
- Payload: `itemAppearanceID: number`, `isFavorite: bool`
- fires synchronously (Blizzard's docs)

### TRANSMOG_COLLECTION_ITEM_UPDATE

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### TRANSMOG_COLLECTION_SOURCE_ADDED

- Status: ✅ verified
- Payload: `itemModifiedAppearanceID: number`
- fires synchronously (Blizzard's docs)

### TRANSMOG_COLLECTION_SOURCE_REMOVED

- Status: ✅ verified
- Payload: `itemModifiedAppearanceID: number`
- fires synchronously (Blizzard's docs)

### TRANSMOG_COLLECTION_UPDATED

- Status: ✅ verified
- Payload: `collectionIndex: luaIndex?`, `modID: number?`, `itemAppearanceID: number?`, `reason: cstring?`
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### TRANSMOG_COSMETIC_COLLECTION_SOURCE_ADDED

- Status: ✅ verified
- Payload: `itemModifiedAppearanceID: number`
- fires synchronously (Blizzard's docs)

### TRANSMOG_SEARCH_UPDATED

- Status: ✅ verified
- Payload: `searchType: TransmogSearchType`, `collectionType: TransmogCollectionType?`
- fires synchronously (Blizzard's docs)
- Seen firing 4 times (0 in combat); argument kinds: `n,-`

### TRANSMOG_SETS_UPDATE_FAVORITE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRANSMOG_SOURCE_COLLECTABILITY_UPDATE

- Status: ✅ verified
- Payload: `itemModifiedAppearanceID: number`, `collectable: bool`
- fires synchronously (Blizzard's docs)

## Types

### TransmogApplyWarningInfo

- Structure
  - `itemLink`: string
  - `text`: string

### TransmogPendingType

- Enumeration — ✅ verified
  - `Apply` = 0
  - `Revert` = 1
  - `ToggleOn` = 2
  - `ToggleOff` = 3

### TransmogSetItemInfo

- Structure
  - `itemID`: number
  - `itemModifiedAppearanceID`: number
  - `invSlot`: number
  - `invType`: string

### TransmogSlotInfo

- Structure
  - `isTransmogrified`: bool
  - `hasPending`: bool
  - `isPendingCollected`: bool
  - `canTransmogrify`: bool
  - `cannotTransmogrifyReason`: number
  - `hasUndo`: bool
  - `isHideVisual`: bool
  - `texture`: fileID?

### TransmogSlotVisualInfo

- Structure
  - `baseSourceID`: number
  - `baseVisualID`: number
  - `appliedSourceID`: number
  - `appliedVisualID`: number
  - `pendingSourceID`: number
  - `pendingVisualID`: number
  - `hasUndo`: bool
  - `isHideVisual`: bool
  - `itemSubclass`: number
