@echo off
schtasks /delete /tn "Nod32 Update Key" /f
schtasks /create /sc WEEKLY /mo 2  /st 00:00:00 /tn "Nod32 Update Key" /tr "\"%~dp0nod32keys.bat"\" /ru System && (
pause
exit
)
