# Tutorial

Namespace: `C_Tutorial`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Tutorial.AbandonTutorialArea](#c_tutorialabandontutorialarea) |  |  |
| ✅ | [C_Tutorial.GetCombatEventInfo](#c_tutorialgetcombateventinfo) |  |  |
| ✅ | [C_Tutorial.ReturnToTutorialArea](#c_tutorialreturntotutorialarea) |  |  |
| ✅ | [C_Tutorial.SendTutorialStartButtonTelem](#c_tutorialsendtutorialstartbuttontelem) |  |  |

### C_Tutorial.AbandonTutorialArea

`C_Tutorial.AbandonTutorialArea()`

- Status: ✅ verified (function)
- Source: client docs `TutorialDocumentation.lua`

### C_Tutorial.GetCombatEventInfo

`C_Tutorial.GetCombatEventInfo()`

- Status: ✅ verified (function)
- RequireNPERestricted (Blizzard's docs; not checked in game)
- Source: client docs `TutorialDocumentation.lua`

### C_Tutorial.ReturnToTutorialArea

`C_Tutorial.ReturnToTutorialArea()`

- Status: ✅ verified (function)
- Source: client docs `TutorialDocumentation.lua`

### C_Tutorial.SendTutorialStartButtonTelem

`C_Tutorial.SendTutorialStartButtonTelem(skipTutorial: bool)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TutorialDocumentation.lua`

## Events

### LEAVING_TUTORIAL_AREA

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### NPE_TUTORIAL_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TUTORIAL_COMBAT_EVENT

- Status: ✅ verified
- Payload: none
- RequireNPERestricted (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### TUTORIAL_HIGHLIGHT_SPELL

- Status: ✅ verified
- Payload: `spellID: number`, `tutorialGlobalStringTag: cstring`
- fires synchronously (Blizzard's docs)

### TUTORIAL_TRIGGER

- Status: ✅ verified
- Payload: `tutorialIndex: number`, `forceShow: bool`
- fires synchronously (Blizzard's docs)

### TUTORIAL_UNHIGHLIGHT_SPELL

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### FrameTutorialAccount

- Enumeration — ✅ verified
  - `HudRevampBagChanges` = 1
  - `PerksProgramActivitiesIntro` = 2
  - `EditModeManager` = 3
  - `TransmogSetsTab` = 4
  - `MountCollectionDragonriding` = 5
  - `LFGList` = 6
  - `HeirloomJournalLevel` = 7
  - `TimerunnersAdvantage` = 8
  - `AccountWideReputation` = 9
  - `TransferableCurrencies` = 10
  - `BindToAccountUntilEquip` = 11
  - `CompletedQuestsFilter` = 12
  - `CompletedQuestsFilterSeen` = 13
  - `ConcentrationCurrency` = 14
  - `MapLegendOpened` = 15
  - `NpcCraftingOrders` = 16
  - `NpcCraftingOrderCreateButton` = 17
  - `NpcCraftingOrderTabNew` = 18
  - `LocalStoriesFilterSeen` = 19
  - `EventSchedulerTabSeen` = 20
  - `AssistedCombatRotationDragSpell` = 21
  - `AssistedCombatRotationActionButton` = 22
  - `HousingDecorCleanup` = 23
  - `HousingDecorPlace` = 24
  - `HousingDecorClippingGrid` = 25
  - `HousingDecorCustomization` = 26
  - `HousingDecorLayout` = 27
  - `HousingHouseFinderMap` = 28
  - `HousingHouseFinderVisitHouse` = 29
  - `HousingItemAcquisition` = 30
  - `HousingNewPip` = 31
  - `PerksProgramActivitiesOpen` = 32
  - `EnconterJournalTutorialsTabSeen` = 33
  - `HousingMarketTab` = 34
  - `HousingTeleportButton` = 35
  - `RPETalentStarterBuild` = 36
  - `HousingInvalidCollision` = 37
  - `HousingModesUnlocked` = 38
  - `HousingExpertMode` = 39
  - `HousingCleanupMode` = 40
  - `TransmogOutfits` = 41
  - `TransmogSets` = 42
  - `TransmogCustomSets` = 43
  - `TransmogSituations` = 44
  - `TransmogWeaponOptions` = 45
  - `TransmogTrialOfStyle` = 46
  - `TransmogCustomSetsMigration` = 47
  - `HousingEndeavorsTabSeen` = 48
  - `RunesOfPower` = 49
  - `HousingPetBeds` = 50
  - `Reserved1` = 51
