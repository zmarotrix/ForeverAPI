# CVars and console commands

From `C_Console.GetAllCommands` in game. Defaults only; the probe never reads current values.

| Name | Default | Category | Help |
|---|---|---|---|
| `accessibilityScreenNarrationEnabled` | `1` | 4 | Enables screen narration for accessibility |
| `accessibilityScreenNarrationSpeechRate` | `0` | 4 | Speed at which voice narration speaks |
| `accessibilityScreenNarrationSpeechVolume` | `100` | 4 | Volume at which voice narration speaks |
| `accessibilityScreenNarrationVoice` | `1` | 4 | Voice option used with screen narration |
| `accountNeedsTurnStrafeDialog` | `1` | 4 | Whether the account needs to show dialog that turn and strafe keybinds have changed |
| `acknowledgedArrowCallouts` | `0` | 4 | Bit field of Looking for guild player settings |
| `ActionButtonUseKeyDown` | `1` | 4 | Activate the action button on a keydown |
| `ActionButtonUseKeyHeldSpell` | `0` | 4 | Activate the press and hold cast option on a keydown |
| `ActionCam` |  | 4 |  |
| `ActionCombatCameraEnable` | `0` | 5 | enable/disable action combat camera. (default: disabled) |
| `actionedAdventureJournalEntries` |  | 4 | Which adventure journal entries flagged with ADVENTURE_JOURNAL_HIDE_AFTER_ACTION the user acted upon |
| `addFriendInfoShown` | `0` | 4 | The info for Add Friend has been shown |
| `addonChallengeModeRestrictionsForced` | `0` | 4 | If set, APIs guarded by challenge mode and mythic plus status will be restricted, or may return secrets. |
| `addonChatRestrictionsForced` | `0` | 4 | If set, APIs guarded by in lockdown will be restricted, or may return secrets. |
| `addonCombatRestrictionsForced` | `0` | 4 | If set, APIs guarded in combat will be restricted, or may return secrets. |
| `addonEncounterRestrictionsForced` | `0` | 4 | If set, APIs guarded in active encounters will be restricted, or may return secrets. |
| `addonLoadDebugging` | `0` | 0 | 0: Disable addon load logging (Default), 1: Enable addon load logging to AddOnLoad.log. |
| `addonMapRestrictionsForced` | `0` | 4 | If set, APIs guarded by current map type will be restricted, or may return secrets. |
| `addonPerformanceMsgError` | `0.000000` | 4 | Threshold for when a performance error is shown for a specific AddOn as a percentage of application performance. |
| `addonPerformanceMsgOverall` | `0.000000` | 4 | Threshold for when an performance error is shown for all AddOns overall as a percentage of application performance. |
| `addonPerformanceMsgWarning` | `0.000000` | 4 | Threshold for when a performance warning is shown for a specific AddOn as a percentage of application performance. |
| `addonPvPMatchRestrictionsForced` | `0` | 4 | If set, APIs guarded by PvP match state will be restricted, or may return secrets. |
| `advancedCombatLogging` | `0` | 4 | Whether we want advanced combat log data sent from the server |
| `AdvFlyingDynamicFOVEnabled` | `1` | 4 | Enables adjustment of camera field of view based on gliding speed |
| `advFlyKeyboardMaxPitchFactor` | `5.000000` | 4 | Modifies the maximum pitch rate when using advFlyKeyboard. |
| `advFlyKeyboardMaxTurnFactor` | `8.000000` | 4 | Modifies the maximum turn rate when using advFlyKeyboard. |
| `advFlyKeyboardMinPitchFactor` | `2.500000` | 4 | Modifies the minimum pitch rate when using advFlyKeyboard. |
| `advFlyKeyboardMinTurnFactor` | `5.000000` | 4 | Modifies the minimum turn rate when using advFlyKeyboard. |
| `advFlyPitchControl` | `3` | 4 | Modifies forward/backwards inputs to control pitch when Dragonriding. |
| `advFlyPitchControlCameraChase` | `20.000000` | 4 | Modifies the speed at which camera pitch follows player pitch while dragonriding with forward/backward pitch control. |
| `advFlyPitchControlGroundDebounce` | `0` | 4 | If enabled, will debounce forwards/backwards inputs used to control pitch when transitioning between dragonriding and grounded. |
| `agentUID` |  | 4 | The UID provided by Battle.net to be passed to Agent |
| `AIBrain` | `0` | 5 |  |
| `AIController` | `0` | 5 |  |
| `AIControllerEventLog` | `0` | 5 |  |
| `AIEventLog` | `0` | 5 |  |
| `allowCompareWithToggle` | `1` | 4 |  |
| `allowDevPublicKey` | `0` | 6 | Enable to allow the use of the Dev key instead of the one sourced from static. |
| `AllowSoftwareRenderer` | `0` | 1 | Allows WoW to run without a GPU. Performance will be very bad |
| `AllowSoftwareRendererDX12` | `0` | 1 | DX11 software render is used by default, due to issues with the DX12 software renderer |
| `AllowSpectateMode` | `1` | 4 | Enables spectate/commentator camera to be used. |
| `AllowWinRT` | `0` | 5 | Disable if WoW is crashing due to issues with the Windows GameBar |
| `alwaysCompareItems` | `1` | 4 | Always show item comparison tooltips |
| `alwaysShowRuneIcons` | `0` | 10 | Show the rune icons on equipment at all times, as opposed to only when the rune UI is open. |
| `animFrameSkipLOD` | `0` | 1 | animations will skip frames at distance |
| `arachnophobiaMode` | `0` | 4 | Swaps out spider creatures for other variants |
| `AreaTriggerEventLog` | `0` | 5 |  |
| `AreaTriggers` | `0` | 5 |  |
| `assaoAdaptiveQualityLimit` | `.45` | 1 | ASSAO Adaptive Quality Limit [0.0, 1.0] (only for Quality Level 3) |
| `assaoBlurPassCount` | `2` | 1 | ASSAO Blur Pass Count [  0,   6] Number of edge-sensitive smart blur passes to apply. Quality 0 is an exception with only one 'dumb' blur pass used. |
| `assaoDetailShadowStrength` | `0` | 1 | ASSAO Detail Shadow Strength [0.0, 5.0] Used for high-res detail AO using neighboring depth pixels: adds a lot of detail but also reduces temporal stability (adds aliasing). |
| `assaoFadeOutFrom` | `50.0` | 1 | ASSAO Fade Out From [0.0,  ~ ] Distance to start start fading out the effect. |
| `assaoFadeOutTo` | `300.0` | 1 | ASSAO Fade Out To [0.0,  ~ ] Distance at which the effect is faded out. |
| `assaoHorizonAngleThresh` | `0.4` | 1 | ASSAO Horizon Angle Thresh [0.0, 0.2] Limits self-shadowing |
| `assaoNormals` | `1` | 1 | Use Normals for ASSAO |
| `assaoRadius` | `1.85` | 1 | ASSAO Radius [0.01,  100,000] World (view) space size of the occlusion sphere |
| `assaoShadowClamp` | `.98` | 1 | ASSAO Shadow Clamp [0.0, 1.0] |
| `assaoShadowMult` | `1.1` | 1 | ASSAO Shadow Multiplier [0.0, 5.0] Effect strength linear multiplier |
| `assaoShadowPower` | `1.34` | 1 | ASSAO Shadow Power [0.5, 5.0] Effect strength pow modifier |
| `assaoSharpness` | `.98` | 1 | ASSAO Sharpness [0.0, 1.0] (How much to bleed over edges; 1: not at all, 0.5: half-half; 0.0: completely ignore edges) |
| `assaoTemporalSSAngleOffset` | `0.0` | 1 | ASSAO Temporal Super Sampling Angle Offset [0.0,  PI] Used to rotate sampling kernel; If using temporal AA / supersampling, suggested to rotate by ( (frame%3)/3.0*PI ) or similar. Kernel is already symmetrical, which is why we use PI and not 2*PI. |
| `assaoTemporalSSRadiusOffset` | `1.0` | 1 | ASSAO Temporal Super Sampling Radius Offset [0.0, 2.0] Used to scale sampling kernel; If using temporal AA / supersampling, suggested to scale by ( 1.0f + (((frame%3)-1.0)/3.0)*0.1 ) or similar. |
| `assistAttack` | `0` | 4 | Whether to start attacking after an assist |
| `assistedCombatHighlight` | `0` | 4 | If enabled, a highlight will be displayed on the next spell that should be cast in combat |
| `assistedCombatHighlightRPE` | `0` | 4 | Will be true if Assisted Highlight was automatically enabled by RPE. Will reset when leaving RPE. |
| `assistedCombatIconUpdateRate` | `0.100000` | 4 | How often (in seconds) to update the icon on the action bar, 0 for every frame, max 1 second |
| `assistedCombatReduceHighlights` | `1` | 4 | Reduces spell alert animations when Single-Button Assistant is on an action bar |
| `AsyncAssistActions` | `0` | 5 |  |
| `asyncHandlerTimeout` | `100` | 1 | Engine option: Async read main thread timeout |
| `asyncThreadSleep` | `0` | 1 | Engine option: Async read thread sleep |
| `auctionHouseDurationDropdown` | `2` | 4 | The previously selected duration index in the auction house duration dropdown |
| `audioLocale` |  | 4 | Set the game locale for audio content |
| `AuraDebugger` | `0` | 5 |  |
| `AuraEventLog` | `0` | 5 |  |
| `autoAcceptQuickJoinRequests` | `0` | 4 | Whether or not to auto-accept players who are trying to join your party through quick join |
| `autoClearAFK` | `1` | 4 | Automatically clear AFK when moving or chatting |
| `autoCompleteResortNamesOnRecency` | `1` | 4 | Shows people you recently spoke with higher up on the AutoComplete list. |
| `autoCompleteUseContext` | `1` | 4 | The system will, for example, only show people in your guild when you are typing /gpromote. Names will also never be removed. |
| `autoCompleteWhenEditingFromCenter` | `1` | 4 | If you edit a name by inserting characters into the center, a smarter auto-complete will occur. |
| `autoDismount` | `1` | 4 | Automatically dismount when needed |
| `autoDismountFlying` | `0` | 4 | If enabled, your character will automatically dismount before casting while flying |
| `autoFilledMultiCastSlots` | `0` | 4 | Bitfield that saves whether multi-cast slots have been automatically filled. |
| `autoInteract` | `0` | 4 | Toggles auto-move to interact target |
| `autojoinBGVoice` | `0` | 7 | Automatically join the voice session in battleground chat |
| `autojoinPartyVoice` | `0` | 7 | Automatically join the voice session in party/raid chat |
| `autoLootDefault` | `0` | 4 | Automatically loot items when the loot window opens |
| `autoLootRate` | `150` | 4 | Rate in milliseconds to tick auto loot |
| `AutoPushSpellToActionBar` | `1` | 4 | Determines if spells are automatically pushed to the Action Bar. 0: No, 1: Yes (default). |
| `autoQuestPopUps` |  | 4 | Saves current pop-ups for quests that are automatically acquired or completed. |
| `autoQuestProgress` | `1` | 4 | Whether to automatically watch all quests when they are updated |
| `autoQuestWatch` | `1` | 4 | Whether to automatically watch all quests when you obtain them |
| `autoRangedCombat` | `1` | 4 | If enabled, your character will automatically switch between auto attack and auto shot. |
| `autoSelfCast` | `1` | 4 | Whether spells should automatically be cast on you if you don't have a valid target |
| `autoStand` | `1` | 4 | Automatically stand when needed |
| `autoUnshift` | `1` | 4 | Automatically leave shapeshift form when needed |
| `bankAutoDepositReagents` | `1` | 4 | Stores whether to include reagents when auto depositing items into your bank |
| `bankConfirmTabCleanUp` | `1` | 4 | Stores whether to show a confirmation dialog when you click the button to auto clean up your bank tabs |
| `BeckonTriggerEventlog` | `0` | 5 |  |
| `BehaviorTree` | `0` | 5 |  |
| `BlizzCon2026ColdSwapFeatureEnabled` | `1` | 10 | Feature flag for ColdSwap. |
| `BlizzCon2026Experience` | `0` | 10 | Which experience the system is currently targeting. |
| `blockChannelInvites` | `0` | 4 | Whether to automatically block chat channel invites |
| `blockTrades` | `0` | 4 | Whether to automatically block trade requests |
| `bloomEnable` | `0` | 1 | Enable/disable bloom |
| `bloomUserMult` | `1.000000` | 5 |  |
| `bodyQuota` | `100` | 1 | Maximum number of componented bodies seen at once |
| `breakUpLargeNumbers` | `1` | 4 | Toggles using commas in large numbers |
| `Brightness` | `50.000000` | 5 |  |
| `buffDurations` | `1` | 4 | Whether to show buff durations |
| `CAADebuffSelfAlert` | `0` | 4 | Announce when a dispellable debuff is applied to the player using a special format (0=off) |
| `CAAEnabled` | `0` | 4 | Enable or disable combat audio alerts |
| `CAAInterruptCast` | `0` | 4 | Announce when the target starts casting something interruptible |
| `CAAInterruptCastSuccess` | `0` | 4 | Announce when the target's cast is interrupted |
| `CAAPartyHealthFrequency` | `0` | 4 | Relative frequency at which party health combat audio alerts are read (-10 to 10). -10 halves the frequency and 10 doubles it |
| `CAAPartyHealthPercent` | `0` | 4 | Announce party member indices to indicate current health when it's below X percent. Frequency of announcements are affected by remaining health and CAAPartyHealthFrequencySpeed |
| `CAAPartyHealthVoice` | `0` | 4 | Voice to use for party health combat audio alerts |
| `CAAPartyHealthVolume` | `100` | 4 | Volume of party health combat audio alerts (0 to 100) |
| `CAAPlayerCastFormat` | `4` | 4 | Format string to use when reading the player's casts |
| `CAAPlayerCastMinTime` | `1.500000` | 4 | The player's casts will only be read out if they have a cast time >= this |
| `CAAPlayerCastMode` | `0` | 4 | When the player's casts should be announced (0=off, 1=cast start, 2=cast end) |
| `CAAPlayerCastThrottle` | `0.000000` | 4 | The player's casts will only be read every X seconds at most |
| `CAAPlayerCastVoice` | `0` | 4 | Voice to use for player cast combat audio alerts |
| `CAAPlayerCastVolume` | `100` | 4 | Volume of player cast combat audio alerts (0 to 100) |
| `CAAPlayerHealthFormat` | `1` | 4 | Format string to use when reading the player's health |
| `CAAPlayerHealthPercent` | `0` | 4 | Announce player health every X percent |
| `CAAPlayerHealthThrottle` | `0.000000` | 4 | The player's health will only be read every X seconds at most |
| `CAAPlayerHealthVoice` | `0` | 4 | Voice to use for player health combat audio alerts |
| `CAAPlayerHealthVolume` | `100` | 4 | Volume of player health combat audio alerts (0 to 100) |
| `CAAPulsePlayerHealthPercent` | `0` | 4 | Play a looping pulse sound once the player's health is below X percent. The pulse gets faster as health drops |
| `CAAPulsePlayerHealthVolume` | `100` | 4 | Volume of the player health pulse combat audio alert (0 to 100) |
| `CAAResource1Formats` |  | 4 | Stores the format string to use (for each spec) when announcing the player's first resource |
| `CAAResource1Percents` |  | 4 | Stores the percentage band sizes to use (for each spec) when announcing the player's first resource  |
| `CAAResource1Throttle` | `0.000000` | 4 | Updates to the player's first resource will only be read every X seconds at most |
| `CAAResource1Voice` |  | 4 | Stores the voice to use (for each spec) when announcing the player's first resource |
| `CAAResource1Volume` |  | 4 | Stores the volume to use (for each spec) when announcing the player's first resource (0 to 100) |
| `CAAResource2Formats` |  | 4 | Stores the format string to use (for each spec) when announcing the player's second resource |
| `CAAResource2Percents` |  | 4 | Stores the percentage band sizes to use (for each spec) when announcing the player's second resource |
| `CAAResource2Throttle` | `0.000000` | 4 | Updates to the player's second resource will only be read every X seconds at most |
| `CAAResource2Voice` |  | 4 | Stores the voice to use (for each spec) when announcing the player's second resource |
| `CAAResource2Volume` |  | 4 | Stores the volume to use (for each spec) when announcing the player's second resource (0 to 100) |
| `CAASayCombatEnd` | `1` | 4 | Announce when combat ends |
| `CAASayCombatStart` | `1` | 4 | Announce when combat starts |
| `CAASayIfTargeted` |  | 4 | Stores the 'say if targeted' settings for each spec |
| `CAASayTargetName` | `1` | 4 | Say the target's name when a new target is selected |
| `CAASayYourDebuffs` | `1` | 4 | Announce when a debuff is applied to the player |
| `CAASayYourDebuffsFormat` | `0` | 4 | Format string to use when announcing debuffs applied to the player |
| `CAASayYourDebuffsMinDuration` | `1.500000` | 4 | Minimum duration of debuffs to be announced (0 means all debuffs) |
| `CAASayYourDebuffsVoice` | `0` | 4 | Voice to use for player debuff combat audio alerts |
| `CAASayYourDebuffsVolume` | `100` | 4 | Volume of player debuff combat audio alerts (0 to 100) |
| `CAASpeed` | `0` | 4 | Speed at which combat audio alerts are read (-10 to 10) |
| `CAATargetCastFormat` | `0` | 4 | Format string to use when reading the target's casts |
| `CAATargetCastMinTime` | `1.500000` | 4 | The target's casts will only be read out if they have a cast time >= this |
| `CAATargetCastMode` | `0` | 4 | When the target's casts should be announced (0=off, 1=cast start, 2=cast end) |
| `CAATargetCastThrottle` | `0.000000` | 4 | The target's casts will only be read every X seconds at most |
| `CAATargetCastVoice` | `0` | 4 | Voice to use for target cast combat audio alerts |
| `CAATargetCastVolume` | `100` | 4 | Volume of target cast combat audio alerts (0 to 100) |
| `CAATargetDeathBehavior` | `0` | 4 | Behavior of announcement when target dies (0=default, 1=target dead) |
| `CAATargetHealthFormat` | `3` | 4 | Format string to use when reading the target's health |
| `CAATargetHealthPercent` | `2` | 4 | Announce target health every X percent |
| `CAATargetHealthThrottle` | `0.000000` | 4 | The target's health will only be read every X seconds at most |
| `CAATargetHealthVoice` | `0` | 4 | Voice to use for target health combat audio alerts |
| `CAATargetHealthVolume` | `100` | 4 | Volume of target health combat audio alerts (0 to 100) |
| `CAAVoice` | `0` | 4 | Primary voice to use for combat audio alerts |
| `CAAVolume` | `100` | 4 | Volume of combat audio alerts (0 to 100) |
| `CACHE-WGOB-GameObjectsHotfixCount` |  | 5 |  |
| `CACHE-WGOB-GameObjectsRecordCount` |  | 5 |  |
| `CACHE-WQST-QuestObjectiveHotfixCount` |  | 5 |  |
| `CACHE-WQST-QuestObjectiveRecordCount` |  | 5 |  |
| `CACHE-WQST-QuestObjectiveXEffectHotfixCount` |  | 5 |  |
| `CACHE-WQST-QuestObjectiveXEffectRecordCount` |  | 5 |  |
| `CACHE-WQST-QuestV2HotfixCount` |  | 5 |  |
| `CACHE-WQST-QuestV2RecordCount` |  | 5 |  |
| `calendarShowBattlegrounds` | `1` | 4 | Whether Battleground holidays should appear in the calendar |
| `calendarShowDarkmoon` | `1` | 4 | Whether Darkmoon Faire holidays should appear in the calendar |
| `calendarShowHolidays` | `1` | 4 | Whether holidays should appear in the calendar |
| `calendarShowLockouts` | `1` | 4 | Whether raid lockouts should appear in the calendar |
| `calendarShowResets` | `0` | 4 | Whether raid resets should appear in the calendar |
| `calendarShowWeeklyHolidays` | `1` | 4 | Whether weekly holidays should appear in the calendar |
| `cameraBobbing` | `0` | 4 |  |
| `cameraBobbingSmoothSpeed` | `0.800000` | 4 |  |
| `cameraCustomViewSmoothing` | `0` | 4 |  |
| `cameraDistanceMaxZoomFactor` | `1.000000` | 4 |  |
| `cameraDistanceRateMult` | `1.000000` | 4 |  |
| `cameraDive` | `1` | 4 |  |
| `CameraFollowGamepadAdjustDelay` | `1.000000` | 4 | Delay before follow resuming after manually adjusting the camera with Gamepad input |
| `CameraFollowGamepadAdjustEaseIn` | `1.000000` | 4 | Ease-in time for follow resuming after manually adjusting the camera with Gamepad input |
| `CameraFollowOnStick` | `0` | 4 | Enable camera to follow target as though being pushed/pulled along on a stick |
| `CameraFollowPitchDeadZone` | `5.000000` | 4 | Controls pitch follow deadzone size |
| `CameraFollowPitchOffset` | `15.000000` | 4 | Controls the pitch offset in degrees that the camera will move towards |
| `CameraFollowPitchSpeed` | `1.000000` | 4 | Controls speed of pitch following |
| `CameraFollowPitchStrength` | `0.700000` | 4 | Controls strength of pitch following |
| `CameraFollowSnapCharacterAngle` | `45.000000` | 4 | Angle beyond which character will snap to camera's facing when moving |
| `CameraFollowTargetCombat` | `1` | 4 | Camera follow the locked target only during combat. |
| `CameraFollowYawSpeed` | `1.000000` | 4 | Controls speed of yaw following |
| `cameraFov` | `90.000000` | 1 | Default camera field of view |
| `cameraFoVSmoothSpeed` | `0.500000` | 4 |  |
| `cameraGroundSmoothSpeed` | `7.500000` | 4 |  |
| `cameraHeightIgnoreStandState` | `0` | 4 |  |
| `cameraIndirectOffset` | `6.000000` | 4 |  |
| `cameraIndirectVisibility` | `1` | 4 |  |
| `CameraKeepCharacterCentered` | `1` | 4 | Motion sickness control to keep character's head at center of screen to act as motion reference point. Can override other cvar settings. |
| `cameraPitchMoveSpeed` | `90.000000` | 4 |  |
| `cameraPitchSmoothMax` | `23.000000` | 4 |  |
| `cameraPitchSmoothMin` | `0.000000` | 4 |  |
| `cameraPitchSmoothSpeed` | `45.000000` | 4 |  |
| `cameraPivot` | `1` | 4 |  |
| `cameraPivotDXMax` | `0.050000` | 4 |  |
| `cameraPivotDYMin` | `0.000000` | 4 |  |
| `CameraReduceUnexpectedMovement` | `0` | 4 | Motion sickness control to reduce camera movement without player input. Can override other cvar settings. |
| `cameraSavedDistance` | `5.550000` | 4 |  |
| `cameraSavedPetBattleDistance` | `10.000000` | 4 |  |
| `cameraSavedPitch` | `10.000000` | 4 |  |
| `cameraSavedVehicleDistance` | `-1.000000` | 4 |  |
| `cameraSmooth` | `1` | 4 |  |
| `cameraSmoothAlwaysFearDelay` | `0.000000` | 4 |  |
| `cameraSmoothAlwaysFearFactor` | `1.000000` | 4 |  |
| `cameraSmoothAlwaysIdleDelay` | `0.000000` | 4 |  |
| `cameraSmoothAlwaysIdleFactor` | `1.000000` | 4 |  |
| `cameraSmoothAlwaysMoveDelay` | `0.000000` | 4 |  |
| `cameraSmoothAlwaysMoveFactor` | `1.000000` | 4 |  |
| `cameraSmoothAlwaysStopDelay` | `0.000000` | 4 |  |
| `cameraSmoothAlwaysStopFactor` | `1.000000` | 4 |  |
| `cameraSmoothAlwaysStrafeDelay` | `0.000000` | 4 |  |
| `cameraSmoothAlwaysStrafeFactor` | `1.000000` | 4 |  |
| `cameraSmoothAlwaysTrackDelay` | `0.000000` | 4 |  |
| `cameraSmoothAlwaysTrackFactor` | `1.000000` | 4 |  |
| `cameraSmoothAlwaysTurnDelay` | `0.000000` | 4 |  |
| `cameraSmoothAlwaysTurnFactor` | `1.000000` | 4 |  |
| `cameraSmoothNeverFearDelay` | `0.000000` | 4 |  |
| `cameraSmoothNeverFearFactor` | `0.000000` | 4 |  |
| `cameraSmoothNeverIdleDelay` | `0.000000` | 4 |  |
| `cameraSmoothNeverIdleFactor` | `0.000000` | 4 |  |
| `cameraSmoothNeverMoveDelay` | `0.000000` | 4 |  |
| `cameraSmoothNeverMoveFactor` | `0.000000` | 4 |  |
| `cameraSmoothNeverStopDelay` | `0.000000` | 4 |  |
| `cameraSmoothNeverStopFactor` | `0.000000` | 4 |  |
| `cameraSmoothNeverStrafeDelay` | `0.000000` | 4 |  |
| `cameraSmoothNeverStrafeFactor` | `0.000000` | 4 |  |
| `cameraSmoothNeverTrackDelay` | `0.000000` | 4 |  |
| `cameraSmoothNeverTrackFactor` | `0.000000` | 4 |  |
| `cameraSmoothNeverTurnDelay` | `0.000000` | 4 |  |
| `cameraSmoothNeverTurnFactor` | `0.000000` | 4 |  |
| `cameraSmoothPitch` | `1` | 4 |  |
| `cameraSmoothSmarterFearDelay` | `0.400000` | 4 |  |
| `cameraSmoothSmarterFearFactor` | `10.000000` | 4 |  |
| `cameraSmoothSmarterIdleDelay` | `0.000000` | 4 |  |
| `cameraSmoothSmarterIdleFactor` | `0.000000` | 4 |  |
| `cameraSmoothSmarterMoveDelay` | `0.000000` | 4 |  |
| `cameraSmoothSmarterMoveFactor` | `1.000000` | 4 |  |
| `cameraSmoothSmarterStopDelay` | `0.000000` | 4 |  |
| `cameraSmoothSmarterStopFactor` | `0.000000` | 4 |  |
| `cameraSmoothSmarterStrafeDelay` | `0.000000` | 4 |  |
| `cameraSmoothSmarterStrafeFactor` | `1.000000` | 4 |  |
| `cameraSmoothSmarterTrackDelay` | `0.400000` | 4 |  |
| `cameraSmoothSmarterTrackFactor` | `10.000000` | 4 |  |
| `cameraSmoothSmarterTurnDelay` | `0.000000` | 4 |  |
| `cameraSmoothSmarterTurnFactor` | `1.000000` | 4 |  |
| `cameraSmoothSmartFearDelay` | `0.400000` | 4 |  |
| `cameraSmoothSmartFearFactor` | `10.000000` | 4 |  |
| `cameraSmoothSmartIdleDelay` | `0.000000` | 4 |  |
| `cameraSmoothSmartIdleFactor` | `0.000000` | 4 |  |
| `cameraSmoothSmartMoveDelay` | `0.000000` | 4 |  |
| `cameraSmoothSmartMoveFactor` | `1.000000` | 4 |  |
| `cameraSmoothSmartStopDelay` | `0.000000` | 4 |  |
| `cameraSmoothSmartStopFactor` | `0.000000` | 4 |  |
| `cameraSmoothSmartStrafeDelay` | `0.000000` | 4 |  |
| `cameraSmoothSmartStrafeFactor` | `1.000000` | 4 |  |
| `cameraSmoothSmartTrackDelay` | `0.400000` | 4 |  |
| `cameraSmoothSmartTrackFactor` | `10.000000` | 4 |  |
| `cameraSmoothSmartTurnDelay` | `0.000000` | 4 |  |
| `cameraSmoothSmartTurnFactor` | `1.000000` | 4 |  |
| `cameraSmoothSplineFearDelay` | `0.000000` | 4 |  |
| `cameraSmoothSplineFearFactor` | `4.000000` | 4 |  |
| `cameraSmoothSplineIdleDelay` | `0.000000` | 4 |  |
| `cameraSmoothSplineIdleFactor` | `4.000000` | 4 |  |
| `cameraSmoothSplineMoveDelay` | `0.000000` | 4 |  |
| `cameraSmoothSplineMoveFactor` | `1.000000` | 4 |  |
| `cameraSmoothSplineStopDelay` | `0.000000` | 4 |  |
| `cameraSmoothSplineStopFactor` | `4.000000` | 4 |  |
| `cameraSmoothSplineStrafeDelay` | `0.000000` | 4 |  |
| `cameraSmoothSplineStrafeFactor` | `1.000000` | 4 |  |
| `cameraSmoothSplineTrackDelay` | `0.000000` | 4 |  |
| `cameraSmoothSplineTrackFactor` | `4.000000` | 4 |  |
| `cameraSmoothSplineTurnDelay` | `0.000000` | 4 |  |
| `cameraSmoothSplineTurnFactor` | `1.000000` | 4 |  |
| `cameraSmoothStyle` | `4` | 4 |  |
| `cameraSmoothTimeMax` | `2.000000` | 4 |  |
| `cameraSmoothTimeMin` | `0.100000` | 4 |  |
| `cameraSmoothTrackingStyle` | `4` | 4 |  |
| `cameraSmoothViewDataAlwaysDistanceDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataAlwaysDistanceFactor` | `0.000000` | 4 |  |
| `cameraSmoothViewDataAlwaysPitchDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataAlwaysPitchFactor` | `1.000000` | 4 |  |
| `cameraSmoothViewDataAlwaysYawDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataAlwaysYawFactor` | `1.000000` | 4 |  |
| `cameraSmoothViewDataNeverDistanceDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataNeverDistanceFactor` | `0.000000` | 4 |  |
| `cameraSmoothViewDataNeverPitchDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataNeverPitchFactor` | `0.000000` | 4 |  |
| `cameraSmoothViewDataNeverYawDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataNeverYawFactor` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSmartDistanceDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSmartDistanceFactor` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSmarterDistanceDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSmarterDistanceFactor` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSmarterPitchDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSmarterPitchFactor` | `1.000000` | 4 |  |
| `cameraSmoothViewDataSmarterYawDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSmarterYawFactor` | `1.000000` | 4 |  |
| `cameraSmoothViewDataSmartPitchDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSmartPitchFactor` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSmartYawDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSmartYawFactor` | `1.000000` | 4 |  |
| `cameraSmoothViewDataSplineDistanceDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSplineDistanceFactor` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSplinePitchDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSplinePitchFactor` | `1.000000` | 4 |  |
| `cameraSmoothViewDataSplineYawDelay` | `0.000000` | 4 |  |
| `cameraSmoothViewDataSplineYawFactor` | `1.000000` | 4 |  |
| `cameraSmoothYaw` | `1` | 4 |  |
| `cameraSubmergePitch` | `18.000000` | 4 |  |
| `cameraSurfacePitch` | `0.000000` | 4 |  |
| `cameraTargetSmoothSpeed` | `90.000000` | 4 |  |
| `cameraTerrainTilt` | `0` | 4 |  |
| `cameraTerrainTiltAlwaysFallAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysFallDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysFallFactor` | `0.750000` | 4 |  |
| `cameraTerrainTiltAlwaysFearAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysFearDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysFearFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysIdleAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysIdleDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysIdleFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysJumpAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysJumpDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysJumpFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysMoveAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysMoveDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysMoveFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysStrafeAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysStrafeDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysStrafeFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysSwimAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysSwimDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysSwimFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysTaxiAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysTaxiDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysTaxiFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysTrackAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysTrackDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysTrackFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysTurnAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltAlwaysTurnDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltAlwaysTurnFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltNeverFallAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverFallDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverFallFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltNeverFearAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverFearDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverFearFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltNeverIdleAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverIdleDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverIdleFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltNeverJumpAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverJumpDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverJumpFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltNeverMoveAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverMoveDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverMoveFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltNeverStrafeAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverStrafeDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverStrafeFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltNeverSwimAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverSwimDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverSwimFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltNeverTaxiAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverTaxiDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverTaxiFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltNeverTrackAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverTrackDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverTrackFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltNeverTurnAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverTurnDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltNeverTurnFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltSmarterFallAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterFallDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterFallFactor` | `0.750000` | 4 |  |
| `cameraTerrainTiltSmarterFearAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterFearDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterFearFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterIdleAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterIdleDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterIdleFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltSmarterJumpAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterJumpDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterJumpFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltSmarterMoveAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterMoveDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterMoveFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterStrafeAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterStrafeDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterStrafeFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterSwimAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterSwimDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterSwimFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterTaxiAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterTaxiDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterTaxiFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterTrackAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterTrackDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterTrackFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterTurnAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmarterTurnDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmarterTurnFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartFallAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartFallDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartFallFactor` | `0.750000` | 4 |  |
| `cameraTerrainTiltSmartFearAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartFearDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartFearFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartIdleAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartIdleDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartIdleFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltSmartJumpAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartJumpDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartJumpFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltSmartMoveAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartMoveDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartMoveFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartStrafeAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartStrafeDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartStrafeFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartSwimAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartSwimDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartSwimFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartTaxiAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartTaxiDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartTaxiFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartTrackAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartTrackDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartTrackFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartTurnAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSmartTurnDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSmartTurnFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineFallAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineFallDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineFallFactor` | `0.750000` | 4 |  |
| `cameraTerrainTiltSplineFearAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineFearDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineFearFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineIdleAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineIdleDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineIdleFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltSplineJumpAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineJumpDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineJumpFactor` | `-1.000000` | 4 |  |
| `cameraTerrainTiltSplineMoveAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineMoveDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineMoveFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineStrafeAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineStrafeDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineStrafeFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineSwimAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineSwimDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineSwimFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineTaxiAbsorb` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineTaxiDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineTaxiFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineTrackAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineTrackDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineTrackFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineTurnAbsorb` | `1.000000` | 4 |  |
| `cameraTerrainTiltSplineTurnDelay` | `0.000000` | 4 |  |
| `cameraTerrainTiltSplineTurnFactor` | `1.000000` | 4 |  |
| `cameraTerrainTiltTimeMax` | `10.000000` | 4 |  |
| `cameraTerrainTiltTimeMin` | `3.000000` | 4 |  |
| `cameraView` | `2` | 4 |  |
| `cameraViewBlendStyle` | `1` | 4 |  |
| `cameraWaterCollision` | `0` | 4 |  |
| `cameraYawMoveSpeed` | `180.000000` | 4 |  |
| `cameraYawSmoothMax` | `0.000000` | 4 |  |
| `cameraYawSmoothMin` | `0.000000` | 4 |  |
| `cameraYawSmoothSpeed` | `180.000000` | 4 |  |
| `cameraZoomSpeed` | `20.000000` | 4 |  |
| `cameraZSmooth` | `1` | 4 | Smooths camera vertical movement. 1 = only while moving, 2 = also while standing still |
| `canUseQuestItemWithLeftClick` | `0` | 4 | Whether you can use a quest item by left clicking on a relevant creature. |
| `casContainerSizeLimit` | `0` | 5 | Approximate limit in GB for the amount of game data to keep on disk at a time |
| `categorizeTrainerUI` | `0` | 4 | If true, shows categories for the trainer UI. |
| `characterFrameCollapsed` | `0` | 4 | Whether or not to show the character stats page |
| `characterNeedsTurnStrafeDialog` | `1` | 4 | Whether the character needs to show dialog that turn and strafe keybinds have changed |
| `characterSocialRestrictionSettingsApplied` | `0` | 4 | Have the character stored settings been set to their required values for AADC restrictions. |
| `ChatAmbienceVolume` | `0.3` | 7 | Ambience Volume (0.0 to 1.0) |
| `chatBubbles` | `1` | 4 | Whether to show in-game chat bubbles |
| `chatBubblesParty` | `1` | 4 | Whether to show in-game chat bubbles for party chat |
| `chatBubblesRaid` | `0` | 4 | Whether to show in-game chat bubbles for raid chat |
| `chatClassColorOverride` | `0` | 4 | Whether or not class names are colored in chat. 0 = always color by class name (where applicable), 1 = never color by class name, 2 = respect the legacy per-channel class color settings |
| `chatMouseScroll` | `1` | 4 | Whether the user can use the mouse wheel to scroll through chat |
| `ChatMusicVolume` | `0.3` | 7 | Music volume (0.0 to 1.0) |
| `ChatSoundVolume` | `0.4` | 7 | Sound volume (0.0 to 1.0) |
| `chatStyle` | `im` | 4 | The style of Edit Boxes for the ChatFrame. Valid values: "classic", "im" |
| `checkAddonVersion` | `1` | 4 | Check interface addon version number |
| `ChromaEffectsEnable` | `1` | 5 | Enable chroma effects on supported peripherals |
| `ChromaEffectsFactionColor` | `1` | 5 | Enable setting chroma base layer color to match current faction |
| `classicStyleWorldText` | `0` | 4 | Whether to have floating world text (such as combat text) display as it does in Classic or in Retail |
| `clear` |  | 2 | Clears the console buffer |
| `clearSeenCustomizationChoices` |  | 4 |  |
| `clearSeenDelvesCurios` |  | 4 |  |
| `ClientCastDebug` | `0` | 0 | debug client cast allocation |
| `ClientCastLimitDebug` | `100` | 0 | Limits the maximum allowed initiated casts in progress. |
| `ClientMessageEventLog` | `0` | 5 |  |
| `ClientSettings_AFTERMATH_BY_API_MASK` |  | 5 |  |
| `ClientSettings_AFTERMATH_BY_GPU_CATEGORY` |  | 5 |  |
| `ClientSettings_ASYNC_COMPUTE_BY_API_MASK` |  | 5 |  |
| `ClientSettings_ASYNC_COMPUTE_BY_GPU_CATEGORY` |  | 5 |  |
| `ClientSettings_ClusteredShading` |  | 5 |  |
| `ClientSettings_CMAA2` |  | 5 |  |
| `ClientSettings_CMD_LIST_MT_BY_API_MASK` |  | 5 |  |
| `ClientSettings_CMD_LIST_MT_BY_GPU_CATEGORY` |  | 5 |  |
| `ClientSettings_COPY_QUEUE_BY_API_MASK` |  | 5 |  |
| `ClientSettings_COPY_QUEUE_BY_GPU_CATEGORY` |  | 5 |  |
| `ClientSettings_CTexAsyncCreate` |  | 5 |  |
| `ClientSettings_FSR` |  | 5 |  |
| `ClientSettings_HIGH_MEM_FEATURES_BY_API_MASK` |  | 5 |  |
| `ClientSettings_HIGH_MEM_FEATURES_BY_GPU_CATEGORY` |  | 5 |  |
| `ClientSettings_LOW_LATENCY_CBS_BY_API_MASK` |  | 5 |  |
| `ClientSettings_LOW_LATENCY_CBS_BY_GPU_CATEGORY` |  | 5 |  |
| `ClientSettings_LowLatency` |  | 5 |  |
| `ClientSettings_LowVramActions` |  | 5 |  |
| `ClientSettings_MemoryAllocationTraces` |  | 5 |  |
| `ClientSettings_MSAA` |  | 5 |  |
| `ClientSettings_NeedsGxRestart` |  | 5 |  |
| `ClientSettings_OPT_FEATURES_BY_API_MASK` |  | 5 |  |
| `ClientSettings_OPT_FEATURES_BY_GPU_CATEGORY` |  | 5 |  |
| `ClientSettings_RAY_TRACING_BY_API_MASK` |  | 5 |  |
| `ClientSettings_RAY_TRACING_BY_GPU_CATEGORY` |  | 5 |  |
| `ClientSettings_RGB10A2_API` |  | 5 |  |
| `ClientSettings_RGB10A2_CAT` |  | 5 |  |
| `ClientSettings_RTShadows` |  | 5 |  |
| `ClientSettings_SHADER_MT_BY_API_MASK` |  | 5 |  |
| `ClientSettings_SHADER_MT_BY_GPU_CATEGORY` |  | 5 |  |
| `ClientSettings_SM6_BY_API_MASK` |  | 5 |  |
| `ClientSettings_SM6_BY_GPU_CATEGORY` |  | 5 |  |
| `ClientSettings_SpellClutter` |  | 5 |  |
| `ClientSettings_VolumeFog` |  | 5 |  |
| `ClientSettings_WORK_OPTIMS_BY_API_MASK` |  | 5 |  |
| `ClientSettings_WORK_OPTIMS_BY_GPU_CATEGORY` |  | 5 |  |
| `ClipCursor` | `0` | 5 | Lock the cursor to the game window |
| `cloakFixEnabled` | `1` | 5 |  |
| `closeconsole` |  | 2 | Closes the Console window |
| `closedExtraAbiltyTutorials` |  | 4 | Bitfield for which extra ability tutorials have been acknowledged by the user |
| `closedInfoFrames` |  | 4 | Bitfield for which help frames have been acknowledged by the user |
| `closedInfoFramesAccountWide` |  | 4 | Bitfield for which help frames have been acknowledged by the user (account-wide) |
| `closedRemixArtifactTutorialFrames` | `0` | 4 | Tutorial bitfield for which Remix Artifacts have been shown so far |
| `clubFinderCacheExpiry` | `1000` | 4 | Value in (MS) for time to expire the cache. |
| `clubFinderCachePendingExpiry` | `5000` | 4 | Value in (MS) for time to expire the cache. |
| `clubFinderPlayerLanguageSettings` | `0` | 4 | Bit field of Looking for club/guild player language settings |
| `clubFinderPlayerSettings` | `1` | 4 | Bit field of Looking for guild player settings |
| `clusteredShading` | `1` | 1 | Allow forward transparent lighting |
| `CMAA2ExtraSharpness` | `0` | 1 | Set to 1 to preserve even more text and shape clarity at the expense of less AA |
| `CMAA2HalfFloat` | `0` | 1 | 0: 32-bit Float. 1: 16-bit Float. |
| `CMAA2Quality` | `3` | 1 | CMAA2 Quality Level. 0 - LOW, 1 - MEDIUM, 2 - HIGH, 3 - ULTRA |
| `collapsedCurrencyCategoryDefaults` | `0` | 4 | Stores the IDs of currency categories that should be collapsed by default in the Token UI |
| `collapsedReputationHeaderDefaults` |  | 4 | Stores the IDs of headers that should be collapsed by default in the Reputation Panel |
| `collapseExpandBuffs` | `1` | 4 | Enables a button to collapse and hide long duration buffs. |
| `Collision` | `0` | 5 |  |
| `colorblindMode` | `0` | 4 | Enables colorblind accessibility features in the game |
| `colorblindSimulator` | `0` | 1 | Type of color blindness |
| `colorblindWeaknessFactor` | `0.5` | 1 | Amount of sensitivity. e.g. Protanope (red-weakness) 0.0 = not colorblind, 1.0 = full weakness(Protanopia), 0.5 = mid weakness(Protanomaly) |
| `colorChatNamesByClass` | `0` | 4 | If enabled, the name of a player speaking in chat will be colored according to his class. |
| `combatLogRetentionTime` | `300` | 4 | The maximum duration in seconds to retain combat log entries |
| `combatLogUniqueFilename` | `1` | 4 | Write combat log file with a timestamped name per client launch |
| `combatWarningsEnabled` | `1` | 4 | If set, enables combat warning UI functionality such as the boss timeline or warnings displays |
| `combinedBags` | `0` | 4 | Use combined bag frame for all bags |
| `comboPointLocation` | `1` | 4 | Location of combo points in UI. 1=target, 2=self |
| `commentatorLossOfControlIconUnitFrame` | `1` | 4 | 0: Off, 1: On. |
| `commentatorLossOfControlTextNameplate` | `0` | 4 | 0: Off, 1: On. |
| `commentatorLossOfControlTextUnitFrame` | `0` | 4 | 0: Off, 1: On. |
| `communitiesShowOffline` | `1` | 4 | Show offline community members in the communities frame roster |
| `componentCompress` | `1` | 1 | Character component texture compression |
| `componentEmissive` | `1` | 1 | Character component unlit/emissive |
| `componentSpecular` | `1` | 1 | Character component specular highlights |
| `componentTexCacheSize` | `32` | 1 | Character component texture cache size (in MB) |
| `componentTexLoadLimit` | `16` | 1 | Character component texture loading limit per frame |
| `componentTextureLevel` | `0` | 1 | Level of detail for character component textures. 0 means full detail. |
| `componentThread` | `1` | 1 | Multi thread character component processing |
| `ConsoleKey` | ``` | 2 | Set key that opens the console |
| `consoleShowDebugMessages` | `0` | 0 | Controls if log messages with Debug priority are displayed to console. |
| `consoleShowSpamMessages` | `0` | 0 | Controls if log messages with Spam priority are displayed to console. |
| `contentTrackingFilter` | `1` | 4 | If enabled, tracked items will display on the world map. |
| `ContentTuning` | `0` | 5 |  |
| `Contrast` | `50.000000` | 5 |  |
| `cooldownViewerEnabled` | `0` | 4 | If true, show the cooldown viewer UI. |
| `cooldownViewerShowUnlearned` | `1` | 4 | In the cooldown viewer settings UI, determines whether or not to show unlearned cooldowns |
| `coordsByTenths` | `1` | 4 | Show coordinates by tenths |
| `countdownForCooldowns` | `0` | 4 | Whether to use number countdown instead of radial swipe for action button cooldowns or not. |
| `covenantMissionTutorial` | `0` | 4 | Stores information about which covenant mission/adventures tutorials the player has seen |
| `craftingOrdersOnlyPreferredArmorCollectable` | `0` | 4 | Determines if crafting orders can treat armor that doesn't match the players best/preferred armor type as collectable |
| `currencyCategoriesCollapsed` | `0` | 4 | Internal CVar for tracking collapsed currency categories. |
| `currentGameMode` | `-1` | 4 | The record ID of the current realm's GameMode. -1 means none, which may happen before connecting to a realm. 0 means the executable's standard game mode. |
| `CursorCenteredYPos` | `0.6` | 5 | 0-1 vertical position of centered cursor/targeting (0 at bottom) |
| `CursorFreelookCentering` | `0` | 5 | Center the cursor when using Mouse freelook |
| `CursorFreelookStartDelta` | `0.001` | 5 | Fraction of the screen the cursor must move to start freelook after mouse button goes down |
| `cursorSizePreferred` | `-1` | 1 | Size of cursor: -1=determine based on system/monitor dpi, 0=32x32, 1=48x48, 2=64x64, 3=96x96, 4=128x128 |
| `CursorStickyCentering` | `0` | 5 | Make the centered position stick after freelook; Don't restore previous cursor position |
| `CustomDesignEventLog` | `0` | 5 |  |
| `CustomWindowEventLog` | `0` | 5 |  |
| `cvar_default` |  | 5 | Set the value of a CVar to its coded default value |
| `cvar_reset` |  | 5 | Set the value of a CVar to its startup value |
| `cvarlist` |  | 5 | List CVars (filtered by substring if provided) |
| `D3D11` |  | 1 |  |
| `D3D12` |  | 1 |  |
| `daltonize` | `1` | 1 | Attempt to correct for color blindness (set colorblindSimulator to type of colorblindness) |
| `DamageCalculator` | `0` | 5 |  |
| `damageMeterEnabled` | `0` | 4 | If true, show the damage meter UI. |
| `damageMeterResetOnNewInstance` | `0` | 4 | If true, reset the damage meter any time the player enters a new instance. |
| `dangerousShipyardMissionWarningAlreadyShown` | `0` | 4 | Boolean indicating whether the shipyard's dangerous mission warning has been shown |
| `DebugTorsoTwist` | `0` | 0 | Debug visualization for Torso Twist: 1 = Player, 2 = Target, 3 = All |
| `deemphasizeOffspecPrimaryStats` | `0` | 4 | Tooltips gray or hide primary stats not used by your spec |
| `defaultReputationSortType` | `2` | 4 | Which sort type option to default to for reputations |
| `DefragmentGPU` |  | 1 | Defragment suballocated GPU resources |
| `DeprecatedWarningThrottle` | `0` | 5 | Time since last warning. A value of "1" will disable this message |
| `DepthBasedOpacity` | `1` | 1 | Enable/Disable Soft Edge Effect |
| `deselectOnClick` | `0` | 4 | Clear the target when clicking on terrain |
| `developerLog` | `0` | 0 | Enables Developer Log - 0: Disabled (default), 1: Enabled. |
| `developerLogFilterDebug` | `0` | 0 | Show Debug messages in Developer Log - 0: Disabled (default), 1: Enabled. |
| `developerLogFilterError` | `1` | 0 | Show Error messages in Developer Log - 0: Disabled, 1: Enabled (default). |
| `developerLogFilterFatal` | `1` | 0 | Show Fatal messages in Developer Log - 0: Disabled, 1: Enabled (default). |
| `developerLogFilterNormal` | `1` | 0 | Show Normal messages in Developer Log - 0: Disabled, 1: Enabled (default). |
| `developerLogFilterSpam` | `0` | 0 | Show Spam messages in Developer Log - 0: Disabled (default), 1: Enabled. |
| `developerLogFilterWarning` | `1` | 0 | Show Warning messages in Developer Log - 0: Disabled, 1: Enabled (default). |
| `developerLogWriteToFile` | `1` | 0 | Enables Developer Log Write to File - 0: Disabled, 1: Enabled (default). |
| `digSites` | `1` | 4 | If enabled, the archaeological dig site system will be used. |
| `DisableAdvancedFlyingFullScreenEffects` | `0` | 4 | Disable the advanced flying full screen effects |
| `DisableAdvancedFlyingVelocityVFX` | `0` | 4 | Disable the advanced flying velocity VFX |
| `disableAELooting` | `0` | 4 | Disable AoE Looting |
| `disableAutoRealmSelect` | `0` | 5 | Disable automatically selecting a realm on login |
| `disableHorizonStart` | `0` | 1 | disable "full fog" distance  |
| `disableServerNagle` | `1` | 6 | Disable server-side nagle algorithm |
| `disableSuggestedLevelActivityFilter` | `0` | 4 | Whether to disable filtering the activity list by the user's level. |
| `disableUILoadErrorDialog` | `0` | 0 | Disables showing an os dialog on critical UI error startup |
| `disableUserAddonsByDefault` | `0` | 4 | Setting this will result in newly installed addons to be disabled by default |
| `discordClientEnabled` | `1` | 0 | Enable the discord client integration |
| `discordDisplayName` | `0` | 4 | The name to show for text from you in-game from Discord |
| `displayFreeBagSlots` | `0` | 4 | Whether or not the backpack button should indicate how many inventory slots you've got free |
| `displaySpellActivationOverlays` | `1` | 4 | Whether to display Spell Activation Overlays (a.k.a. Spell Alerts) |
| `displayTemporaryEnchantIcon` | `1` | 4 | If true, will display the icon of the temporary enchant instead of the item it's on. |
| `displayWorldPVPObjectives` | `1` | 4 | Whether to show world PvP objectives |
| `dnMTUpdate` | `1` | 1 | Update Daynight in parralel. |
| `doNotFlashLowHealthWarning` | `0` | 4 | Do not flash your screen red when you are low on health. |
| `doNotShowTWFraudWarning` | `0` | 4 | If set, the TW Fraud Warning dialog will not show on startup |
| `dontShowEquipmentSetsOnItems` | `0` | 4 | Don't show which equipment sets an item is associated with |
| `doodadLodScale` | `100` | 5 |  |
| `dragonRidingRacesFilter` | `0` | 4 | If enabled, dragonriding races will display on the world map at zone level. |
| `dragonRidingRacesFilterWQ` | `1` | 4 | If enabled, dragonriding races WQ will display on the world map at zone level. |
| `DriveDynamicFOVEnabled` | `1` | 4 | Enables adjustment of camera field of view based on driving speed |
| `DriverVersionCheck` | `1` | 1 | Set 0 to disable driver version based workarounds |
| `DriveSwapReverseTurnDirection` | `0` | 4 | Boolean indicating if we should swap turn directions when driving in reverse. By default, Drive uses the opposite turn direction when moving backwards. |
| `dynamicLod` | `1` | 1 | Dynamic level of detail adjustment |
| `DynamicRenderScale` | `0` | 1 | Lowers render scale if GPU bound to hit Target FPS. Note this feature is in BETA. Known issues: May cause hitching. May behave poorly with vsync on. |
| `DynamicRenderScaleMin` | `0.333333` | 1 | Lowest render scale DynamicRenderScale can use |
| `EJDungeonDifficulty` | `0` | 4 | Stores the last dungeon difficulty viewed in the encounter journal |
| `EJLootClass` | `-1` | 4 | Stores the last class that loot was filtered by in the encounter journal |
| `EJLootSpec` | `0` | 4 | Stores the last spec that loot was filtered by in the encounter journal |
| `EJRaidDifficulty` | `0` | 4 | Stores the last raid difficulty viewed in the encounter journal |
| `EJSelectedTier` | `0` | 4 | Stores the last manually selected journal tier in the encounter journal |
| `EmitterCombatRange` | `900.000000` | 4 | Range to stop shoulder/weapon emissions during combat |
| `emphasizeMySpellEffects` | `1` | 4 | Whether other player's spell impacts are toned down or not. |
| `EmpowerMinHoldStagePercent` | `1.000000` | 4 | Sets a percentage of the first empower stage [0.0,1.0]. Before this point, the spell will be auto-held. After it, releases will be accepted. |
| `empowerTapControls` | `0` | 4 | By default, Empower spells use a press-hold-release control scheme. Set this CVar to use a tap-tap scheme instead. |
| `EmpowerTapControlsReleaseThreshold` | `300` | 4 | Sets the time in milliseconds after which release/re-hold requests will be registered for press-and-tap empowers. Begins when the cast is sent from the client. |
| `enable` |  | 2 | Enable the console with "/console enable" in the chat window. This is the same as launching the client with -console |
| `enableAssetTracking` | `1` | 4 | Whether to track which assets are least recently used |
| `enableBGDL` | `1` | 6 | Background Download (on async net thread) Enabled |
| `EnableBlinkApplicationIcon` | `1` | 4 | Allows the client to blink the application icon in the taskbar in Windows, or bounce the application icon in the dock on macOS |
| `enableCollectionToasts` | `1` | 4 | If enabled, toasts for collection items being unlocked will popup. |
| `enableConnectToPhotoSharing` | `0` | 4 | Enables the photo sharing connection feature. |
| `enableFloatingCombatText` | `0` | 4 | Whether to show floating combat text for the player |
| `enableLearnedRecipeToasts` | `1` | 4 | If enabled, toasts for learning new recipes will popup. |
| `enableLootToasts` | `1` | 4 | If enabled, toasts for loot being received will popup. |
| `enableMouseoverCast` | `0` | 4 | Whether mouseover casting is enabled (optionally with a modifier key). |
| `enableMouseSpeed` | `0` | 4 | Enables setting a custom mouse sensitivity to override the setting from the operating system. |
| `enableMovePad` | `0` | 4 | Enables the MovePad accessibility feature in the game |
| `enableMultiActionBars` | `0` | 4 | Bits for which additional action bars to show |
| `enablePetBattleFloatingCombatText_v2` | `1` | 4 | Whether to show floating combat text for pet battles |
| `enablePings` | `1` | 4 | Enables ping system. |
| `enablePVPNotifyAFK` | `1` | 4 | The ability to shutdown the AFK notification system |
| `enableQuestCacheLogging` | `1` | 4 | Enable logging for requests for the QuestCache |
| `enableRuneSpentAnim` | `1` | 5 | Adjust the time the rune fades after it flashes when you spend it |
| `enableSourceLocationLookup` | `1` | 0 | Allows addon file name lookup for debugging help |
| `enableWowMouse` | `0` | 5 | Enable Steelseries World of Warcraft Mouse |
| `encounterTimelineEnabled` |  | 4 | If true, enable the encounter timeline UI. |
| `encounterTimelineHideForOtherRoles` |  | 4 | If true, hide encounter timeline events that are relevant for roles other than the player's own group role assignment. Events with no assigned role will always be shown. |
| `encounterTimelineHideLongCountdowns` |  | 4 | If true, hide all long countdowns from the timeline. |
| `encounterTimelineHideQueuedCountdowns` |  | 4 | If true, hide all queued countdowns from the timeline. |
| `encounterTimelineHighlightDuration` |  | 4 | Milliseconds at which events will be signaled to trigger a highlight glow animation. |
| `encounterTimelineIconographyEnabled` |  | 4 | If true, enable the display of spell support iconography such as role and effect type indicators. |
| `encounterTimelineIconographyHiddenMask` |  | 4 | Bitmask of support iconography to be disabled for timeline events. |
| `encounterTimelineShowSequenceCount` | `0` | 4 | If true, display the spell sequence count in encounter timeline spell names |
| `encounterWarningsDefaultMessageDuration` | `3500` | 4 | Default duration (in milliseconds) applied to encounter warning text messages |
| `encounterWarningsEnabled` | `1` | 4 | If true, enable the display of encounter warning messages |
| `encounterWarningsHideIfNotTargetingPlayer` | `0` | 4 | If true, hide messages that aren't actively targeting the player. Messages that have no explicit target will always be shown |
| `encounterWarningsLevel` | `0` | 4 | Minimum level of encounter warning severities to be shown |
| `endeavorInitiativesLastPointsMap` |  | 4 | Last seen number of endeavor points in the progress bar per initiative ID |
| `engineSurvey` | `0` | 4 | Engine Survey Index |
| `engineSurveyPatch` | `0` | 4 | Engine Survey Patch |
| `entityLodDist` | `10` | 1 | Entity level of detail distance |
| `entityLodOffset` | `10` | 1 | Entity level of detail offset |
| `entityShadowFadeScale` | `50` | 1 | Entity shadow fade scale |
| `equipmentManager` | `1` | 4 | Enables the equipment management UI |
| `ErrorFilter` | `all` | 0 |  |
| `ErrorLevelMax` | `3` | 0 |  |
| `ErrorLevelMin` | `2` | 0 |  |
| `Errors` | `0` | 0 |  |
| `eventReminders` |  | 4 | Internal cvar for saving event reminders |
| `eventSchedulerLastUpdate` | `0` | 4 | Stores the last time the event scheduler UI was update, for anim purposes |
| `excludedCensorSources` | `1` | 4 | Inappropriate message source exemptions. 0 = Exempt nobody, 1 = Exempt Friends, 3 = Exempt Friends and Guildmates, 255 = Exempt All |
| `ExclusiveWindowMode` | `0` | 5 | Accessibility option for preventing the game window from losing focus |
| `expandBagBar` | `1` | 4 | Expand the main menu bar that shows the bags so you can see all equipped bags instead of just the backpack and reagent bag |
| `expandUpgradePanel` | `1` | 4 | Controls whether the upgrade panel is expanded or collapsed. |
| `expandWarbandCharacterList` | `1` | 4 | Stores if the warband character list is expanded or collapsed. |
| `externalDefensivesEnabled` | `0` | 4 | If true, show the external defensives buff tracker UI. |
| `farclip` | `1000` | 5 |  |
| `fetchBleepProxies` |  | 5 |  |
| `ffxAntiAliasingMode` | `4` | 1 | Anti Aliasing Mode |
| `ffxDeath` | `1` | 1 | full screen death desat effect |
| `ffxGlow` | `1` | 1 | full screen glow effect |
| `ffxLingeringVenari` | `1` | 1 | full screen Lingering Cloak of Ven'ari effect |
| `ffxNether` | `1` | 1 | full screen nether effect |
| `ffxVenari` | `1` | 1 | full screen Cloak of Ven'ari effect |
| `findYourselfAnywhere` | `0` | 4 | Always Highlight your character |
| `findYourselfAnywhereOnlyInCombat` | `0` | 4 | Highlight your character only when in combat |
| `findYourselfInBG` | `1` | 4 | Always Highlight your character in Battlegrounds |
| `findYourselfInBGOnlyInCombat` | `0` | 4 | Highlight your character in Battlegrounds only when in combat |
| `findYourselfInRaid` | `1` | 4 | Always Highlight your character in Raids |
| `findYourselfInRaidOnlyInCombat` | `1` | 4 | Highlight your character in Raids only when in combat |
| `findYourselfMode` | `0` | 4 | Highlight your character. 0 = circle, 1 = circle & outline, 2 = outline |
| `findYourselfModeCircle` | `0` | 4 | Highlight your character with a circle. |
| `findYourselfModeIcon` | `0` | 4 | Highlight your character with an icon. |
| `findYourselfModeOutline` | `0` | 4 | Highlight your character with an outline. |
| `flaggedTutorials` |  | 4 | Internal cvar for saving completed tutorials in order |
| `flashErrorMessageRepeats` | `1` | 4 | Flashes the center screen red error text if the same message is fired. |
| `flightAngleLookAhead` | `0` | 4 | Enables more dynamic attitude adjustments while flying |
| `floatingCombatTextAuraFade_v2` | `0` | 4 |  |
| `floatingCombatTextAuras_v2` | `0` | 4 |  |
| `floatingCombatTextCombatDamage_v2` | `1` | 4 | Display damage numbers over hostile creatures when damaged |
| `floatingCombatTextCombatDamageAllAutos_v2` | `1` | 4 | Show all auto-attack numbers, rather than hiding non-event numbers |
| `floatingCombatTextCombatDamageDirectionalOffset_v2` | `1.000000` | 4 | Amount to offset directional damage numbers when they start |
| `floatingCombatTextCombatDamageDirectionalScale_v2` | `0.000000` | 4 | Directional damage numbers movement scale (0 = no directional numbers) |
| `floatingCombatTextCombatHealing_v2` | `1` | 4 | Display amount of healing you did to the target |
| `floatingCombatTextCombatHealingAbsorbSelf_v2` | `1` | 4 | Display amount of shield added to yourself. |
| `floatingCombatTextCombatHealingAbsorbTarget_v2` | `1` | 4 | Display amount of shield added to the target. |
| `floatingCombatTextCombatLogPeriodicSpells_v2` | `1` | 4 | Display damage caused by periodic effects |
| `floatingCombatTextCombatState_v2` | `0` | 4 |  |
| `floatingCombatTextComboPoints_v2` | `0` | 4 |  |
| `floatingCombatTextDamageReduction_v2` | `0` | 4 |  |
| `floatingCombatTextDodgeParryMiss_v2` | `0` | 4 |  |
| `floatingCombatTextEnergyGains_v2` | `0` | 4 |  |
| `floatingCombatTextFloatMode_v2` | `1` | 4 | The combat text float mode for the player |
| `floatingCombatTextFriendlyHealers_v2` | `0` | 4 |  |
| `floatingCombatTextHonorGains_v2` | `0` | 4 |  |
| `floatingCombatTextLowManaHealth_v2` | `1` | 4 |  |
| `floatingCombatTextPeriodicEnergyGains_v2` | `0` | 4 |  |
| `floatingCombatTextPetMeleeDamage_v2` | `1` | 4 | Display pet melee damage in the world |
| `floatingCombatTextPetSpellDamage_v2` | `1` | 4 | Display pet spell damage in the world |
| `floatingCombatTextReactives_v2` | `1` | 4 |  |
| `floatingCombatTextRepChanges_v2` | `0` | 4 |  |
| `floatingCombatTextSpellMechanics_v2` | `0` | 4 | Whether to display values for effects on other players. |
| `floatingCombatTextSpellMechanicsOther_v2` | `0` | 4 | Whether to display values for effects on other players' targets. |
| `fontcolor` |  | 2 | [ColorClassName] [Red 0-255] [Green 0-255] [Blue 0-255] |
| `fontsize` |  | 2 | [10-50] arbitrary font size |
| `FootstepSounds` | `1` | 7 | play footstep sounds |
| `forceClusteredShading` | `0` | 1 | Force clustered forward lighting for all transparent objects |
| `forceEnglishNames` | `0` | 5 |  |
| `ForceGenerateSlug` | `0` | 0 | Generate .slug files for all loaded fonts before they are actually used rather than deferred load. |
| `forceLODCheck` | `0` | 1 | If enabled, we will skip checking DBC for LOD count and every m2 will scan the folder for skin profiles |
| `ForceResolutionDefaultToMaxSize` | `0` | 5 | Force default resolution to the maximum supported size rather than the auto-detected size |
| `FrameBufferCacheForceNoHeaps` | `0` | 1 | Disable use of texture heaps and force the fallback path |
| `FrameBufferCacheGpuFootprint` |  | 1 |  |
| `frameScriptFunctionInheritanceWarningMode` | `0` | 0 | Displays Lua errors about script handlers that are using inheritance improperly (might add more modes in the future, 0 is off, 1 is on) |
| `friendInvitesCollapsed` | `0` | 4 | Whether friend invites are hidden in the friends list |
| `fstack_enabled` | `0` | 0 | 0: Hide Framestack Tooltip (Default), 1: Show Framestack Tooltip. |
| `fstack_preferParentKeys` | `0` | 0 | 0: Prefer Global Names, 1: Prefer ParentKeys (Default). |
| `fstack_showanchors` | `1` | 0 | 0: Hide Anchors, 1: Show Anchors (Default). |
| `fstack_showhidden` | `0` | 0 | 0: Hide Hidden (Default), 1: Show Hidden. |
| `fstack_showhighlight` | `1` | 0 | 0: Hide Highlight, 1: Show Highlight (Default). |
| `fstack_showRaisedFrameLevels` | `0` | 0 | 0: Show normal frame levels (default), 1: Show raised frame levels instead |
| `fstack_showregions` | `1` | 0 | 0: Hide Regions, 1: Show Regions (Default). |
| `GameDataVisualizer` | `0` | 5 |  |
| `GamePadAnalogMovement` | `1` | 5 | Enable analog movement in any direction, rather than just the 8 cardinal directions |
| `GamePadBackend` | `0` | 4 | Which GamePad backend to use (0=Default, 1=SDL, 2=Paddle) |
| `GamePadBackPedalThreshold` | `0.600000` | 4 | Stick magnitude threshold to face the movement direction instead of back pedal |
| `GamepadCameraFollowOnStick` | `0` | 4 | Enable camera to follow target as though being pushed/pulled along on a stick |
| `GamepadCameraFollowPitchOffset` | `15.000000` | 4 | Controls the pitch offset in degrees that the camera will move towards |
| `GamePadCameraLookMaxPitch` | `0` | 5 | Max pitch 'Look' stick can adjust camera angle |
| `GamePadCameraLookMaxYaw` | `0` | 5 | Max yaw 'Look' stick can adjust camera angle |
| `GamePadCameraPitchSpeed` | `1.000000` | 4 | Pitch speed of GamePad camera moving up/down |
| `GamepadCameraSavedDistance` | `5.550000` | 4 |  |
| `GamepadCameraSavedPetBattleDistance` | `10.000000` | 4 |  |
| `GamepadCameraSavedPitch` | `10.000000` | 4 |  |
| `GamepadCameraSavedVehicleDistance` | `-1.000000` | 4 |  |
| `GamePadCameraYawSpeed` | `1.300000` | 4 | Yaw speed of GamePad camera turning left/right |
| `GamepadCompassCustomFilterBoss` | `0` | 4 | Adds Boss icons to the compass's custom filter. |
| `GamepadCompassCustomFilterCritter` | `0` | 4 | Adds Critter icons to the compass's custom filter. |
| `GamepadCompassCustomFilterEnemy` | `0` | 4 | Adds Enemy icons to the compass's custom filter. |
| `GamepadCompassCustomFilterFriendly` | `0` | 4 | Adds Friendly icons to the compass's custom filter. |
| `GamepadCompassCustomFilterParty` | `0` | 4 | Adds Party icons to the compass's custom filter. |
| `GamepadConstrainedGroundTargetDistanceYds` | `20.000000` | 4 | [Gamepad Specific] Distance at which to constrain AOE spell range to. |
| `GamepadConstrainedGroundTargetEnabled` | `1` | 4 | [Gamepad Specific] Whether AOE offer constrained-range casting. |
| `GamepadConstrainedGroundTargetMaxRange` | `100.000000` | 4 | [Gamepad Specific] Max Range at which to AOE spells become cursor-targeted. |
| `GamePadCursorAutoDisableJump` | `1` | 5 | GamePad cursor control will auto-disable when you jump |
| `GamePadCursorAutoDisableSticks` | `2` | 5 | GamePad cursor control will auto-disable on stick input (0=none, 1=movement, 2=movement+cursor) |
| `GamePadCursorAutoEnable` | `1` | 5 | Auto enable GamePad cursor control when opening UIs that may need it |
| `GamePadCursorCenteredEmulation` | `1` | 5 | When cursor is centered for GamePad movement, also emulate mouse clicks |
| `GamePadCursorCentering` | `0` | 5 | When using GamePad, center the cursor |
| `GamePadCursorForTargeting` | `1` | 5 | Enable GamePad controlled cursor for spell targeting (1=enable, 2=start-at-target) |
| `GamePadCursorLeftClick` | `PADRTRIGGER` | 5 | GamePad button that should emulate mouse Left Click while controlling the mouse cursor |
| `GamePadCursorOnLogin` | `1` | 5 | Enable GamePad cursor control on login and character screens |
| `GamePadCursorPushCamera` | `1` | 5 | Rate for GamePad controlled cursor to push/turn camera when at edge of window |
| `GamePadCursorRightClick` | `PADRSHOULDER` | 5 | GamePad button that should emulate mouse Right Click while controlling the mouse cursor |
| `GamePadCursorSpeedAccel` | `2` | 5 | Acceleration of GamePad cursor per second as it continues to move |
| `GamePadCursorSpeedMax` | `1` | 5 | Top speed of GamePad cursor movement |
| `GamePadCursorSpeedStart` | `0.1` | 5 | Speed of GamePad cursor when it starts moving |
| `GamePadEmulateAlt` | `none` | 5 | GamePad button that should emulate the Alt key |
| `GamePadEmulateCtrl` | `PADLSHOULDER` | 5 | GamePad button that should emulate the Ctrl key |
| `GamePadEmulateShift` | `PADLTRIGGER` | 5 | GamePad button that should emulate the Shift key |
| `GamePadEmulateTapWindowMs` | `350` | 5 | GamePad buttons emulating Ctrl/Alt/Shift will be 'tapped' if released withing this time in MS |
| `GamePadEnable` | `1` | 5 | Whether GamePad input should be enabled |
| `GamepadEnableReticleSwingTimer` | `1` | 4 | Shows a swing timer on the gamepad reticle while attacking. |
| `GamePadFaceMovementFreeFlying` | `1` | 4 | Always face movement direction when free flying and not in combat |
| `GamePadFaceMovementMaxAngle` | `0` | 5 | Max movement to camera angle to face movement direction instead of camera direction. 0 = always, 180 = never (115 allows using strafe with quick turn around) |
| `GamePadFaceMovementMaxAngleCombat` | `105` | 5 | Max movement to camera angle to face movement direction instead of camera direction, in combat. 0 = always, 180 = never (115 allows using strafe with quick turn around) |
| `GamePadFaceMovementMount` | `1` | 4 | Always face movement direction when riding a land mount |
| `GamePadFaceMovementSwimming` | `1` | 4 | Always face movement direction when swimming and not in combat |
| `GamePadFactionColor` | `1` | 5 | Enable setting GamePad's led color to match current faction |
| `GamepadFocusStateColor` | `1` | 4 | Determines which focus state color to use. |
| `GamepadFocusStateOpacity` | `0.500000` | 4 | Determines opacity to use for focus state. Set to 0 for no glow. |
| `GamepadHudModifierUsesToggle` | `0` | 4 | Allows the HUD Modifier state to be toggled on/off when tapped instead of when held/released. |
| `gamepadInvertPitch` | `0` | 4 |  |
| `gamepadInvertYaw` | `0` | 4 |  |
| `GamePadListDevices` |  | 4 | List all connected GamePad devices in the console |
| `GamepadMapEdgePanDistance` | `50.000000` | 4 | The distance from the edge of the map screen that will cause it to pan. |
| `GamepadMapScrollSpeed` | `400.000000` | 4 | How fast the map is scrolled. |
| `GamepadMapScrollSpeedFullScreen` | `1000.000000` | 4 | How fast the map is scrolled when the map is full screen. |
| `GamepadMapZoomSpeed` | `2.000000` | 4 | How fast the map is zoomed in or out. |
| `GamePadOverlapMouseMs` | `2000` | 5 | Duration after gamepad+mouse input to switch to just one or the other. |
| `GamePadPlunderstormDefaults` |  | 4 | Set specific GamePad cvars to better default values for Plunderstorm |
| `GamepadPossessBarOverride` | `1` | 4 | Specifies which of the gamepad action bars is overriden by the possess action bar when it is available. |
| `GamepadPreferScreenTargeting` | `0` | 4 | Use Screen Targeting instead of the Targeting Radial. |
| `GamepadRaidTargetingHoverMode` | `0` | 4 | When raid targeting spells will target the indicated player without changing the player's current target. |
| `GamepadRaidTargetingStyle` | `1` | 4 | The type of targeting style to use when targeting players in a raid group. |
| `GamePadRunThreshold` | `0.5` | 5 | 0-1 Amount of stick movement before character transitions from walk to run |
| `GamepadShowAutoAuraTooltip` | `1` | 4 | Whether to automatically show buff tooltips for Gamepad UI |
| `GamepadShowPersistentInputLegend` | `1` | 4 | Indicates if the list of gamepad actions should always be shown on screen. |
| `GamePadSingleActiveID` | `0` | 5 | ID of single GamePad device to use. 0 = Use all devices' combined input |
| `GamepadStanceBarOverride` | `3` | 4 | Specifies which of the gamepad action bars is overriden by the stance action bar when it is available. |
| `GamePadStickAxisButtons` | `0` | 5 | Enables virtual buttons for the GamePad stick cardinal directions |
| `GamepadSwapFriendlyTargetActions` | `0` | 4 | Swaps the dpad and face button actions when holding the friendly target modifier. |
| `GamepadSwapHostileTargetActions` | `0` | 4 | Swaps the dpad and face button actions when holding the hostile target modifier. |
| `GamepadSwapTargetModifiers` | `0` | 4 | Swaps the friendly and hostile target modifiers. |
| `GamepadTabFriendlyTargetAction` | `1` | 4 | Tab target friendlies on target action release |
| `GamepadTabHostileTargetAction` | `1` | 4 | Tab target hostiles on target action release |
| `GamePadTankTurnSpeed` | `0` | 5 | If non-zero, character turns like a tank from GamePad movement |
| `GamepadTargetingAnalogDeadzone` | `0.600000` | 4 | Magnitude of input the stick must receive for analog targeting to take effect (0.0-1.0) |
| `GamepadTargetingAnalogPullbackThreshold` | `0.150000` | 4 | Magnitude difference at which analog targeting turns itself off (0.0-1.0) |
| `GamepadTargetingModifierVisualDelay` | `0.350000` | 4 | The duration that the Targeting Modifier can be held before updating the UI. Releasing within this window will tab target. |
| `GamePadTouchCursorAccel` | `1.000000` | 5 | Cursor acceleration for touchpad control |
| `GamePadTouchCursorEnable` | `2` | 5 | Enable cursor control with GamePad's touch pad (0=disable, 1=enable, 2=enable in mkb ui / disable in gamepad ui) |
| `GamePadTouchCursorMoveThreshold` | `0.042000` | 5 | Change before touchpad moves the cursor (larger for easier taps) |
| `GamePadTouchCursorSpeed` | `1.000000` | 5 | Cursor speed for touchpad control |
| `GamePadTouchTapButtons` | `0` | 5 | Enable touch tap to press TouchPad buttons |
| `GamePadTouchTapMaxMs` | `200` | 5 | Max time in ms for a touch to register a tap/click |
| `GamePadTouchTapOnlyClick` | `1` | 5 | Only use taps for cursor clicks, do not use tap presses |
| `GamePadTouchTapRightClick` | `0` | 5 | Taps for cursor clicks are right clicks instead of left clicks |
| `GamePadTurnWithCamera` | `3` | 5 | Turn character to match when camera facing is changed (1=in-combat, 2=always, 3=in-combat or casting) |
| `GamepadUsePartyTargeting` | `1` | 4 | If enabled, target specific party members with the dpad rather than using directional targeting |
| `GamePadVibrationStrength` | `1` | 5 | GamePad vibration effect strength |
| `GameplayContext` | `0` | 5 |  |
| `gameTip` | `0` | 5 |  |
| `Gamma` | `1.000000` | 5 |  |
| `garrisonCompleteTalent` | `0` | 4 |  |
| `garrisonCompleteTalentType` | `0` | 4 |  |
| `GetSwapChainSize` |  | 1 |  |
| `GetWindowSize` |  | 1 |  |
| `giQuality` | `1` | 5 |  |
| `graphicsBloomUserMult` |  | 5 |  |
| `graphicsComputeEffects` | `3` | 5 |  |
| `graphicsDepthEffects` | `3` | 5 |  |
| `graphicsEnvironmentDetail` | `6` | 5 |  |
| `graphicsGroundClutter` | `6` | 5 |  |
| `graphicsLightMode` | `2` | 5 |  |
| `graphicsLiquidDetail` | `2` | 5 |  |
| `graphicsOutlineMode` | `2` | 5 |  |
| `graphicsParticleDensity` | `3` | 5 |  |
| `graphicsPBRLiquidDetail` | `1` | 5 |  |
| `graphicsProjectedTextures` | `1` | 5 |  |
| `graphicsQuality` | `6` | 5 |  |
| `graphicsShadowQuality` | `4` | 5 |  |
| `graphicsSpellDensity` | `1` | 5 |  |
| `graphicsSSAO` | `3` | 5 |  |
| `graphicsTextureResolution` | `2` | 5 |  |
| `graphicsViewDistance` | `6` | 5 |  |
| `groundEffectDensity` | `16` | 5 |  |
| `groundEffectDist` | `70` | 5 |  |
| `groundEffectFade` | `70` | 1 | Ground effect fade |
| `guildMemberNotify` | `1` | 4 | Whether to notify when guild members come online or go offline |
| `guildNewsFilter` | `0` | 4 | Stores the guild news filters |
| `guildRewardsCategory` | `0` | 4 | Show category of guild rewards |
| `guildRewardsUsable` | `0` | 4 | Show usable guild rewards only |
| `guildShowOffline` | `1` | 4 | Show offline guild members in the guild UI |
| `GxAdapter` |  | 1 | Set which GPU to use. See GxListGPUs for valid names (empty string to let client choose) |
| `GxAFRDevicesCount` | `0` | 1 | Force to set number of AFR devices |
| `GxAllowCachelessShaderMode` | `0` | 5 | CPU memory saving mode, if supported by backend. When enabled, shaders are fetched from disk as needed instead of being kept resident. This mode may slightly increase the time objects take to appear the first time they are encountered. Computers without solid state drives may want to disable this feature |
| `GxApi` | `auto` | 5 |  |
| `GxCompatAllowSM6` | `1` | 5 | When disabled, DX12 will use Shader Model 5 shaders instead of Shader Model 6 |
| `GxCompatAsyncComputeQueue` | `1` | 5 | Allows some compute work to run on a different GPU work queue |
| `GxCompatAsyncShaderCompilation` | `1` | 5 | Allows async resource shader loading. Disabling this may cause hitching |
| `GxCompatCommandListMultiThreading` | `1` | 5 | Allow multi-threaded rendering. Disabling this will significantly reduce framerate |
| `GxCompatCopyQueue` | `1` | 5 | Allows GPU upload work to run on a different GPU work queue |
| `GxCompatLowLatencyCallbacks` | `0` | 5 | Allows GPU -> CPU readbacks to be checked for more frequently rather than always taking the max GPU frame latency |
| `GxCompatOptionalGpuFeatures` | `1` | 5 | When disabled, makes the engine act as if the GPU only supports the minimum supported feature set |
| `GxCompatWorkSubmitOptimizations` | `1` | 5 | Allows GPU work submission on a secondary thread while the rest of the CPU threads continue on to the next frame |
| `GxCurrentAPI` |  | 1 |  |
| `GxCurrentGPU` |  | 1 |  |
| `GxFrameStats` |  | 1 | Get Engine Frame Stats |
| `GxFullscreenResolution` | `auto` | 5 |  |
| `GxGetVideoMemory` |  | 1 |  |
| `GxIsPrism` |  | 1 |  |
| `GxListGPUs` |  | 1 |  |
| `GxLogFlush` |  | 1 |  |
| `GxLogFullGPUInfo` |  | 1 |  |
| `GxMaxFrameLatency` | `3` | 5 | maximum number of frames ahead of GPU the CPU can be |
| `GxMaximize` | `1` | 5 |  |
| `GxMemReport` |  | 0 |  |
| `GxMonitor` | `0` | 5 | Monitor index. 0 means use the primary monitor |
| `gxMTAlphaM2` | `1` | 1 | Render transparent M2 pass in parallel. |
| `gxMTAlphaPass` | `1` | 1 | Render Alpha Pass in parallel. |
| `gxMTBeginDraw` | `1` | 1 | Do BeginDraw multithreaded. |
| `gxMTDecals` | `0` | 1 | Sort and Render decal passes in parallel. Note enabling this currently will cause visual artifacts in some cases. |
| `gxMTDisable` | `0` | 1 | Disable all render multithreading |
| `gxMTLightShafts` | `1` | 1 | Render light-shaft passes in parallel |
| `gxMTMisc` | `1` | 1 | Render miscelleous passes in parallel |
| `gxMTOpaqueM2` | `1` | 1 | Render opaque model pass in parallel. |
| `gxMTOpaqueM2NoReflect` | `1` | 1 | Render opaque model no reflection pass in parallel. |
| `gxMTOpaqueWMO` | `1` | 1 | Render opaque WMO in parallel. |
| `gxMTOutlines` | `1` | 1 | Render outline passes in parallel |
| `gxMTPrepass` | `1` | 1 | Render prepass in parallel. |
| `gxMTRefraction` | `1` | 1 | Render refraction pass in parallel |
| `gxMTShadow` | `1` | 1 | Render shadow bands in parallel. |
| `gxMTTerrain` | `1` | 1 | Render terrain in parallel. |
| `gxMTTriggerOnBeginDrawComplete` | `1` | 1 | Use Begin Draw Complete Trigger Mechanism |
| `gxMTVolFog` | `1` | 1 | Render volumetric fog in parallel |
| `GxNewResolution` | `0x0` | 5 | resolution to be set |
| `GxPrismEnabled` | `1` | 1 | 0: Prism backends Disabled. 1: Default Prism backends Enabled. 2: Experimental Prism backends Enabled. |
| `GxRestart` |  | 1 |  |
| `GxSimulateEvent` |  | 0 |  |
| `GxSlowShaderWarnThreshold` | `30000` | 5 | Max time (in milliseconds) the shader compile can take before warning via a popup message |
| `GxWindowedResolution` | `auto` | 5 |  |
| `hardcoreDeathAlertType` | `0` | 4 |  |
| `hardcoreDeathChatType` | `0` | 4 |  |
| `hardTrackedQuests` |  | 4 | Internal cvar for saving user manually tracked quests in order |
| `hardTrackedWorldQuests` |  | 4 | Internal cvar for saving user manually tracked world quests |
| `HardwareCursor` | `1` | 1 | If disabled, draws a software cursor (can be used to have cursor appear in screenshots) |
| `hasSelectedExperiencePreset` | `0` | 4 | Whether this client has selected an experience preset (Classic or Modern) yet. |
| `HDRBrightness` | `203` | 1 | Brightness level to use when rendering in HDR, specified in nits (cd/m^2). Only used if useHDRBrightness is set. |
| `HDRFactor` | `2.000000` | 1 | Factor adjusting how far above SDR lighting HDR is allowed to push. Will be clamped to the monitor's peak brightness. |
| `HDROutput` | `0` | 1 | Enables HDR output if supported by the monitor and render settings |
| `HDRPeakBrightness` | `400` | 1 | Peak brightness the monitor is able to display when rendering in HDR, specified in nits (cd/m^2). Only used if useHDRPeakBrightness is set. |
| `HealHandler` | `0` | 5 |  |
| `heirloomCollectedFilters` | `0` | 4 | Bitfield for which collected filters are applied in the heirloom journal |
| `heirloomSourceFilters` | `0` | 4 | Bitfield for which source filters are applied in the heirloom journal |
| `help` |  | 2 | Provides help information about a command. |
| `hideFastLoginLoadingScreen` | `0` | 5 |  |
| `hideRewardedEvents` | `0` | 4 | Stores whether to hide events whose rewards have been claimed |
| `highestUnlockedTieredEntranceTier` |  | 4 | Serialized mapping using a PDE ID. Stores the highest unlocked difficulty tier. Used to notify the player when they have higher difficulty tiers available. |
| `horizonClip` | `1600` | 5 |  |
| `horizonStart` | `800` | 5 |  |
| `HotfixEventLog` | `0` | 5 |  |
| `hotReloadModels` | `1` | 1 | Allow an active model to be reloaded when a new version is detected in the bin folder.  If this is disabled, the model data will only be refreshed after all game objects using the model are deleted |
| `houseExterior_Hide_Decor` | `1` | 4 | Whether or not to hide all decor on the plot while in Exterior Customization |
| `housingDecorFreePlaceEnabled` | `0` | 4 | Whether or not free placement in decor edit modes is enabled |
| `housingDecorGridSnapEnabled` | `0` | 4 | Whether or not snap-to-grid in decor edit modes is enabled |
| `housingDecorGridVisible` | `1` | 4 | Whether or not the grid in decor edit modes is visible |
| `housingDecorLightRadiusIndicatorsEnabled` | `1` | 4 | Whether or not the light radius indicators in decor edit modes are visible |
| `housingExpertGizmos_Scale_FrameOffset` | `0.500000` | 10 | Y Offset of scale frame from target |
| `housingExpertGizmos_Scale_Snap` | `0.100000` | 10 | Amount scale should snap (0.1 being 10%, 1 being 100%, etc) |
| `housingExpertGizmos_SnapOnHold` | `1` | 10 | true: Holding shift turns expert control snapping on, false: Holding shift turns snapping off |
| `housingLayout_Camera_DefaultDistance` | `50.000000` | 10 | Default height of the layout edit mode camera above the floor |
| `housingLayout_Camera_DragFriction` | `8.000000` | 10 | How quickly the camera loses drag momentum |
| `housingLayout_Camera_DragMomentum` | `0.300000` | 10 | How much momentum does the camera have after the user stops dragging |
| `housingLayout_Camera_MaxDistance` | `120.000000` | 10 | Maximum height of the layout edit mode camera above the floor |
| `housingLayout_Camera_MaxDistanceIncr` | `5.000000` | 10 | How much zoom in/out of the layout edit mode camera affects distance from the floor |
| `housingLayout_Camera_MinDistance` | `30.000000` | 10 | Minimum height of the layout edit mode camera above the floor |
| `housingLayout_Camera_Smoothness` | `15.000000` | 10 | Smoothness factor of layout camera movement |
| `housingLayout_Camera_Speed` | `15.000000` | 10 | Units/second that the layout edit mode camera moves |
| `housingOtherDecorLightRadiusIndicatorType` | `1` | 4 | Choose how light radius indicator is shown for non-selected decor |
| `housingSelectedDecorLightRadiusIndicatorType` | `1` | 4 | Choose how light radius indicator is shown for selected decor |
| `housingStoragePanelCollapsed` | `0` | 4 | Whether the housing storage panel is collapsed |
| `housingStoragePanelHeight` | `615.000000` | 4 | The saved height of the housing storage panel |
| `housingStoragePanelWidth` | `530.000000` | 4 | The saved width of the housing storage panel |
| `housingTutorialsEnabled` | `1` | 4 | Housing tutorials enabled or disabled |
| `hwDetect` | `1` | 5 |  |
| `imageSharingPublishCooldown` | `5000` | 4 | Amount of time between allowed photo publish attempts (in milliseconds). |
| `ImpactModelCollisionMelee` | `1` | 4 | Enable model collision checks for melee impact effects |
| `ImpactModelCollisionMissile` | `1` | 4 | Enable model collision checks for missile impact effects |
| `ImpactModelCollisionRanged` | `1` | 4 | Enable model collision checks for ranged attack impact effects |
| `incompleteQuestPriorityThresholdDelta` | `135` | 0 |  |
| `initialRealmListTimeout` | `60` | 5 | How long to wait for the initial realm list before failing login (in seconds) |
| `InputDeviceInterfaceStyle` | `0` | 10 | Switches between the interface types for different devices |
| `instantQuestText` | `1` | 4 | Whether to instantly show quest text instead of fading it in. |
| `interactKeyWarningTutorial` | `0` | 4 | Has the player seen the interact key warning tutorial since they have logged in |
| `interactOnLeftClick` | `1` | 4 | Test CVar for interacting with NPC's on left click |
| `interactQuestItems` | `1` | 4 | Enable Quest Item use as an interaction |
| `InvalidateDeactivatedHandles` | `1` | 0 | Turn on to treat WowCS Handles as invalid if referring to a deactivated entity |
| `KioskCanAutoDeleteCharacters` | `1` | 10 | Determines if characters will be deleted after a session restart. Defaults to 'true'. |
| `KioskCanSessionExpire` | `1` | 10 | Determines if a Kiosk session can expire. Defaults to 'true'. |
| `KioskCharacterTemplateSet1` | `0` | 10 | Character template set ID 1 to select at character creation. Defaults to 0. |
| `KioskCharacterTemplateSet2` | `0` | 10 | Character template set ID 2 to select at character creation. Defaults to 0. |
| `KioskLobbyKickSeconds` | `30.000000` | 10 | Seconds until an expired session kicks the player back to the lobby. Defaults to 30. |
| `KioskWarmupSeconds` | `15.000000` | 10 | Seconds to lockdown controls on the welcome screen. Defaults to 15. |
| `lastAddonVersion` | `0` | 4 | Addon interface version number from previous build |
| `lastAttemptedExternalEventURLHash` | `0` | 4 |  |
| `lastCharacterIndex` | `0` | 4 | Last character selected |
| `lastGarrisonMissionTutorial` | `0` | 4 | Stores the last garrison mission tutorial the player has accepted |
| `lastLockedTieredEntranceCompanionAbilities` |  | 4 | Serialized mapping using a PDE ID. Stores the nodeIDs of the locked delve companion abilities, to highlight them when unlocked. |
| `lastRenownForCovenant1` | `0` | 4 | Stores the Kyrian renown when Renown UI is closed |
| `lastRenownForCovenant2` | `0` | 4 | Stores the Venthyr renown when Renown UI is closed |
| `lastRenownForCovenant3` | `0` | 4 | Stores the NightFae renown when Renown UI is closed |
| `lastRenownForCovenant4` | `0` | 4 | Stores the Necrolord renown when Renown UI is closed |
| `lastRenownForDelvesSeason` | `0` | 4 | Stores the Delves Season faction renown when Renown UI is closed |
| `lastSelectedClubId` | `0` | 4 | The last club that was selected by the user. We default to this club when the player opens the communities frame if the player isn't in a guild. |
| `lastSelectedTieredEntranceTier` |  | 4 | Serialized mapping using a PDE ID. Stores the last selected difficulty tier. If 0, the player will be forced to select a tier. |
| `lastTalkedToGM` |  | 4 | Stores the last GM someone was talking to in case they reload the UI while the GM chat window is open. |
| `lastTransmogCustomSetIDNoSpec` |  | 4 | SetID of the last applied transmog custom set |
| `lastTransmogCustomSetIDSpec1` |  | 4 | SetID of the last applied transmog custom set for the 1st spec |
| `lastTransmogCustomSetIDSpec2` |  | 4 | SetID of the last applied transmog custom set for the 2nd spec |
| `lastTransmogCustomSetIDSpec3` |  | 4 | SetID of the last applied transmog custom set for the 3rd spec |
| `lastTransmogCustomSetIDSpec4` |  | 4 | SetID of the last applied transmog custom set for the 4th spec |
| `lastTransmogOutfitIDNoSpec` |  | 4 | SetID of the last applied transmog outfit |
| `latestSplashScreen` | `0` | 4 | The ID of the latest splash screen from the UISPLASHSCREEN table. |
| `latestTransmogSetSource` | `0` | 4 | itemModifiedAppearanceID of the latest collected source belonging to a set |
| `launchAgent` | `1` | 4 | Set this to have the client start up Agent |
| `lfdCollapsedHeaders` |  | 4 | Stores which LFD headers are collapsed. |
| `lfdSelectedDungeons` |  | 4 | Stores which LFD dungeons are selected. |
| `lfgListAdvancedFilterMinRating` | `0` | 4 | Minimum mythic plus rating of the leader of the group to find |
| `lfgListAdvancedFilterRemovedActivities` |  | 4 | List of activity IDs to filter against |
| `lfgListAdvancedFilters` | `0` | 4 | Advanced LFG filters for dungeons that are booleans |
| `lfgListAdvancedFiltersVersion` | `0` | 4 | Version for lfgListAdvancedFilters |
| `lfgListSearchLanguages` | `0` | 4 | A simple bitfield for what languages we want to search in. |
| `lfgSelectedRoles` | `0` | 4 | Stores what roles the player is willing to take on. |
| `linear` | `1` | 1 | Linear: %d. 0- disabled (live), 1- linear |
| `loadDeprecationFallbacks` | `1` | 4 | When enabled, Deprecation_* addons are loaded to provide fallbacks for deprecated script APIs. |
| `locale` |  | 5 | Set the game locale |
| `locateViewerMaxJobs` | `32` | 1 | Maximum job threads for LocateViewer |
| `lockActionBars` | `1` | 4 | Whether the action bars should be locked, preventing changes |
| `lodObjectCullDist` | `30` | 1 | Lod object culling dist minimum |
| `lodObjectCullSize` | `15` | 5 |  |
| `lodObjectFadeScale` | `100` | 5 |  |
| `lodObjectMinSize` | `20` | 1 | Lod object min size |
| `lodObjectSizeScale` | `1` | 1 | Scales all objects size for culling |
| `LogFps` |  | 1 | Log FPS data to file. Optionally pass in polling freq in seconds, default 1 second. Call again to end logging. |
| `logout` |  | 5 |  |
| `lootUnderMouse` | `1` | 4 | Whether the loot window should open under the mouse |
| `lossOfControl` | `1` | 4 | Enables loss of control spell banner |
| `lossOfControlDisarm` | `2` | 4 | Setting for Loss of Control - Disarm |
| `lossOfControlFull` | `2` | 4 | Setting for Loss of Control - Full Loss |
| `lossOfControlInterrupt` | `2` | 4 | Setting for Loss of Control - Interrupt |
| `lossOfControlRoot` | `2` | 4 | Setting for Loss of Control - Root |
| `lossOfControlSilence` | `2` | 4 | Setting for Loss of Control - Silence |
| `LowLatencyMinInterval` | `-1` | 1 | Min frame time (in microseconds) for Low Latency systems. Pass -1 to use monitor's refresh rate. |
| `LowLatencyMode` | `0` | 5 |  |
| `luaErrorExceptions` | `1` | 4 | Enable exceptions for non-tainted lua errors |
| `M2ForceAdditiveParticleSort` | `0` | 1 | force all particles to sort as though they were additive |
| `M2UseInstancing` | `1` | 1 | use hardware instancing |
| `M2UseThreads` | `1` | 1 | multithread model animations |
| `majorFactionRenownMap` |  | 4 | Serialized mapping of faction ID to last known renown rank/level. Updated when the Renown UI is closed, used to control animations in the Major Faction UI. |
| `mapFade` | `1` | 4 | Whether to fade out the world map when moving |
| `MaxCharacterComponentLoadStartsPerFrame` | `4` | 1 | Maximum number of character component textures to composit per frame - range 1-8 |
| `maxFPS` | `120` | 1 | Set FPS limit. Min 8 |
| `maxFPSBk` | `30` | 1 | Set background FPS limit. Min 8 |
| `maxFPSLoading` | `10` | 1 | Set loading screen max FPS |
| `maximumConnectionAttempts` | `2` | 6 | Maximum number of times to try to connect to a server using QUIC before doing TCP |
| `maxLevelSpecsUsed` | `0` | 4 | The specs the player has switched to at max level |
| `maxLightCount` |  | 1 | Maximum lights to render |
| `maxLightDist` | `2048` | 1 | Maximum distance to render lights |
| `MaxObservedPetBattles` | `4` | 5 | Maximum number of observed pet battles |
| `minFontHeight` | `0.000000` | 4 | Minimum font size. Any font with a height smaller than this will have it clamped to this value. |
| `miniCommunitiesFrame` | `0` | 4 | Whether or not the communities frame has been toggled to smaller size |
| `miniDressUpFrame` | `0` | 4 | Whether or not the dress up has been toggled to smaller size |
| `minimapInsideZoom` | `0` | 4 | The current indoor minimap zoom level |
| `minimapPortalMax` | `99` | 4 | Max Number of Portals to traverse for minimap |
| `minimapShapeshiftTracking` |  | 4 | Stores shapeshift-specific tracking spells that were active last session. |
| `minimapShowPlayerCoords` | `1` | 4 | Show player coordinates on the minimap |
| `minimapTrackedInfov4` | `2162728` | 4 | Stores the minimap tracking that was active last session. |
| `minimapTrackingClosestOnly` | `1` | 4 | If enabled, show only the closest tracked icon for certain minimap icon types. |
| `minimapTrackingShowAll` | `0` | 4 | If enabled, show dropdown for configuring all possible minimap tracking options. |
| `minimapZoom` | `0` | 4 | The current outdoor minimap zoom level |
| `miniWorldMap` | `1` | 4 | Whether or not the world map has been toggled to smaller size |
| `missingTransmogSourceInItemTooltips` | `0` | 4 | Whether to show if you have collected the appearance of an item but not from that item itself |
| `motionSicknessFocalCircle` | `0` | 4 | Enables a focal circle showing up when mounted |
| `motionSicknessLandscapeDarkening` | `0` | 4 | Enables landscape darkening at higher speeds |
| `mountJournalGeneralFilters` | `0` | 4 | Bitfield for which collected filters are applied in the mount journal |
| `mountJournalShowPlayer` | `0` | 4 | Show the player on the mount preview. |
| `mountJournalSourcesFilter` | `0` | 4 | Bitfield for which source filters are applied in the mount journal |
| `mountJournalTypeFilter` | `0` | 4 | Bitfield for which type filters are applied in the mount journal |
| `mouseAcceleration` | `-1` | 4 | -1: use desktop mouse acceleration, 0: disable mouse acceleration, 1: enable mouse acceleration |
| `MouseHiddenInRelativeMode` | `1` | 4 | Disabling may work around issues in relative mode in some rare cases |
| `mouseInvertPitch` | `0` | 4 |  |
| `mouseInvertYaw` | `0` | 4 |  |
| `mouseSpeed` | `0.025000` | 4 |  |
| `MoveHistoryEventLog` | `0` | 5 |  |
| `movePadInPressAndHoldMode` | `0` | 4 | When true the MovePad buttons are activated on mouse down and deactivated on mouse up |
| `movePadLocked` | `1` | 4 | When false the MovePad can be moved by the player |
| `movieSubtitle` | `1` | 4 | Show movie subtitles |
| `movieSubtitleBackground` | `2` | 4 | Adds a background to cinematic subtitles -> 1: off, 2: dark, 3: light |
| `movieSubtitleBackgroundAlpha` | `70` | 4 | Sets the cinematic subtitles background alpha from 0-100. Default is 70% |
| `MSAAAlphaTest` | `1` | 1 | Enable MSAA for alpha-tested geometry |
| `MSAAQuality` | `0` | 1 | Multisampling AA quality |
| `nameplateAuraScale` | `1.000000` | 4 | Controls the size multiplier for buffs and debuffs on nameplates. |
| `nameplateBottomInset` | `0.100000` | 4 | The inset from the bottom (in screen percent) that nameplates are clamped to. |
| `nameplateCastBarDisplay` | `[` | 4 | Determines what information is displayed on nameplate castbars. |
| `nameplateCheckDistanceForTarget` | `0` | 4 | If false, show our target's nameplate even if they're very far away. |
| `nameplateDebuffPadding` | `0` | 4 | The padding between the debuff list and the health bar on nameplates. |
| `nameplateEnemyNpcAuraDisplay` | `G` | 4 | Determines how buffs, debuffs, and crowd control are displayed on enemy Npc nameplates. |
| `nameplateEnemyPlayerAuraDisplay` | `G` | 4 | Determines how buffs, debuffs, and crowd control are displayed on enemy player nameplates. |
| `nameplateForceShowUnitName` | `1` | 4 | If true, nameplates will always show the unit name regardless of other unit name settings. |
| `nameplateFriendlyPlayerAuraDisplay` | `C` | 4 | Determines how buffs, debuffs, and crowd control are displayed on friendly player nameplates. |
| `nameplateGameObjectMaxDistance` | `30.000000` | 4 | The max distance to show player nameplates for game objects |
| `nameplateInfoDisplay` | `D` | 4 | Determines what information is displayed on nameplates. |
| `nameplateMaxAlpha` | `1.000000` | 4 | The max alpha of nameplates (when setting alpha based on distance). |
| `nameplateMaxAlphaDistance` | `40.000000` | 4 | The distance from the camera that nameplates will reach their maximum alpha. |
| `nameplateMaxDistance` | `45.000000` | 4 | The max distance to show nameplates. |
| `nameplateMaxScale` | `1.000000` | 4 | The max scale of nameplates. |
| `nameplateMaxScaleDistance` | `10.000000` | 4 | The distance from the camera that nameplates will reach their maximum scale. |
| `nameplateMinAlpha` | `0.600000` | 4 | The minimum alpha of nameplates (when setting alpha based on distance). |
| `nameplateMinAlphaDistance` | `10.000000` | 4 | The distance from the max distance that nameplates will reach their minimum alpha. |
| `nameplateMinScale` | `0.800000` | 4 | The minimum scale of nameplates. |
| `nameplateMinScaleDistance` | `10.000000` | 4 | The distance from the max distance that nameplates will reach their minimum scale. |
| `nameplateMotionSpeed` | `0.025000` | 4 | Controls the rate at which nameplate animates into their target locations [0.0-1.0] |
| `nameplateNotSelectedAlpha` | `-1.000000` | 4 | When you have a target, the alpha of other nameplates (not used if value is negative). |
| `nameplateOccludedAlphaMult` | `0.400000` | 4 | Alpha multiplier of nameplates for occluded targets. |
| `nameplateOtherAtBase` | `0` | 4 | Position other nameplates at the base, rather than overhead |
| `nameplateOverlapH` | `0.800000` | 4 | Percentage amount for horizontal overlap of nameplates |
| `nameplateOverlapV` | `1.100000` | 4 | Percentage amount for vertical overlap of nameplates |
| `nameplatePlayerMaxDistance` | `40.000000` | 4 | The max distance to show player nameplates. |
| `nameplatePlayRemovalAnimation` | `1` | 4 | If true, play a scale/alpha animation when a nameplate is removed. If false, remove the nameplate instantly. |
| `nameplateSelectedAlpha` | `1.000000` | 4 | The alpha of the selected nameplate. |
| `nameplateSelectedScale` | `1.200000` | 4 | The scale of the selected nameplate. |
| `nameplateShowAll` | `1` | 4 | If true, nameplates are shown all the time. If false, nameplates are only shown in combat. |
| `nameplateShowAllPersonalAuras` | `0` | 4 | If true, show all personal auras on nameplates, regardless of whether they are normally flagged to be shown. |
| `nameplateShowCastBars` | `1` | 4 | Show cast bars for unit nameplates. |
| `nameplateShowClassColor` | `0` | 4 | Used to display the class color in enemy nameplate health bars |
| `nameplateShowDebuffsOnFriendly` | `1` | 4 | Whether debuffs are shown on friendly nameplates. |
| `nameplateShowEnemies` | `0` | 4 | Whether enemy nameplates are shown. |
| `nameplateShowEnemyGuardians` | `0` | 4 | Whether enemy guardian nameplates are shown. |
| `nameplateShowEnemyMinions` | `0` | 4 | Whether enemy minion nameplates are shown. |
| `nameplateShowEnemyMinus` | `0` | 4 | Whether enemy nameplates for entities with a minus sign (indicating they are weaker than the player) are shown. |
| `nameplateShowEnemyPets` | `0` | 4 | Whether enemy pet nameplates are shown. |
| `nameplateShowEnemyTotems` | `0` | 4 | Whether enemy totem nameplates are shown. |
| `nameplateShowFriendlyClassColor` | `0` | 4 | Used to display the class color in friendly nameplate health bars |
| `nameplateShowFriendlyNpcs` | `0` | 4 | Whether nameplates are shown for friendly npcs. |
| `nameplateShowFriendlyPlayerGuardians` | `0` | 4 | Whether friendly player guardian nameplates are shown. |
| `nameplateShowFriendlyPlayerMinions` | `0` | 4 | Whether friendly player minion nameplates are shown. |
| `nameplateShowFriendlyPlayerPets` | `0` | 4 | Whether friendly player pet nameplates are shown. |
| `nameplateShowFriendlyPlayers` | `0` | 4 | Whether nameplates are shown for friendly players. |
| `nameplateShowFriendlyPlayerTotems` | `0` | 4 | Whether friendly player totem nameplates are shown. |
| `nameplateShowFriendlyRealmName` | `1` | 4 | Used to show or hide the realm name in friendly player unit nameplate names. |
| `nameplateShowOffscreen` | `0` | 4 | When enabled, the nameplate is always shown if owner is in combat with player or player's group member. |
| `nameplateShowOnlyNameForFriendlyPlayerUnits` | `0` | 4 | Used to hide every part of the nameplate but the name for friendly player units. |
| `nameplateShowSelf` | `0` | 4 | Whether the personal resource display is shown. |
| `nameplateSimplifiedScale` | `0.300000` | 4 | Scale used for simplified nameplates. |
| `nameplateSimplifiedTypes` | `` | 4 | Determines what types of nameplates are displayed in a more simple and streamlined way. |
| `nameplateSize` | `1` | 4 | Provides discrete values that are translated into specific horizontal and vertical scales defined in lua for displaying nameplates. |
| `nameplateStackingTypes` | `` | 4 | Determines which types of nameplates stack to prevent overlapping each other. |
| `nameplateStyle` | `1` | 4 | Determines how nameplate contents are displayed. |
| `nameplateTargetBehindMaxDistance` | `0.100000` | 4 | The max distance to show the target nameplate when the target is behind the camera. |
| `nameplateTargetRadialPosition` | `0` | 4 | When target is off screen, position its nameplate radially around sides and bottom. 1: Target Only. 2: All In Combat |
| `nameplateThreatDisplay` | `` | 4 | Determines how threat is displayed on nameplates. |
| `nameplateTopInset` | `0.080000` | 4 | The inset from the top (in screen percent) that nameplates are clamped to. |
| `nameplateUseClassColorForFriendlyPlayerUnitNames` | `0` | 4 | Used to display the class color in friendly player unit nameplate names. |
| `nearclip` | `0.2` | 1 | Near clip plane distance |
| `NeighborhoodAddManager` |  | 0 | Add a neighborhood manager. <PlayerGUID> |
| `NeighborhoodCancelInvitation` |  | 0 | Cancel invitation sent for a private charter neighborhood <PlayerGUID> |
| `NeighborhoodGetInvites` |  | 0 | Get all invites for the neighborhood you are in |
| `NeighborhoodInviteResident` |  | 0 | Invite a resident to a private charter neighborhood <PlayerGUID> |
| `NeighborhoodRemoveManager` |  | 0 | Remove a neighborhood manager. <PlayerGUIID> |
| `NeighborhoodSetName` |  | 0 | Renames the current neighborhood <neighborhoodName> |
| `NeighborhoodSetPublic` |  | 0 | Set the neighborhood to either public <1> or private <2> |
| `newDelvesSeason` | `1` | 4 | Signals a new delves season for the user, so when they open the companion config UI it shows them a helptip with season info |
| `newMythicPlusSeason` | `1` | 4 | Signals a new mythic+ season for the user, so when they open the UI it shows them the info about the season |
| `newPvpSeason` | `1` | 4 | Signals a new pvp season for the user, so when they open the UI it shows them the info about the season |
| `noBuffDebuffFilterOnTarget` | `1` | 4 | Do not filter buffs or debuffs at all on targets |
| `NonEmitterCombatRange` | `6400.000000` | 4 | Range to stop shoulder/weapon emissions outside combat |
| `NotchedDisplayMode` | `1` | 5 | Do nothing = 0. Shift UI down = 1. Shift everything down = 2. |
| `notifiedOfNewMail` | `0` | 4 | Stores whether the player has been previously notified of new mail. Only set to false once everything in their Inbox has been marked as read. |
| `numCurrencyCategories` | `0` | 4 | Stores the number of currency categories that existed the last time we logged in |
| `numReputationHeaders` | `0` | 4 | Stores the number of reputation headers that existed the last time we logged in |
| `ObjectSelectionCircle` | `1` | 4 |  |
| `occludedSilhouettePlayer` | `0` | 4 | Show a silhouette of your character when obstructed |
| `occlusionMaxJobs` | `5` | 1 | Maximum job threads for occlusion render |
| `OfferNeighborhoodOwnership` |  | 0 | Offer primary ownership of the neighborhood to another player. <selected target or PlayerGUID> |
| `onlyShowCollectedItemsInJournal` | `1` | 4 | For all Collections, only display items that this account has already collected. |
| `optOutIngameSurveys` | `0` | 4 | Whether we are opted out of receiving surveys. |
| `orderHallMissionTutorial` | `0` | 4 | Stores information about which order hall mission tutorials the player has seen |
| `otherRolesAzeriteEssencesHidden` | `0` | 4 | Whether to collapse the Azerite Essences for player's other roles |
| `outdoorMinAltitudeDistance` | `10` | 4 | Minimum altitude distance for outdoor objects when you are also outdoors before the altitude difference marker displays |
| `Outline` | `0` | 4 | Outline Mode |
| `OutlineEngineMode` | `0` | 5 |  |
| `outlineModeShowLootEffectWhenDisabled` | `0` | 4 | When Outline Mode is disabled, replace passive outlines with loot sparkles |
| `outlineMouseOverFadeDuration` | `0.9` | 0 |  |
| `outlineSelectionFadeDuration` | `0.32` | 0 |  |
| `outlineSoftInteractFadeDuration` | `0.3` | 0 |  |
| `overrideArchive` | `0` | 4 | Whether or not the client loads alternate data |
| `overrideScreenFlash` | `0` | 4 | Overrides fade color options so that it always fades to black |
| `particleDensity` | `100` | 1 | Particle density |
| `particleMTDensity` | `100` | 1 | Multi-Tex particle density |
| `particulatesEnabled` | `1` | 1 | Particulates enabled |
| `partyBackgroundOpacity` | `0.500000` | 4 | The opacity of the party background |
| `partyInvitesCollapsed_Glue` | `0` | 4 | The info for pending invites has been shown |
| `Pathing` | `0` | 5 |  |
| `pathSmoothing` | `1` | 4 | NPC will round corners on ground paths |
| `pbrLiquidDetail` | `0` | 5 |  |
| `pendingInviteInfoShown` | `0` | 4 | The info for pending invites has been shown |
| `performedDeathTutorial` | `0` | 4 | remember that we already did the death tutorial |
| `performedVendorTutorial` | `0` | 4 | remember that we already did the vendor tutorial |
| `perksActivitiesCurrentMonth` | `0` | 4 | Current month for perks activities |
| `perksActivitiesLastPoints` | `0` | 4 | Last seen number of influence points in the perks progress bar |
| `perksActivitiesPendingCompletion` |  | 5 |  |
| `persistMoveLogOnTransfer` | `0` | 0 | Set to 1 to automatically re-enable logging on the current movelog target after a transfer |
| `petJournalFilters` | `0` | 4 | Bitfield for which collected filters are applied in the pet journal |
| `petJournalFilterVersion` | `0` | 4 | Current filter version. Will reset all filters to their defaults if out of date. |
| `petJournalSort` | `0` | 4 | Sorting value for the pet journal |
| `petJournalSourceFilters` | `0` | 4 | Bitfield for which source filters are applied in the pet journal |
| `petJournalTab` | `1` | 4 | Stores the last tab the pet journal was opened to |
| `petJournalTypeFilters` | `0` | 4 | Bitfield for which type filters are applied in the pet journal |
| `petStableShowExoticOnly` | `0` | 4 | Filter value for hunter pet stable. Will only show exotic pets in stable if true |
| `petStableSort` | `1` | 4 | Sorting value for the hunter pet stable |
| `PhaseHistory` | `0` | 5 |  |
| `physCreateForceField` |  | 0 |  |
| `physCulling` |  | 0 |  |
| `physCullingDist` |  | 0 |  |
| `physEnable` |  | 0 |  |
| `physEnableVegOverrides` |  | 0 | Toggles physics vegetation cvars for tuning vegetation physics simulation etc. |
| `physicsLevel` | `1` | 5 |  |
| `physReset` |  | 0 |  |
| `physVegMinPushDist` |  | 0 | Squared distance the unit must be within from the bone to begin pushing it. |
| `physVegPosMaxPush` |  | 0 | Maximum distance in yards a bone can be pushed from its base position before being clamped. |
| `physVegPosPushAmt` |  | 0 | Distance per frame in yards the bone is pushed while a unit moves along the push direction, scaled by delta time. |
| `physVegPosRelaxSpeed` |  | 0 | Speed at which the bone will return to rest once the unit leaves the volume, or crosses the max push threshold. |
| `physVegVelMaxPush` |  | 0 | Max distance the bone can be pushed additionally when a unit has velocity while moving in the veg, pushed along the units vel direction. |
| `physVegVelSpeed` |  | 0 | Speed at which the bone moves along the velocity direction when a unit has move while within the veg. |
| `pingCategoryTutorialShown` | `0` | 4 | Has shown the ping category tutorial dialog |
| `pingMode` | `0` | 4 | Determines which mode is used to use the ping system. |
| `pingTarget` | `0` | 4 | Determines how pinging in the world should behave for the ping system. |
| `pitchLimit` |  | 4 |  |
| `playerColorOverrides` |  | 4 | Any color override values that are different from the default values for an account |
| `PlayerDeclineHousingInvitation` |  | 0 | Decline invitation received for a private charter neighborhood <neighborhoodGUID> |
| `PlayerGetHousingInvitation` |  | 0 | Retrieve a neighborhood invite if player has one |
| `PlayerSpawnTracking` | `0` | 5 |  |
| `playIntroMovie` | `0` | 4 | Starting expansion movie to play on startup |
| `plunderstormRealm` | `0` | 5 |  |
| `POIShiftComplete` | `0.3` | 0 |  |
| `portal` |  | 6 | Name of Battle.net portal to use |
| `PraiseTheSun` | `0` | 4 |  |
| `PreemptiveCastEnable` | `0` | 5 | Enable preemptive triggering of cast visuals based on spell release timing |
| `preloadLoadingDistObject` | `512` | 5 | Object preload distance when loading |
| `preloadLoadingDistTerrain` | `1024` | 5 | Terrain preload distance when loading |
| `preloadPlayerModels` | `1` | 4 | Preload all local racial models into memory |
| `preloadStreamingDistObject` | `64` | 5 | Object preload distance when streaming |
| `preloadStreamingDistTerrain` | `256` | 5 | Terrain preload distance when streaming |
| `PreventOsIdleSleep` | `0` | 10 | Enable this to prevent the computer from idle sleeping while the game is running |
| `primaryProfessionsFilter` | `1` | 4 | If enabled, primary profession world quests icons will be shown on world maps |
| `ProcDebugEventLog` | `0` | 5 |  |
| `profanityFilter` | `1` | 4 | Whether to enable mature language filtering |
| `professionAccessorySlotsExampleShown` | `0` | 4 | If the profession gear slots example has been shown |
| `professionsAllocateBestQualityReagents` | `1` | 4 | Indicates if best quality reagents should be automatically allocated in the crafting UI. |
| `professionsAllocateBestQualityReagentsCustomer` | `1` | 4 | Indicates if best quality reagents should be automatically allocated in the customer crafting order UI. |
| `professionsFlyoutHideUnowned` | `0` | 4 | Boolean indicating if unowned items are hidden in the profession slot flyouts |
| `professionsOrderDurationDropdown` | `2` | 4 | The previously selected duration index in the professions customer order form dropdown |
| `professionsOrderRecipientDropdown` | `1` | 4 | The previously selected order recipient index in the professions customer order form dropdown |
| `professionToolSlotsExampleShown` | `0` | 4 | If the profession gear slots example has been shown |
| `projectedTextures` | `0` | 5 |  |
| `PushToTalkSound` | `0` | 7 | Play a sound when voice recording activates and deactivates |
| `pvpFramesDisplayClassColor` | `0` | 4 | Colors pvp frames with the class color |
| `pvpFramesDisplayOnlyHealerPowerBars` | `0` | 4 | Whether to display power bars only for healers on Pvp Frames |
| `pvpFramesDisplayPowerBars` | `0` | 4 | Whether to display mana, rage, etc. on Pvp Frames |
| `pvpFramesHealthText` | `none` | 4 | How to display health text on the pvp frames |
| `pvpOptionDisplayPets` | `0` | 4 | Whether to display pets on the pvp frames |
| `pvpSelectedRoles` | `0` | 4 | Stores what roles the player will fulfill in a BG. |
| `QuestEventLog` | `0` | 5 |  |
| `questLogOpen` | `1` | 4 | Whether the quest log appears the side of the windowed map.  |
| `questPOI` | `1` | 4 | If enabled, the quest POI system will be used. |
| `questPOILocalStory` | `1` | 4 | Worldmap filter setting for showing any local story quest offers on the map, this is an independent setting for the world map only. |
| `questPOIWQ` | `1` | 4 | Worldmap filter setting for showing any WQs on the map, this is in conjunction with the questPOI cvar. |
| `questTextContrast` | `0` | 4 | Whether to increase text contrast in Quest UIs |
| `quit` |  | 5 |  |
| `RAIDclusteredShading` | `1` | 1 | Allow forward transparent lighting |
| `RAIDcomponentTextureLevel` | `0` | 1 | Level of detail for character component textures. 0 means full detail. |
| `RAIDDepthBasedOpacity` | `1` | 1 | Raid Enable/Disable Soft Edge Effect |
| `RAIDdoodadLodScale` | `100` | 1 | Raid doodad level of detail scale |
| `RAIDentityLodDist` | `10` | 1 | Raid Entity level of detail distance |
| `RAIDentityShadowFadeScale` | `10` | 5 |  |
| `RAIDfarclip` | `1000` | 5 |  |
| `raidFramesCenterBigDefensive` | `1` | 4 | Show big defensive raid buffs in the center of the unit frame |
| `raidFramesDispelIndicatorAnimatedBorder` | `0` | 4 | When showing dispel indicators, display an animated border |
| `raidFramesDispelIndicatorOverlay` | `1` | 4 | When showing dispel indicators, also show a color gradient overlay |
| `raidFramesDispelIndicatorOverlayAnimation` | `0` | 4 | When showing dispel indicators, use a pulsing alpha anim |
| `raidFramesDispelIndicatorType` | `2` | 4 | Choose which dispel icon indicators to show in raid frames |
| `raidFramesDisplayAggroHighlight` | `1` | 4 | Whether to display aggro highlights on Raid Frames |
| `raidFramesDisplayBuffs` | `1` | 4 | Whether to display buffs on Raid Frames |
| `raidFramesDisplayClassColor` | `0` | 4 | Colors raid frames with the class color |
| `raidFramesDisplayDebuffs` | `1` | 4 | Whether to display debuffs on Raid Frames |
| `raidFramesDisplayIncomingHeals` | `1` | 4 | Whether to display incoming heals on Raid Frames |
| `raidFramesDisplayLargerRoleSpecificDebuffs` | `1` | 4 | Show role-specific debuffs as larger on Raid Frames |
| `raidFramesDisplayOnlyDispellableDebuffs` | `0` | 4 | Whether to display only dispellable debuffs on Raid Frames |
| `raidFramesDisplayOnlyHealerPowerBars` | `0` | 4 | Whether to display power bars only for healers on Raid Frames |
| `raidFramesDisplayPowerBars` | `0` | 4 | Whether to display mana, rage, etc. on Raid Frames |
| `raidFramesHealthBarColor` | `FF2B9305` | 4 | Colors raid frame health bars with a custom color if the user doesn't want class colors, ARGB format |
| `raidFramesHealthBarColorBG` | `FF141414` | 4 | Colors raid frame backgrounds with a custom color, ARGB format |
| `raidFramesHealthText` | `none` | 4 | How to display health text on the raid frames |
| `raidFramesHeight` | `36` | 4 | The height of the individual raid frames |
| `raidFramesPosition` |  | 4 | Where the raid frames should be placed |
| `raidFramesWidth` | `72` | 4 | The width of the individual raid frames |
| `RAIDgiQuality` | `1` | 5 |  |
| `raidGraphicsBloomUserMult` |  | 5 |  |
| `raidGraphicsComputeEffects` | `3` | 5 |  |
| `raidGraphicsDepthEffects` | `3` | 5 |  |
| `raidGraphicsEnvironmentDetail` | `6` | 5 |  |
| `raidGraphicsGroundClutter` | `6` | 5 |  |
| `raidGraphicsLightMode` | `2` | 5 |  |
| `raidGraphicsLiquidDetail` | `2` | 5 |  |
| `raidGraphicsOutlineMode` | `2` | 5 |  |
| `raidGraphicsParticleDensity` | `3` | 5 |  |
| `raidGraphicsPBRLiquidDetail` | `1` | 5 |  |
| `raidGraphicsProjectedTextures` | `1` | 5 |  |
| `RAIDgraphicsQuality` | `6` | 5 |  |
| `raidGraphicsShadowQuality` | `4` | 5 |  |
| `raidGraphicsSpellDensity` | `1` | 5 |  |
| `raidGraphicsSSAO` | `3` | 5 |  |
| `raidGraphicsTextureResolution` | `2` | 5 |  |
| `raidGraphicsViewDistance` | `6` | 5 |  |
| `RAIDgroundEffectDensity` | `16` | 5 |  |
| `RAIDgroundEffectDist` | `70` | 5 |  |
| `RAIDgroundEffectFade` | `70` | 1 | Raid Ground effect fade |
| `RAIDhorizonClip` | `1600` | 5 |  |
| `RAIDhorizonStart` | `800` | 5 |  |
| `RAIDlodObjectCullDist` | `30` | 1 | Lod object culling dist minimum |
| `RAIDlodObjectCullSize` | `15` | 5 |  |
| `RAIDlodObjectFadeScale` | `100` | 1 | Lod object fade scale |
| `RAIDlodObjectMinSize` | `20` | 5 |  |
| `raidOptionDisplayMainTankAndAssist` | `1` | 4 | Whether to display main tank and main assist units in the raid frames |
| `raidOptionDisplayPets` | `0` | 4 | Whether to display pets on the raid frames |
| `raidOptionIsShown` | `1` | 4 | Whether the Raid Frames are shown |
| `raidOptionKeepGroupsTogether` | `0` | 4 | The way to group raid frames |
| `raidOptionLocked` | `lock` | 4 | Whether the raid frames are locked |
| `raidOptionShowBorders` | `1` | 4 | Displays borders around the raid frames. |
| `raidOptionSortMode` | `role` | 4 | The way to sort raid frames |
| `RAIDOutlineEngineMode` | `0` | 5 |  |
| `RAIDparticleDensity` | `100` | 5 |  |
| `RAIDparticleMTDensity` | `100` | 1 | Multi-Tex particle density |
| `RAIDParticulatesEnabled` | `1` | 1 | Enabling particulates (0-1) |
| `RAIDpbrLiquidDetail` | `0` | 5 |  |
| `RAIDprojectedTextures` | `0` | 5 |  |
| `RAIDreflectionMode` | `3` | 5 |  |
| `RAIDrefraction` | `0` | 5 |  |
| `RAIDRenderFormat` | `2` | 1 | 0 = BGRA8Unorm, 1 = A2BGR10Unorm, 2 = RGBA16F, 3 = RGBA32F |
| `RAIDrippleDetail` | `2` | 5 |  |
| `RAIDsettingsEnabled` | `0` | 1 | Raid graphic settings are available |
| `RAIDshadowBlendCascades` | `0` | 5 |  |
| `RAIDshadowMode` | `0` | 5 |  |
| `RAIDshadowNumCascades` | `1` | 5 |  |
| `RAIDshadowRt` | `0` | 1 | Raid Raytraced shadows (0-2) |
| `RAIDshadowSoft` | `0` | 5 |  |
| `RAIDshadowTextureSize` | `1024` | 5 |  |
| `RAIDspellClutter` | `2` | 1 | Spell Density |
| `RAIDSSAO` | `0` | 5 |  |
| `RAIDsunShafts` | `0` | 5 |  |
| `RAIDterrainLodDist` | `400` | 5 |  |
| `RAIDTerrainLodDiv` | `768` | 5 |  |
| `RAIDterrainMipLevel` | `0` | 1 | Terrain blend map mip level |
| `RAIDVolumeFog` | `1` | 1 | Volume Fog |
| `RAIDVolumeFogLevel` | `3` | 1 | Volume Fog Level (0-4) |
| `RAIDWaterDetail` | `0` | 5 |  |
| `RAIDweatherDensity` | `2` | 5 |  |
| `RAIDwmoLodDist` | `650` | 5 |  |
| `RAIDworldBaseMip` | `0` | 1 | World texture base mip |
| `rawMouseEnable` | `0` | 4 | Enable raw mouse input |
| `reflectionDownscale` | `0` | 1 | Reflection downscale |
| `reflectionMode` | `3` | 1 | Reflection mode |
| `refraction` | `0` | 5 |  |
| `reloadUI` |  | 1 | Reloads the user interface |
| `reloadUIOnAspectChange` | `0` | 5 | Reload the UI on aspect change |
| `remoteTextToSpeech` | `0` | 4 | Enables typing into a voice chat window to speak to other players using the text to speech system |
| `remoteTextToSpeechVoice` | `1` | 4 | Voice option used with Speak for Me where you can send text to speech to other players in voice chat |
| `RenderFormat` | `2` | 1 | 0 = BGRA8Unorm, 1 = A2BGR10Unorm, 2 = RGBA16F, 3 = RGBA32F |
| `RenderScale` | `1.000000` | 1 | Render scale (for supersampling or undersampling) |
| `RenderScaleDowngradeBackgroundMinSize` | `720` | 1 | Min size (in pixels) we can reduce render scale to when under high VRAM pressure when the game does not has focus |
| `RenderScaleDowngradeForegroundMinSize` | `1080` | 1 | Min size (in pixels) we can reduce render scale to when under high VRAM pressure when the game has focus |
| `repeat` |  | 2 | Repeats a command [repeat <count> <command> <args ...>] |
| `ReplaceMyPlayerPortrait` | `0` | 4 | Replaces local player's unit frame portrait with their class icon |
| `ReplaceOtherPlayerPortraits` | `0` | 4 | Replaces other player unit frame portraits with their class icon |
| `reputationsCollapsed` |  | 4 | List of reputation categories that have been collapsed in the Reputation tab |
| `ResampleAlwaysSharpen` | `0` | 1 | Run sharpness pass, even if not using AMD FSR Upscale [0,1] |
| `ResampleQuality` | `3` | 1 | Resample quality |
| `ResampleSharpness` | `0.2` | 1 | FSR sharpness strength [0.0-2.0]. 0 is full strength. -1 to disable. |
| `ResetChallengeMode` |  | 5 |  |
| `ResizeConstraints` | `1` | 5 | 0=None,1=AspectRatioLocked,2=DisableResizing |
| `restrictCalendarInvites` | `1` | 4 | Whether to restrict calendar invites to friends and guilds only. |
| `rippleDetail` | `2` | 1 | Ripple surface detail |
| `rotateMinimap` | `0` | 4 | Whether to rotate the entire minimap instead of the player arrow |
| `runeFadeTime` | `0.2` | 5 | Adjust the time the rune fades from on CD to ready |
| `runeSpentFadeTime` | `0.1` | 5 | Adjust the time the base rune takes to fade out after the rune flash fades out |
| `runeSpentFlashTime` | `0.15` | 5 | Adjust the time the rune flash takes to fade out |
| `sceneOcclusionEnable` | `1` | 1 | Scene software occlusion |
| `screenEdgeFlash` | `1` | 4 | Whether to show a red flash while you are in combat with the world map up |
| `screenshotFormat` | `jpeg` | 1 | Set the format of screenshots |
| `screenshotQuality` | `3` | 1 | Set the quality of screenshots (1 - 10) |
| `screenshotSizeOverride` | `0x0` | 1 | Set the size of screenshots to a specific resolution (e.g. 7680x4320). 0x0 means use the window size |
| `scriptErrors` | `0` | 4 | Whether or not the UI shows Lua errors |
| `scriptProfile` | `0` | 0 | Whether or not script profiling is enabled |
| `scriptWarnings` | `0` | 0 | Whether or not the UI shows Lua warnings |
| `scrollToLogQuest` | `0` | 4 | Whether to scroll to a quest in the quest log when mousing over its map pin |
| `secondaryProfessionsFilter` | `1` | 4 | If enabled, secondary profession world quests icons will be shown on world maps |
| `secureAbilityToggle` | `1` | 4 | Whether you should be protected against accidentally double-clicking an aura |
| `seenAgeVerificationRestrictionState` | `0` | 4 | Last acknowledged Age Verification restriction state. |
| `seenAlliedRaceUnlocks` | `0` | 4 | Bit array for which allied race unlocks have been seen |
| `seenAsiaCharacterUpgradePopup` | `0` | 4 | Seen the free character upgrade popup (Asia) |
| `seenCharacterUpgradePopup` | `6` | 4 | Seen the free character upgrade popup |
| `seenConfigurationWarnings` | `0` | 4 | A bitfield to track which configuration warnings have been seen |
| `seenExpansionTrialPopup` | `6` | 4 | Seen the expansion trial popup |
| `seenLevelSquishPopup` | `0` | 4 | Seen the level squish popup |
| `seenPurchasableClassCapstone` | `0` | 4 | Whether or not the player has ever opened the class talent UI and seen a purchasable capstone node |
| `seenRegionalChatDisabled` | `0` | 4 | Seen the alert indicating chat has been disabled by default. (UK and CA AADC) |
| `seenTimerunningFirstLoginPopup` | `0` | 4 | Seen the timerunning first login popup (value is timerunning season id) |
| `serverAlert` | `https://breaking-news.support.blizzard.com/service/wow-forever-client/live/us/en-US` | 6 | Get the glue-string tag for the URL |
| `ServerMessageEventLog` | `0` | 5 |  |
| `serviceTypeFilter` | `6` | 4 | Which trainer services to show |
| `set` |  | 5 | Set the value of a CVar |
| `SetDifficulty` |  | 5 |  |
| `SetGraphicsQuality` |  | 1 |  |
| `SetGraphicsQualityRAID` |  | 1 |  |
| `shadowBlendCascades` | `0` | 5 |  |
| `shadowMode` | `0` | 5 |  |
| `shadowNumCascades` | `1` | 5 |  |
| `shadowRt` | `0` | 1 | Raytraced shadows (0-3) |
| `shadowSoft` | `0` | 5 |  |
| `shadowTextureSize` | `1024` | 5 |  |
| `ShakeStrengthCamera` | `1.000000` | 4 | Motion sickness control for how much effects can shake the camera |
| `ShakeStrengthUI` | `1.000000` | 4 | Motion sickness control for how much effects can shake in 2D UI |
| `shipyardMissionTutorialAreaBuff` | `0` | 4 | Stores whether the player has accepted the first area buff mission tutorial |
| `shipyardMissionTutorialBlockade` | `0` | 4 | Stores whether the player has accepted the first blockade mission tutorial |
| `shipyardMissionTutorialFirst` | `0` | 4 | Stores whether the player has accepted the first mission tutorial |
| `showAllItemsInTransmog` | `0` | 4 | Shows all items in the transmogger regardless of armor restrictions |
| `ShowAllSpellRanks` | `0` | 4 | show either all spell ranks, or only the highest rank |
| `showArenaEnemyCastbar` | `1` | 4 | Show the spell enemies are casting on the Arena Enemy frames |
| `showArenaEnemyFrames` | `1` | 4 | Show arena enemy frames while in an Arena |
| `showArenaEnemyPets` | `1` | 4 | Show the enemy team's pets on the ArenaEnemy frames |
| `showBattlefieldMinimap` | `0` | 4 | Whether or not the battlefield minimap is shown |
| `showBuilderFeedback` | `1` | 4 | Show animation when building power for builder/spender bar |
| `showCastableBuffs` | `0` | 4 | Show only Buffs the player can cast.  Only applies to raids. |
| `showCreateCharacterRealmConfirmDialog` | `1` | 5 |  |
| `showCustomSetDetails` | `1` | 4 | Whether or not to show custom set details when the dressing room is opened in maximized mode, default on |
| `showDelveEntrancesOnMap` | `1` | 4 | If enabled, delve entrances will display on the world map. |
| `showDispelDebuffs` | `1` | 4 | Show only Debuffs that the player can dispel.  Only applies to raids. |
| `showDungeonEntrancesOnMap` | `1` | 4 | If enabled, dungeon entrances will display on the world map. |
| `showErrors` | `1` | 0 |  |
| `showfootprintparticles` | `1` | 1 | toggles rendering of footprint particles |
| `showHonorAsExperience` | `0` | 4 | Show the honor bar as a regular experience bar in place of rep |
| `showInGameNavigation` | `0` | 4 | 0: Disable IGN, 1: Enable IGN (Default). |
| `showKeyring` | `0` | 4 | Show the keyring button |
| `showLoadingScreenTips` | `1` | 4 | Show loading screen tooltips |
| `showLootSpam` | `1` | 4 | Whether to show full loot rolls in chat. |
| `showMaxLevelAnnouncements` | `1` | 4 | Enables a chat message and sound when someone reaches max level on the realm. |
| `showNPETutorials` | `1` | 4 | display NPE tutorials |
| `showOutfitDetails` | `1` | 4 | Whether or not to show outfit details when the dressing room is opened in maximized mode, default on |
| `showPartyPets` | `0` | 4 | Whether to show pets in the party UI |
| `showPhotosensitivityWarning` | `-1` | 4 | Showing photosensitivity warning on startup |
| `showPingsInChat` | `1` | 4 | Enables ping details being shown in chat. |
| `showPingsOnRaidFrames` | `1` | 4 | Enables ping details being shown on raid frames. |
| `showPlayer` |  | 1 |  |
| `showQuestDifficultyColor` | `1` | 4 | Stores whether to show quest difficulty color in the quest log and quest text |
| `showQuestLevel` | `0` | 4 | Stores whether to show quest levels in the quest list and quest text |
| `showQuestObjectivesInLog` | `1` | 4 | Stores whether to show quest objectives in the quest list in the log |
| `ShowQuestUnitCircles` | `1` | 4 | Determines if units related to a quest display an indicator on the ground. |
| `showScreenNarrationDialog` | `1` | 4 | Show screen narration dialog on startup |
| `showSpectatorTeamCircles` | `1` | 4 | Determines if the team color circles are visible while spectating or commentating a wargame |
| `showSpenderFeedback` | `1` | 4 | Show animation when spending power for builder/spender bar |
| `showSwingTimer` | `0` | 4 | Whether the swing timer is visible |
| `showTamers` | `1` | 4 | If enabled, pet battle icons will be shown on world maps |
| `showTamersWQ` | `1` | 4 | If enabled, WQ pet battle icons will be shown on world maps |
| `showTargetCastbar` | `1` | 4 | Show the spell your current target is casting |
| `showTargetOfTarget` | `0` | 4 | Whether the target of target frame should be shown |
| `showTaxiNodeLearnedIcon` | `0` | 4 | Whether to show an icon over flightmasters' heads when the taxipath has been learned. |
| `showTempMaxHealthLoss` | `1` | 4 | Weather or not to show temporary max health changes on unit health bars |
| `showTimestamps` | `none` | 4 | The format of timestamps in chat or "none" |
| `showToastBroadcast` | `0` | 4 | Whether to show Battle.net message for broadcasts |
| `showToastClubInvitation` | `1` | 4 | Whether to show Battle.net message for club invitations |
| `showToastConversation` | `1` | 4 | Whether to show Battle.net message for conversations |
| `showToastFriendRequest` | `1` | 4 | Whether to show Battle.net message for friend requests |
| `showToastOffline` | `1` | 4 | Whether to show Battle.net message for friend going offline |
| `showToastOnline` | `1` | 4 | Whether to show Battle.net message for friend coming online |
| `showToastWindow` | `1` | 4 | Whether to show Battle.net system messages in a toast window |
| `showTokenFrame` | `0` | 4 | The token UI has been shown |
| `showTutorials` | `1` | 4 | display tutorials |
| `showVKeyCastbar` | `1` | 4 | If the V key display is up for your current target, show the enemy cast bar with the target's health bar in the game field |
| `showVKeyCastbarOnlyOnTarget` | `0` | 4 |  |
| `showVKeyCastbarSpellName` | `1` | 4 |  |
| `simd` | `-1` | 5 | Enable SIMD features (e.g. SSE) |
| `skipTutorialAchievement` | `0` | 4 | skip the account wide tutorial achievement |
| `SkyCloudLOD` | `0` | 1 | Texture resolution for clouds |
| `SlugOpticalWeight` | `0` | 0 | When rendering, coverage values are remapped to increase the optical weight of the glyphs. This can improve the appearance of small text, but usually looks good only for dark text on a light background. |
| `SmartNavigationCursorAnchor` | `5` | 4 | What edge of the cursor to anchor to the button. |
| `SmartNavigationCursorAppearance` | `2` | 4 | What appearance for the cursor to take. |
| `SmartNavigationCursorButtonAnchor` | `1` | 4 | Where in relation to the button to anchor the cursor. |
| `SmartNavigationCursorFlipHorizontal` | `0` | 4 | Flips smart cursor horizontally, making left right. |
| `SmartNavigationCursorFlipVertical` | `0` | 4 | Flips smart cursor vertically, making up down. |
| `SmartNavigationCursorRotationAngle` | `0.000000` | 4 | How much to rotate the smart cursor, in degrees. |
| `SmartNavigationCursorScale` | `2.000000` | 4 | How much scale the cursor. |
| `SmartNavigationScrollSpeed` | `5000.000000` | 4 | How fast areas are scrolled using the right stick. |
| `smoothUnitPhasing` | `1` | 4 | The client will try to smoothly switch between the same on model different phases. |
| `smoothUnitPhasingActorPurgatoryTimeMs` | `1500` | 4 | Time to keep client-actor displays in purgatory before letting go of them, if they were despawned |
| `smoothUnitPhasingAliveTimeoutMs` | `3500` | 4 | Time to wait for an alive unit to get it's despawn message |
| `smoothUnitPhasingDestroyedPurgatoryTimeMs` | `750` | 4 | Time to keep unit displays in purgatory before letting go of them, if they were destroyed |
| `smoothUnitPhasingDistThreshold` | `0.25` | 4 | Distance threshold to active smooth unit phasing. |
| `smoothUnitPhasingEnableAlive` | `1` | 4 | Use units that have not despawn yet if they match, in hopes the despawn message will come later. |
| `smoothUnitPhasingUnseenPurgatoryTimeMs` | `1000` | 4 | Time to keep unit displays in purgatory before letting go of them, if they were just unseen. |
| `smoothUnitPhasingVehicleExtraTimeoutMs` | `1000` | 4 | Extra time to wait before releasing a vehicle, after it has smooth phased. This allows it's passengers to smooth phase as well. |
| `SoftTargetEnemy` | `1` | 4 | Sets when enemy soft targeting should be enabled. 0=off, 1=gamepad, 2=KBM, 3=always |
| `SoftTargetEnemyArc` | `2` | 4 | 0 = No yaw arc allowance, must be directly in front. 1 = Must be in front yaw arc. 2 = Can be anywhere in tab targeting area. |
| `SoftTargetEnemyRange` | `45.000000` | 4 | Max range to soft target enemies (limited to tab targeting range) |
| `SoftTargetForce` | `1` | 4 | Auto-set target to match soft target. 1 = for enemies, 2 = for friends |
| `SoftTargetFriend` | `0` | 4 | Sets when friend soft targeting should be enabled. 0=off, 1=gamepad, 2=KBM, 3=always |
| `SoftTargetFriendArc` | `2` | 4 | 0 = No yaw arc allowance, must be directly in front. 1 = Must be in front yaw arc. 2 = Can be anywhere in targeting area. |
| `SoftTargetFriendRange` | `45.000000` | 4 | Max range to soft target friends (limited to tab targeting range) |
| `SoftTargetIconEnemy` | `0` | 4 | Show icon for soft enemy target |
| `SoftTargetIconFriend` | `0` | 4 | Show icon for soft friend target |
| `SoftTargetIconGameObject` | `0` | 4 | Show icon for sot interact game objects (interactable objects you cannot normally target) |
| `SoftTargetIconInteract` | `1` | 4 | Show icon for soft interact target |
| `SoftTargetInteract` | `1` | 4 | Sets when soft interact should be enabled. 0=off, 1=gamepad, 2=KBM, 3=always |
| `SoftTargetInteractArc` | `0` | 4 | 0 = No yaw arc allowance, must be directly in front. 1 = Must be in front yaw arc. 2 = Can be anywhere in targeting area. |
| `softTargetInteractionTutorialTotalInteractions` | `0` | 4 | Total interactions that the player has used in soft targeting |
| `SoftTargetInteractOnlyInRange` | `0` | 4 | Sets if soft interacts should only be set for targets that are in interact range. |
| `SoftTargetInteractRange` | `10.000000` | 4 | Max range to soft target interacts (limited to tab targeting and individual interact ranges) |
| `SoftTargetInteractRangeIsHard` | `0` | 4 | Sets if it should be a hard range cutoff, even for something you can interact with right now. |
| `SoftTargetLowPriorityIcons` | `0` | 4 | Show interact icons even when there is other visual indicators, such as quest or loot effects |
| `SoftTargetMatchLocked` | `1` | 4 | Match appropriate soft target to locked target. 1 = hard locked target only, 2 = for targets you attack |
| `SoftTargetNameplateEnemy` | `1` | 4 | Always show nameplates for soft enemy target |
| `SoftTargetNameplateFriend` | `0` | 4 | Always show nameplates for soft friend target |
| `SoftTargetNameplateInteract` | `0` | 4 | Always show nameplates for soft interact target |
| `SoftTargetNameplateSize` | `19` | 4 | Size of soft target icon on nameplate (0 to disable) |
| `softTargettingInteractKeySound` | `0` | 4 | Setting for soft targeting that enables sound cues |
| `SoftTargetTooltipDurationMs` | `2000` | 4 |  |
| `SoftTargetTooltipEnemy` | `0` | 4 |  |
| `SoftTargetTooltipFriend` | `0` | 4 |  |
| `SoftTargetTooltipInteract` | `0` | 4 |  |
| `SoftTargetTooltipLocked` | `0` | 4 |  |
| `SoftTargetWithLocked` | `1` | 4 | Allows soft target selection while player has a locked target. 2 = always do soft targeting |
| `SoftTargetWorldtextFarDist` | `40.000000` | 4 |  |
| `SoftTargetWorldtextNearDist` | `4.000000` | 4 |  |
| `SoftTargetWorldtextNearScale` | `1.000000` | 4 |  |
| `SoftTargetWorldtextSize` | `32.000000` | 4 |  |
| `sortCharListByLastActive` | `0` | 4 | Whether to sort the character list by last active time |
| `sortDiskReads` | `0` | 4 | Sort async disk reads to minimize seeks (requires restart) |
| `soulbindsActivatedTutorial` |  | 4 | Bitfield for tutorializing activating soulbinds |
| `soulbindsLandingPageTutorial` |  | 4 | Boolean indicating if the landing page tutorial has been completed. |
| `soulbindsViewedTutorial` |  | 4 | Bitfield for tutorializing viewing soulbinds trees |
| `Sound_AllyPlayerHighpassDSPCutoff` |  | 7 | The cutoff value to use for the Highpass filter on the Ally Player bus (default 80 Hz) |
| `Sound_AlternateListener` | `1` | 7 | When enabled, calculates listener forward by simply using the camera's yaw value, instead of a vector from camera position to listener position |
| `Sound_AmbienceHighpassDSPCutoff` |  | 7 | The cutoff value to use for the Highpass filter on the Ambience bus (default 100 Hz) |
| `Sound_AmbienceVolume` | `0.6` | 7 | Ambience Volume (0.0 to 1.0) |
| `Sound_DialogVolume` | `1.0` | 5 |  |
| `Sound_DSPBufferSize` | `0` | 7 | sound buffer size, default 0 |
| `Sound_EnableAllSound` | `1` | 7 |  |
| `Sound_EnableAmbience` | `1` | 7 | Enable Ambience |
| `Sound_EnableArmorFoleySoundForOthers` | `1` | 7 |  |
| `Sound_EnableArmorFoleySoundForSelf` | `1` | 7 |  |
| `Sound_EnableDialog` | `1` | 7 | all dialog |
| `Sound_EnableDSPEffects` | `1` | 7 |  |
| `Sound_EnableEmoteSounds` | `1` | 7 |  |
| `Sound_EnableEncounterWarningsSounds` | `1` | 7 | Enable Encounter Warnings Sounds |
| `Sound_EnableErrorSpeech` | `1` | 5 |  |
| `Sound_EnableGameplaySFX` | `1` | 7 | enables gameplay-specific sfx |
| `Sound_EnableMixMode2` | `0` | 7 | test |
| `Sound_EnableMusic` | `1` | 5 |  |
| `Sound_EnablePetBattleMusic` | `1` | 7 | Enables music in pet battles |
| `Sound_EnablePetSounds` | `1` | 7 | Enables pet sounds |
| `Sound_EnablePingSounds` | `1` | 7 | Enable Ping Sounds |
| `Sound_EnablePositionalLowPassFilter` | `1` | 7 | Environmental effect to make sounds duller behind you or far away |
| `Sound_EnableReverb` | `1` | 7 |  |
| `Sound_EnableSFX` | `1` | 7 |  |
| `Sound_EnableSoundWhenGameIsInBG` | `0` | 5 |  |
| `Sound_EncounterWarningsVolume` | `1.000000` | 7 | Encounter Warnings Volume (0.0 to 1.0) |
| `Sound_EnemyPlayerHighpassDSPCutoff` |  | 7 | The cutoff value to use for the Highpass filter on the Enemy Player bus (default 80 Hz) |
| `Sound_GameplaySFX` | `1.000000` | 7 | sound volume (0.0 to 1.0) |
| `Sound_ListenerAtCharacter` | `1` | 7 | lock listener at character |
| `Sound_MasterVolume` | `1.0` | 5 |  |
| `Sound_MaxCacheableSizeInBytes` | `174762` | 7 | Max sound size that will be cached, larger files will be streamed instead |
| `Sound_MaxCacheSizeInBytes` | `134217728` | 7 | Max cache size in bytes |
| `Sound_MusicVolume` | `0.4` | 5 |  |
| `Sound_NPCHighpassDSPCutoff` |  | 7 | The cutoff value to use for the Highpass filter on the NPC bus (default 80 Hz) |
| `Sound_NumChannels` | `64` | 5 |  |
| `Sound_OutputDriverIndex` | `0` | 7 |  |
| `Sound_OutputDriverName` | `Primary Sound Driver` | 5 |  |
| `Sound_OutputSampleRate` | `44100` | 7 | output sample rate |
| `Sound_PingVolume` | `1.0` | 7 | Ping Volume (0.0 to 1.0) |
| `Sound_SFXVolume` | `1.0` | 5 |  |
| `Sound_VoiceChatInputDriverIndex` | `0` | 7 |  |
| `Sound_VoiceChatInputDriverName` | `Primary Sound Capture Driver` | 7 |  |
| `Sound_VoiceChatOutputDriverIndex` | `0` | 7 |  |
| `Sound_VoiceChatOutputDriverName` | `Primary Sound Driver` | 7 |  |
| `Sound_ZoneMusicNoDelay` | `0` | 7 |  |
| `SoundPerf_VariationCap` | `32` | 7 | Limit sound kit variations to cut down on memory usage and disk thrashing on 32-bit machines |
| `SpawnRegion` | `0` | 5 |  |
| `spectate` |  | 4 | Spectate <CharName-Realm> - Begin commentator view of specified player's instance party.  Exclude name to exit spectator mode |
| `specular` | `1` | 1 | Specular lighting multiplier (0-1) |
| `speechToText` | `0` | 4 | Allows enabling transcription on a voice channel in order to see written text based on the words spoken by other players |
| `spellActivationOverlayOpacity` | `0.650000` | 4 | The opacity of the Spell Activation Overlays (a.k.a. Spell Alerts) |
| `spellBookHideFlyouts` | `1` | 4 | If true, Flyout icons will be hidden and member spells will be shown loose in the spellbook. |
| `spellBookHidePassives` | `0` | 4 | Stores whether to hide Passive spells in the SpellBook pane |
| `spellBookMinimize` | `1` | 4 | Stores whether to always show the the SpellBook pane in half-screen minimized mode |
| `spellClutter` | `4` | 1 | Spell Density |
| `SpellCooldownDebugger` | `0` | 5 |  |
| `spellDiminishPVPEnemiesEnabled` | `1` | 4 | Determines if we should show crowd control diminishing returns on enemy unit frames in arenas |
| `spellDiminishPVPOnlyTriggerableByMe` | `0` | 4 | Determines if we should show crowd control diminishing returns for all categories or only the ones you could cause with your spells |
| `SpellEventLog` | `0` | 5 |  |
| `SpellOverrides` | `0` | 5 |  |
| `SpellQueueWindow` | `400` | 4 | Sets how early you can pre-activate/queue a spell/ability. (In Milliseconds) |
| `SpellScriptEventLog` | `0` | 5 |  |
| `SpellTargeting` | `0` | 5 |  |
| `spellVisualDensityFilterSetting` | `4` | 4 | SVK Density, set by the UI Spell Density setting. 0 - none (dev-only), 1 - minimum, 2 - reduced, 3 - performance, 4 - full |
| `SpellVisuals` | `0` | 5 |  |
| `SplineOpt` | `1` | 0 | toggles use of spline coll optimization |
| `SSAO` | `0` | 5 |  |
| `ssaoMagicNormals` | `1` | 1 | SSAO Use combined GBuffer and face normals; attempts to get the best compromise for architecture, foliage, and characters |
| `ssaoMagicThresholdHigh` | `50` | 1 | SSAO High threshold for transitioning from gbuffer to face normal (degrees) |
| `ssaoMagicThresholdLow` | `25` | 1 | SSAO Low threshold for transitioning from gbuffer to face normal (degrees) |
| `statusText` | `0` | 4 | Whether the status bars show numeric health/mana values |
| `statusTextDisplay` | `NONE` | 4 | Whether numeric health/mana values are shown as raw values or percentages, or both |
| `stopAutoAttackOnTargetChange` | `0` | 4 | Whether to stop attacking when changing targets |
| `streamingCameraLookAheadTime` | `2000` | 1 | Look ahead time for streaming. |
| `streamingCameraMaxRadius` | `250` | 1 | Max radius of the streaming camera. |
| `streamingCameraRadius` | `100` | 1 | Base radius of the streaming camera. |
| `streamStatusMessage` | `1` | 4 | Whether to display status messages while streaming content |
| `sunShafts` | `0` | 5 |  |
| `superTrackerDist` | `0.750000` | 4 |  |
| `SuppressCpuMicrocodeChecks` | `0` | 5 | Disables CPU Microcode checks |
| `synchronizeBindings` | `1` | 5 |  |
| `synchronizeChatFrames` | `1` | 5 |  |
| `synchronizeConfig` | `1` | 5 |  |
| `taintLog` | `0` | 0 | Controls debug logging of Lua taint and restricted action events to the 'taint.log' file:
0: Disable all logging
1: Log blocked action errors and taint events leading up to them
2: Log tainted reads and writes of global variables
3: Log tainted reads and writes of upvalues
4: Log tainted reads and writes of table fields |
| `taintLogObjectSecrets` | `0` | 0 | If enabled, include additional taint log entries when script objects gain secret aspects or values. |
| `TakeScreenshot` |  | 1 |  |
| `talentPointsSpent` | `0` | 4 | The player has spent a talent point |
| `TargetAutoEnemy` | `1` | 4 | Auto-Target from your single target helpful spells |
| `TargetAutoFriend` | `1` | 4 | Auto-Target from your single target helpful spells |
| `TargetAutoLock` | `1` | 4 | Lock targets auto-set by the game |
| `TargetEnemyAttacker` | `1` | 4 | Auto-Target Enemy when they attack you |
| `targetFPS` | `60` | 1 | Set target FPS. Dynamic actions will be taken if you fall below the FPS target |
| `targetHighlightAlwaysShown` | `1` | 4 | If enabled, targeted units have a highlight applied regardless of Outline Mode settings. |
| `TargetNearestUseNew` | `1` | 4 | Use new 7.2 'nearest target' functionality (Set to 0 for 6.x style tab targeting) |
| `TargetPriorityCombatLock` | `1` | 4 | 1=Lock to in-combat targets when starting from an in-combat target. 2=Further restrict to in-combat with player. |
| `TargetPriorityCombatLockContextualRelaxation` | `1` | 4 | 1=Enables relaxation of combat lock based on context (eg. no in-combat target infront) |
| `TargetPriorityCombatLockHighlight` | `0` | 4 | 1=Lock to in-combat targets when starting from an in-combat target. 2=Further restrict to in-combat with player. (while doing hold-to-target) |
| `TargetPriorityPvp` | `1` | 4 | When in pvp, give higher priority to players and important pvp targets (1 = players & npc bosses, 2 = all pvp targets, 3 = players only) |
| `telemetryWowlabsPackage` | `Blizzard.Telemetry.Wow_Camelot` | 5 | The secondary package we want to send telemetry to e.g. Wow_Wowlabs |
| `telemetryWowPackage` | `Blizzard.Telemetry.Wow_Camelot` | 5 | The primary package we want to send telemetry to e.g. Wow_Mainline or Wow_Classic |
| `teleportMaxNoLoadDist` | `200` | 1 | Max teleport distanace without preload |
| `terrainLodDist` | `400` | 5 |  |
| `TerrainLodDiv` | `768` | 1 | Terrain lod divisor |
| `terrainMipLevel` | `0` | 1 | Terrain blend map mip level |
| `test_cameraDynamicPitch` | `0.000000` | 4 | Adjust camera pitch according to zoom distance for a more cinematic view |
| `test_cameraDynamicPitchBaseFovPad` | `0.400000` | 4 | Fraction of screen height to keep feet below |
| `test_cameraDynamicPitchBaseFovPadDownScale` | `0.250000` | 4 | Strength of dynamic pitch when looking down |
| `test_cameraDynamicPitchBaseFovPadFlying` | `0.750000` | 4 | Fraction of screen height to keep character below when able to fly |
| `test_cameraDynamicPitchSmartPivotCutoffDist` | `10.000000` | 4 | Dynamic pitch disables Smart Pivot within this camera distance |
| `test_cameraHeadMovementDeadZone` | `0.015000` | 4 |  |
| `test_cameraHeadMovementFirstPersonDampRate` | `20.000000` | 4 |  |
| `test_cameraHeadMovementMovingDampRate` | `10.000000` | 4 |  |
| `test_cameraHeadMovementMovingStrength` | `0.500000` | 4 |  |
| `test_cameraHeadMovementRangeScale` | `5.000000` | 4 |  |
| `test_cameraHeadMovementStandingDampRate` | `10.000000` | 4 |  |
| `test_cameraHeadMovementStandingStrength` | `0.300000` | 4 |  |
| `test_cameraHeadMovementStrength` | `0.000000` | 4 |  |
| `test_cameraOverShoulder` | `0.000000` | 4 |  |
| `test_cameraTargetFocusEnemyEnable` | `0` | 4 |  |
| `test_cameraTargetFocusEnemyStrengthPitch` | `0.400000` | 4 |  |
| `test_cameraTargetFocusEnemyStrengthYaw` | `0.500000` | 4 |  |
| `test_cameraTargetFocusInteractEnable` | `0` | 4 |  |
| `test_cameraTargetFocusInteractStrengthPitch` | `0.750000` | 4 |  |
| `test_cameraTargetFocusInteractStrengthYaw` | `1.000000` | 4 |  |
| `testOutput` |  | 2 | Tests that all output paths work. |
| `textLocale` |  | 4 | Set the game locale for text |
| `textToSpeech` | `0` | 4 | Reads chat text out loud using the voice text to speech system based on the selected options |
| `textureErrorColors` | `1` | 1 | If enabled, replaceable textures that aren't specified will be purple |
| `textureFilteringMode` | `5` | 1 | Texture filtering mode |
| `ThreadPoolLimitHP` | `6` | 10 | Limit num threads for High prio jobs |
| `ThreadPoolLimitLP` | `6` | 10 | Limit num threads for Low prio jobs |
| `ThreadPoolLimitMP` | `6` | 10 | Limit num threads for Mid prio jobs |
| `ThreadPoolPerThreadAllocator` | `1` | 10 | 0=Disabled, 1=Allow, 2=Force (around 12% faster but uses ~300MB more memory) |
| `threatPlaySounds` | `1` | 4 | Whether or not to sounds when certain threat transitions occur |
| `threatShowNumeric` | `0` | 4 | Whether or not to show numeric threat on the target and focus frames |
| `threatWarning` | `3` | 4 | Whether or not to show threat warning UI (0 = off, 1 = in dungeons, 2 = in party/raid, 3 = always) |
| `threatWorldText` | `1` | 4 | Whether or not to show threat floaters in combat |
| `timeMgrAlarmEnabled` | `0` | 4 | Toggles whether or not the time manager's alarm will go off |
| `timeMgrAlarmMessage` |  | 4 | The time manager's alarm message |
| `timeMgrAlarmTime` | `0` | 4 | The time manager's alarm time in minutes |
| `timeMgrUseLocalTime` | `0` | 4 | Toggles the use of either the realm time or your system time |
| `timeMgrUseMilitaryTime` | `0` | 4 | Toggles the display of either 12 or 24 hour time |
| `titleBarShortName` | `0` | 5 |  |
| `titleBarShowAccountName` | `0` | 5 |  |
| `titleBarShowBuildInfo` | `0` | 5 |  |
| `titleBarShowCharacterName` | `0` | 5 |  |
| `titleBarShowConfigName` | `0` | 5 |  |
| `titleBarShowGxInfo` | `0` | 5 |  |
| `titleBarShowPID` | `0` | 5 |  |
| `titleBarShowRealmName` | `0` | 5 |  |
| `toastDuration` | `4` | 4 | How long to display Battle.net toast windows, in seconds |
| `ToggleWindowMode` |  | 1 |  |
| `tooltipPointsShowMinAndMax` | `1` | 4 | True shows tooltip token $s as '[min] to [max]', False shows as '[avg]' |
| `tooltipShowAuraCasterNames` | `0` | 4 | Show caster unit names in tooltips for unit auras. |
| `tooltipShowAuraSpellIDs` | `0` | 4 | Show spell IDs in tooltips for unit auras. |
| `toyBoxCollectedFilters` | `0` | 4 | Bitfield for which collected filters are applied in the toybox |
| `toyBoxExpansionFilters` | `0` | 4 | Bitfield for which expansion filters are applied in the toybox |
| `toyBoxSourceFilters` | `0` | 4 | Bitfield for which source filters are applied in the toybox |
| `trackedAchievements` |  | 4 | Internal cvar for saving tracked achievements in order |
| `trackedInitiativeTasks` |  | 4 | Internal cvar for saving tracked initiative tasks in order |
| `trackedPerksActivities` |  | 5 |  |
| `trackedProfessionRecipes` |  | 4 | Internal cvar for saving tracked recipes in order |
| `trackedProfessionRecraftRecipes` |  | 4 | Internal cvar for saving tracked recraft recipes in order |
| `trackedQuests` |  | 4 | Internal cvar for saving automatically tracked quests in order |
| `trackedWorldQuests` |  | 4 | Internal cvar for saving automatically tracked world quests |
| `transmogCurrentSpecOnly` | `0` | 4 | Stores whether transmogs apply to current spec instead of all specs |
| `transmogDebug` | `0` | 4 | Enables Transmog Debug Logging |
| `transmogHideIgnoredSlots` | `0` | 4 | Whether ignored slots display as hidden or unassigned in the transmog frame |
| `transmogPreviewedWeaponToggle` | `0` | 4 | Whether the transmog ModelScene should show the MH/OH combo or the RangedWeapon |
| `transmogrifySetsFilters` | `0` | 4 | Bitfield for which transmog sets filters are applied in the transmog sets tab |
| `transmogrifyShowCollected` | `1` | 4 | Whether to show collected transmogs in the at the transmogrifier |
| `transmogrifyShowUncollected` | `0` | 4 | Whether to show uncollected transmogs in the at the transmogrifier |
| `transmogrifySourceFilters` | `0` | 4 | Bitfield for which source filters are applied in the  wardrobe at the transmogrifier |
| `transmogShowID` | `0` | 4 | Shows the itemModifiedAppearanceID or setID in transmog tooltips |
| `TTSUseCharacterSettings` | `1` | 5 | If character-specific TTS settings are being used. |
| `TurnSpeed` | `180.000000` | 5 | Set the keyboard turn rate in degrees per second; capped by the server |
| `UberTooltips` | `1` | 4 | Show verbose tooltips |
| `uiScale` | `1.000000` | 4 | The current UI scale |
| `uiScaleMultiplier` | `-1.000000` | 4 | A multiplier for the default UI scale. -1=determine based on system/monitor DPI, 0.5-2.0=multiplier to use when calculating UI scale. Only applied when useUIScale is 0. |
| `unitClutter` | `1` | 4 | Enables/Disables unit clutter |
| `unitClutterInstancesOnly` | `1` | 4 | Whether or not to use unit clutter in instances only (0 or 1) |
| `unitClutterPlayerThreshold` | `9` | 4 | The number of players that have to be nearby to trigger unit clutter |
| `UnitEnterCombatLog` | `0` | 5 |  |
| `unitFacingPlayerDeadZoneDeg` | `60` | 4 | Degrees outside a unit's default facing a player has to be for the unit to face them on interact |
| `UnitNameEnemyGuardianName` | `1` | 4 |  |
| `UnitNameEnemyMinionName` | `1` | 4 |  |
| `UnitNameEnemyPetName` | `1` | 4 |  |
| `UnitNameEnemyPlayerName` | `1` | 4 |  |
| `UnitNameEnemyTotemName` | `1` | 4 |  |
| `UnitNameFocused` | `1` | 4 |  |
| `UnitNameForceHideMinus` | `0` | 4 |  |
| `UnitNameFriendlyGuardianName` | `1` | 4 |  |
| `UnitNameFriendlyMinionName` | `1` | 4 |  |
| `UnitNameFriendlyPetName` | `1` | 4 |  |
| `UnitNameFriendlyPlayerName` | `1` | 4 |  |
| `UnitNameFriendlySpecialNPCName` | `1` | 4 |  |
| `UnitNameFriendlyTotemName` | `1` | 4 |  |
| `UnitNameGuildTitle` | `1` | 4 |  |
| `UnitNameHostleNPC` | `1` | 4 |  |
| `UnitNameInteractiveNPC` | `1` | 4 |  |
| `UnitNameNonCombatCreatureName` | `0` | 4 |  |
| `UnitNameNPC` | `0` | 4 |  |
| `UnitNameOwn` | `0` | 4 |  |
| `UnitNamePlayerGuild` | `1` | 4 |  |
| `UnitNamePlayerPVPTitle` | `1` | 4 |  |
| `unitsLookAtPlayers` | `1` | 4 | Enables units turning their head to look at players |
| `UnitSurnameOwn` | `1` | 4 | show player surname over head |
| `UnitVisibility` | `0` | 5 |  |
| `unlockedMajorFactions` |  | 4 | Internal cvar for tracking unlocked Major Factions. Used to play a toast when a new faction has been unlocked. |
| `UpdatePOI` |  | 4 | Updates Quest POI from User Server |
| `UpdateWindow` |  | 1 |  |
| `useBLEEP` | `0` | 6 | Client override to always prefer BLEEP, when available |
| `useCommentatorSelectionCircles` | `1` | 4 | Determines whether to use the commentator selection circles or the default selection circles while spectating or commentating a wargame |
| `useHDRBrightness` | `0` | 1 | Whether HDRBrightness should be used to override the monitor's detected brightness level. |
| `useHDRPeakBrightness` | `0` | 1 | Whether HDRPeakBrightness should be used to override the monitor's detected peak brightness level. |
| `useHighResTextures` | `1` | 4 | Prefer upscaled versions of texture assets when available |
| `useIPv6` | `0` | 6 | Enable the usage of IPv6 sockets |
| `UseKeyHeldSpellErrorPollTime` | `500` | 4 | (Internal only) Time between a failed cast and when it should attempt to cast again in ms. (Clamped to 100 and 10000) |
| `useMaxFPS` | `0` | 1 | Enables or disables FPS limit |
| `useMaxFPSBk` | `1` | 1 | Enables or disables background FPS limit |
| `userFontScale` | `1.000000` | 4 | in-game: Defines the scale of the font used in places around the UI where readability requires larger defaults which are still customizable by the user. |
| `userFontScaleGlue` | `1.390000` | 4 | glues: Defines the scale of the font used in places around the UI where readability requires larger defaults which are still customizable by the user. |
| `UseSlug` | `1` | 0 | Render with slug text |
| `useTargetFPS` | `1` | 5 |  |
| `useUiScale` | `0` | 4 | Whether or not the UI scale should be used |
| `validateFrameXML` | `1` | 4 | Display warning when FrameXML detects unparsed elements |
| `ver` |  | 5 |  |
| `VerboseSpellScriptEventLog` | `0` | 5 |  |
| `videoOptionsVersion` | `0` | 5 |  |
| `videoOptionsVersionDefault` | `0` | 1 |  |
| `violenceLevel` | `2` | 4 | Sets the violence level of the game |
| `VoiceChatMasterVolumeScale` | `1` | 7 | Voice Chat audio ducking, applied as a scale to the game's master volume when somebody is speaking in voice chat |
| `VoiceCommunicationMode` | `0` | 7 | Which communication mode to use for voice chat: push-to-talk, open mic, etc... |
| `VoiceEnableWhenGameIsInBG` | `1` | 7 | Enable Voice Chat when game is in background |
| `VoiceInputDevice` |  | 5 |  |
| `VoiceInputVolume` | `50` | 7 | The gain applied to your microphone, helps change your speaking volume from other users' perspectives, larger values are louder. |
| `VoiceOutputDevice` |  | 5 |  |
| `VoiceOutputVolume` | `50` | 7 | The volume of incoming voice chat, how loud other users' voices sound |
| `voiceProvider` | `0` | 4 | The preferred voice provider (0 = Legacy, 1 = Discord). |
| `VoiceProxyEventLog` | `0` | 5 |  |
| `VoicePushToTalkKeybind` | ``` | 5 |  |
| `VoiceSelfDeafened` | `0` | 7 | Voice Chat Self Deafened |
| `VoiceSelfMuted` | `0` | 7 | Voice Chat Self Muted |
| `voiceUseDiscordSettings` | `0` | 7 | Import voice volumes, voice mode and push-to-talk key from the Discord client when Discord is the preferred voice provider. |
| `VoiceVADSensitivity` | `43` | 7 | How sensitive voice activity detection is.  Value ranges from 0 to 100, smaller values will transmit at a lower noise threshold. |
| `volumeFog` | `1` | 1 | Volume Fog |
| `volumeFogInterior` | `1` | 1 | Volume Fog Interiors |
| `volumeFogLevel` | `3` | 5 |  |
| `vrsParticles` | `1x1` | 1 | Render scale like effect for particles. Only used if lots of particles are on screen |
| `vrsValar` | `0` | 1 | Generate a shading rate mask based on velocity and luminance. Requires VRS Tier 2. |
| `vrsValarAlwaysOn` | `0` | 1 | Use VRS even when not GPU bound |
| `vrsValarEnvLuma` | `0.050000` | 1 | Env. Luma for VALAR |
| `vrsValarGPUMode` | `0` | 1 | 0 - Auto-detect, 1 - Standard (discrete GPU default), 2 - Low Power (integrated GPU default) modes for VALAR |
| `vrsValarK` |  | 1 |  |
| `vrsValarLPUseCornerSampling` | `0` | 1 | Use corner sampling for VALAR Low Power |
| `vrsValarSensitivityThreshold` |  | 1 |  |
| `vrsValarUseAsyncCompute` | `0` | 1 | Use async compute for VALAR |
| `vrsValarUseMotionVectors` | `0` | 1 | Use motion vectors for VALAR |
| `vrsValarUseWeberFechner` | `0` | 1 | Use Weber-Fechner Algo for VALAR |
| `vrsValarWeberFechnerConstant` | `1.000000` | 1 | Weber-Fechner Constant for VALAR |
| `vrsWorldGeo` | `1x1` | 1 | Render scale like effect for terrain, buildings and liquids |
| `vsync` | `1` | 5 |  |
| `WalkableSurfacesValidationLog` | `0` | 5 |  |
| `wardrobeSetsFilters` | `0` | 4 | Bitfield for which transmog sets filters are applied in the wardrobe in the collection journal |
| `wardrobeShowAllFactions` | `0` | 4 | Stores whether to show both Alliance and Horde transmogs in the Wardrobe |
| `wardrobeShowAllRaces` | `0` | 4 | Stores whether to show race restricted transmogs in the Wardrobe |
| `wardrobeShowCollected` | `1` | 4 | Whether to show collected transmogs in the wardrobe |
| `wardrobeShowUncollected` | `0` | 4 | Whether to show uncollected transmogs in the wardrobe |
| `wardrobeSourceFilters` | `0` | 4 | Bitfield for which source filters are applied in the wardrobe in the collection journal |
| `waterDetail` | `0` | 5 |  |
| `weatherDensity` | `2` | 5 |  |
| `webChallengeURLTimeout` | `60` | 5 | How long to wait for the web challenge URL (in seconds). 0 means wait forever. |
| `whisperMode` | `inline` | 4 | The action new whispers take by default: "popout", "inline", "popout_and_inline" |
| `whois` |  | 0 | Ask the server to do an account/real name lookup on a character name |
| `wholeChatWindowClickable` | `1` | 4 | Whether the user may click anywhere on a chat window to change EditBox focus (only works in IM style) |
| `winePlatformTTS` | `0` | 4 | Use Windows TTS on Wine. Disabled by default as it can cause crashes. |
| `wmoDoodadDist` | `2000` | 1 | Wmo doodad load distance |
| `wmoLodDist` | `300` | 5 |  |
| `wmoLodDistScale` | `1.0` | 1 | Wmo level of detail distance scale |
| `wmoPortalFadeScale` | `1000` | 1 | Wmo portal fade scale |
| `wmoPortalInteriorFade` | `1` | 1 | Wmo portal interior fade |
| `WorldActionsLog` | `0` | 5 |  |
| `worldBaseMip` | `0` | 1 | World texture base mip |
| `worldIntersectMaxJobs` | `32` | 1 | Maximum job threads for culling |
| `worldLoadSort` | `1` | 1 | Sort objects by distance when loading |
| `worldMapShowCursorCoords` | `1` | 4 | Show cursor coordinates on the world map |
| `worldMapShowPlayerCoords` | `1` | 4 | Show player coordinates on the world map |
| `worldPreloadHighResTextures` | `1` | 1 | Require high res textures to be loaded in streaming non critical radius when preloading |
| `worldPreloadNonCritical` | `2` | 1 | Require objects to be loaded in streaming non critical radius when preloading |
| `worldPreloadNonCriticalTimeout` | `45` | 1 | World preload time (in seconds) when non-critical items are automatically ignored |
| `worldPreloadSort` | `1` | 1 | Sort objects by distance when preloading |
| `worldQuestFilterAnima` | `1` | 4 | If enabled, world quests with anima rewards will be shown on the map |
| `worldQuestFilterArtifactPower` | `1` | 4 | If enabled, world quests with artifact power rewards will be shown on the map |
| `worldQuestFilterEquipment` | `1` | 4 | If enabled, world quests with equipment rewards will be shown on the map |
| `worldQuestFilterGold` | `1` | 4 | If enabled, world quests with gold rewards will be shown on the map |
| `worldQuestFilterProfessionMaterials` | `1` | 4 | If enabled, world quests with profession material rewards will be shown on the map |
| `worldQuestFilterReputation` | `1` | 4 | If enabled, world quests with reputation rewards will be shown on the map |
| `worldQuestFilterResources` | `1` | 4 | If enabled, world quests with order resource rewards or war resource rewards will be shown on the map |
| `WorldTextCritScreenY_v2` | `0.0` | 4 |  |
| `WorldTextGravity_v2` | `0.500000` | 4 |  |
| `WorldTextMinAlpha_v2` | `0.500000` | 4 |  |
| `WorldTextMinSize` | `0.000000` | 4 | Smallest size used for world text like player names |
| `WorldTextNonRandomZ_v2` | `2.0` | 4 |  |
| `WorldTextRampDuration_v2` | `1.000000` | 4 |  |
| `WorldTextRampPow_v2` | `1.900000` | 4 |  |
| `WorldTextRampPowCrit_v2` | `8.000000` | 4 |  |
| `WorldTextRandomXY_v2` | `0.0` | 4 |  |
| `WorldTextRandomZMax_v2` | `1.5` | 4 |  |
| `WorldTextRandomZMin_v2` | `0.8` | 4 |  |
| `WorldTextScale_v2` | `1.000000` | 4 |  |
| `WorldTextScreenY_v2` | `0.0` | 4 |  |
| `WorldTextStartPosRandomness_v2` | `1.0` | 4 |  |
| `worldViewCullMaxJobs` | `32` | 1 | Maximum job threads for culling |
| `WriteCustomizationOptions` |  | 4 |  |
| `xpBarText` | `0` | 4 | Whether the XP bar shows the numeric experience value |
