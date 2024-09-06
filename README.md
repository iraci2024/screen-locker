
# Screen Locker

Este projeto é um protetor de tela que bloqueia a tela, teclado e mouse. Para desbloquear, é necessário digitar a senha correta.

## Requisitos

- Python 3.x
- Bibliotecas: `tkinter`, `keyboard`, `mouse`

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd screen-locker
   ```

2. Instale as dependências:
   ```bash
   pip install keyboard mouse
   ```

## Uso

Execute o script `screen_locker.py`:
```bash
python3 screen_locker.py
```

Digite a senha para desbloquear a tela.

## Configuração

Você pode alterar a senha editando a variável `self.password` no arquivo `screen_locker.py`.
