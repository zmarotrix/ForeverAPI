# PhotoSharingUI

Namespace: `C_PhotoSharing`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_PhotoSharing.BeginAuthorizationFlow](#c_photosharingbeginauthorizationflow) |  |  |
| ❔ | [C_PhotoSharing.ClearAuthorization](#c_photosharingclearauthorization) |  |  |
| ❔ | [C_PhotoSharing.CompleteAuthorizationFlow](#c_photosharingcompleteauthorizationflow) |  |  |
| ❔ | [C_PhotoSharing.GetCropRatio](#c_photosharinggetcropratio) |  |  |
| ❔ | [C_PhotoSharing.GetPhotoSharingAuthURL](#c_photosharinggetphotosharingauthurl) |  |  |
| ❔ | [C_PhotoSharing.GetStatus](#c_photosharinggetstatus) |  |  |
| ❔ | [C_PhotoSharing.IsAuthorized](#c_photosharingisauthorized) |  |  |
| ❔ | [C_PhotoSharing.IsEnabled](#c_photosharingisenabled) |  |  |
| ❔ | [C_PhotoSharing.SetScreenshotPreviewTexture](#c_photosharingsetscreenshotpreviewtexture) |  |  |
| ❔ | [C_PhotoSharing.TakePhoto](#c_photosharingtakephoto) |  |  |
| ❔ | [C_PhotoSharing.UploadPhotoToService](#c_photosharinguploadphototoservice) |  |  |

### C_PhotoSharing.BeginAuthorizationFlow

`C_PhotoSharing.BeginAuthorizationFlow()`

- Status: ❔ unverified
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.ClearAuthorization

`C_PhotoSharing.ClearAuthorization()`

- Status: ❔ unverified
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.CompleteAuthorizationFlow

`C_PhotoSharing.CompleteAuthorizationFlow(callbackURL: cstring)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.GetCropRatio

`C_PhotoSharing.GetCropRatio() → cropRatio: number`

- Status: ❔ unverified
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.GetPhotoSharingAuthURL

`C_PhotoSharing.GetPhotoSharingAuthURL() → authUrl: cstring`

- Status: ❔ unverified
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.GetStatus

`C_PhotoSharing.GetStatus() → status: PhotoSharingStatus`

- Status: ❔ unverified
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.IsAuthorized

`C_PhotoSharing.IsAuthorized() → authorized: bool`

- Status: ❔ unverified
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.IsEnabled

`C_PhotoSharing.IsEnabled() → enabled: bool`

- Status: ❔ unverified
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.SetScreenshotPreviewTexture

`C_PhotoSharing.SetScreenshotPreviewTexture(textureObject: SimpleTexture)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.TakePhoto

`C_PhotoSharing.TakePhoto()`

- Status: ❔ unverified
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.UploadPhotoToService

`C_PhotoSharing.UploadPhotoToService(optionalTitle: cstring = , optionalDescription: cstring = )`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PhotoSharingUIDocumentation.lua`

## Events

### PHOTO_SHARING_AUTHORIZATION_NEEDED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PHOTO_SHARING_AUTHORIZATION_UPDATED

- Status: ❔ unverified
- Payload: `showNotification: bool`
- fires synchronously (Blizzard's docs)

### PHOTO_SHARING_PHOTO_UPLOAD_STATUS

- Status: ❔ unverified
- Payload: `uploadStatus: PhotoSharingUploadStatus`
- fires synchronously (Blizzard's docs)

### PHOTO_SHARING_SCREENSHOT_READY

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PHOTO_SHARING_THIRD_PARTY_AUTHORIZATION_NEEDED

- Status: ❔ unverified
- Payload: `authUrl: string`
- fires synchronously (Blizzard's docs)
