from typing import List
from app.models import Compra
from app import db

class CompraRepository:

    def save(self, compra: Compra) -> Compra:
        db.session.add(compra)
        db.session.commit()
        return compra

    def all(self) -> List[Compra]:
        productos = db.session.query(Compra).all()
        return productos
