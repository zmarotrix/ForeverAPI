# PlayerHousingConstants

## Types

### HouseEditingContext

- Enumeration — ✅ verified
  - `None` = 0
  - `Decor` = 1
  - `Room` = 2
  - `Fixture` = 3

### HouseEditorMode

- Enumeration — ✅ verified
  - `None` = 0
  - `BasicDecor` = 1
  - `ExpertDecor` = 2
  - `Layout` = 3
  - `Customize` = 4
  - `Cleanup` = 5
  - `ExteriorCustomization` = 6

### HouseExteriorWMODataFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `UnlockedByDefault` = 1
  - `AllowedInHordeNeighborhoods` = 2
  - `AllowedInAllianceNeighborhoods` = 4
  - `HiddenUnlessOwned` = 8

### HouseFinderSuggestionReason

- Enumeration — ✅ verified
  - `None` = 0
  - `Owner` = 1
  - `CharterInvite` = 2
  - `Guild` = 4
  - `BNetFriends` = 8
  - `PartySync` = 16
  - `Random` = 32
  - `HomeOwner` = 64
  - `Relinquished` = 128

### HouseOwnerError

- Enumeration — ✅ verified
  - `None` = 0
  - `Faction` = 1
  - `Guild` = 2
  - `GenericPermission` = 3

### HousingBlueprintFlag

- Enumeration — ✅ verified
  - `None` = 0
  - `AutomaticBackup` = 1

### HousingBlueprintType

- Enumeration — ✅ verified
  - `None` = 0
  - `House` = 1
  - `Room` = 2
  - `Interior` = 3
  - `Exterior` = 4

### HousingBudgetType

- Enumeration — ✅ verified
  - `RoomPlacement` = 0
  - `DecorPlacement` = 1
  - `PetDecor` = 2

### HousingConsts

- Constants — ✅ verified
  - `NeighborhoodNameMaxCharacters` = 0
  - `NeighborhoodNameMinCharacters` = 0
  - `BlueprintNameMaxCharacters` = 0
  - `BlueprintNameMinCharacters` = 0
  - `HOUSING_BLUEPRINTS_MAX_PER_BNET_ACCOUNT` = 50
  - `HOUSING_BLUEPRINTS_MAX_BACKUPS_PER_BNET_ACCOUNT` = 10
- ⚠️ `NeighborhoodNameMaxCharacters`: docs say 0, game has 50
- ⚠️ `NeighborhoodNameMinCharacters`: docs say 0, game has 3
- ⚠️ `BlueprintNameMaxCharacters`: docs say 0, game has 50
- ⚠️ `BlueprintNameMinCharacters`: docs say 0, game has 3

### HousingDecorTheme

- Enumeration — ✅ verified
  - `None` = 0
  - `Folk` = 1
  - `Rugged` = 2
  - `Generic` = 3
  - `NightElf` = 4
  - `BloodElf` = 5

### HousingFixtureDecorAction

- Enumeration — ✅ verified
- Blizzard: Kinds of actions that can be taken to deal with decor attached to an Exterior Fixture that is being removed or swapped
  - `Store` = 0
  - `Detach` = 1

### HousingFixtureFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `IsDefaultFixture` = 1
  - `UnlockedByDefault` = 2

### HousingFixtureSize

- Enumeration — ✅ verified
  - `None` = 0
  - `Any` = 1
  - `Small` = 2
  - `Medium` = 3
  - `Large` = 4

### HousingFixtureType

- Enumeration — ✅ verified
  - `None` = 0
  - `Base` = 9
  - `Roof` = 10
  - `Door` = 11
  - `Window` = 12
  - `RoofDetail` = 13
  - `RoofWindow` = 14
  - `Tower` = 15
  - `Chimney` = 16

### HousingHouseScope

- Enumeration — ✅ verified
  - `None` = 0
  - `Interior` = 1
  - `Exterior` = 2

### HousingLayoutRestriction

- Enumeration — ✅ verified
  - `None` = 0
  - `RoomNotFound` = 1
  - `NotInsideHouse` = 2
  - `NotHouseOwner` = 3
  - `IsBaseRoom` = 4
  - `RoomNotLeaf` = 5
  - `StairwellConnection` = 6
  - `LastRoom` = 7
  - `UnreachableRoom` = 8
  - `SingleDoor` = 9

### HousingPetBehaviorType

- Enumeration — ✅ verified
  - `Stationary` = 0
  - `Wander` = 1

### HousingPlotOwnerType

- Enumeration — ✅ verified
  - `None` = 0
  - `Stranger` = 1
  - `Friend` = 2
  - `Self` = 3

### HousingResult

- Enumeration — ✅ verified
  - `Success` = 0
  - `AccountBanned` = 1
  - `ActionLockedByCombat` = 2
  - `BlueprintCodeInvalid` = 3
  - `BlueprintDyeFailed` = 4
  - `BlueprintGenericExportError` = 5
  - `BlueprintGenericImportError` = 6
  - `BlueprintLocationInvalid` = 7
  - `BlueprintNameInvalid` = 8
  - `BlueprintNotFound` = 9
  - `BlueprintRequirementsUnmet` = 10
  - `BlueprintRoomPlacementRequired` = 11
  - `BlueprintTypeInvalid` = 12
  - `BlueprintTypeLocationInvalid` = 13
  - `BlueprintStorageLimit` = 14
  - `BlueprintVersionInvalid` = 15
  - `BoundsFailureChildren` = 16
  - `BoundsFailurePlot` = 17
  - `BoundsFailureRoom` = 18
  - `BoundToStartingArea` = 19
  - `CannotAfford` = 20
  - `CharterComplete` = 21
  - `CollisionInvalid` = 22
  - `DbError` = 23
  - `DecorCannotBeRedeemed` = 24
  - `DecorItemNotDestroyable` = 25
  - `DecorNotFound` = 26
  - `DecorNotFoundInStorage` = 27
  - `DuplicateCharterSignature` = 28
  - `FilterRejected` = 29
  - `FixtureCantDeleteDoor` = 30
  - `FixtureHookEmpty` = 31
  - `FixtureHookOccupied` = 32
  - `FixtureHouseTypeMismatch` = 33
  - `FixtureNotFound` = 34
  - `FixtureSizeMismatch` = 35
  - `FixtureTypeMismatch` = 36
  - `GenericFailure` = 37
  - `GuildMoreAccountsNeeded` = 38
  - `GuildMoreActivePlayersNeeded` = 39
  - `GuildNotLoaded` = 40
  - `HouseEditLockFailed` = 41
  - `HouseExteriorAlreadyThatSize` = 42
  - `HouseExteriorAlreadyThatType` = 43
  - `HouseExteriorRootNotFound` = 44
  - `HouseExteriorTypeNeighborhoodMismatch` = 45
  - `HouseExteriorTypeNotFound` = 46
  - `HouseExteriorTypeSizeMismatch` = 47
  - `HouseExteriorSizeNotAvailable` = 48
  - `HookNotChildOfFixture` = 49
  - `HouseNotFound` = 50
  - `IncorrectFaction` = 51
  - `InvalidDecorItem` = 52
  - `InvalidDistance` = 53
  - `InvalidExteriorDocument` = 54
  - `InvalidGuild` = 55
  - `InvalidHouse` = 56
  - `InvalidInstance` = 57
  - `InvalidInteraction` = 58
  - `InvalidInteriorDocument` = 59
  - `InvalidLightOverlap` = 60
  - `InvalidMap` = 61
  - `InvalidNeighborhoodName` = 62
  - `InvalidRoomLayout` = 63
  - `InsufficientRoomBudget` = 64
  - `LockedByOtherPlayer` = 65
  - `LockOperationFailed` = 66
  - `MaxPlacedDecorReached` = 67
  - `MaxPetDecorReached` = 68
  - `MaxPreviewDecorReached` = 69
  - `MaxStorageDecorReached` = 70
  - `MessageTooLong` = 71
  - `MissingCoreFixture` = 72
  - `MissingDye` = 73
  - `MissingExpansionAccess` = 74
  - `MissingFactionMap` = 75
  - `MissingPrivateNeighborhoodInvite` = 76
  - `MoreHouseSlotsNeeded` = 77
  - `MoreSignaturesNeeded` = 78
  - `NeighborhoodNotFound` = 79
  - `NoNeighborhoodOwnershipRequests` = 80
  - `NotInDecorEditMode` = 81
  - `NotInFixtureEditMode` = 82
  - `NotInLayoutEditMode` = 83
  - `NotInsideHouse` = 84
  - `NotOnOwnedPlot` = 85
  - `OperationAborted` = 86
  - `OwnerNotInGuild` = 87
  - `PermissionDenied` = 88
  - `PlacementTargetInvalid` = 89
  - `PlayerNotFound` = 90
  - `PlayerNotInInstance` = 91
  - `PlotNotFound` = 92
  - `PlotNotVacant` = 93
  - `PlotReservationCooldown` = 94
  - `PlotReserved` = 95
  - `RoomNotFound` = 96
  - `RoomPlacementOutOfBounds` = 97
  - `RoomUpdateFailed` = 98
  - `RpcFailure` = 99
  - `ServiceNotAvailable` = 100
  - `StaticDataNotFound` = 101
  - `TimeoutLimit` = 102
  - `TimerunningNotAllowed` = 103
  - `TokenRequired` = 104
  - `TooManyRequests` = 105
  - `TransactionFailure` = 106
  - `UncollectedExteriorFixture` = 107
  - `UncollectedHouseType` = 108
  - `UncollectedRoom` = 109
  - `UncollectedRoomMaterial` = 110
  - `UncollectedRoomTheme` = 111
  - `UnlockOperationFailed` = 112

### HousingRoomComponentCeilingType

- Enumeration — ✅ verified
  - `Flat` = 0
  - `Vaulted` = 1

### HousingRoomComponentDoorType

- Enumeration — ✅ verified
  - `None` = 0
  - `Doorway` = 1
  - `Threshold` = 2

### HousingRoomComponentFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `HiddenInLayoutMode` = 1

### HousingRoomComponentFloorType

- Enumeration — ✅ verified
  - `Floor` = 0

### HousingRoomComponentOptionFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `IsDefault` = 1

### HousingRoomComponentOptionType

- Enumeration — ✅ verified
  - `Cosmetic` = 0
  - `DoorwayWall` = 1
  - `Doorway` = 2

### HousingRoomComponentStairType

- Enumeration — ✅ verified
  - `None` = 0
  - `StartToEnd` = 1
  - `StartToMiddle` = 2
  - `MiddleToMiddle` = 3
  - `MiddleToEnd` = 4

### HousingRoomComponentTextureFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `UnlockedByDefault` = 1

### HousingRoomComponentType

- Enumeration — ✅ verified
  - `None` = 0
  - `Wall` = 1
  - `Floor` = 2
  - `Ceiling` = 3
  - `Stairs` = 4
  - `Pillar` = 5
  - `DoorwayWall` = 6
  - `Doorway` = 7

### HousingRoomFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `BaseRoom` = 1
  - `HasStairs` = 2
  - `UnlockedByDefault` = 4
  - `HasCustomGeometry` = 8

### HousingThemeFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `UnlockedByDefault` = 1
  - `ShowInStyleSelector` = 2

### HousingThrottleType

- Enumeration — ✅ verified
  - `General` = 0
  - `Decoration` = 1

### NeighborhoodFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `PoolParent` = 1
  - `OpenToPublic` = 2

### NeighborhoodInviteResult

- Enumeration — ✅ verified
  - `Success` = 0
  - `DbError` = 1
  - `RpcFailure` = 2
  - `GenericFailure` = 3
  - `Permission` = 4
  - `Faction` = 5
  - `PendingInvitation` = 6
  - `InviteLimit` = 7
  - `NotEnoughPlots` = 8
  - `NotFound` = 9
  - `TooManyRequests` = 10
  - `AlreadyInNeighborhood` = 11

### NeighborhoodMapFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `AlliancePurchasable` = 1
  - `HordePurchasable` = 2
  - `CanSystemGenerate` = 4

### RetroactiveDecorRewardFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `AllCriteriaRequired` = 1

### RoomConnectionType

- Enumeration — ✅ verified
  - `None` = 0
  - `All` = 1
