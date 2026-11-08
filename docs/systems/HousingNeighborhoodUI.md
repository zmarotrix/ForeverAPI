# HousingNeighborhoodUI

Namespace: `C_HousingNeighborhood`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_HousingNeighborhood.CanReturnAfterVisitingHouse](#c_housingneighborhoodcanreturnaftervisitinghouse) |  |  |
| ❔ | [C_HousingNeighborhood.CancelInviteToNeighborhood](#c_housingneighborhoodcancelinvitetoneighborhood) |  |  |
| ❔ | [C_HousingNeighborhood.DemoteToResident](#c_housingneighborhooddemotetoresident) |  |  |
| ❔ | [C_HousingNeighborhood.GetCornerstoneHouseInfo](#c_housingneighborhoodgetcornerstonehouseinfo) |  |  |
| ❔ | [C_HousingNeighborhood.GetCornerstoneNeighborhoodInfo](#c_housingneighborhoodgetcornerstoneneighborhoodinfo) |  |  |
| ❔ | [C_HousingNeighborhood.GetCornerstonePurchaseMode](#c_housingneighborhoodgetcornerstonepurchasemode) |  |  |
| ❔ | [C_HousingNeighborhood.GetCurrentNeighborhoodTextureSuffix](#c_housingneighborhoodgetcurrentneighborhoodtexturesuffix) |  |  |
| ❔ | [C_HousingNeighborhood.GetDiscountedMovePrice](#c_housingneighborhoodgetdiscountedmoveprice) |  |  |
| ❔ | [C_HousingNeighborhood.GetMoveCooldownTime](#c_housingneighborhoodgetmovecooldowntime) |  |  |
| ❔ | [C_HousingNeighborhood.GetNeighborhoodMapData](#c_housingneighborhoodgetneighborhoodmapdata) |  |  |
| ❔ | [C_HousingNeighborhood.GetNeighborhoodName](#c_housingneighborhoodgetneighborhoodname) |  |  |
| ❔ | [C_HousingNeighborhood.GetNeighborhoodPlotName](#c_housingneighborhoodgetneighborhoodplotname) |  |  |
| ❔ | [C_HousingNeighborhood.GetPreviousHouseIdentifier](#c_housingneighborhoodgetprevioushouseidentifier) |  |  |
| ❔ | [C_HousingNeighborhood.HasPermissionToPurchase](#c_housingneighborhoodhaspermissiontopurchase) |  |  |
| ❔ | [C_HousingNeighborhood.InvitePlayerToNeighborhood](#c_housingneighborhoodinviteplayertoneighborhood) |  |  |
| ❔ | [C_HousingNeighborhood.IsNeighborhoodManager](#c_housingneighborhoodisneighborhoodmanager) |  |  |
| ❔ | [C_HousingNeighborhood.IsNeighborhoodOwner](#c_housingneighborhoodisneighborhoodowner) |  |  |
| ❔ | [C_HousingNeighborhood.IsPlayerInOtherPlayersPlot](#c_housingneighborhoodisplayerinotherplayersplot) |  |  |
| ❔ | [C_HousingNeighborhood.IsPlotAvailableForPurchase](#c_housingneighborhoodisplotavailableforpurchase) |  |  |
| ❔ | [C_HousingNeighborhood.IsPlotOwnedByPlayer](#c_housingneighborhoodisplotownedbyplayer) |  |  |
| ❔ | [C_HousingNeighborhood.OnBulletinBoardClosed](#c_housingneighborhoodonbulletinboardclosed) |  |  |
| ❔ | [C_HousingNeighborhood.OnCornerstoneClosed](#c_housingneighborhoodoncornerstoneclosed) |  |  |
| ❔ | [C_HousingNeighborhood.PromoteToManager](#c_housingneighborhoodpromotetomanager) |  |  |
| ❔ | [C_HousingNeighborhood.RequestNeighborhoodInfo](#c_housingneighborhoodrequestneighborhoodinfo) |  |  |
| ❔ | [C_HousingNeighborhood.RequestNeighborhoodRoster](#c_housingneighborhoodrequestneighborhoodroster) |  |  |
| ❔ | [C_HousingNeighborhood.RequestPendingNeighborhoodInvites](#c_housingneighborhoodrequestpendingneighborhoodinvites) |  |  |
| ❔ | [C_HousingNeighborhood.TransferNeighborhoodOwnership](#c_housingneighborhoodtransferneighborhoodownership) |  |  |
| ❔ | [C_HousingNeighborhood.TryEvictPlayer](#c_housingneighborhoodtryevictplayer) |  |  |
| ❔ | [C_HousingNeighborhood.TryMoveHouse](#c_housingneighborhoodtrymovehouse) |  |  |
| ❔ | [C_HousingNeighborhood.TryPurchasePlot](#c_housingneighborhoodtrypurchaseplot) |  |  |

### C_HousingNeighborhood.CanReturnAfterVisitingHouse

`C_HousingNeighborhood.CanReturnAfterVisitingHouse() → canReturn: bool`

- Status: ❔ unverified
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.CancelInviteToNeighborhood

`C_HousingNeighborhood.CancelInviteToNeighborhood(playerName: cstring)`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a bulletin board game object
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.DemoteToResident

`C_HousingNeighborhood.DemoteToResident(playerGUID: WOWGUID)`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a bulletin board game object
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.GetCornerstoneHouseInfo

`C_HousingNeighborhood.GetCornerstoneHouseInfo() → houseInfo: HouseInfo`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.GetCornerstoneNeighborhoodInfo

`C_HousingNeighborhood.GetCornerstoneNeighborhoodInfo() → neighborhoodInfo: NeighborhoodInfo`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.GetCornerstonePurchaseMode

`C_HousingNeighborhood.GetCornerstonePurchaseMode() → purchaseMode: CornerstonePurchaseMode`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.GetCurrentNeighborhoodTextureSuffix

`C_HousingNeighborhood.GetCurrentNeighborhoodTextureSuffix() → neighborhoodTextureSuffix: cstring`

- Status: ❔ unverified
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.GetDiscountedMovePrice

`C_HousingNeighborhood.GetDiscountedMovePrice() → movePrice: number`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- `movePrice`: Can be negative if the refund from moving is more than the cost of the new house
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.GetMoveCooldownTime

`C_HousingNeighborhood.GetMoveCooldownTime() → movecooldownTime: number`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.GetNeighborhoodMapData

`C_HousingNeighborhood.GetNeighborhoodMapData() → neighborhoodPlots: NeighborhoodPlotMapInfo[]`

- Status: ❔ unverified
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.GetNeighborhoodName

`C_HousingNeighborhood.GetNeighborhoodName() → neighborhoodName: string`

- Status: ❔ unverified
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.GetNeighborhoodPlotName

`C_HousingNeighborhood.GetNeighborhoodPlotName(plotIndex: number) → neighborhoodName: string`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.GetPreviousHouseIdentifier

`C_HousingNeighborhood.GetPreviousHouseIdentifier() → previousHouseIdentifier: string`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.HasPermissionToPurchase

`C_HousingNeighborhood.HasPermissionToPurchase() → cantPurchaseReason: PurchaseHouseDisabledReason`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.InvitePlayerToNeighborhood

`C_HousingNeighborhood.InvitePlayerToNeighborhood(playerName: cstring)`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a bulletin board game object
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.IsNeighborhoodManager

`C_HousingNeighborhood.IsNeighborhoodManager() → isManager: bool`

- Status: ❔ unverified
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.IsNeighborhoodOwner

`C_HousingNeighborhood.IsNeighborhoodOwner() → isOwner: bool`

- Status: ❔ unverified
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.IsPlayerInOtherPlayersPlot

`C_HousingNeighborhood.IsPlayerInOtherPlayersPlot() → isInUnownedPlot: bool`

- Status: ❔ unverified
- Blizzard: This returns true if the player is in a plot that is owned by another player
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.IsPlotAvailableForPurchase

`C_HousingNeighborhood.IsPlotAvailableForPurchase() → isAvailable: bool`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.IsPlotOwnedByPlayer

`C_HousingNeighborhood.IsPlotOwnedByPlayer() → isPlayerOwned: bool`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.OnBulletinBoardClosed

`C_HousingNeighborhood.OnBulletinBoardClosed()`

- Status: ❔ unverified
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.OnCornerstoneClosed

`C_HousingNeighborhood.OnCornerstoneClosed()`

- Status: ❔ unverified
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.PromoteToManager

`C_HousingNeighborhood.PromoteToManager(playerGUID: WOWGUID)`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a bulletin board game object
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.RequestNeighborhoodInfo

`C_HousingNeighborhood.RequestNeighborhoodInfo()`

- Status: ❔ unverified
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.RequestNeighborhoodRoster

`C_HousingNeighborhood.RequestNeighborhoodRoster()`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a bulletin board game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.RequestPendingNeighborhoodInvites

`C_HousingNeighborhood.RequestPendingNeighborhoodInvites()`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a bulletin board game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.TransferNeighborhoodOwnership

`C_HousingNeighborhood.TransferNeighborhoodOwnership(playerGUID: WOWGUID)`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a bulletin board game object
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.TryEvictPlayer

`C_HousingNeighborhood.TryEvictPlayer(plotID: number)`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a bulletin board game object
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.TryMoveHouse

`C_HousingNeighborhood.TryMoveHouse()`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

### C_HousingNeighborhood.TryPurchasePlot

`C_HousingNeighborhood.TryPurchasePlot()`

- Status: ❔ unverified
- Blizzard: Only available when interacting with a cornerstone game object
- Source: client docs `HousingNeighborhoodUIDocumentation.lua`

## Events

### CANCEL_NEIGHBORHOOD_INVITE_RESPONSE

- Status: ❔ unverified
- Payload: `result: NeighborhoodInviteResult`, `playerName: cstring?`
- fires synchronously (Blizzard's docs)

### CLOSE_PLOT_CORNERSTONE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### NEIGHBORHOOD_INFO_UPDATED

- Status: ❔ unverified
- Payload: `neighborhoodInfo: NeighborhoodInfo`
- fires synchronously (Blizzard's docs)

### NEIGHBORHOOD_INVITE_RESPONSE

- Status: ❔ unverified
- Payload: `result: NeighborhoodInviteResult`
- fires synchronously (Blizzard's docs)

### NEIGHBORHOOD_MAP_DATA_UPDATED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### NEIGHBORHOOD_NAME_UPDATED

- Status: ❔ unverified
- Payload: `neighborhoodGuid: WOWGUID`, `neighborhoodName: cstring`
- unique event (Blizzard's docs)

### OPEN_PLOT_CORNERSTONE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PENDING_NEIGHBORHOOD_INVITES_RECIEVED

- Status: ❔ unverified
- Payload: `result: NeighborhoodInviteResult`, `pendingInviteList: string[]?`
- fires synchronously (Blizzard's docs)

### PURCHASE_PLOT_RESULT

- Status: ❔ unverified
- Payload: `result: number`
- fires synchronously (Blizzard's docs)

### SHOW_PLAYER_EVICTED_DIALOG

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_BULLETIN_BOARD_MEMBER_TYPE

- Status: ❔ unverified
- Payload: `player: WOWGUID`, `residentType: ResidentType`
- fires synchronously (Blizzard's docs)

### UPDATE_BULLETIN_BOARD_ROSTER

- Status: ❔ unverified
- Payload: `neighborhoodInfo: NeighborhoodInfo`, `rosterMemberList: NeighborhoodRosterMemberInfo[]`
- fires synchronously (Blizzard's docs)

### UPDATE_BULLETIN_BOARD_ROSTER_STATUSES

- Status: ❔ unverified
- Payload: `rosterMemberList: NeighborhoodRosterMemberUpdateInfo[]`
- fires synchronously (Blizzard's docs)

## Types

### CornerstonePurchaseMode

- Enumeration — ❔ unverified
  - `Basic` = 0
  - `Import` = 1
  - `Move` = 2
