# Reported quirks, checked

Behaviour testers reported on Forever, checked in game by the ApiChecks add-on. Each answer comes from what the add-on saw; "not seen yet" means it hasn't watched that happen.

Client 1.60.1.70862, add-on 0.1.0.

## Does PLAYER_DEAD fire twice?

**No**: once each time (2 seen).

- fires per a death: 1× 2

## Does MERCHANT_CLOSED fire twice?

**Yes**: 4 of 5 times it fired more than once.

- fires per closing a vendor: 1× 1, 2× 4
- gap between the copies: up to 0 ms

## Does AUCTION_HOUSE_CLOSED fire twice?

**Yes**: 1 of 1 times it fired more than once.

- fires per closing the auction house: 2× 1
- gap between the copies: up to 0 ms

## Is the zone text stale at PLAYER_ENTERING_WORLD?

**Yes, sometimes**: the text changed within 3 s of the event 3 times. Read it again a moment later (or on ZONE_CHANGED / the next frame). Not covered yet: arriving by taxi.

- loading screen: stale 1 of 9
- spell: stale 2 of 6
- walked: stale 0 of 7

## Is the zone text stale at ZONE_CHANGED_NEW_AREA?

**Yes, sometimes**: the text changed within 3 s of the event 5 times. Read it again a moment later (or on ZONE_CHANGED / the next frame). Not covered yet: arriving by taxi.

- loading screen: stale 0 of 2
- spell: stale 2 of 12
- walked: stale 3 of 13

## Does "You feel rested." skip the CHAT_MSG_ events?

**No**: it arrives as CHAT_MSG_SYSTEM.

- triggered 6 times
- seen on CHAT_MSG_SYSTEM: 2
- seen on chat frame: 2

## Does "Auction created." skip the CHAT_MSG_ events?

Not seen yet.


## Does AFK off skip the CHAT_MSG_ events?

Not seen yet.


## Does AFK on skip the CHAT_MSG_ events?

Not seen yet.


## Are system messages ever secret?

**Yes**: some couldn't be compared because the text was secret.

- CHAT_MSG_SYSTEM: 2

## Does WOW_PROJECT_ID report 1 (Retail)?

**No**: it is 18. WOW_PROJECT_MAINLINE is 1, WOW_PROJECT_CLASSIC 2, WOW_PROJECT_CAMELOT 18.


## Can add-ons say, yell or emote in instances?

Not tested yet: run /apichecks chat in the world and in a dungeon.


## What does UNIT_COMBAT carry?

Fires in combat too; some arguments are secret.

- arguments: s,s,s,N,n ×64620 (capitals are secret)
- when: combat ×63110, just after combat ×247, outside ×1263
- actions: WOUND ×51698, WOUND/CRITICAL ×3978, HEAL ×3167, MISS ×2108, DODGE ×1764, WOUND/GLANCING ×503, PARRY ×389, WOUND/BLOCK_REDUCED ×299, HEAL/CRITICAL ×213, RESIST ×173, IMMUNE ×105, WOUND/CRUSHING ×89, WOUND/ABSORB ×73, WOUND/BLOCK ×33, REFLECT ×28
- units: nameplateN ×32625, target ×11943, player ×8465, targettarget ×7705, partyN ×2035, partypetN ×1331, softenemy ×479, softfriend ×32, npc ×5

## What does COMBAT_LOG_MESSAGE carry?

Fires in combat too; no secret arguments seen.

- arguments: s,n,n,n,n ×1560 (capitals are secret)
- when: combat ×841, outside ×719
- readable lines: 1560, wrapped in |K...|k: 1560

## What does COMBAT_TEXT_UPDATE carry?

Fires in combat too; no secret arguments seen.

- arguments: s ×223 (capitals are secret)
- when: combat ×212, just after combat ×1, outside ×10
- types: FACTION ×223
- GetCurrentCombatTextEventInfo: S,N ×223

## What does DAMAGE_METER_COMBAT_SESSION_UPDATED carry?

Fires in combat too; no secret arguments seen.

- arguments: n,n ×119538 (capitals are secret)
- when: combat ×116336, just after combat ×556, outside ×2646

## What does C_DamageMeter give add-ons?

Shapes below; *secret* marks a secret value.

- **outside**
- GetAvailableCombatSessions → {[n]={durationSeconds=number,name=string,sessionID=number},...}#24
- GetCombatSessionFromID → {combatSources={[n]=table}#3,durationSeconds=number,maxAmount=number,totalAmount=number}
- GetCombatSessionFromType → {combatSources={[n]=table}#5,durationSeconds=number,maxAmount=number,totalAmount=number}
- GetCombatSessionSourceFromType → {combatSpells={[n]=table}#8,maxAmount=number,totalAmount=number}
- GetSessionDurationSeconds → number
- IsDamageMeterAvailable → boolean, string
- source → {amountPerSecond=number,classFilename=string,classification=string,deathRecapID=number,deathTimeSeconds=number,isLocalPlayer=boolean,name=string,sourceDisplayType=number,sourceGUID=string,specIconID=secret number,totalAmount=number}
- **combat**
- GetAvailableCombatSessions → {[n]={durationSeconds=number,name=string,sessionID=number},...}#24
- GetCombatSessionFromID → {combatSources={[n]=table}#3,durationSeconds=secret number,maxAmount=secret number,totalAmount=secret number}
- GetCombatSessionFromType → {combatSources={[n]=table}#5,durationSeconds=secret number,maxAmount=secret number,totalAmount=secret number}
- GetCombatSessionSourceFromType → error: bad argument #3 to '?' (Usage: local sessionSource = C_DamageMeter.GetCombatSessionSourceFromType(sessionType, type [, sourceGUID, sourceCreatureID]). Secret values are only allowed during untainted 
- GetSessionDurationSeconds → number
- IsDamageMeterAvailable → boolean, string
- source → {amountPerSecond=secret number,classFilename=string,classification=string,deathRecapID=number,deathTimeSeconds=secret number,isLocalPlayer=boolean,name=secret string,sourceDisplayType=secret number,sourceGUID=secret string,specIconID=secret number,totalAmount=secret number}
- **after combat**
- GetAvailableCombatSessions → {[n]={durationSeconds=number,name=string,sessionID=number},...}#24
- GetCombatSessionFromID → {combatSources={[n]=table}#3,durationSeconds=number,maxAmount=number,totalAmount=number}
- GetCombatSessionFromType → {combatSources={[n]=table}#5,durationSeconds=number,maxAmount=number,totalAmount=number}
- GetCombatSessionSourceFromType → {combatSpells={[n]=table}#8,maxAmount=number,totalAmount=number}
- GetSessionDurationSeconds → number
- IsDamageMeterAvailable → boolean, string
- source → {amountPerSecond=number,classFilename=string,classification=string,deathRecapID=number,deathTimeSeconds=number,isLocalPlayer=boolean,name=string,sourceDisplayType=number,sourceGUID=string,specIconID=secret number,totalAmount=number}

## Is UNIT_SPELLCAST_SENT's target secret?

**Yes, in the cases below.**

- enemy target, in combat: target nil ×187, target plain ×1656, target secret ×1928
- enemy target, out of combat: target nil ×29, target plain ×102, target secret ×67
- friendly target, in combat: target plain ×4, target secret ×4
- friendly target, out of combat: target nil ×29, target plain ×27
- no target, in combat: target nil ×1, target plain ×7
- no target, out of combat: target nil ×21, target plain ×39
- target is you, out of combat: target nil ×4

## Does UnitIsUnit return a secret against enemy units?

**No secret seen.**

- enemy nameplate: UnitIsUnit(nameplateN, player): plain ×998
- enemy nameplate: UnitIsUnit(nameplateN, player) in combat: plain ×2103
- enemy nameplate: UnitIsUnit(nameplateN, target): plain ×998
- enemy nameplate: UnitIsUnit(nameplateN, target) in combat: plain ×2103
- enemy nameplate: UnitIsUnit(player, nameplate1): plain ×320
- enemy nameplate: UnitIsUnit(player, nameplate1) in combat: plain ×344
- enemy nameplate: UnitIsUnit(player, nameplate10): plain ×4
- enemy nameplate: UnitIsUnit(player, nameplate10) in combat: plain ×49
- enemy nameplate: UnitIsUnit(player, nameplate11): plain ×2
- enemy nameplate: UnitIsUnit(player, nameplate11) in combat: plain ×35
- enemy nameplate: UnitIsUnit(player, nameplate12) in combat: plain ×20
- enemy nameplate: UnitIsUnit(player, nameplate13) in combat: plain ×11
- enemy nameplate: UnitIsUnit(player, nameplate14) in combat: plain ×8
- enemy nameplate: UnitIsUnit(player, nameplate15) in combat: plain ×2
- enemy nameplate: UnitIsUnit(player, nameplate16) in combat: plain ×1
- enemy nameplate: UnitIsUnit(player, nameplate2): plain ×192
- enemy nameplate: UnitIsUnit(player, nameplate2) in combat: plain ×299
- enemy nameplate: UnitIsUnit(player, nameplate3): plain ×153
- enemy nameplate: UnitIsUnit(player, nameplate3) in combat: plain ×252
- enemy nameplate: UnitIsUnit(player, nameplate4): plain ×110
- enemy nameplate: UnitIsUnit(player, nameplate4) in combat: plain ×303
- enemy nameplate: UnitIsUnit(player, nameplate5): plain ×83
- enemy nameplate: UnitIsUnit(player, nameplate5) in combat: plain ×244
- enemy nameplate: UnitIsUnit(player, nameplate6): plain ×66
- enemy nameplate: UnitIsUnit(player, nameplate6) in combat: plain ×185
- enemy nameplate: UnitIsUnit(player, nameplate7): plain ×36
- enemy nameplate: UnitIsUnit(player, nameplate7) in combat: plain ×157
- enemy nameplate: UnitIsUnit(player, nameplate8): plain ×23
- enemy nameplate: UnitIsUnit(player, nameplate8) in combat: plain ×112
- enemy nameplate: UnitIsUnit(player, nameplate9): plain ×9
- enemy nameplate: UnitIsUnit(player, nameplate9) in combat: plain ×81
- enemy target: UnitIsUnit(player, target): plain ×407
- enemy target: UnitIsUnit(player, target) in combat: plain ×2818
- enemy target: UnitIsUnit(target, player): plain ×407
- enemy target: UnitIsUnit(target, player) in combat: plain ×2818
- enemy target: UnitIsUnit(target, target): plain ×407
- enemy target: UnitIsUnit(target, target) in combat: plain ×2818
- friendly target: UnitIsUnit(player, target): plain ×93
- friendly target: UnitIsUnit(player, target) in combat: plain ×82
- friendly target: UnitIsUnit(target, player): plain ×93
- friendly target: UnitIsUnit(target, player) in combat: plain ×82
- friendly target: UnitIsUnit(target, target): plain ×93
- friendly target: UnitIsUnit(target, target) in combat: plain ×82
- target: UnitIsUnit(player, target) in combat: plain ×19
- target: UnitIsUnit(target, player) in combat: plain ×19
- target: UnitIsUnit(target, target) in combat: plain ×19

## Is UnitHealth("pet") secret?

Not seen yet.

