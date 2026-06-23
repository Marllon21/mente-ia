import json
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)




def dashboard():

    total_clientes = 0
    total_leads = 0
    convertidos = 0
    qualificados = 0
    novos = 0

    total_projetos = 0
    andamento = 0
    concluidos = 0

    pendentes = 0
    tarefas_concluidas = 0

    # Leads
    try:

        with open(
            os.path.join(
                BASE_DIR,
                "crm_data",
                "leads.json"
            ),
            "r",
            encoding="utf-8"
        ) as arq:

            leads = json.load(arq)

            total_leads = len(leads)

            for lead in leads:

                status = lead["status"]

                if status == "Novo":
                    novos += 1

                elif status == "Qualificado":
                    qualificados += 1

                elif status == "Convertido":
                    convertidos += 1

    except:
        pass

    # Projetos
    try:

        with open(
            os.path.join(
                BASE_DIR,
                "memory",
                "projetos.json"
            ),
            "r",
            encoding="utf-8"
        ) as arq:

            projetos = json.load(arq)

            total_projetos = len(projetos)

            for projeto in projetos:

                if projeto["status"] == "Em andamento":
                    andamento += 1

                elif projeto["status"] == "Concluído":
                    concluidos += 1

    except:
        pass

    # Tarefas
    try:

        with open(
            os.path.join(
                BASE_DIR,
                "memory",
                "tarefas.json"
            ),
            "r",
            encoding="utf-8"
        ) as arq:

            tarefas = json.load(arq)

            for tarefa in tarefas:

                if tarefa["status"] == "Pendente":
                    pendentes += 1

                elif tarefa["status"] == "Concluída":
                    tarefas_concluidas += 1

    except:
        pass

    # Clientes
    try:

        with open(
            os.path.join(
                BASE_DIR,
                "memory",
                "clientes.md"
            ),
            "r",
            encoding="utf-8"
        ) as arq:

            texto = arq.read()

            total_clientes = texto.count("## Cliente")

    except:
        pass

    conversao = 0

    if total_leads > 0:
        conversao = round(
            (convertidos / total_leads) * 100
        )

    return f"""
📊 DASHBOARD

👥 Clientes: {total_clientes}

📞 Leads: {total_leads}
🟢 Convertidos: {convertidos}
🟡 Qualificados: {qualificados}
🔵 Novos: {novos}

📁 Projetos: {total_projetos}
⚙️ Em andamento: {andamento}
✅ Concluídos: {concluidos}

📋 Tarefas:
Pendentes: {pendentes}
Concluídas: {tarefas_concluidas}

🎯 Conversão:
{conversao}%
"""

