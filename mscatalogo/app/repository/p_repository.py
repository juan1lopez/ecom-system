from typing import List
from app.models import Producto
from app import db

class ProductoRepository:

    def save(self, producto: Producto) -> Producto:
        db.session.add(producto)
        db.session.commit()
        return producto

    def all(self) -> List[Producto]:
        productos = db.session.query(Producto).all()
        return productos
