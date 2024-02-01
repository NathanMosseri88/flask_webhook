@echo off
pip install virtualenv

cd /d "C:\Users\%USERNAME%\Desktop\New Projects\Nathan's\delegation_webhook"
python -m virtualenv venv

cd venv/scripts
call activate.bat

cd /d "C:\Users\%USERNAME%\Desktop\New Projects\Nathan's\delegation_webhook"
pip install -r requirements.txt

IF EXIST "C:\Users\%USERNAME%\Desktop\ngrok-v3-stable-windows-amd64\ngrok.exe" (
    echo ngrok is already installed
) ELSE (
    echo Downloading ngrok
    curl -0 https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip
    unzip ngrok-stable-windows-amd64.zip -d C:\Users\%USERNAME%\Desktop\
    echo ngrok downloaded
)

cd /d "C:\Users\%USERNAME%\Desktop\New Projects\Nathan's\delegation_webhook"
echo version: "2" > ngrok.yml
echo authtoken: "1exTA3FUMpg1OOC6vR5sA2PVtk8_2raxh83uKPB57CfSf5jdh" >> ngrok.yml
echo tunnels: >> ngrok.yml
echo  %COMPUTERNAME%: >> ngrok.yml
echo   proto: http >> ngrok.yml
echo   addr: 5000 >> ngrok.yml
echo   domain: easy-macaw-nearly.ngrok-free.app >> ngrok.yml

start cmd /k "C:\Users\%USERNAME%\Desktop\ngrok-v3-stable-windows-amd64\ngrok.exe start --config="C:\\Users\\%USERNAME%\\Desktop\\New Projects\\Nathan's\\delegation_webhook\\ngrok.yml" %COMPUTERNAME%"

cd "Python Files"
start cmd /k "python app.py"

cmd /k

