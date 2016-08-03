@echo off


cd C:\Program Files\ESET\ESET NOD32 Antivirus\ || (
						   echo Nod32 not installing
						   pause
						   exit
						   )

ecmd.exe /update && (
		      echo Nod32 update ok
		      pause
		      exit
		     )

