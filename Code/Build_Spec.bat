pyi-makespec --onefile --add-data="blue.ico;." --icon="blue.ico" autofeedv3.4.4.py
pause
pyinstaller --clean autofeedv3.4.4.spec
pause