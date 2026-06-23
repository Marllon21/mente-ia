import os
import json
from tools.file_tools import (
    listar_agentes,
    salvar_ideia,
    salvar_projeto,
    ler_ideias,
    ler_projetos,
    buscar_obsidian,
    salvar_roadmap,
    ler_roadmap,
    ler_aprendizados,
    salvar_memoria_obsidian,
    salvar_perfil,
    ler_perfil,
    status_sistema,
    status_sistema_real,
    salvar_objetivo,
    ler_objetivos,
    gerar_status_json,
    salvar_aprendizado,
    gerar_base_roadmap,
    status_sistema,
    criar_arquivo,
    listar_pasta,
    ler_arquivo,
    editar_arquivo,
    deletar_arquivo,
    criar_pasta,
    executar_python,
    criar_projeto_python,
    resumir_memoria,
    salvar_obsidian,
    auto_corrigir,
    criar_site,
    gerar_codigo,
    criar_api_flask,
    corrigir_erro,
    gerar_frontend_login
)
from crm.pipeline import mostrar_pipeline
from tools.dashboard_tools import dashboard
from crm.proposta_generator import (
    gerar_proposta
)
from crm.lead_manager import (
    novo_lead,
    listar_leads,
    mostrar_lead,
    converter_lead,
    qualificar_lead
)
from tools.project_memory import (
    mostrar_memoria_projeto
)
from tools.note_tools import (
    nova_nota,
    mostrar_notas
)

from tools.roadmap_tools import (
    gerar_roadmap
)
from tools.objective_tools import (
    novo_objetivo,
    buscar_objetivo
)
from tools.link_tools import (
    vincular_cliente_projeto,
    projetos_cliente
)
from tools.project_context import gerar_contexto_projeto, salvar_contexto_projeto
from tools.project_dashboard import mostrar_projeto
from tools import task_tools

from tools.project_tools import novo_projeto, listar_projetos
from tools.client_tools import salvar_cliente, listar_clientes
from core.ia_router import escolher_modelo
from tools.terminal_tools import executar_terminal
from agents.programmer_agent import programmer_prompt
from agents.architect_agent import architect_prompt
from agents.business_agent import business_prompt
from memory.memory_manager import (
    adicionar_memoria,
    ultimas_memorias
)
from tools.voice_manager import speak, listen

from openai import OpenAI
from dotenv import load_dotenv

from rich import print
from datetime import datetime

# =========================
# CONFIG
# =========================

load_dotenv()

client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("OPENROUTER_API_KEY")

)

ARQUIVO_MEMORIA = "memory/memoria.json"

# Carregar definições de ferramentas
with open("tools.json", "r", encoding="utf-8") as f:
    available_tools = json.load(f)

# Mapeamento de funções para execução
function_map = {
    "mostrar_memoria_projeto": mostrar_memoria_projeto,
    "gerar_roadmap": gerar_roadmap,
    "mostrar_notas": mostrar_notas,
    "nova_nota": nova_nota,
    "vincular_cliente_projeto": vincular_cliente_projeto,
    "projetos_cliente": projetos_cliente,
    "salvar_contexto_projeto": salvar_contexto_projeto,
    "gerar_contexto_projeto": gerar_contexto_projeto,
    "mostrar_projeto": mostrar_projeto,
    "concluir_tarefa": task_tools.concluir_tarefa,
    "nova_tarefa_projeto": task_tools.nova_tarefa_projeto,
    "nova_tarefa": task_tools.nova_tarefa,
    "listar_tarefas": task_tools.listar_tarefas,
    "dashboard": task_tools.dashboard,
    "novo_projeto": novo_projeto,
    "listar_projetos": listar_projetos,
    "salvar_cliente": salvar_cliente,
    "listar_clientes": listar_clientes,
    "gerar_status_json": gerar_status_json,
    "status_sistema_real": status_sistema_real,
    "ler_roadmap": ler_roadmap,
    "salvar_roadmap": salvar_roadmap,
    "status_sistema": status_sistema,
    "listar_agentes": listar_agentes,
    "salvar_objetivo": salvar_objetivo,
    "ler_objetivos": ler_objetivos,
    "ler_perfil": ler_perfil,
    "salvar_perfil": salvar_perfil,
    "salvar_memoria_obsidian": salvar_memoria_obsidian,
    "resumir_memoria": resumir_memoria,
    "ler_projetos": ler_projetos,
    "ler_aprendizados": ler_aprendizados,
    "ler_ideias": ler_ideias,
    "auto_corrigir": auto_corrigir,
    "quem_sou_eu": ler_perfil,
    "gerar_roadmap_ia": gerar_base_roadmap,
    "salvar_obsidian_nota": salvar_obsidian,
    "buscar_obsidian": buscar_obsidian,
    "o_que_voce_sabe_sobre": buscar_obsidian,
    "criar_arquivo": criar_arquivo,
    "ler_arquivo": ler_arquivo,
    "editar_arquivo": editar_arquivo,
    "criar_pasta": criar_pasta,
    "deletar_arquivo": deletar_arquivo,
    "executar_python": executar_python,
    "executar_terminal": executar_terminal,
    "criar_api_flask": criar_api_flask,
    "criar_site": criar_site,
    "criar_projeto_python": criar_projeto_python,
    "corrigir_erro": corrigir_erro,
    "gerar_frontend_login": gerar_frontend_login,
    "gerar_codigo": gerar_codigo,
    "salvar_ideia": salvar_ideia,
    "salvar_projeto": salvar_projeto,
    "salvar_aprendizado": salvar_aprendizado
}

# =========================
# MEMÓRIA
# =========================

def carregar_memoria():

    try:

        with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as arquivo:

            return json.load(arquivo)

    except:

        return []

def salvar_memoria(usuario, resposta):

    memoria = carregar_memoria()

    memoria.append({

        "hora": datetime.now().strftime("%H:%M:%S"),
        "usuario": usuario,
        "resposta": resposta

    })

    with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as arquivo:

        json.dump(memoria, arquivo, indent=4, ensure_ascii=False)

# =========================
# IA REAL
# =========================
        
def limpar_codigo(codigo):

    codigo = codigo.replace("```python", "")
    codigo = codigo.replace("```", "")

    linhas = codigo.splitlines()

    for i, linha in enumerate(linhas):
        if linha.strip().startswith("from ") or linha.strip().startswith("import "):
            return "\n".join(linhas[i:]).strip()

    return codigo.strip()


<<<<<<< HEAD
    comando_lower = comando.lower()
    
    if comando_lower == "pipeline":
        return mostrar_pipeline()
    
    if comando_lower == "dashboard":
        return dashboard()
    
    if "converter lead" in comando_lower:

        nome = comando.replace(
            "converter lead",
            ""
        ).strip()

        return converter_lead(nome)
    
    if "gerar proposta" in comando_lower:

        nome = comando.replace(
            "gerar proposta",
            ""
        ).strip()

        return gerar_proposta(nome)
    
    if "qualificar lead" in comando_lower:

        partes = comando.split("|")

        nome = partes[1].strip()
        tipo = partes[2].strip()
        orcamento = partes[3].strip()
        prazo = partes[4].strip()

        return qualificar_lead(
            nome,
            tipo,
            orcamento,
            prazo
        )
        
    if "mostrar lead" in comando_lower:

        nome = comando.replace(
            "mostrar lead",
            ""
        ).strip()

        return mostrar_lead(nome)
    
    if "listar leads" in comando_lower:

        return listar_leads()
    
    if "novo lead" in comando_lower:

        nome = comando.replace(
            "novo lead",
            ""
        ).strip()

        return novo_lead(nome)
    
    if "mostrar memoria projeto" in comando_lower:

        nome = comando_lower.replace(
            "mostrar memoria projeto",
            ""
        ).strip()

        return mostrar_memoria_projeto(nome)
        
    if "gerar roadmap projeto" in comando_lower:

        nome = comando_lower.replace(
            "gerar roadmap projeto",
            ""
        ).strip()

        return gerar_roadmap(nome)
    
    if "mostrar notas projeto" in comando_lower:

        nome = comando_lower.replace(
            "mostrar notas projeto",
            ""
        ).strip()

        return mostrar_notas(nome)
    
    if "nova nota projeto" in comando_lower:

        texto = comando.replace(
            "nova nota projeto",
            ""
        ).strip()

        projeto = "site el shaday"

        nota = texto.replace(
            projeto,
            ""
        ).strip()

        return nova_nota(
            projeto,
            nota
        )
    
    if "vincular cliente" in comando_lower:

        partes = comando_lower.replace(
            "vincular cliente",
            ""
        ).split("projeto")

        cliente = partes[0].strip()

        projeto = partes[1].strip()

        return vincular_cliente_projeto(
            cliente,
            projeto
        )
        
    if "mostrar cliente" in comando_lower:

        nome = comando_lower.replace(
            "mostrar cliente",
            ""
        ).strip()

        return projetos_cliente(nome)
    
    if "salvar contexto projeto" in comando_lower:

        nome = comando_lower.replace(
            "salvar contexto projeto",
            ""
        ).strip()

        return salvar_contexto_projeto(nome)
    
    if "gerar contexto projeto" in comando_lower:

        nome = comando_lower.replace(
            "gerar contexto projeto",
            ""
        ).strip()

        return gerar_contexto_projeto(nome)
        
    if "mostrar projeto" in comando_lower:

        nome = comando_lower.replace(
            "mostrar projeto",
            ""
        ).strip()

        return mostrar_projeto(nome)
    
    if "concluir tarefa" in comando_lower:
        numero = comando_lower.replace("concluir tarefa", "").strip()

        if numero.isdigit():
            return task_tools.concluir_tarefa(int(numero))

        return "Informe o número da tarefa. Exemplo: concluir tarefa 2"
    
    if "nova tarefa" in comando_lower and "projeto" in comando_lower:

        texto_completo = comando_lower.replace("nova tarefa", "").strip()

        partes = texto_completo.split("projeto", 1)

        tarefa = partes[0].strip()
        projeto = partes[1].strip()

        return task_tools.nova_tarefa_projeto(projeto, tarefa)


    if "nova tarefa" in comando_lower:

        texto = comando.replace("nova tarefa", "").strip()

        return task_tools.nova_tarefa(texto)


    if "listar tarefas" in comando_lower:

        return task_tools.listar_tarefas()
    
    if comando.startswith("novo projeto"):

        nome = comando.replace("novo projeto", "").strip()

        return novo_projeto(nome)


    if comando == "listar projetos":

        return listar_projetos()
    
    if "novo cliente" in comando_lower:

        texto = comando.replace("novo cliente", "").strip()

        return salvar_cliente(texto)
    
    if "listar clientes" in comando_lower:

        return listar_clientes()
    
    if "atualizar dashboard" in comando_lower:

        return gerar_status_json()
    
    if "status sistema real" in comando_lower:

        return status_sistema_real()
    
    if "mostrar roadmap" in comando_lower:

        return ler_roadmap()
    if "salvar roadmap" in comando_lower:

        texto = comando.replace("salvar roadmap", "").strip()

        return salvar_roadmap(texto)
    
    if "status sistema" in comando_lower:

        return status_sistema()
    
    if "listar agentes" in comando_lower:

        return listar_agentes()
    
    if "salvar objetivo" in comando_lower:

        texto = comando.replace("salvar objetivo", "").strip()

        return salvar_objetivo(texto)
    
    if "listar objetivos" in comando_lower:

        return ler_objetivos()
    if "mostrar perfil" in comando_lower:

        return ler_perfil()
    
    if "salvar perfil" in comando_lower:

        texto = comando.replace("salvar perfil", "").strip()

        return salvar_perfil(texto)
    
    if "salvar memoria" in comando_lower:

        texto = comando.replace("salvar memoria", "").strip()

        return salvar_memoria_obsidian(texto)
    
    if "resumir memoria" in comando_lower:

        return resumir_memoria()
    if "listar projetos" in comando_lower:

        return ler_projetos()

    if "listar aprendizados" in comando_lower:

        return ler_aprendizados()
    
    if "listar ideias" in comando_lower:

        return ler_ideias()
    if "auto corrigir" in comando_lower:

        nome = comando.replace("auto corrigir", "").strip()

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
    if "quem sou eu" in comando_lower:

        perfil = ler_perfil()

        prompt = f"""
    Responda usando APENAS as informações abaixo.

    Não invente nada.
    Não assuma sobrenome.
    Não adicione tecnologias.

    PERFIL:

    {perfil}
    """

        return chamar_ia(prompt)
    if "gerar roadmap" in comando_lower:

        base = gerar_base_roadmap()

        prompt = f"""
    Crie um roadmap prático para a MENTE IA usando os dados abaixo.

    Separe em:
    - Agora
    - Próximos passos
    - Futuro
    - Prioridades

    DADOS:
    {base}
    """

        return chamar_ia(prompt)
    if "salvar obsidian" in comando_lower:

        texto = comando.replace("salvar obsidian", "").strip()

        return salvar_obsidian(
            "Nova Nota",
            texto
        )
    if comando_lower.startswith("buscar "):

        termo = comando.replace("buscar", "").strip()

        return buscar_obsidian(termo)
    if comando_lower.startswith("o que voce sabe sobre") or comando_lower.startswith("o que você sabe sobre"):

        termo = comando_lower.replace("o que voce sabe sobre", "").replace("o que você sabe sobre", "").strip()

        memoria = buscar_obsidian(termo)

        prompt = f"""
    Você é a MENTE IA do Marllon.

    Responda usando APENAS as informações encontradas na memória abaixo.

    Se não encontrar nada útil, diga que ainda não tem memória suficiente sobre isso.

    TEMA:
    {termo}

    MEMÓRIA:
    {memoria}
    """

        return chamar_ia(prompt)
    if "criar arquivo" in comando_lower:

        partes = comando.split("criar arquivo ")

        if len(partes) > 1 and partes[1].strip() != "":
            nome = partes[1].strip()
        else:
            nome = "teste.py"

        conteudo = ""

        return criar_arquivo(nome, conteudo)

    if "ler arquivo" in comando_lower:

        nome = comando.split("ler arquivo ")[1]

        return ler_arquivo(nome)
    
    if "editar arquivo" in comando_lower:

        nome = "teste.py"

        novo_conteudo = """
print('ARQUIVO EDITADO PELA IA')
"""

        return editar_arquivo(nome, novo_conteudo)
    
    if "criar pasta" in comando_lower:

        nome = "nova_pasta"

        return criar_pasta(nome)

    if "deletar arquivo" in comando_lower:

        nome = "teste.py"

        return deletar_arquivo(nome)

    if "executar python" in comando_lower:

        nome = "teste.py"

        return executar_python(nome)
    
    if "terminal" in comando_lower:

        comando_terminal = comando.split("terminal ")[1]

        return executar_terminal(comando_terminal)
    if "criar api flask" in comando_lower:

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
    if "criar site" in comando_lower:

        tema = comando.replace("criar site", "").strip()

        if tema == "":
            tema = "site moderno"

        criar_pasta("site_ia")

        html = f'''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{tema}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>{tema}</h1>
    <p>Site criado automaticamente pela Mente IA.</p>
</body>
</html>
'''

        css = '''
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
'''

        criar_arquivo("site_ia/index.html", html)
        criar_arquivo("site_ia/style.css", css)

        return "Site HTML criado com sucesso."

    if "criar projeto python" in comando_lower:

        nome = comando.replace("criar projeto python", "").strip()

        if nome == "":
            nome = "novo_projeto"

        return criar_projeto_python(nome)
    if "corrigir erro" in comando_lower:

        erro = ler_arquivo("logs_erro.txt")

        prompt = f"""
Analise esse erro Python e explique como corrigir:

{erro}
"""

        return chamar_ia(prompt)
    if "gerar frontend login" in comando_lower:

        html = """
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Login MENTE IA</title>
        </head>
        <body>
            <h2>Login</h2>

            <form id="loginForm">
                <input type="text" id="username" placeholder="Usuário" required>
                <input type="password" id="password" placeholder="Senha" required>
                <button type="submit">Entrar</button>
            </form>

            <p id="mensagem"></p>
        </body>
        </html>
        """

        criar_arquivo("login.html", html)

        return "Frontend de login criado em login.html"
    
    if "gerar codigo" in comando_lower:

        pedido = comando.replace("gerar codigo", "").strip()

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
    
    if "auto corrigir" in comando_lower:

        nome = comando.replace("auto corrigir", "").strip()

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
    if "salvar ideia" in comando_lower:

        texto = comando.replace("salvar ideia", "").strip()

        return salvar_ideia(texto)
    if "salvar projeto" in comando_lower:

        texto = comando.replace("salvar projeto", "").strip()

        return salvar_projeto(texto)
    if "salvar aprendizado" in comando_lower:

        texto = comando.replace("salvar aprendizado", "").strip()

        return salvar_aprendizado(texto)
    return None
=======
>>>>>>> b0059289a59d53080a896a493402c868ab79f3f3

def escolher_agente(comando):

    comando = comando.lower()

    if "codigo" in comando or "python" in comando or "programar" in comando:

        return programmer_prompt()

    elif "arquitetura" in comando or "sistema" in comando or "backend" in comando:

        return architect_prompt()

    elif "startup" in comando or "dinheiro" in comando or "empresa" in comando:

        return business_prompt()

    return """
Você é a MENTE IA principal.
"""

def chamar_ia(comando, tools=None, tool_choice="auto"):
    
    modelo = escolher_modelo(comando)

    print(f"[MODELO ESCOLHIDO]: {modelo}")

    contexto_memoria = montar_contexto()
    memoria_obsidian = resumir_memoria()
    agente_escolhido = escolher_agente(comando)
    print(f"\n[AGENTE USADO]: {agente_escolhido[:40]}")

    messages = [
        {
            "role": "system",
            "content": f"""
{agente_escolhido}

MEMÓRIA DO USUÁRIO ATUAL:

O usuário desta conversa se chama Marllon.

As informações abaixo pertencem ao próprio usuário e devem ser usadas para responder perguntas sobre ele.

{memoria_obsidian}

MEMÓRIA RECENTE:

{contexto_memoria}
"""
        },
        {
            "role": "user",
            "content": comando
        }
    ]

    if tools:
        response = client.chat.completions.create(
            model=modelo,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice
        )
    else:
        response = client.chat.completions.create(
            model=modelo,
            messages=messages
        )

    return response.choices[0].message

def montar_contexto():

    memorias = ultimas_memorias()

    contexto = ""

    for item in memorias:

        contexto += f"""
Usuário: {item['usuario']}
IA: {item['ia']}
"""

    return contexto

# =========================
# CÉREBRO CENTRAL
# =========================
def cerebro(comando):

    response = chamar_ia(comando, tools=available_tools)
    message = response

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        if function_name in function_map:
            # Executar a função mapeada
            try:
                # Desempacotar argumentos diretamente para a função
                tool_output = function_map[function_name](**function_args)
            except TypeError as e:
                tool_output = f"Erro ao executar a ferramenta {function_name}: {e}. Argumentos fornecidos: {function_args}"
        else:
            tool_output = f"Ferramenta {function_name} não encontrada."

        # Enviar a saída da ferramenta de volta para o modelo
        second_response = client.chat.completions.create(
            model=escolher_modelo(comando),
            messages=[
                {"role": "system", "content": escolher_agente(comando)},
                {"role": "user", "content": comando},
                message,
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_output,
                },
            ],
        )
        return second_response.choices[0].message.content

    else:
        # Se não houver tool_calls, é uma resposta normal
        adicionar_memoria(comando, message.content)
        return message.content

# =========================
# LOOP PRINCIPAL
# =========================

if __name__ == "__main__":

    print("[bold green]MENTE IA ONLINE[/bold green]")
    speak("Olá, eu sou a Mente IA. Como posso ajudar?")

    while True:
        comando = listen()

        if comando.lower() == "sair":
            speak("Sistema encerrado.")
            print("[red]Sistema encerrado.[/red]")
            break
        
        if comando:
            resposta = cerebro(comando)
            print(f"\n[cyan]MENTE IA:[/cyan]\n{resposta}")
            speak(resposta)
