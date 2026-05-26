from flask import Flask, jsonify

app = Flask(__name__)

clientes = [
    {
        "id": 1,
        "nombre": "Camila Rojas",
        "email": "camila.rojas@email.com"
    },
    {
        "id": 2,
        "nombre": "Pedro Soto",
        "email": "pedro.soto@email.com"
    },
    {
        "id": 3,
        "nombre": "Ana Torres",
        "email": "ana.torres@email.com"
    }
]

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok"
        }), 200

@app.route("/clientes", methods=["GET"])
def obtener_clientes():
    return jsonify({
        "clientes": clientes
    }), 200


