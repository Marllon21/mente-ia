from tools.task_tools import carregar_tarefas
from tools.link_tools import carregar_vinculos


def mostrar_projeto(nome_projeto):
    cliente_projeto = "Não vinculado"

    vinculos = carregar_vinculos()

    for vinculo in vinculos:
        if vinculo["projeto"].lower() == nome_projeto.lower():
            cliente_projeto = vinculo["cliente"]
            break

    tarefas = carregar_tarefas()

    tarefas_projeto = [
        t for t in tarefas
        if t["projeto"].lower() == nome_projeto.lower()
    ]

    if not tarefas_projeto:
        return f"Projeto '{nome_projeto}' não encontrado."

    resultado = (
        f"\n📁 PROJETO: {nome_projeto}\n\n"
        f"👤 CLIENTE: {cliente_projeto}\n\n"
    )

    concluidas = 0

    for i, tarefa in enumerate(tarefas_projeto, start=1):
        resultado += (
            f"{i}. {tarefa['tarefa']}\n"
            f"   Status: {tarefa['status']}\n\n"
        )

        if tarefa["status"] == "Concluída":
            concluidas += 1

    progresso = round((concluidas / len(tarefas_projeto)) * 100)

    resultado += f"📊 Progresso: {progresso}%"

    return resultado
