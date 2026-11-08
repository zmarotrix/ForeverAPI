# Movie

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [CancelPreloadingMovie](#cancelpreloadingmovie) |  |  |
| ✅ | [GetMovieDownloadProgress](#getmoviedownloadprogress) |  |  |
| ✅ | [IsMovieLocal](#ismovielocal) |  |  |
| ✅ | [IsMoviePlayable](#ismovieplayable) |  |  |
| ✅ | [IsMovieReadable](#ismoviereadable) |  |  |
| ✅ | [PreloadMovie](#preloadmovie) |  |  |

### CancelPreloadingMovie

`CancelPreloadingMovie(movieId: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MovieDocumentation.lua`

### GetMovieDownloadProgress

`GetMovieDownloadProgress(movieId: number) → inProgress: bool, downloaded: BigUInteger, total: BigUInteger`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MovieDocumentation.lua`

### IsMovieLocal

`IsMovieLocal(movieId: number) → isLocal: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MovieDocumentation.lua`

### IsMoviePlayable

`IsMoviePlayable(movieId: number) → isPlayable: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MovieDocumentation.lua`

### IsMovieReadable

`IsMovieReadable(movieId: number) → readable: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MovieDocumentation.lua`

### PreloadMovie

`PreloadMovie(movieId: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MovieDocumentation.lua`
