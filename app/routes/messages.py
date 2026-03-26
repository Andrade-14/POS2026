from flask import Blueprint, jsonify, request

messages_bp = Blueprint("messages", __name__)

@messages_bp.route("/", methods=["Post"])
def enviar_mensagem():
    return ""

@messages_bp.route("/", methods=["Get"])
def listar_mensagens():
    return jsonify({
        "mensagens": [
            "Primeira mensagem",
            "Segunda mensagem"
        ]
    })

