@Echo off
title LTC P2WSH (MMDRZA.COM)
Pushd "%~dp0"
:loop
python P2WSH.py
goto loop
