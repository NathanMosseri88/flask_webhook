@echo off
pip install virtualenv

cd /d "C:\Users\%USERNAME%\Desktop\New Projects\SimpleToWork\delegation_webhook"
python -m virtualenv venv

cd venv/scripts
call activate.bat

cd /d "C:\Users\%USERNAME%\Desktop\New Projects\SimpleToWork\delegation_webhook"
pip install -r requirements.txt

IF EXIST "C:\Users\%USERNAME%\Desktop\ngrok-v3-stable-windows-amd64\ngrok.exe" (
    echo ngrok is already installed
) ELSE (
    echo Downloading ngrok
    curl -0 https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip
    unzip ngrok-stable-windows-amd64.zip -d C:\Users\%USERNAME%\Desktop\
    echo ngrok downloaded
)

cmd /k

