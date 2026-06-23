from crm.lead_manager import carregar_leads


def mostrar_pipeline():

    leads = carregar_leads()

    novos = []
    qualificados = []
    convertidos = []

    for lead in leads:

        status = lead["status"]

        if status == "Novo":
            novos.append(lead["nome"])

        elif status == "Qualificado":
            qualificados.append(lead["nome"])

        elif status == "Convertido":
            convertidos.append(lead["nome"])

    resultado = "\n📊 PIPELINE COMERCIAL\n\n"

    resultado += "🔵 NOVOS\n"

    if novos:
        for nome in novos:
            resultado += f"- {nome}\n"
    else:
        resultado += "Nenhum\n"

    resultado += "\n🟡 QUALIFICADOS\n"

    if qualificados:
        for nome in qualificados:
            resultado += f"- {nome}\n"
    else:
        resultado += "Nenhum\n"

    resultado += "\n🟢 CONVERTIDOS\n"

    if convertidos:
        for nome in convertidos:
            resultado += f"- {nome}\n"
    else:
        resultado += "Nenhum\n"

    return resultado
