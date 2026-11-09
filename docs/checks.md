# Reported quirks, checked

Behaviour testers reported on Forever, checked in game by the ApiChecks add-on. Each answer comes from what the add-on saw; "not seen yet" means it hasn't watched that happen.

Client 1.60.1.70862, add-on 0.1.0.

## Does PLAYER_DEAD fire twice?

**No**: once each time (5 seen).

- fires per a death: 1× 5

## Does MERCHANT_CLOSED fire twice?

**Yes**: 13 of 16 times it fired more than once.

- fires per closing a vendor: 1× 3, 2× 13
- gap between the copies: up to 0 ms

## Does AUCTION_HOUSE_CLOSED fire twice?

**Yes**: 3 of 4 times it fired more than once.

- fires per closing the auction house: 1× 1, 2× 3
- gap between the copies: up to 0 ms

## Is the zone text stale at PLAYER_ENTERING_WORLD?

**Yes, sometimes**: the text changed within 3 s of the event 30 times. Read it again a moment later (or on ZONE_CHANGED / the next frame). Not covered yet: arriving by taxi.

- loading screen: stale 11 of 19
- spell: stale 16 of 20
- walked: stale 3 of 18

## Is the zone text stale at ZONE_CHANGED_NEW_AREA?

**Yes, sometimes**: the text changed within 3 s of the event 10 times. Read it again a moment later (or on ZONE_CHANGED / the next frame). Not covered yet: arriving by taxi.

- loading screen: stale 0 of 4
- spell: stale 3 of 36
- walked: stale 7 of 51

## Does "You feel rested." skip the CHAT_MSG_ events?

**No**: it arrives as CHAT_MSG_SYSTEM.

- triggered 23 times
- seen on CHAT_MSG_SYSTEM: 4
- seen on chat frame: 4

## Does "Auction created." skip the CHAT_MSG_ events?

Not seen yet.


## Does AFK off skip the CHAT_MSG_ events?

**No**: it arrives as CHAT_MSG_SYSTEM.

- triggered 5 times
- seen on CHAT_MSG_SYSTEM: 4
- seen on chat frame: 4

## Does AFK on skip the CHAT_MSG_ events?

**No**: it arrives as CHAT_MSG_SYSTEM.

- triggered 5 times
- seen on CHAT_MSG_SYSTEM: 5
- seen on chat frame: 5

## Are system messages ever secret?

**Yes**: some couldn't be compared because the text was secret.

- CHAT_MSG_SYSTEM: 3

## Does WOW_PROJECT_ID report 1 (Retail)?

**No**: it is 18. WOW_PROJECT_MAINLINE is 1, WOW_PROJECT_CLASSIC 2, WOW_PROJECT_CAMELOT 18.


## Can add-ons say, yell or emote (world)?

**Nothing went through.**

- EMOTE from a timer: blocked, never came back
- SAY from a keypress: type /apichecks chat again to send this one from a key press
- SAY from a timer: blocked, never came back
- YELL from a timer: blocked, never came back

## What does UNIT_COMBAT carry?

Fires in combat too; some arguments are secret.

- arguments: s,s,s,N,n ×128992 (capitals are secret)
- when: combat ×125094, just after combat ×529, outside ×3369
- actions: WOUND ×100269, WOUND/CRITICAL ×8758, HEAL ×7268, MISS ×4692, DODGE ×3445, WOUND/GLANCING ×1435, PARRY ×884, WOUND/BLOCK_REDUCED ×620, HEAL/CRITICAL ×442, WOUND/CRUSHING ×396, RESIST ×272, IMMUNE ×221, WOUND/ABSORB ×159, WOUND/BLOCK ×74, REFLECT ×46
- units: nameplateN ×63005, target ×26131, player ×15120, targettarget ×13762, partyN ×5705, partypetN ×4153, softenemy ×1029, softfriend ×82, npc ×5

## What does COMBAT_LOG_MESSAGE carry?

Fires in combat too; no secret arguments seen.

- arguments: s,n,n,n,n ×2848 (capitals are secret)
- when: combat ×929, outside ×1919
- readable lines: 2848, wrapped in |K...|k: 2848

## What does COMBAT_TEXT_UPDATE carry?

Fires in combat too; no secret arguments seen.

- arguments: s ×263 (capitals are secret)
- when: combat ×212, just after combat ×1, outside ×50
- types: FACTION ×263
- GetCurrentCombatTextEventInfo: S,N ×263

## What does DAMAGE_METER_COMBAT_SESSION_UPDATED carry?

Fires in combat too; no secret arguments seen.

- arguments: n,n ×252828 (capitals are secret)
- when: combat ×241930, just after combat ×1272, outside ×9626

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

- enemy target, in combat: target nil ×451, target plain ×2885, target secret ×4871
- enemy target, out of combat: target nil ×75, target plain ×167, target secret ×188
- friendly target, in combat: target nil ×1, target plain ×6, target secret ×6
- friendly target, out of combat: target nil ×59, target plain ×63, target secret ×6
- no target, in combat: target nil ×8, target plain ×12, target secret ×1
- no target, out of combat: target nil ×77, target plain ×67, target secret ×7
- target is you, out of combat: target nil ×4

## Does UnitIsUnit return a secret against enemy units?

**No secret seen.**

- enemy nameplate: UnitIsUnit(nameplateN, player): plain ×2082
- enemy nameplate: UnitIsUnit(nameplateN, player) in combat: plain ×4790
- enemy nameplate: UnitIsUnit(nameplateN, target): plain ×2082
- enemy nameplate: UnitIsUnit(nameplateN, target) in combat: plain ×4790
- enemy nameplate: UnitIsUnit(player, nameplate1): plain ×709
- enemy nameplate: UnitIsUnit(player, nameplate1) in combat: plain ×796
- enemy nameplate: UnitIsUnit(player, nameplate10): plain ×5
- enemy nameplate: UnitIsUnit(player, nameplate10) in combat: plain ×101
- enemy nameplate: UnitIsUnit(player, nameplate11): plain ×2
- enemy nameplate: UnitIsUnit(player, nameplate11) in combat: plain ×63
- enemy nameplate: UnitIsUnit(player, nameplate12) in combat: plain ×43
- enemy nameplate: UnitIsUnit(player, nameplate13) in combat: plain ×25
- enemy nameplate: UnitIsUnit(player, nameplate14) in combat: plain ×21
- enemy nameplate: UnitIsUnit(player, nameplate15) in combat: plain ×14
- enemy nameplate: UnitIsUnit(player, nameplate16) in combat: plain ×14
- enemy nameplate: UnitIsUnit(player, nameplate17) in combat: plain ×4
- enemy nameplate: UnitIsUnit(player, nameplate18) in combat: plain ×2
- enemy nameplate: UnitIsUnit(player, nameplate19) in combat: plain ×1
- enemy nameplate: UnitIsUnit(player, nameplate2): plain ×443
- enemy nameplate: UnitIsUnit(player, nameplate2) in combat: plain ×783
- enemy nameplate: UnitIsUnit(player, nameplate20) in combat: plain ×1
- enemy nameplate: UnitIsUnit(player, nameplate21) in combat: plain ×1
- enemy nameplate: UnitIsUnit(player, nameplate22) in combat: plain ×1
- enemy nameplate: UnitIsUnit(player, nameplate23) in combat: plain ×1
- enemy nameplate: UnitIsUnit(player, nameplate24) in combat: plain ×1
- enemy nameplate: UnitIsUnit(player, nameplate3): plain ×306
- enemy nameplate: UnitIsUnit(player, nameplate3) in combat: plain ×687
- enemy nameplate: UnitIsUnit(player, nameplate4): plain ×231
- enemy nameplate: UnitIsUnit(player, nameplate4) in combat: plain ×650
- enemy nameplate: UnitIsUnit(player, nameplate5): plain ×156
- enemy nameplate: UnitIsUnit(player, nameplate5) in combat: plain ×550
- enemy nameplate: UnitIsUnit(player, nameplate6): plain ×119
- enemy nameplate: UnitIsUnit(player, nameplate6) in combat: plain ×396
- enemy nameplate: UnitIsUnit(player, nameplate7): plain ×63
- enemy nameplate: UnitIsUnit(player, nameplate7) in combat: plain ×295
- enemy nameplate: UnitIsUnit(player, nameplate8): plain ×33
- enemy nameplate: UnitIsUnit(player, nameplate8) in combat: plain ×202
- enemy nameplate: UnitIsUnit(player, nameplate9): plain ×15
- enemy nameplate: UnitIsUnit(player, nameplate9) in combat: plain ×138
- enemy target: UnitIsUnit(player, target): plain ×910
- enemy target: UnitIsUnit(player, target) in combat: plain ×5598
- enemy target: UnitIsUnit(target, player): plain ×910
- enemy target: UnitIsUnit(target, player) in combat: plain ×5598
- enemy target: UnitIsUnit(target, target): plain ×910
- enemy target: UnitIsUnit(target, target) in combat: plain ×5598
- friendly target: UnitIsUnit(player, target): plain ×251
- friendly target: UnitIsUnit(player, target) in combat: plain ×189
- friendly target: UnitIsUnit(target, player): plain ×251
- friendly target: UnitIsUnit(target, player) in combat: plain ×189
- friendly target: UnitIsUnit(target, target): plain ×251
- friendly target: UnitIsUnit(target, target) in combat: plain ×189
- target: UnitIsUnit(player, target) in combat: plain ×30
- target: UnitIsUnit(target, player) in combat: plain ×30
- target: UnitIsUnit(target, target) in combat: plain ×30

## Is UnitHealth("pet") secret?

Not seen yet.

