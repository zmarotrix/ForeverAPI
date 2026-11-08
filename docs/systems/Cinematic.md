# Cinematic

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [CinematicFinished](#cinematicfinished) |  |  |
| ❔ | [CinematicStarted](#cinematicstarted) |  |  |
| ❔ | [GetCurrentCinematicSummary](#getcurrentcinematicsummary) |  |  |
| ❔ | [InCinematic](#incinematic) |  |  |
| ❔ | [MouseOverrideCinematicDisable](#mouseoverridecinematicdisable) |  |  |
| ❔ | [OpeningCinematic](#openingcinematic) |  |  |
| ❔ | [StopCinematic](#stopcinematic) |  |  |

### CinematicFinished

`CinematicFinished(movieType: CinematicType, userCanceled: bool = False, didError: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CinematicDocumentation.lua`

### CinematicStarted

`CinematicStarted(movieType: CinematicType, movieID: number, canCancel: bool = True)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CinematicDocumentation.lua`

### GetCurrentCinematicSummary

`GetCurrentCinematicSummary() → summary: cstring`

- Status: ❔ unverified
- Source: client docs `CinematicDocumentation.lua`

### InCinematic

`InCinematic() → inCinematic: bool`

- Status: ❔ unverified
- Source: client docs `CinematicDocumentation.lua`

### MouseOverrideCinematicDisable

`MouseOverrideCinematicDisable(doOverride: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CinematicDocumentation.lua`

### OpeningCinematic

`OpeningCinematic()`

- Status: ❔ unverified
- Source: client docs `CinematicDocumentation.lua`

### StopCinematic

`StopCinematic()`

- Status: ❔ unverified
- Source: client docs `CinematicDocumentation.lua`

## Events

### CINEMATIC_START

- Status: ❔ unverified
- Payload: `canBeCancelled: bool`, `forcedAspectRatio: CameraModeAspectRatio`
- fires synchronously (Blizzard's docs)

### CINEMATIC_STOP

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### HIDE_SUBTITLE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAY_MOVIE

- Status: ❔ unverified
- Payload: `movieID: number`
- fires synchronously (Blizzard's docs)

### SHOW_SUBTITLE

- Status: ❔ unverified
- Payload: `subtitle: cstring`, `sender: cstring?`
- fires synchronously (Blizzard's docs)

### STOP_MOVIE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
