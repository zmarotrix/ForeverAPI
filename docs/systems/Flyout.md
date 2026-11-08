# Flyout

Namespace: `C_Flyout`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Flyout.FlyoutHasSpell](#c_flyoutflyouthasspell) |  |  |
| ✅ | [C_Flyout.GetFlyoutID](#c_flyoutgetflyoutid) | 1 value | 1 value |
| ✅ | [C_Flyout.GetFlyoutInfo](#c_flyoutgetflyoutinfo) |  |  |
| ✅ | [C_Flyout.GetFlyoutSlotInfo](#c_flyoutgetflyoutslotinfo) |  |  |
| ✅ | [C_Flyout.GetFlyoutTexture](#c_flyoutgetflyouttexture) |  |  |
| ✅ | [C_Flyout.GetNumFlyouts](#c_flyoutgetnumflyouts) | 1 value | 1 value |

### C_Flyout.FlyoutHasSpell

`C_Flyout.FlyoutHasSpell(flyoutID: number, spellID: number) → hasSpell: bool`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `FlyoutDocumentation.lua`

### C_Flyout.GetFlyoutID

`C_Flyout.GetFlyoutID(index: luaIndex) → flyoutID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `FlyoutDocumentation.lua`

### C_Flyout.GetFlyoutInfo

`C_Flyout.GetFlyoutInfo(flyoutID: number) → info: FlyoutInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `FlyoutDocumentation.lua`

### C_Flyout.GetFlyoutSlotInfo

`C_Flyout.GetFlyoutSlotInfo(flyoutID: number, slotIndex: luaIndex) → slotInfo: FlyoutSlotInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `FlyoutDocumentation.lua`

### C_Flyout.GetFlyoutTexture

`C_Flyout.GetFlyoutTexture(flyoutID: number) → textureID: fileID`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `FlyoutDocumentation.lua`

### C_Flyout.GetNumFlyouts

`C_Flyout.GetNumFlyouts() → numFlyouts: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `FlyoutDocumentation.lua`

## Types

### FlyoutInfo

- Structure
  - `name`: string
  - `description`: string
  - `numSlots`: number
  - `isKnown`: bool

### FlyoutSlotInfo

- Structure
  - `spellID`: number
  - `overrideSpellID`: number
  - `isKnown`: bool
  - `name`: string?
  - `specID`: number?
