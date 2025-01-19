@echo off
echo loading MirosoftWinDB
echo installing local script packages
echo script.init@MirsosftPACKAGES(system54.init) >> PACKAGES.exe
powershell -command "java MirosoftWinDB.java"

:: VBS script to open .mwText files in VS Code
setlocal
cscript //nologo openInVSCode.vbs
endlocal

pause
