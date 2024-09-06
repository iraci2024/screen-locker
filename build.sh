
#!/bin/bash

# Instalar dependências
pip install -r requirements.txt

# Gerar o executável do servidor
pyinstaller --onefile server.py

# Gerar o executável do cliente
pyinstaller --onefile client.py

# Mover os executáveis para a pasta dist
mv dist/server ./server.exe
mv dist/client ./client.exe
