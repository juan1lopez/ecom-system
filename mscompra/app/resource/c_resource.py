from flask import Blueprint, jsonify, request, abort
from app.service import CompraService
from app.schema import CompraSchema
from datetime import datetime
import requests 

compra_blueprint = Blueprint('compras', __name__)
compra_service = CompraService()
compra_schema = CompraSchema()
compras_schema = CompraSchema(many=True)

CATALOGO_URL = "http://localhost:5000/productos/todos"  # URL del microservicio de catálogo y traigo todos los prods del catalogo

@compra_blueprint.route('/', methods=['GET'])
def obtener_compras():
    compras = compra_service.obtener_todos()
    return compras_schema.dump(compras), 200

@compra_blueprint.route('/', methods=['POST'])
def agregar_compra():
    json_data = request.get_json()
    #print(json_data)
    # Extraer el nombre del producto
    producto_nombre = json_data.get("producto_id")
    fecha_compra = json_data.get("fecha_compra")
    direccion_envio = json_data.get("direccion_envio")

    response = requests.get(CATALOGO_URL)

    if response.status_code != 200:
        abort(500, description="Error al obtener productos del catálogo.")
    if response.status_code != 200:
        abort(500, description="Error al obtener productos del catálogo.")

    productos = response.json()
    print(productos)

    # Buscar el producto por nombre y obtener el ID
    producto_id = None
    for producto in productos:
        if producto["nombre"] == producto_nombre:
            producto_id = producto["id"]
            break  # Salir del bucle si encontramos el producto

    if not producto_id:
        abort(400, description="El producto no existe en el catálogo.")

    compra_data = {
        "producto_id": producto_id,
        "fecha_compra": fecha_compra,
        "direccion_envio": direccion_envio
    }
    print(compra_data)

    compra = compra_schema.load(compra_data)  # Validar y cargar el esquema
    compra_guardado = compra_service.guardar(compra)  # Guardar la compra en la base de datos

    return compra_schema.dump(compra_guardado), 201