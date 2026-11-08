@echo off
rem After you /reload or log out: imports what the API add-ons collected in game, rebuilds the docs,
rem commits them and publishes the website. Does nothing if the game hasn't saved anything new.
rem Needs Python 3 (python on PATH).
cd /d "%~dp0"
python tools\update.py %* || goto failed
echo.
pause
exit /b 0

:failed
echo.
echo Something went wrong (see above). Nothing was published.
pause
exit /b 1
