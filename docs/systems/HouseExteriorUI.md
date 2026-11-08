# HouseExteriorUI

Namespace: `C_HouseExterior`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_HouseExterior.CancelActiveExteriorEditing](#c_houseexteriorcancelactiveexteriorediting) | 0 values | 0 values |
| ✅ | [C_HouseExterior.GetCoreFixtureOptionsInfo](#c_houseexteriorgetcorefixtureoptionsinfo) |  |  |
| ✅ | [C_HouseExterior.GetCurrentHouseExteriorSize](#c_houseexteriorgetcurrenthouseexteriorsize) | 1 value | 1 value |
| ✅ | [C_HouseExterior.GetCurrentHouseExteriorType](#c_houseexteriorgetcurrenthouseexteriortype) | 2 values | 2 values |
| 🆕 | [C_HouseExterior.GetFixtureDebugInfoForGUID](#c_houseexteriorgetfixturedebuginfoforguid) |  |  |
| ✅ | [C_HouseExterior.GetHouseExteriorSizeOptions](#c_houseexteriorgethouseexteriorsizeoptions) | 1 value | 1 value |
| ✅ | [C_HouseExterior.GetHouseExteriorTypeOptions](#c_houseexteriorgethouseexteriortypeoptions) | 1 value | 1 value |
| 🆕 | [C_HouseExterior.GetHoveredFixtureDebugInfo](#c_houseexteriorgethoveredfixturedebuginfo) |  |  |
| 🆕 | [C_HouseExterior.GetSelectedFixtureDebugInfo](#c_houseexteriorgetselectedfixturedebuginfo) |  |  |
| ✅ | [C_HouseExterior.GetSelectedFixturePointInfo](#c_houseexteriorgetselectedfixturepointinfo) | 1 value | 1 value |
| ✅ | [C_HouseExterior.HasHoveredFixture](#c_houseexteriorhashoveredfixture) | 1 value | 1 value |
| ✅ | [C_HouseExterior.HasSelectedFixturePoint](#c_houseexteriorhasselectedfixturepoint) | 1 value | 1 value |
| ✅ | [C_HouseExterior.IsAnyDecorAttachedToCoreFixture](#c_houseexteriorisanydecorattachedtocorefixture) |  |  |
| ✅ | [C_HouseExterior.IsAnyDecorAttachedToDoor](#c_houseexteriorisanydecorattachedtodoor) | 1 value | 1 value |
| ✅ | [C_HouseExterior.IsAnyDecorAttachedToHouseExterior](#c_houseexteriorisanydecorattachedtohouseexterior) | 1 value | 1 value |
| ✅ | [C_HouseExterior.IsAnyDecorAttachedToSelectedFixturePoint](#c_houseexteriorisanydecorattachedtoselectedfixturepoint) | 1 value | 1 value |
| ✅ | [C_HouseExterior.IsExteriorDecorHidden](#c_houseexteriorisexteriordecorhidden) | 1 value | 1 value |
| ✅ | [C_HouseExterior.RemoveFixtureFromSelectedPoint](#c_houseexteriorremovefixturefromselectedpoint) |  |  |
| ✅ | [C_HouseExterior.SelectCoreFixtureOption](#c_houseexteriorselectcorefixtureoption) |  |  |
| ✅ | [C_HouseExterior.SelectFixtureOption](#c_houseexteriorselectfixtureoption) |  |  |
| ✅ | [C_HouseExterior.SetExteriorDecorHidden](#c_houseexteriorsetexteriordecorhidden) |  |  |
| ✅ | [C_HouseExterior.SetHouseExteriorSize](#c_houseexteriorsethouseexteriorsize) |  |  |
| ✅ | [C_HouseExterior.SetHouseExteriorType](#c_houseexteriorsethouseexteriortype) |  |  |

### C_HouseExterior.CancelActiveExteriorEditing

`C_HouseExterior.CancelActiveExteriorEditing()`

- Status: ✅ verified (function)
- Blizzard: Cancels all in-progress editing of house exterior fixtures, which will deselect any active targets
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.GetCoreFixtureOptionsInfo

`C_HouseExterior.GetCoreFixtureOptionsInfo(coreFixtureType: HousingFixtureType) → coreFixtureOptionsInfo: HousingCoreFixtureInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.GetCurrentHouseExteriorSize

`C_HouseExterior.GetCurrentHouseExteriorSize() → houseExteriorSize: HousingFixtureSize?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.GetCurrentHouseExteriorType

`C_HouseExterior.GetCurrentHouseExteriorType() → houseExteriorTypeID: number?, houseExteriorTypeName: cstring?`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `nil`, `nil`
- Called in combat: returned 2 values: `nil`, `nil`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.GetFixtureDebugInfoForGUID

`C_HouseExterior.GetFixtureDebugInfoForGUID(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_HouseExterior.GetHouseExteriorSizeOptions

`C_HouseExterior.GetHouseExteriorSizeOptions() → options: HouseExteriorSizeOptionsInfo?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.GetHouseExteriorTypeOptions

`C_HouseExterior.GetHouseExteriorTypeOptions() → options: HouseExteriorTypeOptionsInfo?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.GetHoveredFixtureDebugInfo

`C_HouseExterior.GetHoveredFixtureDebugInfo(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_HouseExterior.GetSelectedFixtureDebugInfo

`C_HouseExterior.GetSelectedFixtureDebugInfo(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_HouseExterior.GetSelectedFixturePointInfo

`C_HouseExterior.GetSelectedFixturePointInfo() → fixturePointInfo: HousingFixturePointInfo?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.HasHoveredFixture

`C_HouseExterior.HasHoveredFixture() → anyHoveredFixture: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.HasSelectedFixturePoint

`C_HouseExterior.HasSelectedFixturePoint() → anySelectedFixturePoint: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.IsAnyDecorAttachedToCoreFixture

`C_HouseExterior.IsAnyDecorAttachedToCoreFixture(coreFixtureType: HousingFixtureType) → anyAttachedDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if any decor is attached to the specified core fixture type, OR any child fixtures attached to it; Will also return false if the type provided is not a core fixture type, or if not in Exterior Customization mode on an owned plot
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.IsAnyDecorAttachedToDoor

`C_HouseExterior.IsAnyDecorAttachedToDoor() → anyAttachedDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if any decor is attached to the current House Exterior's door; Will also return false if not in Exterior Customization mode on an owned plot
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.IsAnyDecorAttachedToHouseExterior

`C_HouseExterior.IsAnyDecorAttachedToHouseExterior() → anyAttachedDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if any decor is attached to any component of the current House Exterior; Will also return false if not in House Exterior Customization mode on an owned Plot
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.IsAnyDecorAttachedToSelectedFixturePoint

`C_HouseExterior.IsAnyDecorAttachedToSelectedFixturePoint() → anyAttachedDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if any decor is attached to the Fixture occupying the currently selected fixture point; Will also return false if no point is currently selected, or if there is currently no Fixture there
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.IsExteriorDecorHidden

`C_HouseExterior.IsExteriorDecorHidden() → decorHidden: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.RemoveFixtureFromSelectedPoint

`C_HouseExterior.RemoveFixtureFromSelectedPoint(attachedDecorAction: HousingFixtureDecorAction = Store)`

- Status: ✅ verified (function)
- `attachedDecorAction`: What to do with any decor currently attached to the fixture
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.SelectCoreFixtureOption

`C_HouseExterior.SelectCoreFixtureOption(fixtureID: number, attachedDecorAction: HousingFixtureDecorAction = Store)`

- Status: ✅ verified (function)
- `attachedDecorAction`: What to do with any decor attached to the old core fixture; If the fixture being swapped is a variant (ie recolor) of the existing one, attached decor will always be reparented directly to the new one
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.SelectFixtureOption

`C_HouseExterior.SelectFixtureOption(fixtureID: number, attachedDecorAction: HousingFixtureDecorAction = Store)`

- Status: ✅ verified (function)
- `attachedDecorAction`: If this fixture choice is replacing an existing one that has decor attached, what to do with any decor attached to the old one
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.SetExteriorDecorHidden

`C_HouseExterior.SetExteriorDecorHidden(decorHidden: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.SetHouseExteriorSize

`C_HouseExterior.SetHouseExteriorSize(size: HousingFixtureSize, attachedDecorAction: HousingFixtureDecorAction = Store)`

- Status: ✅ verified (function)
- `attachedDecorAction`: What to do with decor attached to any of the house's existing exterior components
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HouseExteriorUIDocumentation.lua`

### C_HouseExterior.SetHouseExteriorType

`C_HouseExterior.SetHouseExteriorType(houseExteriorTypeID: number, attachedDecorAction: HousingFixtureDecorAction = Store)`

- Status: ✅ verified (function)
- `attachedDecorAction`: What to do with decor attached to any of the house's existing exterior components
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HouseExteriorUIDocumentation.lua`

## Events

### HOUSE_EXTERIOR_DECOR_HIDDEN_CHANGED

- Status: ✅ verified
- Payload: `isDecorHidden: bool`
- fires synchronously (Blizzard's docs)

### HOUSE_EXTERIOR_TYPE_UNLOCKED

- Status: ✅ verified
- Payload: `fixtureID: number`
- unique event (Blizzard's docs)

### HOUSING_CORE_FIXTURE_CHANGED

- Status: ✅ verified
- Payload: `coreFixtureType: HousingFixtureType`
- unique event (Blizzard's docs)

### HOUSING_FIXTURE_HOVER_CHANGED

- Status: ✅ verified
- Payload: `anyHovered: bool`
- fires synchronously (Blizzard's docs)

### HOUSING_FIXTURE_POINT_FRAMES_RELEASED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_FIXTURE_POINT_FRAME_ADDED

- Status: ✅ verified
- Payload: `pointFrame: HousingFixturePointFrame`
- fires synchronously (Blizzard's docs)

### HOUSING_FIXTURE_POINT_FRAME_RELEASED

- Status: ✅ verified
- Payload: `pointFrame: HousingFixturePointFrame`
- fires synchronously (Blizzard's docs)

### HOUSING_FIXTURE_POINT_SELECTION_CHANGED

- Status: ✅ verified
- Payload: `hasSelection: bool`
- fires synchronously (Blizzard's docs)

### HOUSING_FIXTURE_UNLOCKED

- Status: ✅ verified
- Payload: `fixtureID: number`
- unique event (Blizzard's docs)

### HOUSING_SET_EXTERIOR_HOUSE_SIZE_RESPONSE

- Status: ✅ verified
- Payload: `result: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_SET_EXTERIOR_HOUSE_TYPE_RESPONSE

- Status: ✅ verified
- Payload: `result: HousingResult`
- fires synchronously (Blizzard's docs)

### HOUSING_SET_FIXTURE_RESPONSE

- Status: ✅ verified
- Payload: `result: HousingResult`
- fires synchronously (Blizzard's docs)
