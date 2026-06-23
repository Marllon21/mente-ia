import os
import subprocess
import os

from main import chamar_ia, limpar_codigo, executar_python, ler_arquivo, editar_arquivo # Importar aqui para evitar circular dependency

def auto_corrigir(nome):
    if nome == "":
        nome = "gerado.py"

    resultado = executar_python(nome)

    if "ERRO AO EXECUTAR" not in resultado:
        return f"Arquivo {nome} executou sem erros:\n{resultado}"

    erro = ler_arquivo("logs_erro.txt")
    codigo_atual = ler_arquivo(nome)

    prompt = f"""
Corrija este código Python com base no erro.

Retorne APENAS o código corrigido, sem explicação.

ERRO:
{erro}

CÓDIGO ATUAL:
{codigo_atual}
"""

    codigo_corrigido = limpar_codigo(chamar_ia(prompt))

    editar_arquivo(nome, codigo_corrigido)

    novo_resultado = executar_python(nome)

    return f"""
Arquivo {nome} corrigido.

RESULTADO APÓS CORREÇÃO:

{novo_resultado}
"""

def criar_arquivo(nome, conteudo):

    with open(nome, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    return f"Arquivo {nome} criado com sucesso."


def listar_pasta():

    arquivos = os.listdir()

    return "\n".join(arquivos)


def ler_arquivo(nome):

    try:

        with open(nome, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    except:
        return "Arquivo não encontrado."
    
def editar_arquivo(nome, conteudo):

    try:

        with open(nome, "w", encoding="utf-8") as arquivo:

            arquivo.write(conteudo)

        return f"{nome} editado com sucesso."

    except:

        return "Erro ao editar arquivo."
def deletar_arquivo(nome):

    try:

        os.remove(nome)

        return f"{nome} deletado com sucesso."

    except:

        return "Erro ao deletar arquivo."


def criar_pasta(nome):

    try:

        os.makedirs(nome, exist_ok=True)

        return f"Pasta {nome} criada com sucesso."

    except:

        return "Erro ao criar pasta."
    
import subprocess


def executar_python(nome):

    try:
        resultado = subprocess.run(
            ["python", nome],
            capture_output=True,
            text=True
        )

        saida = resultado.stdout
        erro = resultado.stderr

        if resultado.returncode != 0:
            with open("logs_erro.txt", "w", encoding="utf-8") as log:
                log.write(erro)

            return f"ERRO AO EXECUTAR:\n{erro}"

        return saida

    except Exception as e:
        with open("logs_erro.txt", "w", encoding="utf-8") as log:
                log.write(str(e))

                return f"ERRO AO EXECUTAR:\n{e}"

        return saida

    except Exception as e:
        return f"Erro ao executar Python: {e}"
    
def criar_projeto_python(nome):

    criar_pasta(nome)

    codigo = """
print("Projeto criado pela MENTE IA")
"""

    criar_arquivo(f"{nome}/main.py", codigo)

    return f"Projeto {nome} criado com sucesso."

def criar_projeto_python(nome):

    os.makedirs(nome, exist_ok=True)

    os.makedirs(f"{nome}/api", exist_ok=True)
    os.makedirs(f"{nome}/frontend", exist_ok=True)
    os.makedirs(f"{nome}/database", exist_ok=True)

    main = '''
print("Projeto iniciado")
'''

    requirements = '''
flask
openai
python-dotenv
'''

    readme = f'''
# {nome}

Projeto criado automaticamente pela MENTE IA.
'''

    env = '''
OPENAI_API_KEY=
'''

    with open(f"{nome}/main.py", "w", encoding="utf-8") as arquivo:
        arquivo.write(main)

    with open(f"{nome}/requirements.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(requirements)

    with open(f"{nome}/README.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(readme)

    with open(f"{nome}/.env", "w", encoding="utf-8") as arquivo:
        arquivo.write(env)

    return f"Projeto {nome} criado com sucesso."
def salvar_obsidian(nome_nota, conteudo):
    try:
        vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

        caminho = f"{vault}\\{nome_nota}.md"

        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)

        return f"Nota {nome_nota} criada com sucesso no Obsidian."

    except Exception as e:
        return f"Erro: {e}"
def salvar_ideia(conteudo):

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\💡 IDEIAS.md"

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n\n## Ideia\n{conteudo}\n")

    return "Ideia salva."
def salvar_projeto(conteudo):

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\💻 PROJETOS.md"

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n\n## Projeto\n{conteudo}\n")

    return "Projeto salvo."
def salvar_aprendizado(conteudo):

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\📚 APRENDIZADOS.md"

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n\n## Aprendizado\n{conteudo}\n")

    return "Aprendizado salvo."
def ler_ideias():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\💡 IDEIAS.md"

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    except Exception as e:
        return f"Erro ao ler ideias: {e}"
def ler_projetos():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\💻 PROJETOS.md"

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    except Exception as e:
        return f"Erro ao ler projetos: {e}"


def ler_aprendizados():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\📚 APRENDIZADOS.md"

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    except Exception as e:
        return f"Erro ao ler aprendizados: {e}"
def buscar_obsidian(termo):

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    arquivos = [
        "💡 IDEIAS.md",
        "💻 PROJETOS.md",
        "📚 APRENDIZADOS.md"
    ]

    resultados = []

    for nome_arquivo in arquivos:
        caminho = f"{vault}\\{nome_arquivo}"

        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()

            if termo.lower() in conteudo.lower():
                resultados.append(f"\n--- Encontrado em {nome_arquivo} ---\n{conteudo}")

        except Exception as e:
            resultados.append(f"Erro ao ler {nome_arquivo}: {e}")

    if len(resultados) == 0:
        return "Nada encontrado no Obsidian."

    return "\n".join(resultados)   
def resumir_memoria():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    arquivos = [
        "💡 IDEIAS.md",
        "💻 PROJETOS.md",
        "📚 APRENDIZADOS.md",
        "🧠 MEMORIA CENTRAL.md"
    ]
    
    
    memoria = ""

    for nome_arquivo in arquivos:

        caminho = f"{vault}\\{nome_arquivo}"

        try:

            with open(caminho, "r", encoding="utf-8") as arquivo:

                memoria += f"\n\n### {nome_arquivo}\n"
                memoria += arquivo.read()

        except:
            pass

    return memoria
def salvar_memoria_obsidian(conteudo):
    
    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\🧠 MEMORIA CENTRAL.md"

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n\n{conteudo}\n")

    return "Memória salva."

def salvar_perfil(conteudo):

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\👤 PERFIL.md"

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n{conteudo}\n")

    return "Perfil atualizado."
def ler_perfil():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\👤 PERFIL.md"

    try:

        with open(caminho, "r", encoding="utf-8") as arquivo:

            return arquivo.read()

    except:

        return "Perfil vazio."
def salvar_objetivo(conteudo):

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\🎯 OBJETIVOS.md"

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n{conteudo}\n")

    return "Objetivo salvo."
def ler_objetivos():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\🎯 OBJETIVOS.md"

    try:

        with open(caminho, "r", encoding="utf-8") as arquivo:

            return arquivo.read()

    except:

        return "Nenhum objetivo encontrado."
def listar_agentes():

    return """
🤖 AGENTES DISPONÍVEIS

🧠 MENTE IA PRINCIPAL
- Controle central
- Conversa geral
- Coordena agentes

💻 PROGRAMMER_AGENT
- Programação
- Python
- APIs
- Correção de código
- Criação de sistemas

🏗️ ARCHITECT_AGENT
- Estrutura de projetos
- Arquitetura backend/frontend
- Organização de pastas
- Escalabilidade

💼 BUSINESS_AGENT
- Negócios
- Marketing
- Estratégias
- Automação comercial
- El Shaday

🎨 CREATIVE_AGENT
- Ideias criativas
- Design
- Interfaces
- Branding
- UX/UI

⚙️ AUTOMATION_AGENT
- Bots
- WhatsApp
- Integrações
- APIs externas
- Automação
"""
def status_sistema():

    return """
🧠 MENTE IA STATUS

MEMÓRIA:
✅ Online

OBSIDIAN:
✅ Conectado

AGENTES:
✅ Programmer Agent
✅ Architect Agent
✅ Business Agent
✅ Creative Agent
✅ Automation Agent

PERFIL:
✅ Carregado

VERSÃO:
MENTE IA CORE v0.3
"""
def criar_site(tema):
    if tema == "":
        tema = "site moderno"

    criar_pasta("site_ia")

    html = f"""
<!DOCTYPE html>
<html lang=\"pt-BR\">
<head>
    <meta charset=\"UTF-8\">
    <title>{tema}</title>
    <link rel=\"stylesheet\" href=\"style.css\">
</head>
<body>
    <h1>{tema}</h1>
    <p>Site criado automaticamente pela Mente IA.</p>
</body>
</html>
"""

    css = """
body {
    font-family: Arial, sans-serif;
    background: #111;
    color: white;
    text-align: center;
    padding: 50px;
}

h1 {
    color: #00ffcc;
}
"""

    criar_arquivo("site_ia/index.html", html)
    criar_arquivo("site_ia/style.css", css)

    return "Site HTML criado com sucesso."

def gerar_codigo(pedido):
    prompt = f"""
Crie apenas código Python.

Pedido:
{pedido}

Não explique nada.
Retorne apenas o código.
"""

    codigo = limpar_codigo(chamar_ia(prompt))
    criar_arquivo("gerado.py", codigo)

    pedido_lower = pedido.lower()

    if "flask" in pedido_lower or " api " in f" {pedido_lower} ":
        return """
CÓDIGO GERADO EM gerado.py.

Como é Flask/API, não executei automaticamente para não travar.

Para rodar:
python gerado.py
"""

    resultado = executar_python("gerado.py")
    return resultado

def criar_tarefa(conteudo):

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\📋 TAREFAS.md"

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n- [ ] {conteudo}\n")

    return "Tarefa criada."
def listar_tarefas():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\📋 TAREFAS.md"

    try:

        with open(caminho, "r", encoding="utf-8") as arquivo:

            return arquivo.read()

    except:

        return "Nenhuma tarefa encontrada."

def gerar_base_roadmap():

    partes = []

    partes.append("## PERFIL\n" + ler_perfil())
    partes.append("## OBJETIVOS\n" + ler_objetivos())
    partes.append("## PROJETOS\n" + ler_projetos())
    partes.append("## IDEIAS\n" + ler_ideias())
    partes.append("## TAREFAS\n" + listar_tarefas())

    return "\n\n".join(partes)
def salvar_roadmap(conteudo):

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\🗺️ ROADMAP.md"

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n\n{conteudo}\n")

    return "Roadmap salvo."
def ler_roadmap():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    caminho = f"{vault}\\🗺️ ROADMAP.md"

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    except:
        return "Nenhum roadmap encontrado."
def status_sistema_real():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    arquivos = {
        "👤 Perfil": "👤 PERFIL.md",
        "💡 Ideias": "💡 IDEIAS.md",
        "💻 Projetos": "💻 PROJETOS.md",
        "📚 Aprendizados": "📚 APRENDIZADOS.md",
        "🎯 Objetivos": "🎯 OBJETIVOS.md",
        "📋 Tarefas": "📋 TAREFAS.md",
        "🗺️ Roadmap": "🗺️ ROADMAP.md"
    }

    resultado = ["🧠 MENTE IA STATUS REAL\n"]

    for nome, arquivo in arquivos.items():

        caminho = os.path.join(vault, arquivo)

        if os.path.exists(caminho):
            resultado.append(f"✅ {nome}")
        else:
            resultado.append(f"❌ {nome}")
    resultado.append("")
    resultado.append(f"📊 Módulos ativos: {sum(1 for n,a in arquivos.items() if os.path.exists(os.path.join(vault,a)))}/{len(arquivos)}")
    resultado.append("🤖 Agentes: 5")
    resultado.append("🧠 Versão: MENTE IA CORE v0.3")
    resultado.append("")

    ideias = contar_registros(
        os.path.join(vault, "💡 IDEIAS.md"),
        "## Ideia"
    )

    projetos = contar_registros(
        os.path.join(vault, "💻 PROJETOS.md"),
        "## Projeto"
    )

    aprendizados = contar_registros(
        os.path.join(vault, "📚 APRENDIZADOS.md"),
        "## Aprendizado"
    )

    objetivos = contar_registros(
        os.path.join(vault, "🎯 OBJETIVOS.md"),
        "## Objetivo"
    )

    tarefas = contar_registros(
        os.path.join(vault, "📋 TAREFAS.md"),
        "## Tarefa"
    )

    resultado.append(f"💡 Ideias: {ideias}")
    resultado.append(f"💻 Projetos: {projetos}")
    resultado.append(f"📚 Aprendizados: {aprendizados}")
    resultado.append(f"🎯 Objetivos: {objetivos}")
    resultado.append(f"📋 Tarefas: {tarefas}")

    return "\n".join(resultado)
def contar_registros(arquivo, marcador):

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()

        return conteudo.count(marcador)

    except:
        return 0
import json

def gerar_status_json():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    dados = {
        "perfil": contar_registros(os.path.join(vault, "👤 PERFIL.md"), "\n"),
        "ideias": contar_registros(os.path.join(vault, "💡 IDEIAS.md"), "## Ideia"),
        "projetos": contar_registros(os.path.join(vault, "💻 PROJETOS.md"), "## Projeto"),
        "aprendizados": contar_registros(os.path.join(vault, "📚 APRENDIZADOS.md"), "## Aprendizado"),
        "objetivos": contar_registros(os.path.join(vault, "🎯 OBJETIVOS.md"), "\n"),
        "tarefas": contar_registros(os.path.join(vault, "📋 TAREFAS.md"), "- [ ]"),
        "agentes": 5,
        "versao": "MENTE IA CORE v0.3"
    }

    with open("site_ia/status.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    return "Status JSON atualizado para o dashboard."
def gerar_memoria_json():

    vault = r"C:\Users\marllon.araujo\Desktop\Nova pasta (2)\MENTE IA CORE"

    arquivos = {
        "perfil": "👤 PERFIL.md",
        "objetivos": "🎯 OBJETIVOS.md",
        "projetos": "💻 PROJETOS.md",
        "ideias": "💡 IDEIAS.md",
        "aprendizados": "📚 APRENDIZADOS.md",
        "roadmap": "🗺️ ROADMAP.md"
    }

    dados = {}

    for chave, arquivo in arquivos.items():

        caminho = os.path.join(vault, arquivo)

        try:
            with open(caminho, "r", encoding="utf-8") as f:
                dados[chave] = f.read()
        except:
            dados[chave] = "Nada encontrado."

    with open("site_ia/memoria.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    return "Memória JSON atualizada."
from datetime import datetime

def criar_api_flask():
    codigo = '''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"mensagem": "API ONLINE"}

app.run(debug=True)
'''

    criar_arquivo("app.py", codigo)

    return "API Flask criada com sucesso."

def corrigir_erro():
    erro = ler_arquivo("logs_erro.txt")

    prompt = f"""
Analise esse erro Python e explique como corrigir:

{erro}
"""

    return chamar_ia(prompt)

def gerar_frontend_login():
    html = """
        <!DOCTYPE html>
        <html lang=\"pt-BR\">
        <head>
            <meta charset=\"UTF-8\">
            <title>Login MENTE IA</title>
        </head>
        <body>
            <h2>Login</h2>

            <form id=\"loginForm\">
                <input type=\"text\" id=\"username\" placeholder=\"Usuário\" required>
                <input type=\"password\" id=\"password\" placeholder=\"Senha\" required>
                <button type=\"submit\">Entrar</button>
            </form>

            <p id=\"mensagem\"></p>
        </body>
        </html>
        """

    criar_arquivo("login.html", html)

    return "Frontend de login criado em login.html"
