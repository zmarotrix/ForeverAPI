# Reported quirks, checked

Behaviour testers reported on Forever, checked in game by the ApiChecks add-on. Each answer comes from what the add-on saw; "not seen yet" means it hasn't watched that happen.

Client 1.60.1.70862, add-on 0.1.0.

## Does PLAYER_DEAD fire twice?

**No**: once each time (2 seen).

- fires per a death: 1× 2

## Does MERCHANT_CLOSED fire twice?

**Yes**: 1 of 2 times it fired more than once.

- fires per closing a vendor: 1× 1, 2× 1
- gap between the copies: up to 0 ms

## Does AUCTION_HOUSE_CLOSED fire twice?

Not seen yet: needs closing the auction house.


## Is the zone text stale at PLAYER_ENTERING_WORLD?

**Yes, sometimes**: the text changed within 3 s of the event 1 times. Read it again a moment later (or on ZONE_CHANGED / the next frame). Not covered yet: arriving by taxi.

- loading screen: stale 0 of 8
- spell: stale 1 of 5
- walked: stale 0 of 6

## Is the zone text stale at ZONE_CHANGED_NEW_AREA?

**Yes, sometimes**: the text changed within 3 s of the event 5 times. Read it again a moment later (or on ZONE_CHANGED / the next frame). Not covered yet: arriving by taxi.

- loading screen: stale 0 of 1
- spell: stale 2 of 10
- walked: stale 3 of 11

## Does "You feel rested." skip the CHAT_MSG_ events?

**No**: it arrives as CHAT_MSG_SYSTEM.

- triggered 6 times
- seen on CHAT_MSG_SYSTEM: 1
- seen on chat frame: 1

## Does "Auction created." skip the CHAT_MSG_ events?

Not seen yet.


## Does AFK off skip the CHAT_MSG_ events?

Not seen yet.


## Does AFK on skip the CHAT_MSG_ events?

Not seen yet.


## Are system messages ever secret?

**Yes**: some couldn't be compared because the text was secret.

- CHAT_MSG_SYSTEM: 1

## Does WOW_PROJECT_ID report 1 (Retail)?

**No**: it is 18. WOW_PROJECT_MAINLINE is 1, WOW_PROJECT_CLASSIC 2, WOW_PROJECT_CAMELOT 18.


## Can add-ons say, yell or emote in instances?

Not tested yet: run /apichecks chat in the world and in a dungeon.


## What does UNIT_COMBAT carry?

Fires in combat too; some arguments are secret.

- arguments: s,s,s,N,n ×53861 (capitals are secret)
- when: combat ×52497, just after combat ×212, outside ×1152
- actions: WOUND ×43032, WOUND/CRITICAL ×3261, HEAL ×2616, MISS ×1802, DODGE ×1502, WOUND/GLANCING ×389, PARRY ×351, WOUND/BLOCK_REDUCED ×256, HEAL/CRITICAL ×179, RESIST ×160, IMMUNE ×94, WOUND/CRUSHING ×87, WOUND/ABSORB ×73, WOUND/BLOCK ×31, REFLECT ×28
- units: nameplateN ×26953, target ×9752, player ×7243, targettarget ×6632, partyN ×1696, partypetN ×1127, softenemy ×425, softfriend ×28, npc ×5

## What does COMBAT_LOG_MESSAGE carry?

Fires in combat too; no secret arguments seen.

- arguments: s,n,n,n,n ×1260 (capitals are secret)
- when: combat ×541, outside ×719
- readable lines: 1260, wrapped in |K...|k: 1260

## What does COMBAT_TEXT_UPDATE carry?

Fires in combat too; no secret arguments seen.

- arguments: s ×169 (capitals are secret)
- when: combat ×159, just after combat ×1, outside ×9
- types: FACTION ×169
- GetCurrentCombatTextEventInfo: S,N ×169

## What does DAMAGE_METER_COMBAT_SESSION_UPDATED carry?

Fires in combat too; no secret arguments seen.

- arguments: n,n ×100244 (capitals are secret)
- when: combat ×97114, just after combat ×490, outside ×2640

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

- enemy target, in combat: target nil ×162, target plain ×1656, target secret ×1436
- enemy target, out of combat: target nil ×26, target plain ×89, target secret ×52
- friendly target, in combat: target plain ×4, target secret ×3
- friendly target, out of combat: target nil ×13, target plain ×9
- no target, in combat: target nil ×1, target plain ×7
- no target, out of combat: target nil ×17, target plain ×34

## Does UnitIsUnit return a secret against enemy units?

**No secret seen.**

- enemy nameplate: UnitIsUnit(nameplateN, player): plain ×828
- enemy nameplate: UnitIsUnit(nameplateN, player) in combat: plain ×1892
- enemy nameplate: UnitIsUnit(nameplateN, target): plain ×828
- enemy nameplate: UnitIsUnit(nameplateN, target) in combat: plain ×1892
- enemy nameplate: UnitIsUnit(player, nameplate1): plain ×271
- enemy nameplate: UnitIsUnit(player, nameplate1) in combat: plain ×316
- enemy nameplate: UnitIsUnit(player, nameplate10): plain ×3
- enemy nameplate: UnitIsUnit(player, nameplate10) in combat: plain ×41
- enemy nameplate: UnitIsUnit(player, nameplate11): plain ×2
- enemy nameplate: UnitIsUnit(player, nameplate11) in combat: plain ×27
- enemy nameplate: UnitIsUnit(player, nameplate12) in combat: plain ×14
- enemy nameplate: UnitIsUnit(player, nameplate13) in combat: plain ×9
- enemy nameplate: UnitIsUnit(player, nameplate14) in combat: plain ×6
- enemy nameplate: UnitIsUnit(player, nameplate15) in combat: plain ×1
- enemy nameplate: UnitIsUnit(player, nameplate2): plain ×158
- enemy nameplate: UnitIsUnit(player, nameplate2) in combat: plain ×271
- enemy nameplate: UnitIsUnit(player, nameplate3): plain ×129
- enemy nameplate: UnitIsUnit(player, nameplate3) in combat: plain ×237
- enemy nameplate: UnitIsUnit(player, nameplate4): plain ×90
- enemy nameplate: UnitIsUnit(player, nameplate4) in combat: plain ×279
- enemy nameplate: UnitIsUnit(player, nameplate5): plain ×70
- enemy nameplate: UnitIsUnit(player, nameplate5) in combat: plain ×220
- enemy nameplate: UnitIsUnit(player, nameplate6): plain ×57
- enemy nameplate: UnitIsUnit(player, nameplate6) in combat: plain ×166
- enemy nameplate: UnitIsUnit(player, nameplate7): plain ×27
- enemy nameplate: UnitIsUnit(player, nameplate7) in combat: plain ×136
- enemy nameplate: UnitIsUnit(player, nameplate8): plain ×15
- enemy nameplate: UnitIsUnit(player, nameplate8) in combat: plain ×100
- enemy nameplate: UnitIsUnit(player, nameplate9): plain ×6
- enemy nameplate: UnitIsUnit(player, nameplate9) in combat: plain ×69
- enemy target: UnitIsUnit(player, target): plain ×361
- enemy target: UnitIsUnit(player, target) in combat: plain ×2438
- enemy target: UnitIsUnit(target, player): plain ×361
- enemy target: UnitIsUnit(target, player) in combat: plain ×2438
- enemy target: UnitIsUnit(target, target): plain ×361
- enemy target: UnitIsUnit(target, target) in combat: plain ×2438
- friendly target: UnitIsUnit(player, target): plain ×60
- friendly target: UnitIsUnit(player, target) in combat: plain ×63
- friendly target: UnitIsUnit(target, player): plain ×60
- friendly target: UnitIsUnit(target, player) in combat: plain ×63
- friendly target: UnitIsUnit(target, target): plain ×60
- friendly target: UnitIsUnit(target, target) in combat: plain ×63
- target: UnitIsUnit(player, target) in combat: plain ×16
- target: UnitIsUnit(target, player) in combat: plain ×16
- target: UnitIsUnit(target, target) in combat: plain ×16

## Is UnitHealth("pet") secret?

Not seen yet.

