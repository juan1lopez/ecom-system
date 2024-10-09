from typing import List
from app.models import Compra
from app import db

class CompraRepository:
    @staticmethod
    def save(compra: Compra) -> Compra:
        db.session.add(compra)
        db.session.commit()
        return compra
    @staticmethod
    def all() -> List[Compra]:
        productos = db.session.query(Compra).all()
        return productos
