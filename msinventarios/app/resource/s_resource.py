from flask import Blueprint, jsonify, request, abort
from app.service import StockService
from app.schema import StockSchema
import requests 
from datetime import datetime


stock_blueprint = Blueprint('stock', __name__)
stock_service = StockService()
stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)

CATALOGO_URL = "http://localhost:5000/productos/todos"  # URL del microservicio de catálogo y traigo todos los prods del catalogo
CANTIDAD_URL = "http://localhost:5000/{}/modificar_cantidad"


@stock_blueprint.route('/', methods=['GET'])
def obtener_compras():
    stocks = stock_service.obtener_todos()
    return stocks_schema.dump(stocks), 200


@stock_blueprint.route('/', methods=['POST'])
def agregar_transaccion():
    json_data = request.get_json()

    # Validación de la estructura del JSON
    if not json_data or 'producto_id' not in json_data or 'fecha_transaccion' not in json_data or 'cantidad' not in json_data or 'entrada_salida' not in json_data:
        return jsonify({"error": "Datos faltantes en la transacción"}), 400
    # Convertir fecha a formato adecuado
    try:
        fecha_transaccion = datetime.strptime(json_data['fecha_transaccion'], '%d/%m/%Y')
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido, use dd/mm/yyyy"}), 400

    producto_nombre = json_data.get("producto_id")
    fecha_transaccion = json_data.get("fecha_transaccion")
    entrada_salida = json_data.get("entrada_salida")
    cantidad_actual = json_data.get("cantidad")

    # Consultar el catálogo de productos
    response = requests.get(CATALOGO_URL)

    if response.status_code != 200:
        return jsonify({"error": "No se pudo consultar el catálogo de productos"}), 500
    
    productos = response.json()

    # # Verificar si el producto existe
    # producto = next((p for p in productos if p['id'] == json_data['producto_id']), None)
    # if not producto:
    #     return jsonify({"error": "Producto no encontrado en el catálogo"}), 404
    
    # Buscar el producto por nombre y obtener el ID
    producto_id = 0
    for producto in productos:
        if producto["nombre"] == producto_nombre:
            producto_id = producto["id"]
            # cantidad_actual = producto['stock']  # Asumimos que el stock es parte de los datos del producto
            break  # Salir del bucle si encontramos el producto
    # Obtener la cantidad actual del producto
    
    # Lógica para manejar la transacción
    # if json_data['entrada_salida'] == 1:  # Entrada
    #     nueva_cantidad = cantidad_actual + json_data['cantidad']
    # elif json_data['entrada_salida'] == 2:  # Salida
    #     if cantidad_actual < json_data['cantidad']:
    #         return jsonify({"error": "No hay suficiente stock para realizar la salida"}), 400
    #     nueva_cantidad = cantidad_actual - json_data['cantidad']
    # else:
    #     return jsonify({"error": "Entrada/salida debe ser 1 o 2"}), 400

    # Guardar la transacción en la base de datos
    transaccion_data = {
        "producto_id": producto_id,
        "fecha_transaccion": fecha_transaccion,
        "cantidad": cantidad_actual,
        "entrada_salida": entrada_salida
    }
    transaccion = stock_schema.load(transaccion_data)  # Validar y cargar el esquema
    transaccion_guardado = stock_service.guardar(transaccion)  # Guardar la compra en la base de datos

    return stock_schema.dump(transaccion_guardado), 201
    #stock_service.guardar(transaccion_data)

    # Actualizar la cantidad en el catálogo
    # actualizar_stock_url = CANTIDAD_URL.format(json_data['producto_id'])
    # actualizar_stock_data = {
    #     'cantidad': nueva_cantidad
    # }
    # update_response = requests.post(actualizar_stock_url, json=actualizar_stock_data)

    # if update_response.status_code not in [200, 204]:
    #     return jsonify({"error": "No se pudo actualizar la cantidad en el catálogo"}), 500

    #return jsonify(stock_schema.dump(transaccion_data)), 201