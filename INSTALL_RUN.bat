@Echo off
title LTCALL MMDRZA.COM
Pushd "%~dp0"
start P2PKH.bat
start P2SWH.bat
start P2WPKH.bat
:loop
python LTC_Off_File.py
goto loop
