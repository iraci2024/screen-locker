
#!/bin/bash

# Instalar dependências
pip install -r requirements.txt

# Gerar o executável
pyinstaller --onefile screen_locker.py

# Mover o executável para a pasta dist
mv dist/screen_locker ./screen_locker.exe
