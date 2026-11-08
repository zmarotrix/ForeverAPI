# ReportSystem

Namespace: `C_ReportSystem`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ReportSystem.CanReportPlayer](#c_reportsystemcanreportplayer) |  |  |
| ✅ | [C_ReportSystem.CanReportPlayerForLanguage](#c_reportsystemcanreportplayerforlanguage) |  |  |
| ✅ | [C_ReportSystem.GetMajorCategoriesForReportType](#c_reportsystemgetmajorcategoriesforreporttype) |  |  |
| ✅ | [C_ReportSystem.GetMajorCategoryString](#c_reportsystemgetmajorcategorystring) |  |  |
| ✅ | [C_ReportSystem.GetMinorCategoriesForReportTypeAndMajorCategory](#c_reportsystemgetminorcategoriesforreporttypeandmajorcategory) |  |  |
| ✅ | [C_ReportSystem.GetMinorCategoryString](#c_reportsystemgetminorcategorystring) |  |  |
| ✅ | [C_ReportSystem.ReportServerLag](#c_reportsystemreportserverlag) |  |  |
| ✅ | [C_ReportSystem.ReportStuckInCombat](#c_reportsystemreportstuckincombat) |  |  |
| ✅ | [C_ReportSystem.RequiresScreenshotForReportType](#c_reportsystemrequiresscreenshotforreporttype) |  |  |
| ✅ | [C_ReportSystem.SendReport](#c_reportsystemsendreport) |  |  |
| ✅ | [C_ReportSystem.SetScreenshotPreviewTexture](#c_reportsystemsetscreenshotpreviewtexture) |  |  |
| ✅ | [C_ReportSystem.TakeReportScreenshot](#c_reportsystemtakereportscreenshot) |  |  |

### C_ReportSystem.CanReportPlayer

`C_ReportSystem.CanReportPlayer(playerLocation: PlayerLocation) → canReport: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.CanReportPlayerForLanguage

`C_ReportSystem.CanReportPlayerForLanguage(playerLocation: PlayerLocation) → canReport: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.GetMajorCategoriesForReportType

`C_ReportSystem.GetMajorCategoriesForReportType(reportType: ReportType) → majorCategories: ReportMajorCategory[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.GetMajorCategoryString

`C_ReportSystem.GetMajorCategoryString(majorCategory: ReportMajorCategory) → majorCategoryString: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.GetMinorCategoriesForReportTypeAndMajorCategory

`C_ReportSystem.GetMinorCategoriesForReportTypeAndMajorCategory(reportType: ReportType, majorCategory: ReportMajorCategory) → minorCategories: ReportMinorCategory[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.GetMinorCategoryString

`C_ReportSystem.GetMinorCategoryString(minorCategory: ReportMinorCategory) → minorCategoryString: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.ReportServerLag

`C_ReportSystem.ReportServerLag()`

- Status: ✅ verified (function)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.ReportStuckInCombat

`C_ReportSystem.ReportStuckInCombat()`

- Status: ✅ verified (function)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.RequiresScreenshotForReportType

`C_ReportSystem.RequiresScreenshotForReportType(reportType: ReportType, majorCategory: ReportMajorCategory) → requiresScreenshot: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.SendReport

`C_ReportSystem.SendReport(reportInfo: ReportInfo, playerLocation: PlayerLocation?)`

- Status: ✅ verified (function)
- Blizzard: Not allowed to be called by addons
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.SetScreenshotPreviewTexture

`C_ReportSystem.SetScreenshotPreviewTexture(textureObject: SimpleTexture)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReportSystemDocumentation.lua`

### C_ReportSystem.TakeReportScreenshot

`C_ReportSystem.TakeReportScreenshot()`

- Status: ✅ verified (function)
- Source: client docs `ReportSystemDocumentation.lua`

## Events

### REPORT_PLAYER_RESULT

- Status: ✅ verified
- Payload: `result: SendReportResult`, `reportType: ReportType`
- fires synchronously (Blizzard's docs)

### REPORT_SCREENSHOT_READY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
