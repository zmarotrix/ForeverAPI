@echo off
rem After a client patch, or after the game crashed while an API add-on was running:
rem re-reads Blizzard's docs from the client, reads the crash logs (any call that crashed goes on the skip list),
rem and copies fresh API add-ons into the game. Restart the game afterwards.
cd /d "%~dp0"
echo Reading Blizzard's docs and the crash logs from the client...
python tools\apidoc.py extract || goto failed
echo.
echo Copying the API add-ons into the game...
python tools\apidoc.py deploy || goto failed
echo.
echo Done. Restart the game (not just /reload) so it loads the new add-ons.
pause
exit /b 0

:failed
echo.
echo Something went wrong (see above). Close the game first if a file was locked.
pause
exit /b 1
