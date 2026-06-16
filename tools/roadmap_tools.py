import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def gerar_roadmap(projeto):

    pasta = os.path.join(
        BASE_DIR,
        "memory",
        "roadmaps"
    )

    os.makedirs(
        pasta,
        exist_ok=True
    )

    nome = projeto.lower().replace(
        " ",
        "_"
    )

    caminho = os.path.join(
        pasta,
        f"{nome}.md"
    )

    roadmap = f"""
# ROADMAP

Projeto: {projeto}

## FASE 1
- Planejamento
- Layout
- Estrutura

## FASE 2
- Desenvolvimento
- Testes

## FASE 3
- Deploy
- Ajustes finais
"""

    with open(
        caminho,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(roadmap)

    return f"Roadmap criado para '{projeto}'."
