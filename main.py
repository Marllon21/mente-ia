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
