# Vehicle

## Events

### PLAYER_GAINS_VEHICLE_DATA

- Status: ✅ verified
- Payload: `unitTarget: UnitTokenVariant`, `vehicleUIIndicatorID: number`
- fires synchronously (Blizzard's docs)

### PLAYER_LOSES_VEHICLE_DATA

- Status: ✅ verified
- Payload: `unitTarget: UnitTokenVariant`
- fires synchronously (Blizzard's docs)

### UNIT_ENTERED_VEHICLE

- Status: ✅ verified
- Payload: `unitTarget: UnitTokenVariant`, `showVehicleFrame: bool`, `isControlSeat: bool`, `vehicleUIIndicatorID: number`, `vehicleGUID: WOWGUID`, `mayChooseExit: bool`, `hasPitch: bool`
- fires synchronously (Blizzard's docs)

### UNIT_ENTERING_VEHICLE

- Status: ✅ verified
- Payload: `unitTarget: UnitTokenVariant`, `showVehicleFrame: bool`, `isControlSeat: bool`, `vehicleUIIndicatorID: number`, `vehicleGUID: WOWGUID`, `mayChooseExit: bool`, `hasPitch: bool`
- fires synchronously (Blizzard's docs)

### UNIT_EXITED_VEHICLE

- Status: ✅ verified
- Payload: `unitTarget: UnitTokenVariant`
- fires synchronously (Blizzard's docs)

### UNIT_EXITING_VEHICLE

- Status: ✅ verified
- Payload: `unitTarget: UnitTokenVariant`
- fires synchronously (Blizzard's docs)

### VEHICLE_ANGLE_SHOW

- Status: ✅ verified
- Payload: `shouldShow: number?`
- fires synchronously (Blizzard's docs)
- Seen firing 192 times (6 in combat); argument kinds: `-`

### VEHICLE_PASSENGERS_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### VEHICLE_POWER_SHOW

- Status: ✅ verified
- Payload: `shouldShow: number?`
- fires synchronously (Blizzard's docs)
- Seen firing 192 times (6 in combat); argument kinds: `-`

### VEHICLE_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 75 times (3 in combat); argument kinds: ``
