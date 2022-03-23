@Echo off
title LTCALL MMDRZA.COM
Pushd "%~dp0"
pip install hdwallet
pip install colorama
pip install lxml
pip install requests
start P2PKH.bat
start P2SWH.bat
start P2WPKH.bat
:loop
python LTC_OFF_File.py
goto loop
