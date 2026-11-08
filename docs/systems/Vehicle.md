# Vehicle

## Events

### PLAYER_GAINS_VEHICLE_DATA

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`, `vehicleUIIndicatorID: number`
- fires synchronously (Blizzard's docs)

### PLAYER_LOSES_VEHICLE_DATA

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`
- fires synchronously (Blizzard's docs)

### UNIT_ENTERED_VEHICLE

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`, `showVehicleFrame: bool`, `isControlSeat: bool`, `vehicleUIIndicatorID: number`, `vehicleGUID: WOWGUID`, `mayChooseExit: bool`, `hasPitch: bool`
- fires synchronously (Blizzard's docs)

### UNIT_ENTERING_VEHICLE

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`, `showVehicleFrame: bool`, `isControlSeat: bool`, `vehicleUIIndicatorID: number`, `vehicleGUID: WOWGUID`, `mayChooseExit: bool`, `hasPitch: bool`
- fires synchronously (Blizzard's docs)

### UNIT_EXITED_VEHICLE

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`
- fires synchronously (Blizzard's docs)

### UNIT_EXITING_VEHICLE

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`
- fires synchronously (Blizzard's docs)

### VEHICLE_ANGLE_SHOW

- Status: ❔ unverified
- Payload: `shouldShow: number?`
- fires synchronously (Blizzard's docs)

### VEHICLE_PASSENGERS_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### VEHICLE_POWER_SHOW

- Status: ❔ unverified
- Payload: `shouldShow: number?`
- fires synchronously (Blizzard's docs)

### VEHICLE_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
