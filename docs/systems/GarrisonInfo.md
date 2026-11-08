# GarrisonInfo

Namespace: `C_Garrison`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Garrison.AddFollowerToMission](#c_garrisonaddfollowertomission) |  |  |
| ❔ | [C_Garrison.GetAutoCombatDamageClassValues](#c_garrisongetautocombatdamageclassvalues) |  |  |
| ❔ | [C_Garrison.GetAutoMissionBoardState](#c_garrisongetautomissionboardstate) |  |  |
| ❔ | [C_Garrison.GetAutoMissionEnvironmentEffect](#c_garrisongetautomissionenvironmenteffect) |  |  |
| ❔ | [C_Garrison.GetAutoMissionTargetingInfo](#c_garrisongetautomissiontargetinginfo) |  |  |
| ❔ | [C_Garrison.GetAutoMissionTargetingInfoForSpell](#c_garrisongetautomissiontargetinginfoforspell) |  |  |
| ❔ | [C_Garrison.GetAutoTroops](#c_garrisongetautotroops) |  |  |
| ❔ | [C_Garrison.GetCombatLogSpellInfo](#c_garrisongetcombatlogspellinfo) |  |  |
| ❔ | [C_Garrison.GetCurrentCypherEquipmentLevel](#c_garrisongetcurrentcypherequipmentlevel) |  |  |
| ❔ | [C_Garrison.GetCurrentGarrTalentTreeFriendshipFactionID](#c_garrisongetcurrentgarrtalenttreefriendshipfactionid) |  |  |
| ❔ | [C_Garrison.GetCurrentGarrTalentTreeID](#c_garrisongetcurrentgarrtalenttreeid) |  |  |
| ❔ | [C_Garrison.GetCyphersToNextEquipmentLevel](#c_garrisongetcypherstonextequipmentlevel) |  |  |
| ❔ | [C_Garrison.GetFollowerAutoCombatSpells](#c_garrisongetfollowerautocombatspells) |  |  |
| ❔ | [C_Garrison.GetFollowerAutoCombatStats](#c_garrisongetfollowerautocombatstats) |  |  |
| ❔ | [C_Garrison.GetFollowerMissionCompleteInfo](#c_garrisongetfollowermissioncompleteinfo) |  |  |
| ❔ | [C_Garrison.GetGarrisonPlotsInstancesForMap](#c_garrisongetgarrisonplotsinstancesformap) |  |  |
| ❔ | [C_Garrison.GetGarrisonTalentTreeCurrencyTypes](#c_garrisongetgarrisontalenttreecurrencytypes) |  |  |
| ❔ | [C_Garrison.GetGarrisonTalentTreeType](#c_garrisongetgarrisontalenttreetype) |  |  |
| ❔ | [C_Garrison.GetMaxCypherEquipmentLevel](#c_garrisongetmaxcypherequipmentlevel) |  |  |
| ❔ | [C_Garrison.GetMissionCompleteEncounters](#c_garrisongetmissioncompleteencounters) |  |  |
| ❔ | [C_Garrison.GetMissionDeploymentInfo](#c_garrisongetmissiondeploymentinfo) |  |  |
| ❔ | [C_Garrison.GetMissionEncounterIconInfo](#c_garrisongetmissionencountericoninfo) |  |  |
| ❔ | [C_Garrison.GetTalentInfo](#c_garrisongettalentinfo) |  |  |
| ❔ | [C_Garrison.GetTalentPointsSpentInTalentTree](#c_garrisongettalentpointsspentintalenttree) |  |  |
| ❔ | [C_Garrison.GetTalentTreeIDsByClassID](#c_garrisongettalenttreeidsbyclassid) |  |  |
| ❔ | [C_Garrison.GetTalentTreeInfo](#c_garrisongettalenttreeinfo) |  |  |
| ❔ | [C_Garrison.GetTalentTreeResetInfo](#c_garrisongettalenttreeresetinfo) |  |  |
| ❔ | [C_Garrison.GetTalentTreeTalentPointResearchInfo](#c_garrisongettalenttreetalentpointresearchinfo) |  |  |
| ❔ | [C_Garrison.GetTalentUnlockWorldQuest](#c_garrisongettalentunlockworldquest) |  |  |
| ❔ | [C_Garrison.HasAdventures](#c_garrisonhasadventures) |  |  |
| ❔ | [C_Garrison.IsAtGarrisonMissionNPC](#c_garrisonisatgarrisonmissionnpc) |  |  |
| ❔ | [C_Garrison.IsEnvironmentCountered](#c_garrisonisenvironmentcountered) |  |  |
| ❔ | [C_Garrison.IsFollowerOnCompletedMission](#c_garrisonisfolloweroncompletedmission) |  |  |
| ❔ | [C_Garrison.IsLandingPageMinimapButtonVisible](#c_garrisonislandingpageminimapbuttonvisible) |  |  |
| ❔ | [C_Garrison.IsTalentConditionMet](#c_garrisonistalentconditionmet) |  |  |
| ❔ | [C_Garrison.RegenerateCombatLog](#c_garrisonregeneratecombatlog) |  |  |
| ❔ | [C_Garrison.RemoveFollowerFromMission](#c_garrisonremovefollowerfrommission) |  |  |
| ❔ | [C_Garrison.RushHealAllFollowers](#c_garrisonrushhealallfollowers) |  |  |
| ❔ | [C_Garrison.RushHealFollower](#c_garrisonrushhealfollower) |  |  |
| ❔ | [C_Garrison.SetAutoCombatSpellFastForward](#c_garrisonsetautocombatspellfastforward) |  |  |

### C_Garrison.AddFollowerToMission

`C_Garrison.AddFollowerToMission(missionID: number, followerID: GarrisonFollower, boardIndex: number?) → followerAdded: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetAutoCombatDamageClassValues

`C_Garrison.GetAutoCombatDamageClassValues() → damageClassStrings: AutoCombatDamageClassString[]`

- Status: ❔ unverified
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetAutoMissionBoardState

`C_Garrison.GetAutoMissionBoardState(missionID: number) → targetInfo: AutoMissionTargetingInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetAutoMissionEnvironmentEffect

`C_Garrison.GetAutoMissionEnvironmentEffect(missionID: number) → autoMissionEnvEffect: AutoMissionEnvironmentEffect?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetAutoMissionTargetingInfo

`C_Garrison.GetAutoMissionTargetingInfo(missionID: number, followerID: GarrisonFollower, casterBoardIndex: number) → targetInfo: AutoMissionTargetingInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetAutoMissionTargetingInfoForSpell

`C_Garrison.GetAutoMissionTargetingInfoForSpell(missionID: number, autoCombatSpellID: number, casterBoardIndex: number) → targetInfo: AutoMissionTargetingInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetAutoTroops

`C_Garrison.GetAutoTroops(followerType: number) → autoTroopInfo: AutoCombatTroopInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetCombatLogSpellInfo

`C_Garrison.GetCombatLogSpellInfo(autoCombatSpellID: number) → spellInfo: AutoCombatSpellInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetCurrentCypherEquipmentLevel

`C_Garrison.GetCurrentCypherEquipmentLevel() → equipmentLevel: number`

- Status: ❔ unverified
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetCurrentGarrTalentTreeFriendshipFactionID

`C_Garrison.GetCurrentGarrTalentTreeFriendshipFactionID() → currentGarrTalentTreeFriendshipFactionID: number?`

- Status: ❔ unverified
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetCurrentGarrTalentTreeID

`C_Garrison.GetCurrentGarrTalentTreeID() → currentGarrTalentTreeID: number?`

- Status: ❔ unverified
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetCyphersToNextEquipmentLevel

`C_Garrison.GetCyphersToNextEquipmentLevel() → cyphersToNext: number?`

- Status: ❔ unverified
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetFollowerAutoCombatSpells

`C_Garrison.GetFollowerAutoCombatSpells(garrFollowerID: GarrisonFollower, followerLevel: number) → autoCombatSpells: AutoCombatSpellInfo[], autoCombatAutoAttack: AutoCombatSpellInfo?`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetFollowerAutoCombatStats

`C_Garrison.GetFollowerAutoCombatStats(garrFollowerID: GarrisonFollower) → autoCombatInfo: FollowerAutoCombatStatsInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetFollowerMissionCompleteInfo

`C_Garrison.GetFollowerMissionCompleteInfo(followerID: GarrisonFollower) → followerMissionCompleteInfo: FollowerMissionCompleteInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetGarrisonPlotsInstancesForMap

`C_Garrison.GetGarrisonPlotsInstancesForMap(uiMapID: number) → garrisonPlotInstances: GarrisonPlotInstanceMapInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetGarrisonTalentTreeCurrencyTypes

`C_Garrison.GetGarrisonTalentTreeCurrencyTypes(garrTalentTreeID: number) → garrTalentTreeCurrencyType: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetGarrisonTalentTreeType

`C_Garrison.GetGarrisonTalentTreeType(garrTalentTreeID: number) → garrTalentTreeType: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetMaxCypherEquipmentLevel

`C_Garrison.GetMaxCypherEquipmentLevel() → maxEquipmentLevel: number`

- Status: ❔ unverified
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetMissionCompleteEncounters

`C_Garrison.GetMissionCompleteEncounters(missionID: number) → encounters: GarrisonEnemyEncounterInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetMissionDeploymentInfo

`C_Garrison.GetMissionDeploymentInfo(missionID: number) → missionDeploymentInfo: MissionDeploymentInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetMissionEncounterIconInfo

`C_Garrison.GetMissionEncounterIconInfo(missionID: number) → missionEncounterIconInfo: MissionEncounterIconInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetTalentInfo

`C_Garrison.GetTalentInfo(talentID: number) → info: GarrisonTalentInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetTalentPointsSpentInTalentTree

`C_Garrison.GetTalentPointsSpentInTalentTree(garrTalentTreeID: number) → talentPoints: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetTalentTreeIDsByClassID

`C_Garrison.GetTalentTreeIDsByClassID(garrType: number, classID: number) → treeIDs: number[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetTalentTreeInfo

`C_Garrison.GetTalentTreeInfo(treeID: number) → info: GarrisonTalentTreeInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetTalentTreeResetInfo

`C_Garrison.GetTalentTreeResetInfo(garrTalentTreeID: number) → goldCost: number, currencyCosts: GarrisonTalentCurrencyCostInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetTalentTreeTalentPointResearchInfo

`C_Garrison.GetTalentTreeTalentPointResearchInfo(garrTalentID: number, researchRank: number, garrTalentTreeID: number, talentPointIndex: number, isRespec: bool) → goldCost: number, currencyCosts: GarrisonTalentCurrencyCostInfo[], durationSecs: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.GetTalentUnlockWorldQuest

`C_Garrison.GetTalentUnlockWorldQuest(talentID: number) → worldQuestID: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.HasAdventures

`C_Garrison.HasAdventures() → hasAdventures: bool`

- Status: ❔ unverified
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.IsAtGarrisonMissionNPC

`C_Garrison.IsAtGarrisonMissionNPC() → atGarrisonMissionNPC: bool`

- Status: ❔ unverified
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.IsEnvironmentCountered

`C_Garrison.IsEnvironmentCountered(missionID: number) → environmentCountered: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.IsFollowerOnCompletedMission

`C_Garrison.IsFollowerOnCompletedMission(followerID: GarrisonFollower) → followerOnCompletedMission: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.IsLandingPageMinimapButtonVisible

`C_Garrison.IsLandingPageMinimapButtonVisible(garrType: number) → isLandingPageMinimapButtonVisible: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.IsTalentConditionMet

`C_Garrison.IsTalentConditionMet(talentID: number) → isMet: bool, failureString: cstring?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.RegenerateCombatLog

`C_Garrison.RegenerateCombatLog(missionID: number) → success: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.RemoveFollowerFromMission

`C_Garrison.RemoveFollowerFromMission(missionID: number, followerID: GarrisonFollower, boardIndex: number?)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.RushHealAllFollowers

`C_Garrison.RushHealAllFollowers(followerType: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.RushHealFollower

`C_Garrison.RushHealFollower(garrFollowerID: GarrisonFollower)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

### C_Garrison.SetAutoCombatSpellFastForward

`C_Garrison.SetAutoCombatSpellFastForward(state: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GarrisonInfoDocumentation.lua`

## Events

### GARRISON_ARCHITECT_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_ARCHITECT_OPENED

- Status: ❔ unverified
- Payload: `followerTypeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_BUILDING_ACTIVATABLE

- Status: ❔ unverified
- Payload: `buildingName: cstring`, `garrisonType: number`
- fires synchronously (Blizzard's docs)

### GARRISON_BUILDING_ACTIVATED

- Status: ❔ unverified
- Payload: `garrisonPlotInstanceID: number`, `garrisonBuildingID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_BUILDING_ERROR

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_BUILDING_LIST_UPDATE

- Status: ❔ unverified
- Payload: `categoryID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_BUILDING_PLACED

- Status: ❔ unverified
- Payload: `garrisonPlotInstanceID: number`, `newPlacement: bool`
- fires synchronously (Blizzard's docs)

### GARRISON_BUILDING_REMOVED

- Status: ❔ unverified
- Payload: `garrPlotInstanceID: number`, `garrBuildingID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_BUILDING_UPDATE

- Status: ❔ unverified
- Payload: `garrisonBuildingID: number`, `garrPlotInstanceID: number?`
- fires synchronously (Blizzard's docs)

### GARRISON_FOLLOWER_ADDED

- Status: ❔ unverified
- Payload: `followerDbID: GarrisonFollower`, `followerName: cstring`, `followerClassName: cstring`, `followerLevel: number`, `followerQuality: number`, `isUpgraded: bool`, `textureKit: textureKit`, `followerTypeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_FOLLOWER_CATEGORIES_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_FOLLOWER_DURABILITY_CHANGED

- Status: ❔ unverified
- Payload: `garrFollowerTypeID: number`, `followerDbID: GarrisonFollower`, `followerDurability: number`
- fires synchronously (Blizzard's docs)

### GARRISON_FOLLOWER_HEALED

- Status: ❔ unverified
- Payload: `followerID: GarrisonFollower`
- fires synchronously (Blizzard's docs)

### GARRISON_FOLLOWER_LIST_UPDATE

- Status: ❔ unverified
- Payload: `followerTypeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_FOLLOWER_REMOVED

- Status: ❔ unverified
- Payload: `followerTypeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_FOLLOWER_UPGRADED

- Status: ❔ unverified
- Payload: `followerDbID: GarrisonFollower`
- fires synchronously (Blizzard's docs)

### GARRISON_FOLLOWER_XP_CHANGED

- Status: ❔ unverified
- Payload: `garrFollowerTypeID: number`, `followerDbID: GarrisonFollower`, `xpChange: number`, `oldFollowerXp: number`, `oldFollowerLevel: number`, `oldFollowerQuality: number`
- fires synchronously (Blizzard's docs)

### GARRISON_HIDE_LANDING_PAGE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_INVASION_AVAILABLE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_INVASION_UNAVAILABLE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_LANDINGPAGE_SHIPMENTS

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### GARRISON_MISSION_AREA_BONUS_ADDED

- Status: ❔ unverified
- Payload: `garrisonMissonBonusAbilityID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_MISSION_BONUS_ROLL_COMPLETE

- Status: ❔ unverified
- Payload: `missionID: number`, `success: bool`
- fires synchronously (Blizzard's docs)

### GARRISON_MISSION_COMPLETE_RESPONSE

- Status: ❔ unverified
- Payload: `missionID: number`, `canComplete: bool`, `success: bool`, `bonusRollSuccess: bool`, `followerDeaths: GarrisonFollowerDeathInfo[]`, `autoCombatResult: AutoCombatResult?`
- fires synchronously (Blizzard's docs)

### GARRISON_MISSION_FINISHED

- Status: ❔ unverified
- Payload: `followerTypeID: number`, `missionID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_MISSION_LIST_UPDATE

- Status: ❔ unverified
- Payload: `garrFollowerTypeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_MISSION_NPC_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_MISSION_NPC_OPENED

- Status: ❔ unverified
- Payload: `followerTypeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_MISSION_REWARD_INFO

- Status: ❔ unverified
- Payload: `missionID: number`, `followerDbID: GarrisonFollower`
- fires synchronously (Blizzard's docs)

### GARRISON_MISSION_STARTED

- Status: ❔ unverified
- Payload: `garrFollowerTypeID: number`, `missionID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_MONUMENT_CLOSE_UI

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_MONUMENT_LIST_LOADED

- Status: ❔ unverified
- Payload: `success: bool`
- fires synchronously (Blizzard's docs)

### GARRISON_MONUMENT_REPLACED

- Status: ❔ unverified
- Payload: `success: bool`
- fires synchronously (Blizzard's docs)

### GARRISON_MONUMENT_SELECTED_TROPHY_ID_LOADED

- Status: ❔ unverified
- Payload: `success: bool`
- fires synchronously (Blizzard's docs)

### GARRISON_MONUMENT_SHOW_UI

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_RANDOM_MISSION_ADDED

- Status: ❔ unverified
- Payload: `followerTypeID: number`, `missionID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_RECALL_PORTAL_LAST_USED_TIME

- Status: ❔ unverified
- Payload: `success: bool`, `recallPortalLastUsedTime: number`
- fires synchronously (Blizzard's docs)

### GARRISON_RECALL_PORTAL_USED

- Status: ❔ unverified
- Payload: `success: bool`
- fires synchronously (Blizzard's docs)

### GARRISON_RECRUITMENT_FOLLOWERS_GENERATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_RECRUITMENT_NPC_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_RECRUITMENT_NPC_OPENED

- Status: ❔ unverified
- Payload: `followerTypeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_RECRUITMENT_READY

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_RECRUIT_FOLLOWER_RESULT

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_SHIPMENT_RECEIVED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### GARRISON_SHIPYARD_NPC_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_SHIPYARD_NPC_OPENED

- Status: ❔ unverified
- Payload: `followerTypeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_SHOW_LANDING_PAGE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_SPEC_GROUPS_CLEARED

- Status: ❔ unverified
- Payload: `garrTypeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_SPEC_GROUP_UPDATED

- Status: ❔ unverified
- Payload: `garrTypeID: number`, `specID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_TALENT_COMPLETE

- Status: ❔ unverified
- Payload: `garrTypeID: number`, `doAlert: bool`
- fires synchronously (Blizzard's docs)

### GARRISON_TALENT_EVENT_UPDATE

- Status: ❔ unverified
- Payload: `eventType: number`, `eventID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_TALENT_NPC_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_TALENT_NPC_OPENED

- Status: ❔ unverified
- Payload: `garrisonTypeID: number`, `garrisonTalentTreeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_TALENT_RESEARCH_STARTED

- Status: ❔ unverified
- Payload: `garrTypeID: number`, `garrisonTalentTreeID: number`, `garrTalentID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_TALENT_UNLOCKS_RESULT

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_TALENT_UPDATE

- Status: ❔ unverified
- Payload: `garrTypeID: number`
- fires synchronously (Blizzard's docs)

### GARRISON_TRADESKILL_NPC_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### GARRISON_UPGRADEABLE_RESULT

- Status: ❔ unverified
- Payload: `garrisonUpgradeable: bool`
- fires synchronously (Blizzard's docs)

### GARRISON_USE_PARTY_GARRISON_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHIPMENT_CRAFTER_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHIPMENT_CRAFTER_INFO

- Status: ❔ unverified
- Payload: `success: number`, `shipmentCount: number`, `maxShipments: number`, `ownedShipments: number`, `plotInstanceID: number`
- fires synchronously (Blizzard's docs)

### SHIPMENT_CRAFTER_OPENED

- Status: ❔ unverified
- Payload: `charShipmentContainerID: number`
- fires synchronously (Blizzard's docs)

### SHIPMENT_CRAFTER_REAGENT_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHIPMENT_UPDATE

- Status: ❔ unverified
- Payload: `shipmentStarted: bool?`, `hasAttachedFollower: bool?`
- fires synchronously (Blizzard's docs)

## Types

### AutoCombatDamageClassString

- Structure
  - `damageClassValue`: number
  - `locString`: cstring

### AutoCombatResult

- Structure
  - `winner`: bool
  - `combatLog`: AutoMissionRound[]

### AutoCombatSpellInfo

- Structure
  - `autoCombatSpellID`: number
  - `name`: cstring
  - `description`: string
  - `cooldown`: number
  - `duration`: number
  - `schoolMask`: number
  - `previewMask`: number
  - `icon`: fileID
  - `spellTutorialFlag`: number
  - `hasThornsEffect`: bool

### AutoCombatTroopInfo

- Structure
  - `name`: cstring
  - `followerID`: GarrisonFollower
  - `garrFollowerID`: GarrisonFollower
  - `followerTypeID`: number
  - `displayIDs`: FollowerDisplayID[]
  - `level`: number
  - `quality`: number
  - `levelXP`: number
  - `maxXP`: number
  - `height`: number
  - `scale`: number
  - `displayScale`: number?
  - `displayHeight`: number?
  - `classSpec`: number?
  - `className`: string?
  - `flavorText`: string?
  - `classAtlas`: textureAtlas
  - `portraitIconID`: fileID
  - `textureKit`: textureKit
  - `isTroop`: bool
  - `raceID`: number
  - `health`: number
  - `maxHealth`: number
  - `role`: number
  - `isAutoTroop`: bool
  - `isSoulbind`: bool
  - `isCollected`: bool
  - `autoCombatStats`: FollowerAutoCombatStatsInfo

### AutoMissionCombatEventInfo

- Structure
  - `boardIndex`: number
  - `oldHealth`: number
  - `newHealth`: number
  - `maxHealth`: number
  - `points`: number?

### AutoMissionEnvironmentEffect

- Structure
  - `name`: string
  - `autoCombatSpellInfo`: AutoCombatSpellInfo

### AutoMissionEvent

- Structure
  - `type`: number
  - `spellID`: number
  - `schoolMask`: number
  - `effectIndex`: number
  - `casterBoardIndex`: number
  - `auraType`: number
  - `targetInfo`: AutoMissionCombatEventInfo[]

### AutoMissionRound

- Structure
  - `events`: AutoMissionEvent[]

### AutoMissionTargetingInfo

- Structure
  - `targetIndex`: number
  - `previewType`: number
  - `spellID`: number
  - `effectIndex`: number

### FollowerAutoCombatStatsInfo

- Structure
  - `currentHealth`: number
  - `maxHealth`: number
  - `attack`: number
  - `healingTimestamp`: time_t
  - `healCost`: number
  - `minutesHealingRemaining`: number

### FollowerDisplayID

- Structure
  - `id`: number
  - `followerPageScale`: number
  - `showWeapon`: bool

### FollowerMissionCompleteInfo

- Structure
  - `name`: cstring
  - `displayIDs`: FollowerDisplayID[]
  - `level`: number
  - `quality`: number
  - `currentXP`: number
  - `maxXP`: number
  - `height`: number
  - `scale`: number
  - `movementType`: number?
  - `impactDelay`: number?
  - `castID`: number?
  - `castSoundID`: number?
  - `impactID`: number?
  - `impactSoundID`: number?
  - `targetImpactID`: number?
  - `targetImpactSoundID`: number?
  - `className`: string?
  - `classAtlas`: textureAtlas
  - `portraitIconID`: fileID
  - `textureKit`: textureKit
  - `isTroop`: bool
  - `boardIndex`: number
  - `health`: number
  - `maxHealth`: number
  - `role`: number

### GarrisonAbilityCounterInfo

- Structure
  - `id`: number
  - `icon`: fileID
  - `name`: cstring
  - `factor`: number
  - `description`: cstring

### GarrisonAbilityInfo

- Structure
  - `id`: number
  - `name`: cstring
  - `description`: string
  - `icon`: fileID
  - `isTrait`: bool
  - `isSpecialization`: bool
  - `temporary`: bool
  - `category`: string?
  - `counters`: GarrisonAbilityCounterInfo[]
  - `isEmptySlot`: bool

### GarrisonEnemyEncounterInfo

- Structure
  - `name`: cstring
  - `displayID`: fileID
  - `portraitFileDataID`: fileID
  - `textureKit`: textureKit
  - `scale`: number
  - `height`: number
  - `mechanics`: GarrisonMechanicInfo[]
  - `autoCombatSpells`: AutoCombatSpellInfo[]
  - `autoCombatAutoAttack`: AutoCombatSpellInfo?
  - `role`: number
  - `health`: number
  - `maxHealth`: number
  - `attack`: number
  - `boardIndex`: number
  - `isElite`: bool

### GarrisonFollowerDeathInfo

- Structure
  - `followerID`: GarrisonFollower
  - `state`: luaIndex

### GarrisonMechanicInfo

- Structure
  - `mechanicTypeID`: number
  - `icon`: fileID
  - `name`: cstring
  - `factor`: number
  - `description`: cstring
  - `ability`: GarrisonAbilityInfo?

### GarrisonPlotInstanceMapInfo

- Structure
  - `buildingPlotInstanceID`: number
  - `position`: vector2
  - `name`: cstring
  - `atlasName`: textureAtlas

### MissionDeploymentInfo

- Structure
  - `location`: cstring
  - `xp`: number
  - `environment`: string?
  - `environmentDesc`: string?
  - `environmentTexture`: fileID
  - `locTextureKit`: textureKit
  - `isExhausting`: bool
  - `enemies`: GarrisonEnemyEncounterInfo[]

### MissionEncounterIconInfo

- Structure
  - `portraitFileDataID`: fileID
  - `missionScalar`: number
  - `isElite`: bool
  - `isRare`: bool
