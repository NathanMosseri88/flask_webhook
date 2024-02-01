cd /d "C:\Users\%USERNAME%\Desktop\New Projects\Nathan's\delegation_webhook"
start cmd /k "C:\Users\%USERNAME%\Desktop\ngrok-v3-stable-windows-amd64\ngrok.exe start --config="C:\\Users\\%USERNAME%\\Desktop\\New Projects\\Nathan's\\delegation_webhook\\ngrok.yml" %COMPUTERNAME%"

cd "Python Files"
start cmd /k "python app.py"