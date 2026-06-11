import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAULT = os.path.join(BASE_DIR, "memory")

os.makedirs(VAULT, exist_ok=True)


def salvar_cliente(conteudo):
    caminho = os.path.join(VAULT, "clientes.md")
    data = datetime.now().strftime("%d/%m/%Y")

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"""

## Cliente

Data: {data}
Status: Prospect

{conteudo}

-------------------------
""")

    return "Cliente salvo."


def listar_clientes():
    caminho = os.path.join(VAULT, "clientes.md")

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return "Nenhum cliente encontrado."