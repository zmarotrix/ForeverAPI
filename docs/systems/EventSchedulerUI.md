# EventSchedulerUI

Namespace: `C_EventScheduler`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_EventScheduler.CanShowEvents](#c_eventschedulercanshowevents) |  |  |
| ❔ | [C_EventScheduler.ClearReminder](#c_eventschedulerclearreminder) |  |  |
| ❔ | [C_EventScheduler.GetActiveContinentName](#c_eventschedulergetactivecontinentname) |  |  |
| ❔ | [C_EventScheduler.GetEventUiMapID](#c_eventschedulergeteventuimapid) |  |  |
| ❔ | [C_EventScheduler.GetEventZoneName](#c_eventschedulergeteventzonename) |  |  |
| ❔ | [C_EventScheduler.GetOngoingEvents](#c_eventschedulergetongoingevents) |  |  |
| ❔ | [C_EventScheduler.GetScheduledEvents](#c_eventschedulergetscheduledevents) |  |  |
| ❔ | [C_EventScheduler.HasData](#c_eventschedulerhasdata) |  |  |
| ❔ | [C_EventScheduler.HasSavedReminders](#c_eventschedulerhassavedreminders) |  |  |
| ❔ | [C_EventScheduler.RequestEvents](#c_eventschedulerrequestevents) |  |  |
| ❔ | [C_EventScheduler.SetReminder](#c_eventschedulersetreminder) |  |  |

### C_EventScheduler.CanShowEvents

`C_EventScheduler.CanShowEvents() → canShow: bool`

- Status: ❔ unverified
- Blizzard: Returns true if there are any events eligible to show for the player.
- Source: client docs `EventSchedulerUIDocumentation.lua`

### C_EventScheduler.ClearReminder

`C_EventScheduler.ClearReminder(eventKey: string)`

- Status: ❔ unverified
- Blizzard: Clears reminder on a scheduled event. Must use endTime to identify which specific instance in the case of repeating ones.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EventSchedulerUIDocumentation.lua`

### C_EventScheduler.GetActiveContinentName

`C_EventScheduler.GetActiveContinentName() → name: string`

- Status: ❔ unverified
- Blizzard: Returns the name of the continent with current events
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `EventSchedulerUIDocumentation.lua`

### C_EventScheduler.GetEventUiMapID

`C_EventScheduler.GetEventUiMapID(areaPoiID: number) → uiMapID: number?`

- Status: ❔ unverified
- Blizzard: Will try to figure out a UiMap for an areaPOI.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EventSchedulerUIDocumentation.lua`

### C_EventScheduler.GetEventZoneName

`C_EventScheduler.GetEventZoneName(areaPoiID: number) → name: string?`

- Status: ❔ unverified
- Blizzard: Will try to figure out a map zone name for an areaPOI
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EventSchedulerUIDocumentation.lua`

### C_EventScheduler.GetOngoingEvents

`C_EventScheduler.GetOngoingEvents() → events: OngoingEventInfo[]`

- Status: ❔ unverified
- Blizzard: Will request data from the server on a throttle
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `EventSchedulerUIDocumentation.lua`

### C_EventScheduler.GetScheduledEvents

`C_EventScheduler.GetScheduledEvents() → events: ScheduledEventInfo[]`

- Status: ❔ unverified
- Blizzard: Will request data from the server on a throttle
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `EventSchedulerUIDocumentation.lua`

### C_EventScheduler.HasData

`C_EventScheduler.HasData() → hasData: bool`

- Status: ❔ unverified
- Blizzard: True if the server sent a list, even if the list had 0 events.
- Source: client docs `EventSchedulerUIDocumentation.lua`

### C_EventScheduler.HasSavedReminders

`C_EventScheduler.HasSavedReminders() → hasSavedReminders: bool`

- Status: ❔ unverified
- Blizzard: Returns whether there are any event reminders saved. Can include reminders that have expired since set and haven't gotten removed yet. Has to be called after cvars are loaded.
- Source: client docs `EventSchedulerUIDocumentation.lua`

### C_EventScheduler.RequestEvents

`C_EventScheduler.RequestEvents()`

- Status: ❔ unverified
- Blizzard: Requests events from the server, subject to throttle
- Source: client docs `EventSchedulerUIDocumentation.lua`

### C_EventScheduler.SetReminder

`C_EventScheduler.SetReminder(eventKey: string)`

- Status: ❔ unverified
- Blizzard: Sets reminder on a scheduled event. Must use endTime to identify which specific instance in the case of repeating ones.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EventSchedulerUIDocumentation.lua`

## Events

### EVENT_SCHEDULER_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### EventDisplayInfo

- Structure
  - `hideTimeLeft`: bool
  - `hideDescription`: bool
  - `overrideAtlas`: textureAtlas?
  - `overrideTooltipWidgetSetID`: number?

### OngoingEventInfo

- Structure
  - `areaPoiID`: number
  - `rewardsClaimed`: bool
  - `displayInfo`: EventDisplayInfo

### ScheduledEventInfo

- Structure
  - `eventKey`: string
  - `eventID`: number
  - `areaPoiID`: number
  - `startTime`: time_t
  - `endTime`: time_t
  - `duration`: time_t
  - `hasReminder`: bool
  - `rewardsClaimed`: bool
  - `displayInfo`: EventDisplayInfo
