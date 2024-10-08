from flask import Blueprint, jsonify, request
from app.service import ProductoService
from app.schema import ProductoSchema

producto_blueprint = Blueprint('productos', __name__)
producto_service = ProductoService()
producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

@producto_blueprint.route('/todos', methods=['GET'])
def obtener_productos():
    productos = producto_service.obtener_todos()
    return productos_schema.jsonify(productos), 200

@producto_blueprint.route('/', methods=['POST'])
def agregar_producto():
    json_data = request.get_json()
    producto = producto_schema.load(json_data)
    producto_guardado = producto_service.guardar(producto)
    return producto_schema.jsonify(producto_guardado), 201
