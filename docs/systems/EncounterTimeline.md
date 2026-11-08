# EncounterTimeline

Namespace: `C_EncounterTimeline`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_EncounterTimeline.AddEditModeEvents](#c_encountertimelineaddeditmodeevents) |  |  |
| ✅ | [C_EncounterTimeline.AddScriptEvent](#c_encountertimelineaddscriptevent) |  |  |
| ✅ | [C_EncounterTimeline.CancelAllScriptEvents](#c_encountertimelinecancelallscriptevents) | 0 values |  |
| ✅ | [C_EncounterTimeline.CancelEditModeEvents](#c_encountertimelinecanceleditmodeevents) | 0 values |  |
| ✅ | [C_EncounterTimeline.CancelScriptEvent](#c_encountertimelinecancelscriptevent) |  |  |
| ✅ | [C_EncounterTimeline.FinishScriptEvent](#c_encountertimelinefinishscriptevent) |  |  |
| ✅ | [C_EncounterTimeline.GetCurrentTime](#c_encountertimelinegetcurrenttime) | 1 value |  |
| ✅ | [C_EncounterTimeline.GetEventColor](#c_encountertimelinegeteventcolor) |  |  |
| ✅ | [C_EncounterTimeline.GetEventCountBySource](#c_encountertimelinegeteventcountbysource) |  |  |
| ✅ | [C_EncounterTimeline.GetEventHighlightTime](#c_encountertimelinegeteventhighlighttime) | 1 value |  |
| ✅ | [C_EncounterTimeline.GetEventInfo](#c_encountertimelinegeteventinfo) |  |  |
| ✅ | [C_EncounterTimeline.GetEventList](#c_encountertimelinegeteventlist) | 1 value |  |
| ✅ | [C_EncounterTimeline.GetEventState](#c_encountertimelinegeteventstate) |  |  |
| ✅ | [C_EncounterTimeline.GetEventTimeElapsed](#c_encountertimelinegeteventtimeelapsed) |  |  |
| ✅ | [C_EncounterTimeline.GetEventTimeRemaining](#c_encountertimelinegeteventtimeremaining) |  |  |
| ✅ | [C_EncounterTimeline.GetEventTimer](#c_encountertimelinegeteventtimer) |  |  |
| ✅ | [C_EncounterTimeline.GetEventTrack](#c_encountertimelinegeteventtrack) |  |  |
| ✅ | [C_EncounterTimeline.GetSortedEventList](#c_encountertimelinegetsortedeventlist) | 1 value |  |
| ✅ | [C_EncounterTimeline.GetTrackInfo](#c_encountertimelinegettrackinfo) |  |  |
| ✅ | [C_EncounterTimeline.GetTrackList](#c_encountertimelinegettracklist) | 1 value |  |
| ✅ | [C_EncounterTimeline.GetTrackMaxEventDuration](#c_encountertimelinegettrackmaxeventduration) |  |  |
| ✅ | [C_EncounterTimeline.GetTrackType](#c_encountertimelinegettracktype) |  |  |
| ✅ | [C_EncounterTimeline.GetViewType](#c_encountertimelinegetviewtype) | 1 value |  |
| ✅ | [C_EncounterTimeline.HasActiveEvents](#c_encountertimelinehasactiveevents) | 1 value |  |
| ✅ | [C_EncounterTimeline.HasAnyEvents](#c_encountertimelinehasanyevents) | 1 value |  |
| ✅ | [C_EncounterTimeline.HasPausedEvents](#c_encountertimelinehaspausedevents) | 1 value |  |
| ✅ | [C_EncounterTimeline.HasVisibleEvents](#c_encountertimelinehasvisibleevents) | 1 value |  |
| ✅ | [C_EncounterTimeline.IsEventBlocked](#c_encountertimelineiseventblocked) |  |  |
| ✅ | [C_EncounterTimeline.IsFeatureAvailable](#c_encountertimelineisfeatureavailable) | 1 value |  |
| ✅ | [C_EncounterTimeline.IsFeatureEnabled](#c_encountertimelineisfeatureenabled) | 1 value |  |
| ✅ | [C_EncounterTimeline.PauseScriptEvent](#c_encountertimelinepausescriptevent) |  |  |
| ✅ | [C_EncounterTimeline.ResumeScriptEvent](#c_encountertimelineresumescriptevent) |  |  |
| ✅ | [C_EncounterTimeline.SetEventIconTextures](#c_encountertimelineseteventicontextures) |  |  |
| ✅ | [C_EncounterTimeline.SetViewType](#c_encountertimelinesetviewtype) |  |  |

### C_EncounterTimeline.AddEditModeEvents

`C_EncounterTimeline.AddEditModeEvents() → loopTimerDuration: Seconds`

- Status: ✅ verified (function)
- Blizzard: Adds a predefined set of events to the timeline for display in Edit Mode.
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.AddScriptEvent

`C_EncounterTimeline.AddScriptEvent(eventInfo: EncounterTimelineScriptEventRequest) → eventID: EncounterTimelineEventID`

- Status: ✅ verified (function)
- Blizzard: Adds a custom event to the timeline.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.CancelAllScriptEvents

`C_EncounterTimeline.CancelAllScriptEvents()`

- Status: ✅ verified (function)
- Blizzard: Cancels all custom timeline events, removing them from the timeline.
- Called out of combat: returned 0 values
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.CancelEditModeEvents

`C_EncounterTimeline.CancelEditModeEvents()`

- Status: ✅ verified (function)
- Blizzard: Removes all Edit Mode events from the timeline.
- Called out of combat: returned 0 values
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.CancelScriptEvent

`C_EncounterTimeline.CancelScriptEvent(eventID: EncounterTimelineEventID)`

- Status: ✅ verified (function)
- Blizzard: Cancels a custom timeline event, removing it from the timeline.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.FinishScriptEvent

`C_EncounterTimeline.FinishScriptEvent(eventID: EncounterTimelineEventID)`

- Status: ✅ verified (function)
- Blizzard: Finishes a custom timeline event, removing it from the timeline.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetCurrentTime

`C_EncounterTimeline.GetCurrentTime() → currentTime: Seconds`

- Status: ✅ verified (function)
- Blizzard: Returns the current timestamp used for rendering the timeline display.
- Called out of combat: returned 1 value: `number`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetEventColor

`C_EncounterTimeline.GetEventColor(eventID: EncounterTimelineEventID, overrideTrigger: EncounterEventColorTrigger?) → color: colorRGBA`

- Status: ✅ verified (function)
- Blizzard: Returns the current color used to render timeline event.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- secret during encounter events (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetEventCountBySource

`C_EncounterTimeline.GetEventCountBySource(source: EncounterTimelineEventSource) → count: number`

- Status: ✅ verified (function)
- Blizzard: Returns the number of present events in the timeline by their source type.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetEventHighlightTime

`C_EncounterTimeline.GetEventHighlightTime() → highlightTime: Seconds`

- Status: ✅ verified (function)
- Blizzard: Returns the duration at which timeline events will be highlighted for imminency.
- Called out of combat: returned 1 value: `number`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetEventInfo

`C_EncounterTimeline.GetEventInfo(eventID: EncounterTimelineEventID) → info: EncounterTimelineEventInfo`

- Status: ✅ verified (function)
- Blizzard: Returns information about a timeline event. This data is generally expected to be static for the lifetime of an event.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- secret during encounter events (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetEventList

`C_EncounterTimeline.GetEventList() → events: EncounterTimelineEventID[]`

- Status: ✅ verified (function)
- Blizzard: Returns an unsorted list of event IDs present in the timeline.
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetEventState

`C_EncounterTimeline.GetEventState(eventID: EncounterTimelineEventID) → state: EncounterTimelineEventState`

- Status: ✅ verified (function)
- Blizzard: Returns the current state of a timeline event.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetEventTimeElapsed

`C_EncounterTimeline.GetEventTimeElapsed(eventID: EncounterTimelineEventID) → timeElapsed: Seconds`

- Status: ✅ verified (function)
- Blizzard: Returns the elapsed duration of a timeline event.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetEventTimeRemaining

`C_EncounterTimeline.GetEventTimeRemaining(eventID: EncounterTimelineEventID) → timeRemaining: Seconds`

- Status: ✅ verified (function)
- Blizzard: Returns the remaining duration of a timeline event.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetEventTimer

`C_EncounterTimeline.GetEventTimer(eventID: EncounterTimelineEventID) → duration: LuaDurationObject?`

- Status: ✅ verified (function)
- Blizzard: Returns a Duration object that tracks the elapsed duration of a timeline event. This object tracks the range [0, duration] of the event and automatically pauses its progression based on event state.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetEventTrack

`C_EncounterTimeline.GetEventTrack(eventID: EncounterTimelineEventID) → track: EncounterTimelineTrack, trackSortIndex: luaIndex?`

- Status: ✅ verified (function)
- Blizzard: Returns information about the position of an event on the timeline.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetSortedEventList

`C_EncounterTimeline.GetSortedEventList(maxEventCount: number?, maxEventDuration: Seconds?, excludeTerminalStates: bool = True, excludeHiddenEvents: bool = True) → events: EncounterTimelineEventID[]`

- Status: ✅ verified (function)
- Blizzard: Returns a sorted list of event IDs present in the timeline from shortest to longest remaining durations, meeting the requirements of the specified filters.
- `maxEventCount`: Maximum number of sorted events to return.
- `maxEventDuration`: Maximum duration of sorted events to return.
- `excludeTerminalStates`: If false, include events that are terminal states such as Canceled or Finished.
- `excludeHiddenEvents`: If false, include events that should be hidden by user configuration, such as events on long tracks when the user has opted to not show long countdowns.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetTrackInfo

`C_EncounterTimeline.GetTrackInfo(track: EncounterTimelineTrack) → trackInfo: EncounterTimelineTrackInfo`

- Status: ✅ verified (function)
- Blizzard: Returns information for a single timeline track.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetTrackList

`C_EncounterTimeline.GetTrackList() → tracks: EncounterTimelineTrackInfo[]`

- Status: ✅ verified (function)
- Blizzard: Returns information about all timeline tracks.
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table}`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetTrackMaxEventDuration

`C_EncounterTimeline.GetTrackMaxEventDuration(track: EncounterTimelineTrack) → maxEventDuration: Seconds`

- Status: ✅ verified (function)
- Blizzard: Returns the maximum permitted event duration on a single timeline track.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetTrackType

`C_EncounterTimeline.GetTrackType(track: EncounterTimelineTrack) → trackType: EncounterTimelineTrackType`

- Status: ✅ verified (function)
- Blizzard: Returns the type of a single timeline track.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.GetViewType

`C_EncounterTimeline.GetViewType() → viewType: EncounterTimelineViewType`

- Status: ✅ verified (function)
- Blizzard: Returns the current view type of the timeline.
- Called out of combat: returned 1 value: `number`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.HasActiveEvents

`C_EncounterTimeline.HasActiveEvents() → hasActiveEvents: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the timeline contains any events in the active state.
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.HasAnyEvents

`C_EncounterTimeline.HasAnyEvents() → hasAnyEvents: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the timeline contains any events in any state.
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.HasPausedEvents

`C_EncounterTimeline.HasPausedEvents() → hasPausedEvents: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the timeline contains any events in the paused state.
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.HasVisibleEvents

`C_EncounterTimeline.HasVisibleEvents() → hasVisibleEvents: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the timeline contains any events that are on visible tracks.
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.IsEventBlocked

`C_EncounterTimeline.IsEventBlocked(eventID: EncounterTimelineEventID) → blocked: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the event is in a 'blocked' state, where the cast for this event may not occur due to encounter conditions not being met.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.IsFeatureAvailable

`C_EncounterTimeline.IsFeatureAvailable() → isAvailable: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the encounter timeline feature is available on this client.
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.IsFeatureEnabled

`C_EncounterTimeline.IsFeatureEnabled() → isAvailableAndEnabled: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the encounter timeline feature has been enabled by the player. This function will always return false if the feature is not available.
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.PauseScriptEvent

`C_EncounterTimeline.PauseScriptEvent(eventID: EncounterTimelineEventID)`

- Status: ✅ verified (function)
- Blizzard: Pauses a custom timeline event, hiding it from the timeline. A paused event can later be resumed to show it again, or canceled.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.ResumeScriptEvent

`C_EncounterTimeline.ResumeScriptEvent(eventID: EncounterTimelineEventID)`

- Status: ✅ verified (function)
- Blizzard: Resumes a custom timeline event, showing it on the timeline again if it is currently paused.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.SetEventIconTextures

`C_EncounterTimeline.SetEventIconTextures(eventID: EncounterTimelineEventID, includeIcons: EncounterEventIconmask, textures: SimpleTexture[])`

- Status: ✅ verified (function)
- Blizzard: Updates a given vector of texture objects to reference art assets for icons associated with an event.
- `includeIcons`: Mask to apply to candidate icons. Any icon bits not present in this set will not be assigned to textures.
- `textures`: Array of texture objects to update. This will change the assigned atlases and alpha values of the region, applying secret aspects to protect the data.
- RequiresValidTimelineEvent (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

### C_EncounterTimeline.SetViewType

`C_EncounterTimeline.SetViewType(viewType: EncounterTimelineViewType)`

- Status: ✅ verified (function)
- Blizzard: Changes the view type for the timeline. This adjusts track layouts to be more appropriate for a specific mode and optimizes event processing.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterTimelineDocumentation.lua`

## Events

### ENCOUNTER_TIMELINE_EVENT_ADDED

- Status: ✅ verified
- Payload: `eventInfo: EncounterTimelineEventInfo`
- Blizzard: Fired when an event has been added to the timeline.
- secret during encounter events (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### ENCOUNTER_TIMELINE_EVENT_BLOCK_STATE_CHANGED

- Status: ✅ verified
- Payload: `eventID: EncounterTimelineEventID`
- Blizzard: Fired when an event has transitioned into or out of a 'blocked' status.
- unique event (Blizzard's docs)

### ENCOUNTER_TIMELINE_EVENT_COLOR_CHANGED

- Status: ✅ verified
- Payload: `eventID: EncounterTimelineEventID`
- Blizzard: Fired when an event has met a condition that should trigger a color change.
- unique event (Blizzard's docs)

### ENCOUNTER_TIMELINE_EVENT_HIGHLIGHT

- Status: ✅ verified
- Payload: `eventID: EncounterTimelineEventID`
- Blizzard: Fired when an event has met a condition that should trigger its highlight glow animation.
- unique event (Blizzard's docs)

### ENCOUNTER_TIMELINE_EVENT_REMOVED

- Status: ✅ verified
- Payload: `eventID: EncounterTimelineEventID`
- Blizzard: Fired when an event has been removed from the timeline. This is guaranteed to fire after an event has transitioned to a 'final' state such as Canceled or Finished, and will be delayed at least one game tick to allow for API queries to still access event data in OnUpdate scripts. This is fired post-removal of the event, and so queries using the supplied event ID will return nil.
- unique event (Blizzard's docs)

### ENCOUNTER_TIMELINE_EVENT_STATE_CHANGED

- Status: ✅ verified
- Payload: `eventID: EncounterTimelineEventID`
- Blizzard: Fired when an event has changed state.
- unique event (Blizzard's docs)

### ENCOUNTER_TIMELINE_EVENT_TRACK_CHANGED

- Status: ✅ verified
- Payload: `eventID: EncounterTimelineEventID`
- Blizzard: Fired when an event has changed track, or has been re-ordered within its existing track.
- unique event (Blizzard's docs)

### ENCOUNTER_TIMELINE_LAYOUT_UPDATED

- Status: ✅ verified
- Payload: none
- Blizzard: Fired when the layout of tracks on the timeline has been updated. This can include changes to the minimum or maximum durations of tracks.
- fires synchronously (Blizzard's docs)
- Seen firing 3 times (0 in combat); argument kinds: ``

### ENCOUNTER_TIMELINE_STATE_UPDATED

- Status: ✅ verified
- Payload: none
- Blizzard: Signaled when conditions controlling the visibility of the encounter timeline are updated.
- unique event (Blizzard's docs)

### ENCOUNTER_TIMELINE_VIEW_ACTIVATED

- Status: ✅ verified
- Payload: `viewType: EncounterTimelineViewType`
- Blizzard: Fired when a new timeline view is being activated. This is fired after a full layout and timeline data update, allowing the UI to immediately query the API and get usable results.
- fires synchronously (Blizzard's docs)

### ENCOUNTER_TIMELINE_VIEW_DEACTIVATED

- Status: ✅ verified
- Payload: `viewType: EncounterTimelineViewType`
- Blizzard: Fired when the current timeline view is being deactivated. The UI should clear all stored timeline event data and release all frames back to pools during this event.
- fires synchronously (Blizzard's docs)

## Types

### EncounterTimelineEventFilter

- Structure
  - `maxEventCount`: number?
  - `maxEventDuration`: Seconds?
  - `excludeTerminalStates`: bool
  - `excludeHiddenEvents`: bool

### EncounterTimelineEventInfo

- Structure
  - `id`: EncounterTimelineEventID
  - `source`: EncounterTimelineEventSource
  - `spellName`: string
  - `spellID`: number
  - `iconFileID`: fileID
  - `duration`: Seconds
  - `maxQueueDuration`: Seconds
  - `icons`: EncounterEventIconmask
  - `severity`: EncounterEventSeverity
  - `isApproximate`: bool

### EncounterTimelineScriptEventRequest

- Structure
  - `spellID`: number
  - `iconFileID`: fileID
  - `duration`: Seconds
  - `maxQueueDuration`: Seconds
  - `overrideName`: stringView
  - `icons`: EncounterEventIconmask?
  - `severity`: EncounterEventSeverity
  - `paused`: bool

### EncounterTimelineTrackInfo

- Structure
  - `id`: EncounterTimelineTrack
  - `type`: EncounterTimelineTrackType
  - `minimumDuration`: Seconds?
  - `maximumDuration`: Seconds?
  - `minimumEventIntroDuration`: Seconds?
  - `minimumEventGapDuration`: Seconds?
  - `maximumEventCount`: number?
  - `sortDirection`: EncounterTimelineEventSortDirection?
