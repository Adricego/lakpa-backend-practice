from flask import Flask, jsonify, request

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

@app.route("/clientes/<int:cliente_id>", methods=["GET"])
def obtener_cliente_por_id(cliente_id):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return jsonify({
                "cliente": cliente
            }), 200
    
    return jsonify({
        "error": "Cliente no encontrado"
    }), 404

@app.route("/clientes", methods=["POST"])
def crear_cliente():
    if not request.is_json:
        return jsonify({
            "error": "La solicitud debe enviarse en formato JSON"
        }), 400
    
    data = request.get_json()

    nombre = data.get("nombre")
    email = data.get("email")

    if not nombre or not email:
        return jsonify({
            "error": "Nombre y email son obligatorios"
        }), 400

    nuevo_cliente = {
        "id": len(clientes) + 1,
        "nombre": data["nombre"],
        "email": data["email"]
    }

    clientes.append(nuevo_cliente)
    
    return jsonify({
        "mensaje": "Cliente creado correctamente",
        "cliente": nuevo_cliente
    }), 201