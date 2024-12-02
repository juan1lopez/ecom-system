from flask import Blueprint, jsonify, request
from app.service import ProductoService
from app.mapping import ProductoSchema

producto_blueprint = Blueprint('productos', __name__)

producto_service = ProductoService()
producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

@producto_blueprint.route('/', methods=['GET'])
def home():
    return "el sistema esta andando",200

@producto_blueprint.route('/buscar/<int:id>', methods=['GET'])
def get_producto(id: int):
    result = producto_schema.dump(producto_service.find(id))
    if result:
        status_code = 200 
    else:
        status_code = 404
    return result, status_code # Enviar la lista serializada en formato JSON

@producto_blueprint.route('/guardar', methods=['POST'])
def agregar_producto():
    json_data = request.get_json()
    
    producto = producto_schema.load(json_data)  # Deserializar los datos del JSON a un objeto Producto
    producto_guardado = producto_service.guardar(producto)
    
    producto_data = producto_schema.dump(producto_guardado)  # Serializar el producto guardado
    
    return jsonify(producto_data), 201  # Devolver el producto serializado en formato JSON
