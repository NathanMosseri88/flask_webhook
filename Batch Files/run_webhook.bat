cd /d "C:\Users\%USERNAME%\Desktop\New Projects\Nathan's\delegation_webhook"
echo version: "2" > ngrok.yml
echo authtoken: "1exTA3FUMpg1OOC6vR5sA2PVtk8_2raxh83uKPB57CfSf5jdh" >> ngrok.yml
echo tunnels: >> ngrok.yml
echo  %COMPUTERNAME%: >> ngrok.yml
echo   proto: http >> ngrok.yml
echo   addr: 5000 >> ngrok.yml
echo   domain: '*-stw.ngrok.app' >> ngrok.yml
echo   ip_restriction: >> ngrok.yml
echo    allow_cidrs: ['47.21.68.62/32', '77.137.74.229/32'] >> ngrok.yml

cd /d "C:\Users\%USERNAME%\Desktop\New Projects\Nathan's\delegation_webhook"
start cmd /k "C:\Users\%USERNAME%\Desktop\ngrok-v3-stable-windows-amd64\ngrok.exe start --config="C:\\Users\\%USERNAME%\\Desktop\\New Projects\\Nathan's\\delegation_webhook\\ngrok.yml" %COMPUTERNAME%"

cd "Python Files"
start cmd /k "python app.py"