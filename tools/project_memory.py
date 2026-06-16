from tools.project_dashboard import mostrar_projeto
from tools.note_tools import mostrar_notas


def mostrar_memoria_projeto(nome_projeto):

    projeto = mostrar_projeto(nome_projeto)

    notas = mostrar_notas(nome_projeto)

    return (
        f"{projeto}\n\n"
        f"{notas}"
    )