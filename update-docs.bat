@echo off
rem Reads what the API add-ons collected in game and rebuilds the docs and website, then opens the website.
rem Run it after you /reload or log out. Needs Python 3 (python on PATH).
cd /d "%~dp0"
echo Importing what the add-ons collected...
python tools\apidoc.py import || goto failed
echo.
echo Rebuilding the docs and website...
python tools\apidoc.py build || goto failed
echo.
echo Done. Opening the website.
start "" "%~dp0site\index.html"
pause
exit /b 0

:failed
echo.
echo Something went wrong (see above). Nothing was changed on the website.
pause
exit /b 1
