@echo off
pip install virtualenv

cd /d "C:\Users\%USERNAME%\Desktop\New Projects\Nathan's\delegation_webhook"
python -m virtualenv venv

cd venv/scripts
call activate.bat

cd /d "C:\Users\%USERNAME%\Desktop\New Projects\Nathan's\delegation_webhook"
pip install -r requirements.txt

start cmd /k "C:\Users\%USERNAME%\Desktop\ngrok-v3-stable-windows-amd64\ngrok.exe start --config="C:\\Users\\%USERNAME%\\Desktop\\New Projects\\Nathan's\\delegation_webhook\\ngrok.yml" delegation"

cd "Python Files"
start cmd /k "python app.py"

cmd /k

