@echo off

TITLE nod32keys
::color 02
color F5

echo nod32keys & echo.

echo	     _____$$$$$$$$$$$$$$$$_____
echo	     ____4$$$$$$$$$$$$$$$$F____
echo	     ____4$$$$$$$$$$$$$$$$F____
echo	     ____$$$$"_"$$$$"_"$$$$_____
echo	     _____?$F___4$$F___4$"_____
echo	     ______$$___$$$$___$P______
echo	     ______4$$$$$"^$$$$$%_____
echo	     ________"$$$ee$$$"________
echo	     _4$$c_____*$$$$F4____.$$r_
echo	     _^$$$b______________e$$$"_
echo	     _d$$$$$e__________z$$$$$b_
echo	     4$$$*$$$$$c____.$$$$$*$$$r
echo	     _""____^*$$$be$$$*"____^"_
echo	     __________"$$$$"__________
echo	     ________.d$$P$$$b_________
echo	     _______d$$P___^$$$b_______
echo	     ___.ed$$$"______"$$$be.___
echo	     _$$$$$$P__________*$$$$$$_
echo	     4$$$$$P____________$$$$$$"
echo	     _"*$$$"____________^$$P___
echo	     ____""______________^"___
echo.
:=====================================================

ping -n 2 -w 500 ya.ru >nul || (
				echo does not internet
				pause
				exit
				)
			 
keyParsing.py

::====================================================

cd C:\Program Files\ESET\ESET NOD32 Antivirus\ || (
						   echo Nod32 not installing
						   pause
						   exit
						   )
egui.exe /Max

	"%~dp0program\nircmd.exe" sendkey ctrl down 
	"%~dp0program\nircmd.exe" sendkey u down
	"%~dp0program\nircmd.exe" sendkey ctrl up 
	"%~dp0program\nircmd.exe" sendkey u up 
	
(SetLocal EnableDelayedExpansion  
for /f "usebackq tokens=* delims=:" %%a in ("%~dp0\keys.txt") do ( 
	set "$o=%%a"
	if not "!$o!"=="!$o:Username=!" echo !$o:~9! | clip

						  			  )
 )
 
	"%~dp0program\nircmd.exe" sendkey ctrl down 
	"%~dp0program\nircmd.exe" sendkey v down
	"%~dp0program\nircmd.exe" sendkey ctrl up 
	"%~dp0program\nircmd.exe" sendkey v up 
	"%~dp0program\nircmd.exe" sendkey tab press

(SetLocal EnableDelayedExpansion  
for /f "usebackq tokens=* delims=:" %%a in ("%~dp0\keys.txt") do ( 
	set "$p=%%a"
	if not "!$p!"=="!$p:Password=!" echo !$p:~9! | clip
				 					  )
 )
 
	"%~dp0program\nircmd.exe" sendkey ctrl down 
	"%~dp0program\nircmd.exe" sendkey v down
	"%~dp0program\nircmd.exe" sendkey ctrl up 
	"%~dp0program\nircmd.exe" sendkey v up
	"%~dp0program\nircmd.exe" sendkey enter press

ecmd.exe /update && echo Nod32 update ok

	"%~dp0program\nircmd.exe" win hide ititle "ESET NOD32 Antivirus"
exit

