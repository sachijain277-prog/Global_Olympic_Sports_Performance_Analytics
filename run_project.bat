@echo off
py -m pip install -r requirements.txt
py src\data_prep.py
py app.py
pause
