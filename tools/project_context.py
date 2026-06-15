import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARQUIVO_TAREFAS = os.path.join(
    BASE_DIR,
    "memory",
    "tarefas.json"
)


def gerar_contexto_projeto(nome_projeto):

    with open(
        ARQUIVO_TAREFAS,
        "r",
        encoding="utf-8"
    ) as arquivo:

        tarefas = json.load(arquivo)

    tarefas_projeto = [

        t for t in tarefas

        if t["projeto"].lower()
        == nome_projeto.lower()

    ]

    if not tarefas_projeto:
        return "Projeto não encontrado."

    contexto = f"""
PROJETO: {nome_projeto}

TAREFAS:
"""

    for tarefa in tarefas_projeto:

        contexto += (
            f"\n- {tarefa['tarefa']}"
            f" ({tarefa['status']})"
        )

    return contexto

def salvar_contexto_projeto(nome_projeto):

    contexto = gerar_contexto_projeto(nome_projeto)

    if contexto == "Projeto não encontrado.":
        return contexto

    pasta_contextos = os.path.join(BASE_DIR, "memory", "contextos")
    os.makedirs(pasta_contextos, exist_ok=True)

    nome_arquivo = nome_projeto.lower().replace(" ", "_") + ".md"
    caminho = os.path.join(pasta_contextos, nome_arquivo)

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(contexto)

    return f"Contexto do projeto '{nome_projeto}' salvo em memory/contextos/{nome_arquivo}"
