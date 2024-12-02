import logging
from flask import Blueprint, jsonify, request, abort
from app.service import CompraService
from app.mapping import CompraSchema
from datetime import datetime
import requests 

compra_blueprint = Blueprint('compras', __name__)
compra_service = CompraService()
compra_schema = CompraSchema()
compras_schema = CompraSchema(many=True)

@compra_blueprint.route("/obtener/<int:id>", methods=["GET"])
def obtener_compra(id):
    """
    Endpoint para obtener una compra específica por ID.
    Utiliza caché para acceder rápidamente si está disponible.
    """        
    compra = compra_service.find(id)  # Llama al método 'find' del servicio
    if not compra:
        logging.warning(f"Compra con ID {id} no encontrada.")
        abort(404, description="Compra no encontrada.")
        
    logging.info(f"Compra {id} obtenida exitosamente.")
    return compra_schema.dump(compra), 200
    
@compra_blueprint.route("/agregar", methods=["POST"])
def guardar_compra():
    """
    Endpoint para crear una nueva compra.
    Guarda en la base de datos y actualiza el caché.
    """
    try:
        # Valida y deserializa los datos entrantes
        data = request.get_json()
        compra = compra_schema.load(data)

        # Guarda la compra
        nueva_compra = compra_service.save(compra)
        logging.info(f"Compra creada exitosamente: {nueva_compra}")
        
        return compra_schema.dump(nueva_compra), 201
    except Exception as e:
        logging.error(f"Error al guardar la compra: {str(e)}")
        abort(500, description="Error interno del servidor.")

@compra_blueprint.route("/borrar/<int:id>", methods=["DELETE"])
def borrar_compra(id):
    """
    Endpoint para eliminar una compra por ID.
    Elimina tanto en la base de datos como en el caché.
    """
    
    compra = compra_service.delete(id)  # Llama al método 'delete' del servicio
    if not compra:
        logging.warning(f"Compra con ID {id} no encontrada.")
        abort(404, description="Compra no encontrada.")

    logging.info(f"Compra {id} eliminada exitosamente.")
    return jsonify({"message": f"Compra {id} eliminada exitosamente."}), 200
    