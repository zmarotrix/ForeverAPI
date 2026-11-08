# SplashScreen

Namespace: `C_SplashScreen`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_SplashScreen.AcknowledgeSplash](#c_splashscreenacknowledgesplash) |  |  |
| ❔ | [C_SplashScreen.CanViewSplashScreen](#c_splashscreencanviewsplashscreen) |  |  |
| ❔ | [C_SplashScreen.RequestLatestSplashScreen](#c_splashscreenrequestlatestsplashscreen) |  |  |
| ❔ | [C_SplashScreen.SendSplashScreenActionLaunchedTelem](#c_splashscreensendsplashscreenactionlaunchedtelem) |  |  |
| ❔ | [C_SplashScreen.SendSplashScreenCloseTelem](#c_splashscreensendsplashscreenclosetelem) |  |  |

### C_SplashScreen.AcknowledgeSplash

`C_SplashScreen.AcknowledgeSplash()`

- Status: ❔ unverified
- Source: client docs `SplashScreenDocumentation.lua`

### C_SplashScreen.CanViewSplashScreen

`C_SplashScreen.CanViewSplashScreen() → canView: bool`

- Status: ❔ unverified
- Source: client docs `SplashScreenDocumentation.lua`

### C_SplashScreen.RequestLatestSplashScreen

`C_SplashScreen.RequestLatestSplashScreen(fromGameMenu: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SplashScreenDocumentation.lua`

### C_SplashScreen.SendSplashScreenActionLaunchedTelem

`C_SplashScreen.SendSplashScreenActionLaunchedTelem()`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `SplashScreenDocumentation.lua`

### C_SplashScreen.SendSplashScreenCloseTelem

`C_SplashScreen.SendSplashScreenCloseTelem()`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `SplashScreenDocumentation.lua`

## Events

### OPEN_SPLASH_SCREEN

- Status: ❔ unverified
- Payload: `info: SplashScreenInfo?`
- fires synchronously (Blizzard's docs)

## Types

### SplashScreenInfo

- Structure
  - `textureKit`: textureKit
  - `minDisplayCharLevel`: number
  - `minQuestDisplayLevel`: number
  - `soundKitID`: number
  - `allianceQuestID`: number?
  - `hordeQuestID`: number?
  - `header`: string
  - `topLeftFeatureTitle`: string
  - `topLeftFeatureDesc`: string
  - `bottomLeftFeatureTitle`: string
  - `bottomLeftFeatureDesc`: string
  - `rightFeatureTitle`: string
  - `rightFeatureDesc`: string
  - `shouldShowQuest`: bool
  - `screenType`: SplashScreenType
  - `gameMenuRequest`: bool
