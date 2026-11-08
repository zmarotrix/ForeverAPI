# In-game checklist: ApiProbe 0.2.2

The probe is deployed to `_forever_\Interface\AddOns\ApiProbe`. It's a new add-on folder, so the game needs a
**full restart** (not `/reload`) before it shows up. It's under **Probes** in the add-on list.

1. Restart the game, make sure **API probe** is enabled, log in on any character. Your normal add-ons can stay on.
2. Wait about 10 seconds. Chat shows `API probe dumping N globals...` then `dump done`. (The dump may hitch for a
   second.)
3. Type `/apiprobe calls`. It calls about 2,000 getters over a few seconds and says `outside calls done` and `armed`.
4. Get into a fight (any mob). The same getters run again during combat; wait for `combat calls done`. If combat ends
   first, it says how far it got and finishes in your next fight.
5. Play normally for a while if you like: the live event counter records which events fire and what argument kinds
   they carry. A dungeon or group run adds the most.
6. `/reload` or log out so the SavedVariables are written.
7. Tell me, or run:

   ```
   python tools/apidoc.py import
   python tools/apidoc.py build
   ```

Worth reporting back: a red "blocked-action reports" line in `/apiprobe` status, any Lua error naming
ApiProbe, and roughly how big `WTF\Account\<account>\SavedVariables\ApiProbe.lua` came out.

## 0.2.0: getters with sample arguments

0.2.0 also calls about 890 documented getters that need arguments, using samples it reads from your own character:
your GUID, Hearthstone (6948), a spell from your spellbook, your first equipped item, your current map, the first quest
in your log, your class, race and guild. Index arguments get 1 and enum arguments their first value. Only the
kind of sample is saved, never its value.

1. `/reload` (no restart needed). Have at least one quest in your log and something equipped, so those samples exist.
2. `/apiprobe calls`, wait for "outside calls done" and "armed".
3. Fight a mob until "combat calls done".
4. `/reload`, then tell me "import".

If the client crashes, don't worry: tell me, and I'll read the crash log, put that call on the skip list and redeploy.

## Background collectors (new add-on folders: restart the game once)

Three more add-ons under **Probes**, all on by default, all quiet. Leave them on while you play normally, and
`/reload` or log out now and then so their files get written. Then tell me "import".

- **API watch** (`/apiwatch`): the first time it sees a situation (open world, dungeon, raid, battleground; idle, in
  combat, in a boss fight) it runs the getters there, and the first time it sees a kind of unit (an enemy or friendly
  target, a party or raid member, a nameplate, a boss) it runs the unit getters on it. It also logs every time
  add-on restrictions switch on or off. **Most useful: a dungeon run with a group, including the bosses.**
  It skips everything that crashed the client or that the probe saw refused, so it shouldn't pop up any
  "blocked" messages; if one does, it remembers and never repeats that call.
- **API timeline** (`/apitimeline`): records which events fire, in what order, around login, zoning, combat, boss
  pulls, loot, vendors, mail, bank, quests, death, level-up, groups, trades, flights and casts. Three of each.
- **API widgets** (`/apiwidgets`): once, 10 seconds after login, tests which widget setters accept a secret value;
  again in your next fight. Takes a few seconds; nothing shows on screen.

None of them stores names, chat, values or anything about your character: only event names, types, "ok" or error
text. ApiProbe itself can stay off now unless you want another `/apiprobe calls` run.

## API checks 0.1.0 (new add-on folder: restart the game once)

One more add-on under **Probes**: **API checks** (`/apichecks`). It checks things testers reported. It only
listens, so leave it on and play; each item fills in when you do the thing:

- [ ] **Die once** (PLAYER_DEAD twice?). A duel loss doesn't count; a mob or falling does.
- [ ] **Open and close a vendor, and the auction house** (MERCHANT_CLOSED / AUCTION_HOUSE_CLOSED twice?).
- [ ] **Hearth, take a flight, and use a portal or a dungeon entrance** (is the zone text stale when the zone events fire?).
- [ ] **Walk into an inn or a city** ("You feel rested."), **post an auction** ("Auction created."), **go AFK and come back** (`/afk` twice).
- [ ] **Fight a few mobs**, best with a pet if your class has one (combat feed, damage meter, pet health).
- [ ] **Target an enemy and have nameplates on** (UnitIsUnit against enemy units).
- [ ] **Cast a spell on yourself, on a friend and on an enemy** (UNIT_SPELLCAST_SENT's target).
- [ ] **Chat test, only if you're OK with it**: `/apichecks chat`, then `/apichecks chat yes`, then `/apichecks chat`
      once more when it asks. It sends "." in /say, /yell and /emote, so people near you see it. Do it once in the
      open world and once inside a dungeon. Out in the world, Blizzard may block the say and yell sent without a key
      press and show a "blocked" message: that's the answer, and the add-on won't try that one again.

Then `/reload` and run update-docs.bat. The answers are on the site's **Reported quirks** page.

