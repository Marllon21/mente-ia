import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO = os.path.join(BASE_DIR, "memory", "tarefas.json")


def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_tarefas(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)


def nova_tarefa(texto):
    tarefas = carregar_tarefas()

    tarefas.append({
        "projeto": "Sem Projeto",
        "tarefa": texto,
        "status": "Pendente"
    })

    salvar_tarefas(tarefas)

    return f"Tarefa '{texto}' criada com sucesso."


def nova_tarefa_projeto(projeto, tarefa):
    tarefas = carregar_tarefas()

    tarefas.append({
        "projeto": projeto,
        "tarefa": tarefa,
        "status": "Pendente"
    })

    salvar_tarefas(tarefas)

    return f"Tarefa '{tarefa}' criada para o projeto '{projeto}'."


def listar_tarefas():
    tarefas = carregar_tarefas()

    if not tarefas:
        return "Nenhuma tarefa encontrada."

    resultado = "\n📋 TAREFAS\n\n"

    for i, tarefa in enumerate(tarefas, start=1):
        projeto = tarefa.get("projeto", "Sem Projeto")
        nome = tarefa.get("tarefa", "")
        status = tarefa.get("status", "Pendente")

        resultado += f"{i}. Projeto: {projeto} | {nome} | Status: {status}\n"

    return resultado


def concluir_tarefa(numero):
    tarefas = carregar_tarefas()
    indice = numero - 1

    if indice < 0 or indice >= len(tarefas):
        return "Tarefa não encontrada."

    tarefas[indice]["status"] = "Concluída"
    salvar_tarefas(tarefas)

    return "Tarefa concluída com sucesso."

def nova_tarefa_projeto(projeto, tarefa):
    tarefas = carregar_tarefas()

    tarefas.append({
        "projeto": projeto,
        "tarefa": tarefa,
        "status": "Pendente"
    })

    salvar_tarefas(tarefas)

    return f"Tarefa '{tarefa}' criada para o projeto '{projeto}'."


