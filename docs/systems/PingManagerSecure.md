# PingManagerSecure

Namespace: `C_PingSecure`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ⛔ | [C_PingSecure.ClearHitTestPingInfo](#c_pingsecureclearhittestpinginfo) |  |  |
| ⛔ | [C_PingSecure.CreateFrame](#c_pingsecurecreateframe) |  |  |
| ⛔ | [C_PingSecure.DisplayError](#c_pingsecuredisplayerror) |  |  |
| ⛔ | [C_PingSecure.GetTargetPingReceiver](#c_pingsecuregettargetpingreceiver) |  |  |
| ⛔ | [C_PingSecure.SendHitTestPing](#c_pingsecuresendhittestping) |  |  |
| ⛔ | [C_PingSecure.SendPlayerItemPing](#c_pingsecuresendplayeritemping) |  |  |
| ⛔ | [C_PingSecure.SendPlayerSpellCategoryPing](#c_pingsecuresendplayerspellcategoryping) |  |  |
| ⛔ | [C_PingSecure.SendPlayerSpellPing](#c_pingsecuresendplayerspellping) |  |  |
| ⛔ | [C_PingSecure.SendUnitPing](#c_pingsecuresendunitping) |  |  |
| ⛔ | [C_PingSecure.SetHitTestPingTarget](#c_pingsecuresethittestpingtarget) |  |  |
| ⛔ | [C_PingSecure.SetHitTestTargetAndSendPing](#c_pingsecuresethittesttargetandsendping) |  |  |
| ⛔ | [C_PingSecure.SetPendingPingOffScreenCallback](#c_pingsecuresetpendingpingoffscreencallback) |  |  |
| ⛔ | [C_PingSecure.SetPingCooldownStartedCallback](#c_pingsecuresetpingcooldownstartedcallback) |  |  |
| ⛔ | [C_PingSecure.SetPingPinFrameAddedCallback](#c_pingsecuresetpingpinframeaddedcallback) |  |  |
| ⛔ | [C_PingSecure.SetPingPinFrameRemovedCallback](#c_pingsecuresetpingpinframeremovedcallback) |  |  |
| ⛔ | [C_PingSecure.SetPingPinFrameScreenClampStateUpdatedCallback](#c_pingsecuresetpingpinframescreenclampstateupdatedcallback) |  |  |
| ⛔ | [C_PingSecure.SetPingRadialWheelCreatedCallback](#c_pingsecuresetpingradialwheelcreatedcallback) |  |  |
| ⛔ | [C_PingSecure.SetSendMacroPingCallback](#c_pingsecuresetsendmacropingcallback) |  |  |
| ⛔ | [C_PingSecure.SetTogglePingListenerCallback](#c_pingsecuresettogglepinglistenercallback) |  |  |

### C_PingSecure.ClearHitTestPingInfo

`C_PingSecure.ClearHitTestPingInfo()`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.CreateFrame

`C_PingSecure.CreateFrame()`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.DisplayError

`C_PingSecure.DisplayError(error: cstring)`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.GetTargetPingReceiver

`C_PingSecure.GetTargetPingReceiver(mousePosX: number, mousePosY: number) → frame: ScriptRegion`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SendHitTestPing

`C_PingSecure.SendHitTestPing(type: PingSubjectType?) → result: SendPingResult`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SendPlayerItemPing

`C_PingSecure.SendPlayerItemPing(itemID: number) → result: SendPingResult`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SendPlayerSpellCategoryPing

`C_PingSecure.SendPlayerSpellCategoryPing(spellCategoryID: number) → result: SendPingResult`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SendPlayerSpellPing

`C_PingSecure.SendPlayerSpellPing(spellID: number) → result: SendPingResult`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SendUnitPing

`C_PingSecure.SendUnitPing(target: WOWGUID, type: PingSubjectType?, isPlayerResource: bool?) → result: SendPingResult`

- Status: ⛔ in Blizzard's docs, not in game
- `isPlayerResource`: Player unit frame contextual pings have the optional ability to call out the player's health and in some cases mana. This field does nothing for non player pings.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SetHitTestPingTarget

`C_PingSecure.SetHitTestPingTarget(mousePosX: number, mousePosY: number, forcePointPing: bool?) → state: PingSetTargetState`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SetHitTestTargetAndSendPing

`C_PingSecure.SetHitTestTargetAndSendPing() → result: SendPingResult`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SetPendingPingOffScreenCallback

`C_PingSecure.SetPendingPingOffScreenCallback(cb: PendingPingOffScreenCallback)`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SetPingCooldownStartedCallback

`C_PingSecure.SetPingCooldownStartedCallback(cb: PingCooldownStartedCallback)`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SetPingPinFrameAddedCallback

`C_PingSecure.SetPingPinFrameAddedCallback(cb: PingPinFrameAddedCallback)`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SetPingPinFrameRemovedCallback

`C_PingSecure.SetPingPinFrameRemovedCallback(cb: PingPinFrameRemovedCallback)`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SetPingPinFrameScreenClampStateUpdatedCallback

`C_PingSecure.SetPingPinFrameScreenClampStateUpdatedCallback(cb: PingPinFrameScreenClampStateUpdatedCallback)`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SetPingRadialWheelCreatedCallback

`C_PingSecure.SetPingRadialWheelCreatedCallback(cb: PingRadialWheelCreatedCallback)`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SetSendMacroPingCallback

`C_PingSecure.SetSendMacroPingCallback(cb: SendMacroPingCallback)`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

### C_PingSecure.SetTogglePingListenerCallback

`C_PingSecure.SetTogglePingListenerCallback(cb: TogglePingListenerCallback)`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerSecureDocumentation.lua`

## Events

### UNIT_PING_PIN_ADDED

- Status: ✅ verified
- Payload: `guid: WOWGUID`, `uiTextureKit: textureKit`
- restricted in some situations (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- ⛔ Add-ons may not register it: RegisterEvent raised ADDON_ACTION_FORBIDDEN

### UNIT_PING_PIN_REMOVED

- Status: ✅ verified
- Payload: `guid: WOWGUID`
- restricted in some situations (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- ⛔ Add-ons may not register it: RegisterEvent raised ADDON_ACTION_FORBIDDEN

## Types

### PendingPingOffScreenCallback

- CallbackType

### PingActionCooldownUIInfo

- Structure
  - `durationMs`: number
  - `remainingMs`: number

### PingActionUIInfo

- Structure
  - `spellID`: number
  - `itemID`: number
  - `textureFileDataID`: number
  - `cooldownInfo`: PingActionCooldownUIInfo?
  - `spellCategoryID`: number

### PingCooldownStartedCallback

- CallbackType

### PingPinFrameAddedCallback

- CallbackType

### PingPinFrameRemovedCallback

- CallbackType

### PingPinFrameScreenClampStateUpdatedCallback

- CallbackType

### PingRadialWheelCreatedCallback

- CallbackType

### SendMacroPingCallback

- CallbackType

### SendPingResult

- Structure
  - `type`: PingSubjectType?
  - `result`: PingResult

### TogglePingListenerCallback

- CallbackType
