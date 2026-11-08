# Cinematic

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [CinematicFinished](#cinematicfinished) |  |  |
| ✅ | [CinematicStarted](#cinematicstarted) |  |  |
| ✅ | [GetCurrentCinematicSummary](#getcurrentcinematicsummary) |  |  |
| ✅ | [InCinematic](#incinematic) |  |  |
| ✅ | [MouseOverrideCinematicDisable](#mouseoverridecinematicdisable) |  |  |
| ✅ | [OpeningCinematic](#openingcinematic) |  |  |
| ✅ | [StopCinematic](#stopcinematic) |  |  |

### CinematicFinished

`CinematicFinished(movieType: CinematicType, userCanceled: bool = False, didError: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CinematicDocumentation.lua`

### CinematicStarted

`CinematicStarted(movieType: CinematicType, movieID: number, canCancel: bool = True)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CinematicDocumentation.lua`

### GetCurrentCinematicSummary

`GetCurrentCinematicSummary() → summary: cstring`

- Status: ✅ verified (function)
- Source: client docs `CinematicDocumentation.lua`

### InCinematic

`InCinematic() → inCinematic: bool`

- Status: ✅ verified (function)
- Source: client docs `CinematicDocumentation.lua`

### MouseOverrideCinematicDisable

`MouseOverrideCinematicDisable(doOverride: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CinematicDocumentation.lua`

### OpeningCinematic

`OpeningCinematic()`

- Status: ✅ verified (function)
- Source: client docs `CinematicDocumentation.lua`

### StopCinematic

`StopCinematic()`

- Status: ✅ verified (function)
- Source: client docs `CinematicDocumentation.lua`

## Events

### CINEMATIC_START

- Status: ✅ verified
- Payload: `canBeCancelled: bool`, `forcedAspectRatio: CameraModeAspectRatio`
- fires synchronously (Blizzard's docs)

### CINEMATIC_STOP

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HIDE_SUBTITLE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAY_MOVIE

- Status: ✅ verified
- Payload: `movieID: number`
- fires synchronously (Blizzard's docs)

### SHOW_SUBTITLE

- Status: ✅ verified
- Payload: `subtitle: cstring`, `sender: cstring?`
- fires synchronously (Blizzard's docs)

### STOP_MOVIE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
