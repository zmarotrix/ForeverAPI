# HousingLayoutUITypes

## Types

### DoorConnectionInfo

- Structure
  - `doorID`: number
  - `connectionType`: HousingRoomComponentType
  - `doorFacing`: number

### HousingLayoutCameraDirection

- Enumeration — ❔ unverified
  - `None` = 0
  - `Up` = 1
  - `Down` = 2
  - `Left` = 4
  - `Right` = 8

### HousingLayoutPinType

- Enumeration — ❔ unverified
  - `Door` = 0
  - `Room` = 1

### HousingLayoutStairDirection

- Enumeration — ❔ unverified
  - `Up` = 0
  - `Down` = 1

### PinUpdatedCallback

- CallbackType

### RoomOptionInfo

- Structure
  - `roomName`: cstring
  - `roomID`: number
  - `learned`: bool
  - `numOwned`: number
