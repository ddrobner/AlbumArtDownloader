py -3 -m pip install venv
py -3 -m venv %~dp0
%~dp0\activate.bat
py -3 -m pip install -r requirements.txt