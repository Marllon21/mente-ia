import os

from crm.lead_manager import carregar_leads

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


def gerar_proposta(nome):

    leads = carregar_leads()

    for lead in leads:

        if lead["nome"].lower() == nome.lower():

            pasta = os.path.join(
                BASE_DIR,
                "crm_data",
                "propostas"
            )

            os.makedirs(
                pasta,
                exist_ok=True
            )

            arquivo = os.path.join(
                pasta,
                nome.lower().replace(
                    " ",
                    "_"
                ) + ".md"
            )

            conteudo = f"""
# PROPOSTA COMERCIAL

Cliente: {lead['nome']}

Tipo Projeto:
{lead.get('tipo_projeto','Não informado')}

Orçamento:
R$ {lead.get('orcamento','Não informado')}

Prazo:
{lead.get('prazo','Não informado')}

---

Proposta gerada pela MENTE IA.
"""

            with open(
                arquivo,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(conteudo)

            return (
                f"Proposta criada:\n{arquivo}"
            )

    return "Lead não encontrado."
