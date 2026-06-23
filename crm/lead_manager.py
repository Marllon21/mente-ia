import json
import os

from tools.client_tools import salvar_cliente
from tools.project_tools import novo_projeto

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

ARQUIVO = os.path.join(
    BASE_DIR,
    "crm_data",
    "leads.json"
)


def carregar_leads():

    if not os.path.exists(ARQUIVO):
        return []

    with open(
        ARQUIVO,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


def salvar_leads(leads):

    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            leads,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def novo_lead(nome):

    leads = carregar_leads()

    leads.append({

        "nome": nome,

        "status": "Novo"

    })

    salvar_leads(leads)

    return f"Lead '{nome}' criado."

def listar_leads():

    leads = carregar_leads()

    if not leads:
        return "Nenhum lead encontrado."

    resultado = "\n📞 LEADS\n\n"

    for i, lead in enumerate(
        leads,
        start=1
    ):

        resultado += (
            f"{i}. "
            f"{lead['nome']} "
            f"[{lead['status']}]\n"
        )

    return resultado

def mostrar_lead(nome):

    leads = carregar_leads()

    for lead in leads:

        if lead["nome"].lower() == nome.lower():

            return (
                f"\n👤 LEAD\n\n"
                f"Nome: {lead['nome']}\n"
                f"Status: {lead['status']}\n"
                f"Tipo Projeto: {lead.get('tipo_projeto','-')}\n"
                f"Orçamento: {lead.get('orcamento','-')}\n"
                f"Prazo: {lead.get('prazo','-')}"
            )

    return "Lead não encontrado."

def qualificar_lead(
    nome,
    tipo_projeto,
    orcamento,
    prazo
):

    leads = carregar_leads()

    for lead in leads:

        if lead["nome"].lower() == nome.lower():

            lead["status"] = "Qualificado"
            lead["tipo_projeto"] = tipo_projeto
            lead["orcamento"] = orcamento
            lead["prazo"] = prazo

            salvar_leads(leads)

            return (
                f"Lead '{nome}' qualificado."
            )

    return "Lead não encontrado."

def converter_lead(nome):

    leads = carregar_leads()

    for lead in leads:

        if lead["nome"].lower() == nome.lower():

            projeto = (
                f"{lead['tipo_projeto']} - "
                f"{lead['nome']}"
            )

            salvar_cliente(
                f"Nome: {lead['nome']}"
            )

            novo_projeto(projeto)

            lead["status"] = "Convertido"

            salvar_leads(leads)

            return (
                f"✅ Lead convertido\n"
                f"👤 Cliente criado\n"
                f"📁 Projeto criado: {projeto}"
            )

    return "Lead não encontrado."
