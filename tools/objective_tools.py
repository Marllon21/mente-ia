import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARQUIVO = os.path.join(
    BASE_DIR,
    "memory",
    "objetivos.json"
)


def carregar_objetivos():

    if not os.path.exists(ARQUIVO):
        return []

    with open(
        ARQUIVO,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


def salvar_objetivos(lista):

    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            lista,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def novo_objetivo(projeto, objetivo):

    objetivos = carregar_objetivos()

    objetivos.append({
        "projeto": projeto,
        "objetivo": objetivo
    })

    salvar_objetivos(objetivos)

    return (
        f"Objetivo salvo para o projeto "
        f"'{projeto}'."
    )


def buscar_objetivo(projeto):

    objetivos = carregar_objetivos()

    for item in objetivos:

        if item["projeto"].lower() == projeto.lower():

            return item["objetivo"]

    return "Nenhum objetivo definido."
