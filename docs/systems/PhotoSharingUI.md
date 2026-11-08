# PhotoSharingUI

Namespace: `C_PhotoSharing`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PhotoSharing.BeginAuthorizationFlow](#c_photosharingbeginauthorizationflow) |  |  |
| ✅ | [C_PhotoSharing.ClearAuthorization](#c_photosharingclearauthorization) |  |  |
| ✅ | [C_PhotoSharing.CompleteAuthorizationFlow](#c_photosharingcompleteauthorizationflow) |  |  |
| ✅ | [C_PhotoSharing.GetCropRatio](#c_photosharinggetcropratio) | 1 value |  |
| ✅ | [C_PhotoSharing.GetPhotoSharingAuthURL](#c_photosharinggetphotosharingauthurl) | 1 value |  |
| ✅ | [C_PhotoSharing.GetStatus](#c_photosharinggetstatus) | 1 value |  |
| ✅ | [C_PhotoSharing.IsAuthorized](#c_photosharingisauthorized) | 1 value |  |
| ✅ | [C_PhotoSharing.IsEnabled](#c_photosharingisenabled) | 1 value |  |
| ✅ | [C_PhotoSharing.SetScreenshotPreviewTexture](#c_photosharingsetscreenshotpreviewtexture) |  |  |
| ✅ | [C_PhotoSharing.TakePhoto](#c_photosharingtakephoto) |  |  |
| ✅ | [C_PhotoSharing.UploadPhotoToService](#c_photosharinguploadphototoservice) |  |  |

### C_PhotoSharing.BeginAuthorizationFlow

`C_PhotoSharing.BeginAuthorizationFlow()`

- Status: ✅ verified (function)
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.ClearAuthorization

`C_PhotoSharing.ClearAuthorization()`

- Status: ✅ verified (function)
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.CompleteAuthorizationFlow

`C_PhotoSharing.CompleteAuthorizationFlow(callbackURL: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.GetCropRatio

`C_PhotoSharing.GetCropRatio() → cropRatio: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.GetPhotoSharingAuthURL

`C_PhotoSharing.GetPhotoSharingAuthURL() → authUrl: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.GetStatus

`C_PhotoSharing.GetStatus() → status: PhotoSharingStatus`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.IsAuthorized

`C_PhotoSharing.IsAuthorized() → authorized: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.IsEnabled

`C_PhotoSharing.IsEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.SetScreenshotPreviewTexture

`C_PhotoSharing.SetScreenshotPreviewTexture(textureObject: SimpleTexture)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.TakePhoto

`C_PhotoSharing.TakePhoto()`

- Status: ✅ verified (function)
- Source: client docs `PhotoSharingUIDocumentation.lua`

### C_PhotoSharing.UploadPhotoToService

`C_PhotoSharing.UploadPhotoToService(optionalTitle: cstring = , optionalDescription: cstring = )`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PhotoSharingUIDocumentation.lua`

## Events

### PHOTO_SHARING_AUTHORIZATION_NEEDED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PHOTO_SHARING_AUTHORIZATION_UPDATED

- Status: ✅ verified
- Payload: `showNotification: bool`
- fires synchronously (Blizzard's docs)

### PHOTO_SHARING_PHOTO_UPLOAD_STATUS

- Status: ✅ verified
- Payload: `uploadStatus: PhotoSharingUploadStatus`
- fires synchronously (Blizzard's docs)

### PHOTO_SHARING_SCREENSHOT_READY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PHOTO_SHARING_THIRD_PARTY_AUTHORIZATION_NEEDED

- Status: ✅ verified
- Payload: `authUrl: string`
- fires synchronously (Blizzard's docs)
