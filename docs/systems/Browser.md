# Browser

Namespace: `C_Browser`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Browser.CloseFullscreenBrowser](#c_browserclosefullscreenbrowser) |  |  |

### C_Browser.CloseFullscreenBrowser

`C_Browser.CloseFullscreenBrowser()`

- Status: ✅ verified (function)
- Source: client docs `BrowserDocumentation.lua`

## Events

### FULLSCREEN_BROWSER_SPINNER_HIDE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### FULLSCREEN_BROWSER_SPINNER_SHOW

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SIMPLE_BROWSER_POPUP

- Status: ✅ verified
- Payload: `url: string`
- fires synchronously (Blizzard's docs)

### SIMPLE_BROWSER_SOCIAL_CALLBACK_INVOKED

- Status: ✅ verified
- Payload: `url: string`
- unique event (Blizzard's docs)

### SIMPLE_BROWSER_WEB_ERROR

- Status: ✅ verified
- Payload: `errorCode: number`
- fires synchronously (Blizzard's docs)

### SIMPLE_BROWSER_WEB_PROXY_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SIMPLE_CHECKOUT_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
