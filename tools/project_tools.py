import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_DIR = os.path.join(BASE_DIR, "memory")

os.makedirs(MEMORY_DIR, exist_ok=True)

ARQUIVO = os.path.join(MEMORY_DIR, "projetos.json")


def carregar_projetos():

    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_projetos(projetos):

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(projetos, arquivo, ensure_ascii=False, indent=4)


def novo_projeto(nome):

    projetos = carregar_projetos()

    projetos.append({
        "nome": nome,
        "status": "Em andamento"
    })

    salvar_projetos(projetos)

    return f"Projeto '{nome}' criado com sucesso."


def listar_projetos():

    projetos = carregar_projetos()

    if not projetos:
        return "Nenhum projeto encontrado."

    resposta = "\n📁 PROJETOS\n\n"

    for projeto in projetos:
        resposta += f"- {projeto['nome']} ({projeto['status']})\n"

    return resposta
