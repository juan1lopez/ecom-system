from typing import List
from app.models import Pago
from app import db

class PagoRepository:
    @staticmethod
    def save(pago: Pago) -> Pago:
        db.session.add(pago)
        db.session.commit()
        return pago

    @staticmethod
    def all() -> List[Pago]:
        productos = db.session.query(Pago).all()
        return productos
