import json
import os

ARQUIVO_MEMORIA = "memory/memoria.json"


def carregar_memoria():

    if not os.path.exists(ARQUIVO_MEMORIA):
        return []

    with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_memoria(memoria):

    with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as arquivo:
        json.dump(memoria, arquivo, indent=4, ensure_ascii=False)


def adicionar_memoria(usuario, resposta):

    memoria = carregar_memoria()

    memoria.append({
        "usuario": usuario,
        "ia": resposta
    })

    salvar_memoria(memoria)


def ultimas_memorias(limite=5):

    memoria = carregar_memoria()

    return memoria[-limite:]
