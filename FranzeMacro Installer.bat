@echo off
title FranzeMacro Installer
goto info

:info
cls
color 0b
echo FranzeMacro 1.1 is being installed, do not close this program!
cd %SystemDrive%
mkdir FranzeMacro
cd FranzeMacro
set cl=%cd%
powershell.exe Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/PacifiqSoftware/FranzeMacro/main/macro11.py' -Outfile 'macro11.py'
powershell.exe Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/PacifiqSoftware/FranzeMacro/main/franze_icon.ico' -Outfile 'franze_icon.ico'
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "%userprofile%\Desktop\FranzeMacro V1.1.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%userprofile%\Desktop\macro11.py" >> CreateShortcut.vbs
echo oLink.WorkingDirectory = "%cl%" >> CreateShortcut.vbs
echo oLink.Description = "FranzeMacro for Roblox" >> CreateShortcut.vbs
echo oLink.IconLocation = "%userprofile%\Desktop\franze_icon.ico" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript CreateShortcut.vbs
del CreateShortcut.vbs
cls
echo FranzeMacro 1.1 is being installed, do not close this program!
echo Cleaning up...
copy "macro11.py" "%userprofile%\Desktop"
copy "franze_icon.ico" "%userprofile%\Desktop"
attrib +h %userprofile%\Desktop\macro11.py
attrib +h %userprofile%\Desktop\franze_icon.ico
del macro11.py /Q
del franze_icon.ico /Q
cd %userprofile%\Desktop
attrib +h FranzeMacro
rmdir FranzeMacro /Q
echo Installation is finished!
echo Press any key to exit.
pause>nul