from typing import List
from app.models import Producto
from app import db

class ProductoRepository:

    def save(self, producto: Producto) -> Producto:
        db.session.add(producto)
        db.session.commit()
        return producto

    def find(self, id: int) -> Producto:
        result = None
        if id is not None:
            result = db.session.query(Producto).filter(Producto.id == id, Producto.activado == True).one_or_none()
        return result

    # def all(self) -> List[Producto]:
    #     productos = db.session.query(Producto).all()
    #     return productos

    # @staticmethod
    # def update_cantidad(producto_id, nueva_cantidad):
    #     # Buscar el producto por su ID
    #     producto = Producto.query.get(producto_id)
        
    #     if not producto:
    #         return None  # El producto no existe
    #     # Actualizar la cantidad (stock)
    #     producto.stock = nueva_cantidad
    #     # Guardar los cambios en la base de datos
    #     db.session.commit()
    #     return producto  # Retornar el producto actualizado