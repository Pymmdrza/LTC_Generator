@Echo off
title LTC P2PKH .PY
Pushd "%~dp0"
:loop
python P2PKH.py
goto loop
