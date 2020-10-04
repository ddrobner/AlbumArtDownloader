py -3 -m pip install venv
py -3 -m venv %~dp0\venv
%~dp0\venv\activate.bat
pip install -r requirements.txt
