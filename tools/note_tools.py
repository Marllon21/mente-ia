import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARQUIVO = os.path.join(
    BASE_DIR,
    "memory",
    "notas.json"
)


def carregar_notas():

    if not os.path.exists(ARQUIVO):
        return []

    with open(
        ARQUIVO,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


def salvar_notas(notas):

    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            notas,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def nova_nota(projeto, nota):

    notas = carregar_notas()

    notas.append({
        "projeto": projeto,
        "nota": nota
    })

    salvar_notas(notas)

    return f"Nota salva para o projeto '{projeto}'."


def mostrar_notas(projeto):

    notas = carregar_notas()

    resultado = "\n📝 NOTAS\n\n"

    encontrou = False

    for item in notas:

        if item["projeto"].lower() == projeto.lower():

            resultado += f"- {item['nota']}\n"

            encontrou = True

    if not encontrou:
        return "Nenhuma nota encontrada."

    return resultado