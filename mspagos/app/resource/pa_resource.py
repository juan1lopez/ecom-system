from flask import Blueprint, jsonify, request, abort
from app.service import PagoService
from app.schema import PagoSchema
import requests 

pago_blueprint = Blueprint('pagos', __name__)
pago_service = PagoService()
pago_schema = PagoSchema()
pagos_schema = PagoSchema(many=True)

CATALOGO_URL = "http://localhost:5000/catalogo/productos/todos"  # URL del microservicio de catálogo y traigo todos los prods del catalogo

@pago_blueprint.route('/', methods=['GET'])
def obtener_compras():
    pagos = pago_service.obtener_todos()
    return pagos_schema.jsonify(pagos), 200

@pago_blueprint.route('/', methods=['POST'])
def agregar_pago():
    json_data = request.get_json()

    producto_nombre = json_data.get("producto_id")
    medio_pago = json_data.get("medio_pago")
    
    if not json_data or 'producto_id' not in json_data or 'medio_pago' not in json_data:
        abort(400, description="Los datos de pago son inválidos.")
    
    producto_id = json_data['producto_id']
    medio_pago = json_data['medio_pago']

    # Comprobar si el producto existe en el catálogo
    productos = requests.get(CATALOGO_URL)
    
    for producto in productos:
        if producto["nombre"] == producto_nombre:
            producto_id = producto["id"] 
            precio_real = producto["precio"]               
        else:
            abort(400, description="El producto no existe en el catálogo.")

    pago_data = {
        "producto_id": producto_id,
        "precio": precio_real,
        "medio_pago": medio_pago
    }
    pago = pago_schema.load(pago_data)  # Validar y cargar el esquema
    pago_guardado = pago_service.guardar(pago)  # Guardar la compra en la base de datos


    return pago_schema.jsonify(pago_guardado), 201