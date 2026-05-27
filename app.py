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

portafolios = [
    {
        "id": 1,
        "cliente_id": 1,
        "nombre": "Portafolio Conservador",
        "valor_total": 1500000,
        "moneda": "CLP"
    },
    {
        "id": 2,
        "cliente_id": 2,
        "nombre": "Portafolio Balanceado",
        "valor_total": 2500000,
        "moneda": "CLP"
    },
    {
        "id": 3,
        "cliente_id": 3,
        "nombre": "Portafolio Crecimiento",
        "valor_total": 3500000,
        "moneda": "CLP"
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

@app.route("/portafolios", methods=["GET"])
def obtener_portafolios():
    return jsonify({
        "portafolios": portafolios
    }), 200

@app.route("/portafolios/<int:portafolio_id>", methods=["GET"])
def obtener_portafolio_por_id(portafolio_id):
    for portafolio in portafolios:
        if portafolio["id"] == portafolio_id:
            return jsonify({
                "portafolio": portafolio
            }), 200
    
    return jsonify({
        "error": "Portafolio no encontrado"
    }), 404

@app.route("/portafolios", methods=["POST"])
def crear_portafolio():
    if not request.is_json:
        return jsonify({
            "error": "La solicitud debe enviarse en formato JSON"
        }), 400
    
    data = request.get_json()

    cliente_id = data.get("cliente_id")
    nombre = data.get("nombre")
    valor_total = data.get("valor_total")
    moneda = data.get("moneda")

    if not cliente_id or not nombre or not valor_total or not moneda:
        return jsonify({
            "error": "Todos los campos son obligatorios"
        }), 400

    nuevo_portafolio = {
        "id": len(portafolios) + 1,
        "cliente_id": data["cliente_id"],
        "nombre": data["nombre"],
        "valor_total": data["valor_total"],
        "moneda": data["moneda"]
    }

    portafolios.append(nuevo_portafolio)
    
    return jsonify({
        "mensaje": "Portafolio creado correctamente",
        "portafolio": nuevo_portafolio
    }), 201