from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from main import cerebro
from flask import Flask, jsonify, send_from_directory, request
from tools.file_tools import gerar_status_json, gerar_memoria_json

app = Flask(__name__, static_folder="site_ia")
CORS(app)

@app.route("/")
def home():
    return send_from_directory("site_ia", "index.html")

@app.route("/site_ia/<path:arquivo>")
def site_ia(arquivo):
    return send_from_directory("site_ia", arquivo)

@app.route("/atualizar-dashboard")
def atualizar_dashboard():
    gerar_status_json()
    return jsonify({"status": "ok", "mensagem": "Dashboard atualizado"})
@app.route("/atualizar-memoria")
def atualizar_memoria():
    gerar_memoria_json()
    return jsonify({"status": "ok", "mensagem": "Memória atualizada"})
@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json()
    comando = dados.get("comando", "")

    resposta = cerebro(comando)

    return jsonify({
        "resposta": resposta
    })
if __name__ == "__main__":
    app.run(debug=True, port=5000)