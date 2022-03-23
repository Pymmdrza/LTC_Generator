@Echo off
title LTC P2WPKH MMDRZA.CoM
Pushd "%~dp0"
:loop
python P2PKH.py
goto loop
