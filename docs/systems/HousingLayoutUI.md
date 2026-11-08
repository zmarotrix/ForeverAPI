# HousingLayoutUI

Namespace: `C_HousingLayout`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_HousingLayout.AnyRoomsOnFloor](#c_housinglayoutanyroomsonfloor) |  |  |
| ✅ | [C_HousingLayout.CanSetViewedFloor](#c_housinglayoutcansetviewedfloor) |  |  |
| ✅ | [C_HousingLayout.CancelActiveLayoutEditing](#c_housinglayoutcancelactivelayoutediting) |  |  |
| ✅ | [C_HousingLayout.ConfirmStairChoice](#c_housinglayoutconfirmstairchoice) |  |  |
| ✅ | [C_HousingLayout.DeselectFloorplan](#c_housinglayoutdeselectfloorplan) |  |  |
| ✅ | [C_HousingLayout.DeselectRoomOrDoor](#c_housinglayoutdeselectroomordoor) |  |  |
| ✅ | [C_HousingLayout.GetBaseRoomFloor](#c_housinglayoutgetbaseroomfloor) |  |  |
| ✅ | [C_HousingLayout.GetHighestOccupiedFloorIndex](#c_housinglayoutgethighestoccupiedfloorindex) |  |  |
| ✅ | [C_HousingLayout.GetLowestOccupiedFloorIndex](#c_housinglayoutgetlowestoccupiedfloorindex) |  |  |
| ✅ | [C_HousingLayout.GetNumActiveRooms](#c_housinglayoutgetnumactiverooms) |  |  |
| 🆕 | [C_HousingLayout.GetNumFloors](#c_housinglayoutgetnumfloors) |  |  |
| ✅ | [C_HousingLayout.GetRoomPlacementBudget](#c_housinglayoutgetroomplacementbudget) |  |  |
| ✅ | [C_HousingLayout.GetRoomPlayerIsIn](#c_housinglayoutgetroomplayerisin) |  |  |
| ✅ | [C_HousingLayout.GetSelectedBlueprintFloorplan](#c_housinglayoutgetselectedblueprintfloorplan) |  |  |
| ✅ | [C_HousingLayout.GetSelectedDoor](#c_housinglayoutgetselecteddoor) |  |  |
| ✅ | [C_HousingLayout.GetSelectedFloorplan](#c_housinglayoutgetselectedfloorplan) |  |  |
| ✅ | [C_HousingLayout.GetSelectedRoom](#c_housinglayoutgetselectedroom) |  |  |
| ✅ | [C_HousingLayout.GetSelectedStairwellRoomCount](#c_housinglayoutgetselectedstairwellroomcount) |  |  |
| ✅ | [C_HousingLayout.GetSpentPlacementBudget](#c_housinglayoutgetspentplacementbudget) |  |  |
| ✅ | [C_HousingLayout.GetViewedFloor](#c_housinglayoutgetviewedfloor) |  |  |
| ✅ | [C_HousingLayout.HasAnySelections](#c_housinglayouthasanyselections) |  |  |
| ✅ | [C_HousingLayout.HasRoomPlacementBudget](#c_housinglayouthasroomplacementbudget) |  |  |
| ✅ | [C_HousingLayout.HasSelectedBlueprintFloorplan](#c_housinglayouthasselectedblueprintfloorplan) |  |  |
| ✅ | [C_HousingLayout.HasSelectedDoor](#c_housinglayouthasselecteddoor) |  |  |
| ✅ | [C_HousingLayout.HasSelectedFloorplan](#c_housinglayouthasselectedfloorplan) |  |  |
| ✅ | [C_HousingLayout.HasSelectedRoom](#c_housinglayouthasselectedroom) |  |  |
| ✅ | [C_HousingLayout.HasStairs](#c_housinglayouthasstairs) |  |  |
| ✅ | [C_HousingLayout.HasValidConnection](#c_housinglayouthasvalidconnection) |  |  |
| ✅ | [C_HousingLayout.IsBaseRoom](#c_housinglayoutisbaseroom) |  |  |
| ✅ | [C_HousingLayout.IsDraggingRoom](#c_housinglayoutisdraggingroom) |  |  |
| ✅ | [C_HousingLayout.MoveDraggedRoom](#c_housinglayoutmovedraggedroom) |  |  |
| ✅ | [C_HousingLayout.MoveLayoutCamera](#c_housinglayoutmovelayoutcamera) |  |  |
| ✅ | [C_HousingLayout.RemoveRoom](#c_housinglayoutremoveroom) |  |  |
| ✅ | [C_HousingLayout.RoomHasStairs](#c_housinglayoutroomhasstairs) |  |  |
| ✅ | [C_HousingLayout.RotateFocusedRoom](#c_housinglayoutrotatefocusedroom) |  |  |
| ✅ | [C_HousingLayout.RotateRoom](#c_housinglayoutrotateroom) |  |  |
| ✅ | [C_HousingLayout.SelectFloorplan](#c_housinglayoutselectfloorplan) |  |  |
| ✅ | [C_HousingLayout.SetViewedFloor](#c_housinglayoutsetviewedfloor) |  |  |
| ✅ | [C_HousingLayout.StartDrag](#c_housinglayoutstartdrag) |  |  |
| ✅ | [C_HousingLayout.StopDrag](#c_housinglayoutstopdrag) |  |  |
| ✅ | [C_HousingLayout.StopDraggingRoom](#c_housinglayoutstopdraggingroom) |  |  |
| ✅ | [C_HousingLayout.ZoomLayoutCamera](#c_housinglayoutzoomlayoutcamera) |  |  |

### C_HousingLayout.AnyRoomsOnFloor

`C_HousingLayout.AnyRoomsOnFloor(floor: number) → anyRooms: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.CanSetViewedFloor

`C_HousingLayout.CanSetViewedFloor(floor: number) → canSet: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.CancelActiveLayoutEditing

`C_HousingLayout.CancelActiveLayoutEditing()`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.ConfirmStairChoice

`C_HousingLayout.ConfirmStairChoice(choice: HousingLayoutStairDirection?)`

- Status: ✅ verified (function)
- `choice`: If not set, the pending stair operation will be cancelled
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.DeselectFloorplan

`C_HousingLayout.DeselectFloorplan()`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.DeselectRoomOrDoor

`C_HousingLayout.DeselectRoomOrDoor()`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetBaseRoomFloor

`C_HousingLayout.GetBaseRoomFloor() → floor: number`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetHighestOccupiedFloorIndex

`C_HousingLayout.GetHighestOccupiedFloorIndex() → highestFloorIndex: number`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetLowestOccupiedFloorIndex

`C_HousingLayout.GetLowestOccupiedFloorIndex() → lowestFloorIndex: number`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetNumActiveRooms

`C_HousingLayout.GetNumActiveRooms() → numRooms: number`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetNumFloors

`C_HousingLayout.GetNumFloors(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_HousingLayout.GetRoomPlacementBudget

`C_HousingLayout.GetRoomPlacementBudget() → placementBudget: number?`

- Status: ✅ verified (function)
- Blizzard: Returns the max room placement budget for the current owned house's interior; Can be increased via house level
- `placementBudget`: Will be nil if not in an owned House or Plot
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetRoomPlayerIsIn

`C_HousingLayout.GetRoomPlayerIsIn() → roomGUID: WOWGUID`

- Status: ✅ verified (function)
- Blizzard: Returns the guid of the interior room the player is standing in, or nil if not currently standing in one
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetSelectedBlueprintFloorplan

`C_HousingLayout.GetSelectedBlueprintFloorplan() → roomID: number, shareCode: cstring`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetSelectedDoor

`C_HousingLayout.GetSelectedDoor() → selectedDoorComponentID: number, roomGUID: WOWGUID`

- Status: ✅ verified (function)
- Blizzard: If a door is selected, returns its component id and the guid of the room it belongs to; Otherwise returns nothing
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetSelectedFloorplan

`C_HousingLayout.GetSelectedFloorplan() → roomID: number?`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetSelectedRoom

`C_HousingLayout.GetSelectedRoom() → roomGUID: WOWGUID`

- Status: ✅ verified (function)
- Blizzard: If a Room is selected, returns the room's guid; Otherwise returns nothing
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetSelectedStairwellRoomCount

`C_HousingLayout.GetSelectedStairwellRoomCount() → stairwellRoomCount: number`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetSpentPlacementBudget

`C_HousingLayout.GetSpentPlacementBudget() → spentPlacementBudget: number?`

- Status: ✅ verified (function)
- Blizzard: Returns how much of the current owned house's room placement budget has been spent; Different kinds of rooms take up different budget amounts, so this value isn't an individual room count, see GetNumActiveRooms for that
- `spentPlacementBudget`: Will be nil if not in an owned House
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.GetViewedFloor

`C_HousingLayout.GetViewedFloor() → floor: number`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.HasAnySelections

`C_HousingLayout.HasAnySelections() → hasAnySelections: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if any room, door, or floorplan is currently selected or being dragged
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.HasRoomPlacementBudget

`C_HousingLayout.HasRoomPlacementBudget() → hasBudget: bool`

- Status: ✅ verified (function)
- Blizzard: Returns whether there's a max room placement budget available and active for the current player, in the current house's interior
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.HasSelectedBlueprintFloorplan

`C_HousingLayout.HasSelectedBlueprintFloorplan() → hasSelectedBlueprintFloorplan: bool`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.HasSelectedDoor

`C_HousingLayout.HasSelectedDoor() → hasSelectedDoor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a door component is currently selected
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.HasSelectedFloorplan

`C_HousingLayout.HasSelectedFloorplan() → hasSelectedFloorplan: bool`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.HasSelectedRoom

`C_HousingLayout.HasSelectedRoom() → hasSelectedRoom: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a room is selected, will NOT return true if a door is selected
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.HasStairs

`C_HousingLayout.HasStairs(roomRecordID: number) → hasStairs: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.HasValidConnection

`C_HousingLayout.HasValidConnection(roomGUID: WOWGUID, componentID: number, roomId: number) → canPlace: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.IsBaseRoom

`C_HousingLayout.IsBaseRoom(roomGUID: WOWGUID) → isBaseRoom: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.IsDraggingRoom

`C_HousingLayout.IsDraggingRoom() → isDragging: bool, isAccessibleDrag: bool`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.MoveDraggedRoom

`C_HousingLayout.MoveDraggedRoom(sourceDoorIndex: number, destRoom: WOWGUID, destDoorIndex: number)`

- Status: ✅ verified (function)
- Blizzard: Attempt to move the room currently being dragged to a specific connection point on a specific other room
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.MoveLayoutCamera

`C_HousingLayout.MoveLayoutCamera(direction: HousingLayoutCameraDirection, isPressed: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.RemoveRoom

`C_HousingLayout.RemoveRoom(roomGUID: WOWGUID)`

- Status: ✅ verified (function)
- Blizzard: Attempt to return a previously placed room to the House Chest
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.RoomHasStairs

`C_HousingLayout.RoomHasStairs(roomGUID: WOWGUID) → hasStairs: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true of the provided roomGUID is a stairwell. Returns false if roomGUID is invalid
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.RotateFocusedRoom

`C_HousingLayout.RotateFocusedRoom(isLeft: bool)`

- Status: ✅ verified (function)
- Blizzard: Rotates either the currently dragged or currently selected room, if either exist
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.RotateRoom

`C_HousingLayout.RotateRoom(roomGUID: WOWGUID, isLeft: bool)`

- Status: ✅ verified (function)
- Blizzard: Attempt to rotate an already placed room
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.SelectFloorplan

`C_HousingLayout.SelectFloorplan(roomID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.SetViewedFloor

`C_HousingLayout.SetViewedFloor(floor: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.StartDrag

`C_HousingLayout.StartDrag()`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.StopDrag

`C_HousingLayout.StopDrag()`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.StopDraggingRoom

`C_HousingLayout.StopDraggingRoom()`

- Status: ✅ verified (function)
- Source: client docs `HousingLayoutUIDocumentation.lua`

### C_HousingLayout.ZoomLayoutCamera

`C_HousingLayout.ZoomLayoutCamera(zoomIn: bool) → zoomChanged: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingLayoutUIDocumentation.lua`

## Events

### HOUSING_LAYOUT_DOOR_SELECTED

- Status: ✅ verified
- Payload: `roomGUID: WOWGUID`, `componentID: number`
- Blizzard: Fired when one of the door nodes of an already placed room has been selected
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_DOOR_SELECTION_CHANGED

- Status: ✅ verified
- Payload: `hasSelection: bool`
- Blizzard: Fired when one of the door nodes of an already placed room has been selected or deselected
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_DRAG_TARGET_CHANGED

- Status: ✅ verified
- Payload: `isDraggingRoom: bool`
- Blizzard: Fired when an already placed room has either started or stopped being dragged
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_FLOORPLAN_SELECTION_CHANGED

- Status: ✅ verified
- Payload: `hasSelection: bool`, `roomID: number`, `blueprintShareCode: cstring?`
- Blizzard: Fired when a room option in the House Chest has been selected or deselected
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_OCCUPIED_FLOOR_RANGE_CHANGED

- Status: ✅ verified
- Payload: `lowestFloor: number`, `highestFloor: number`
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_PIN_FRAMES_RELEASED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_PIN_FRAME_ADDED

- Status: ✅ verified
- Payload: `pinFrame: HousingLayoutPinFrame`
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_PIN_FRAME_RELEASED

- Status: ✅ verified
- Payload: `pinFrame: HousingLayoutPinFrame`
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_ROOM_COMPONENT_THEME_SET_CHANGED

- Status: ✅ verified
- Payload: `roomGUID: WOWGUID`, `componentID: number`, `newThemeSet: number`, `result: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_ROOM_MOVED

- Status: ✅ verified
- Payload: none
- Blizzard: Fired when a previously placed room has been moved to a different position or rotation
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_ROOM_MOVE_INVALID

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_ROOM_RECEIVED

- Status: ✅ verified
- Payload: `playAddedSound: bool`
- Blizzard: Fired when info for a newly placed room has been recieved while in Layout Mode
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_ROOM_REMOVED

- Status: ✅ verified
- Payload: none
- Blizzard: Fired when a previously placed room has been removed while in Layout Mode
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_ROOM_RETURNED

- Status: ✅ verified
- Payload: none
- Blizzard: Fired when a room that was being dragged is let go of without being placed, and is returned to the House Chest
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_ROOM_SELECTION_CHANGED

- Status: ✅ verified
- Payload: `hasSelection: bool`
- Blizzard: Fired when an already placed room has been selected or deselected
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_ROOM_SNAPPED

- Status: ✅ verified
- Payload: none
- Blizzard: Fired when a room being dragged has been snapped to a particular door connection
- fires synchronously (Blizzard's docs)

### HOUSING_LAYOUT_VIEWED_FLOOR_CHANGED

- Status: ✅ verified
- Payload: `floor: number`
- fires synchronously (Blizzard's docs)

### SHOW_STAIR_DIRECTION_CONFIRMATION

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
