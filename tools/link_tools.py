import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARQUIVO = os.path.join(
    BASE_DIR,
    "memory",
    "vinculos.json"
)

def carregar_vinculos():

    if not os.path.exists(ARQUIVO):
        return []

    with open(
        ARQUIVO,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


def salvar_vinculos(vinculos):

    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            vinculos,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def vincular_cliente_projeto(
    cliente,
    projeto
):

    vinculos = carregar_vinculos()

    vinculos.append({

        "cliente": cliente,

        "projeto": projeto

    })

    salvar_vinculos(vinculos)

    return (
        f"Cliente '{cliente}' "
        f"vinculado ao projeto "
        f"'{projeto}'."
    )


def projetos_cliente(cliente):

    vinculos = carregar_vinculos()

    projetos = [

        v["projeto"]

        for v in vinculos

        if v["cliente"].lower()
        == cliente.lower()

    ]

    if not projetos:
        return "Nenhum projeto encontrado."

    resultado = (
        f"\n👤 CLIENTE: {cliente}\n\n"
    )

    for projeto in projetos:

        resultado += f"- {projeto}\n"

    return resultado
