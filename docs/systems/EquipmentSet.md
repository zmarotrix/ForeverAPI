# EquipmentSet

Namespace: `C_EquipmentSet`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_EquipmentSet.AssignSpecToEquipmentSet](#c_equipmentsetassignspectoequipmentset) |  |  |
| ✅ | [C_EquipmentSet.CanUseEquipmentSets](#c_equipmentsetcanuseequipmentsets) |  |  |
| ✅ | [C_EquipmentSet.ClearIgnoredSlotsForSave](#c_equipmentsetclearignoredslotsforsave) |  |  |
| ✅ | [C_EquipmentSet.CreateEquipmentSet](#c_equipmentsetcreateequipmentset) |  |  |
| ✅ | [C_EquipmentSet.DeleteEquipmentSet](#c_equipmentsetdeleteequipmentset) |  |  |
| ✅ | [C_EquipmentSet.EquipmentSetContainsLockedItems](#c_equipmentsetequipmentsetcontainslockeditems) |  |  |
| ✅ | [C_EquipmentSet.GetEquipmentSetAssignedSpec](#c_equipmentsetgetequipmentsetassignedspec) |  |  |
| ✅ | [C_EquipmentSet.GetEquipmentSetForSpec](#c_equipmentsetgetequipmentsetforspec) |  |  |
| ✅ | [C_EquipmentSet.GetEquipmentSetID](#c_equipmentsetgetequipmentsetid) |  |  |
| ✅ | [C_EquipmentSet.GetEquipmentSetIDs](#c_equipmentsetgetequipmentsetids) |  |  |
| ✅ | [C_EquipmentSet.GetEquipmentSetInfo](#c_equipmentsetgetequipmentsetinfo) |  |  |
| ✅ | [C_EquipmentSet.GetIgnoredSlots](#c_equipmentsetgetignoredslots) |  |  |
| ✅ | [C_EquipmentSet.GetItemIDs](#c_equipmentsetgetitemids) |  |  |
| ✅ | [C_EquipmentSet.GetItemLocations](#c_equipmentsetgetitemlocations) |  |  |
| ✅ | [C_EquipmentSet.GetNumEquipmentSets](#c_equipmentsetgetnumequipmentsets) |  |  |
| ✅ | [C_EquipmentSet.IgnoreSlotForSave](#c_equipmentsetignoreslotforsave) |  |  |
| ✅ | [C_EquipmentSet.IsSlotIgnoredForSave](#c_equipmentsetisslotignoredforsave) |  |  |
| ✅ | [C_EquipmentSet.ModifyEquipmentSet](#c_equipmentsetmodifyequipmentset) |  |  |
| ✅ | [C_EquipmentSet.PickupEquipmentSet](#c_equipmentsetpickupequipmentset) |  |  |
| ✅ | [C_EquipmentSet.SaveEquipmentSet](#c_equipmentsetsaveequipmentset) |  |  |
| ✅ | [C_EquipmentSet.UnassignEquipmentSetSpec](#c_equipmentsetunassignequipmentsetspec) |  |  |
| ✅ | [C_EquipmentSet.UnignoreSlotForSave](#c_equipmentsetunignoreslotforsave) |  |  |
| ✅ | [C_EquipmentSet.UseEquipmentSet](#c_equipmentsetuseequipmentset) |  |  |

### C_EquipmentSet.AssignSpecToEquipmentSet

`C_EquipmentSet.AssignSpecToEquipmentSet(equipmentSetID: number, specIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.CanUseEquipmentSets

`C_EquipmentSet.CanUseEquipmentSets() → canUseEquipmentSets: bool`

- Status: ✅ verified (function)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.ClearIgnoredSlotsForSave

`C_EquipmentSet.ClearIgnoredSlotsForSave()`

- Status: ✅ verified (function)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.CreateEquipmentSet

`C_EquipmentSet.CreateEquipmentSet(equipmentSetName: cstring, icon: cstring?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.DeleteEquipmentSet

`C_EquipmentSet.DeleteEquipmentSet(equipmentSetID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.EquipmentSetContainsLockedItems

`C_EquipmentSet.EquipmentSetContainsLockedItems(equipmentSetID: number) → hasLockedItems: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.GetEquipmentSetAssignedSpec

`C_EquipmentSet.GetEquipmentSetAssignedSpec(equipmentSetID: number) → specIndex: luaIndex`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.GetEquipmentSetForSpec

`C_EquipmentSet.GetEquipmentSetForSpec(specIndex: luaIndex) → equipmentSetID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.GetEquipmentSetID

`C_EquipmentSet.GetEquipmentSetID(equipmentSetName: cstring) → equipmentSetID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.GetEquipmentSetIDs

`C_EquipmentSet.GetEquipmentSetIDs() → equipmentSetIDs: number[]`

- Status: ✅ verified (function)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.GetEquipmentSetInfo

`C_EquipmentSet.GetEquipmentSetInfo(equipmentSetID: number) → name: string, iconFileID: number, setID: number, isEquipped: bool, numItems: number, numEquipped: number, numInInventory: number, numLost: number, numIgnored: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.GetIgnoredSlots

`C_EquipmentSet.GetIgnoredSlots(equipmentSetID: number) → slotIgnored: bool[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.GetItemIDs

`C_EquipmentSet.GetItemIDs(equipmentSetID: number) → itemIDs: number[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.GetItemLocations

`C_EquipmentSet.GetItemLocations(equipmentSetID: number) → locations: number[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.GetNumEquipmentSets

`C_EquipmentSet.GetNumEquipmentSets() → numEquipmentSets: number`

- Status: ✅ verified (function)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.IgnoreSlotForSave

`C_EquipmentSet.IgnoreSlotForSave(slot: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.IsSlotIgnoredForSave

`C_EquipmentSet.IsSlotIgnoredForSave(slot: luaIndex) → isSlotIgnored: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.ModifyEquipmentSet

`C_EquipmentSet.ModifyEquipmentSet(equipmentSetID: number, newName: cstring, newIcon: cstring?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.PickupEquipmentSet

`C_EquipmentSet.PickupEquipmentSet(equipmentSetID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.SaveEquipmentSet

`C_EquipmentSet.SaveEquipmentSet(equipmentSetID: number, icon: cstring?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.UnassignEquipmentSetSpec

`C_EquipmentSet.UnassignEquipmentSetSpec(equipmentSetID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.UnignoreSlotForSave

`C_EquipmentSet.UnignoreSlotForSave(slot: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

### C_EquipmentSet.UseEquipmentSet

`C_EquipmentSet.UseEquipmentSet(equipmentSetID: number) → setWasEquipped: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EquipmentManagerDocumentation.lua`

## Events

### EQUIPMENT_SETS_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### EQUIPMENT_SWAP_FINISHED

- Status: ✅ verified
- Payload: `result: bool`, `setID: number?`
- fires synchronously (Blizzard's docs)

### EQUIPMENT_SWAP_PENDING

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRANSMOG_CUSTOM_SETS_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
