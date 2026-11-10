# ForeverAPI

A reference for the **WoW Forever add-on API** (product `wowf`, interface 16001) as the client really has it, for
add-on developers. The rule: **nothing is documented as fact unless the game confirmed it.** Everything else is a
lead and says so.

- **Read it:** https://zmarotrix.github.io/ForeverAPI/ (search with `/`). Every function, event, enum, structure and
  widget method; what's secret, protected or forbidden; what classic globals moved where; quirks testers reported.
- **Code against it in VS Code:** the `ForeverAPI-LuaLS` zip on the
  [releases page](https://github.com/zmarotrix/ForeverAPI/releases) (typed definitions with the same notes).
- **Port classic code:** [docs/compat.json](docs/compat.json) maps each classic global to its Forever replacement.
- **Build on it:** [LibForever-1.0](lib/README.md), a library that handles what the Forever client doesn't: the
  classic functions that are gone, secret values, combat lockdown, first and last names, add-on messages and chat
  lines that arrive.

By Maro. Built with AI assistance (Anthropic's Claude), directed by Maro.

**Licence:** the library (`lib/`, [LICENSE](lib/LICENSE)), the reference (`docs/`, [LICENSE](docs/LICENSE)) and the
VS Code definitions (`luals/`, [LICENSE](luals/LICENSE)) are MIT. The libraries bundled with LibForever keep their own
licences ([lib/THIRD-PARTY-NOTICES.md](lib/THIRD-PARTY-NOTICES.md)). Everything else here (the probe add-on, the
tools and the website) is All Rights Reserved.

## How to help

The reference grows from probe runs in real games: dungeons, raids, boss fights, PvP, classes and situations one
person can't cover alone. If you play Forever, you can add yours.

1. Download **ForeverAPI Probe** from the [releases page](https://github.com/zmarotrix/ForeverAPI/releases) and
   unzip it into `_forever_/Interface/AddOns/`. Restart the game.
2. Type `/fapi` to see the modules, and `/fapi on all` (or pick some), then `/reload`. Nothing records until you
   do this.
3. Play normally. Dungeons, raids, boss fights and PvP add the most.
4. Type `/fapi export`, copy the box (Ctrl+C), and
   [open an "API data" issue](https://github.com/zmarotrix/ForeverAPI/issues/new?template=api-data.yml). Paste it
   there, or save it to a `.txt` file and drag that in.

**What it records:** names, types, "secret or not", error text and the order events fire in. **Never** a value, a
chat line, a character's or player's name, or a setting's value. It only calls getters, never anything that acts.
The export header holds the client build, the probe version and a random ID made once per account (so two exports
from you count once).

**What happens to it:** your data shows on the reference as **reported** (with a count) until Maro's own run, or a
second independent contributor, confirms it. One person's file never turns anything into verified. Files from
another client build, or naming functions and events this client doesn't have, are turned away.

The modules:

| Module | Records |
|---|---|
| `probe` | once per client build: every global, namespace member, enum, widget method and event name; getters out of and in combat; a live count of every event and its argument types |
| `watch` | getters again in each situation (dungeon, raid, boss fight, PvP) and on each kind of unit |
| `timeline` | which events fire, in what order, around login, zoning, combat, loot, vendors, flights... |
| `widgets` | which widget setters and Lua operations accept a secret value (a few seconds, once per build) |
| `checks` | behaviour testers reported: events firing twice, stale zone text, the combat feed, secret cases. `/fapi checks chat` is an opt-in test that sends "." in /say, /yell and /emote |

## Where the facts come from

| Source | What it gives | Trusted? |
|---|---|---|
| **ForeverAPI Probe** (in game, Maro's runs) | every global, `C_*` namespace member, `Enum`/`Constants` value, widget method and script handler; which event names `RegisterEvent` accepts; events seen firing and their argument kinds; CVars with help and defaults; what each getter returns out of combat and in combat (types and secret-ness only) | yes: this is what "verified" means |
| **Client docs** | `Blizzard_APIDocumentationGenerated` from the installed client (642 files): signatures, descriptions, restriction and secret flags | lead: shown with signatures, marked unverified until the dump confirms |
| **Client UI code** | `Interface/ui-code-list.txt`: event names Blizzard's own UI registers, functions it calls and defines | lead: names to check in game; also separates Blizzard's Lua helpers from client API |
| **Contributors** | other developers' `/fapi export` files (`apidoc.py contrib`) | reported, with a count; verified once two independent accounts agree |
| **Web** | anything you drop in `sources/web/` | lead only, never verified by itself |

Client files are read through a read-only CASC reader from Maro's add-on suite (not in this repo), so `extract`
runs on Maro's machine; everything else runs anywhere with Python 3.

Statuses in the docs: ✅ verified · 🆕 in game, not in Blizzard's docs (Forever-only or legacy) · ⛔ in Blizzard's
docs, not in game · ❔ unverified. Restriction and secret flags quoted from Blizzard's docs stay marked "not checked in
game"; [docs/restrictions.md](docs/restrictions.md) lists what the probe actually saw change in combat.

## Layout

```
addon/ForeverAPIProbe/  the add-on: core.lua (/fapi, module switches), export.lua (/fapi export), and one file
                      per module: probe, watch, timeline, widgets, checks. leads.lua and plan.lua are generated
tools/contrib.py      other people's exports: decode, check, file under contrib/<build>/, trust counts
tools/test_collectors.py  stub-client checks for watch, timeline, widgets, export, contrib and trust
tools/test_checks.py  stub-client checks for ApiChecks
tools/relocated.py    the relocated-API table: classic globals Forever dropped or moved, and where they went
tools/luals.py        the VS Code (LuaLS) definitions
tools/checkspage.py   turns ApiChecks data into plain answers (docs/checks.md, the Reported quirks page)
sources/relocated.json  hand-written relocated-API entries (Blizzard's own guide and shims cover the rest)
sources/classic-usage.json  globals the classic add-ons on disk call (`classic-scan`)
tools/apidoc.py       the command-line tool
tools/test_probe.py   runs the probe in a stub client and checks it, then import/build/diff
sources/client-docs/  docs and UI-code leads per client build (gzipped JSON)
sources/web/          web leads you add by hand (format below)
dumps/<build>/        each imported in-game dump (gzipped JSON); diffs compare these
docs/                 the generated docs: index.md, systems/, events.md, enums.md, widgets/, cvars.md, api.json,
                      relocated.md + compat.json (classic -> Forever), checks.md (reported quirks)
site/                 the generated website (open site/index.html; source in tools/site_src/)
luals/                the generated VS Code definitions (see below)
```

## Website

`build` also writes `site/`: open `site/index.html` straight from disk in any browser (no server needed). It has a
search box (press `/`), a page per system with every function's signature, Blizzard's flags and what the game
returned out of and in combat, plus events (filter by seen firing or protected), enums and structures, widgets with
their methods, undocumented globals, CVars and a restrictions page. Type names in signatures link to their
definitions. The page source lives in `tools/site_src/`; `tools/website.py` writes the data file.

## Moved from classic

`build` writes `docs/relocated.md`, `docs/compat.json` and the site's **Moved from classic** page: each classic
(1.15) global that's gone on Forever or only kept alive by a Blizzard shim, where it went, and how the arguments
and returns changed. The mappings come from, in order of trust: Blizzard's 11.0 spell book transition guide and
its deprecation add-ons (both ship in the client and are read by `extract`), `sources/relocated.json`, and a
same-named `C_` function (marked as a lead). Every old and new name is checked against the in-game dump. Which
classic names to look at comes from those sources plus what the classic add-ons on disk call:

```
python tools/apidoc.py classic-scan                    # Maro's local copies of Questie and AtlasLoot
python tools/apidoc.py classic-scan <folder> <folder>  # any other add-ons
```

Forever's `WOW_PROJECT_ID` is 18 (`WOW_PROJECT_CAMELOT`), and it loads Blizzard's mainline shims, not the classic
ones: the page says so at the top.

## VS Code

`build` also writes `luals/` (and `release` zips it as `ForeverAPI-LuaLS-<build>.zip`): definitions for the Lua
extension by sumneko (LuaLS). Every function, event, enum
and structure from Blizzard's docs plus what the game has undocumented, each with what the probes saw: verified,
always secret, secret in combat or in a given situation, protected, forbidden. Classic names that are gone on
Forever are declared deprecated (VS Code strikes them through) with where they went. To use it, unzip
`ForeverAPI-LuaLS` into your workspace and copy its `.luarc.json` to the workspace root, or add its `library` folder
to `Lua.workspace.library` in VS Code's settings. Lua 5.1.

## Maintaining it (Maro)

Two double-click files in this folder:

- **update-docs.bat**: after you `/reload` or log out, imports what ForeverAPI Probe saved, rebuilds `docs/`, the
  website and the VS Code definitions, commits, and pushes (GitHub Pages republishes the site).
- **refresh-addons.bat**: after a client patch, or after the game crashed with an API add-on running. It re-reads
  Blizzard's docs and the crash logs (any call that crashed goes on the skip list) and copies fresh add-ons into
  the game. Restart the game afterwards.

Both need Python 3 on PATH. Nothing else is needed for them (the stub tests need `lupa`, contributions in the
compact format need `cbor2`).

Contributions:

```
python tools/apidoc.py contrib --github --dry-run   # what it would do with the open "API data" issues
python tools/apidoc.py contrib --github             # file them, thank each sender, close the issues
python tools/apidoc.py contrib <file> --as <name>   # file one from a file (sent some other way)
python tools/apidoc.py build                        # the site shows them as reported
```

Releasing the add-on: bump `## Version` in `addon/ForeverAPIProbe/ForeverAPIProbe.toc`, run
`python tools/apidoc.py release`, and attach both zips in `dist/` to a GitHub release.

## Use

```
python tools/apidoc.py extract    # after a client patch: re-read Blizzard's docs, regenerate leads.lua
python tools/apidoc.py deploy     # copy ForeverAPI Probe into _forever_/Interface/AddOns (removes the old Api* add-ons)
# in game: see CHECKLIST.md
python tools/apidoc.py import     # read WTF/Account/*/SavedVariables/ForeverAPIProbe.lua into dumps/
python tools/apidoc.py build      # write docs/
python tools/apidoc.py diff       # compare the last two dumps -> docs/changes/
python tools/apidoc.py diff A B   # compare any two dumps or client-doc extracts
python tools/test_probe.py        # stub-client checks (needs lupa)
```

After a client patch: `extract`, `deploy`, run the probe once (it re-dumps by itself on a new build), `import`,
`build`, `diff`. The diff shows added, removed and changed globals, namespace members, widget methods, events,
CVars and call results.

## The probe

`/fapi probe` shows status. `dump` re-runs the dump (it also runs by itself 5 seconds after login whenever the build,
probe version or leads change). `calls` calls every getter out of combat now and arms a second run for your next
combat. `events on|off` toggles the live event counter (on by default). `reset` clears everything.

What it never does: store a return value, an event argument, a string global's text or a CVar's current value (only
types, kinds and defaults, so no character, chat or account data reaches the file); compare or print a secret value
(only `issecretvalue` touches them); call anything that isn't named like a getter (`Get`, `Is`, `Has`, `Can`,
`Should`, `Are`, `Does`, `Unit`, `Num`), anything Blizzard marks protected, anything with `Reward` or `Request` in its
name, or getters Blizzard's own Lua UI defines. It records any `ADDON_ACTION_BLOCKED`/`FORBIDDEN` naming itself,
with the call it was making.

Globals written by other add-ons (per `issecurevariable`) are left out of the API and counted by add-on, so the dump
works with your normal add-ons on. Namespace members an add-on replaced are flagged.

How it tells built-in API from Lua: `tostring` showing `builtin` if this client does that, else `string.dump` if it
exists, else Blizzard's own UI code (anything its Lua defines is a UI helper). The docs' Lua page shows which
the client allowed.

## Web leads

Put a JSON file in `sources/web/`:

```json
{ "site": "warcraft.wiki.gg", "url": "https://warcraft.wiki.gg/wiki/World_of_Warcraft_API", "retrieved": "2026-11-07",
  "items": { "GetItemInfo": { "text": "Returns info for an item.", "url": "https://warcraft.wiki.gg/wiki/API_GetItemInfo" } },
  "events": ["SOME_EVENT_TO_CHECK"] }
```

`items` text appears under the matching function as "Web lead (unverified)". `events` are added to the names the
probe checks (run `extract` and redeploy).

## Not covered yet

- Behaviour that needs arguments (getters with required non-unit arguments, setters, secret-value handling by widget
  setters). Those need targeted probes, like the suite's HealProbe; their findings could be fed in the same way as
  web leads.
- A web scraper. The client's own generated docs cover this build better than any wiki; web text would mostly add
  descriptions for legacy globals Blizzard never documented.
