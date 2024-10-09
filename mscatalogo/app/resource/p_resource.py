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
    productos_data = productos_schema.dump(productos)  # Serializar la lista de productos
    return jsonify(productos_data), 200  # Enviar la lista serializada en formato JSON

@producto_blueprint.route('/', methods=['POST'])
def agregar_producto():
    json_data = request.get_json()
    producto = producto_schema.load(json_data)  # Deserializar los datos del JSON a un objeto Producto
    producto_guardado = producto_service.guardar(producto)
    producto_data = producto_schema.dump(producto_guardado)  # Serializar el producto guardado
    return jsonify(producto_data), 201  # Devolver el producto serializado en formato JSON

# Nueva ruta para modificar la cantidad del producto
@producto_blueprint.route('/<int:producto_id>/modificar_cantidad', methods=['PUT'])
def modificar_cantidad_producto(producto_id):
    try:
        # Obtener el JSON de la solicitud
        json_data = request.get_json()

        # Validar que la nueva cantidad esté en el JSON
        if 'nueva_cantidad' not in json_data:
            return jsonify({"error": "La nueva cantidad es requerida"}), 400

        nueva_cantidad = json_data['nueva_cantidad']

        # Llamar al servicio para actualizar la cantidad del producto
        producto_actualizado = producto_service.modificar_cantidad(producto_id, nueva_cantidad)

        # Serializar el producto actualizado
        producto_data = producto_schema.dump(producto_actualizado)

        # Devolver el producto actualizado
        return jsonify(producto_data), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "El producto no se pudo actualizar o no existe"}), 404