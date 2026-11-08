# WorldLootObject

Namespace: `C_WorldLootObject`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_WorldLootObject.DoesSlotMatchInventoryType](#c_worldlootobjectdoesslotmatchinventorytype) |  |  |
| ✅ | [C_WorldLootObject.GetWorldLootObjectDistanceSquared](#c_worldlootobjectgetworldlootobjectdistancesquared) |  |  |
| ✅ | [C_WorldLootObject.GetWorldLootObjectInfo](#c_worldlootobjectgetworldlootobjectinfo) |  |  |
| ✅ | [C_WorldLootObject.GetWorldLootObjectInfoByGUID](#c_worldlootobjectgetworldlootobjectinfobyguid) |  |  |
| ✅ | [C_WorldLootObject.IsWorldLootObject](#c_worldlootobjectisworldlootobject) |  |  |
| ✅ | [C_WorldLootObject.IsWorldLootObjectByGUID](#c_worldlootobjectisworldlootobjectbyguid) |  |  |
| ✅ | [C_WorldLootObject.IsWorldLootObjectInRange](#c_worldlootobjectisworldlootobjectinrange) |  |  |
| ✅ | [C_WorldLootObject.OnWorldLootObjectClick](#c_worldlootobjectonworldlootobjectclick) |  |  |

### C_WorldLootObject.DoesSlotMatchInventoryType

`C_WorldLootObject.DoesSlotMatchInventoryType(slot: number, inventoryType: InventoryType) → matches: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WorldLootObjectDocumentation.lua`

### C_WorldLootObject.GetWorldLootObjectDistanceSquared

`C_WorldLootObject.GetWorldLootObjectDistanceSquared(unitToken: UnitToken) → distanceSquared: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WorldLootObjectDocumentation.lua`

### C_WorldLootObject.GetWorldLootObjectInfo

`C_WorldLootObject.GetWorldLootObjectInfo(unitToken: UnitToken) → info: WorldLootObjectInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WorldLootObjectDocumentation.lua`

### C_WorldLootObject.GetWorldLootObjectInfoByGUID

`C_WorldLootObject.GetWorldLootObjectInfoByGUID(objectGUID: WOWGUID) → info: WorldLootObjectInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WorldLootObjectDocumentation.lua`

### C_WorldLootObject.IsWorldLootObject

`C_WorldLootObject.IsWorldLootObject(unitToken: UnitToken) → isWorldLootObject: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WorldLootObjectDocumentation.lua`

### C_WorldLootObject.IsWorldLootObjectByGUID

`C_WorldLootObject.IsWorldLootObjectByGUID(guid: WOWGUID) → isWorldLootObject: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WorldLootObjectDocumentation.lua`

### C_WorldLootObject.IsWorldLootObjectInRange

`C_WorldLootObject.IsWorldLootObjectInRange(unitToken: UnitToken) → isWorldLootObjectInRange: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WorldLootObjectDocumentation.lua`

### C_WorldLootObject.OnWorldLootObjectClick

`C_WorldLootObject.OnWorldLootObjectClick(unitToken: UnitToken, isLeftClick: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WorldLootObjectDocumentation.lua`

## Events

### WORLD_LOOT_OBJECT_INFO_UPDATED

- Status: ✅ verified
- Payload: `guid: WOWGUID`
- fires synchronously (Blizzard's docs)

## Types

### WorldLootObjectInfo

- Structure
  - `inventoryType`: InventoryType
  - `atMaxQuality`: bool
  - `isUpgrade`: bool
