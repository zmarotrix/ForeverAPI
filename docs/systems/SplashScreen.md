# SplashScreen

Namespace: `C_SplashScreen`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SplashScreen.AcknowledgeSplash](#c_splashscreenacknowledgesplash) |  |  |
| ✅ | [C_SplashScreen.CanViewSplashScreen](#c_splashscreencanviewsplashscreen) | 1 value | 1 value |
| ✅ | [C_SplashScreen.RequestLatestSplashScreen](#c_splashscreenrequestlatestsplashscreen) |  |  |
| ✅ | [C_SplashScreen.SendSplashScreenActionLaunchedTelem](#c_splashscreensendsplashscreenactionlaunchedtelem) |  |  |
| ✅ | [C_SplashScreen.SendSplashScreenCloseTelem](#c_splashscreensendsplashscreenclosetelem) |  |  |

### C_SplashScreen.AcknowledgeSplash

`C_SplashScreen.AcknowledgeSplash()`

- Status: ✅ verified (function)
- Source: client docs `SplashScreenDocumentation.lua`

### C_SplashScreen.CanViewSplashScreen

`C_SplashScreen.CanViewSplashScreen() → canView: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SplashScreenDocumentation.lua`

### C_SplashScreen.RequestLatestSplashScreen

`C_SplashScreen.RequestLatestSplashScreen(fromGameMenu: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SplashScreenDocumentation.lua`

### C_SplashScreen.SendSplashScreenActionLaunchedTelem

`C_SplashScreen.SendSplashScreenActionLaunchedTelem()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `SplashScreenDocumentation.lua`

### C_SplashScreen.SendSplashScreenCloseTelem

`C_SplashScreen.SendSplashScreenCloseTelem()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `SplashScreenDocumentation.lua`

## Events

### OPEN_SPLASH_SCREEN

- Status: ✅ verified
- Payload: `info: SplashScreenInfo?`
- fires synchronously (Blizzard's docs)
- Seen firing 17 times (0 in combat); argument kinds: `-`

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
