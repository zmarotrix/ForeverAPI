# In-game checklist: ApiProbe 0.2.0

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
