from typing import List
from app.models import Pago
from app import db

class PagoRepository:

    def save(self, pago: Pago) -> Pago:
        db.session.add(pago)
        db.session.commit()
        return pago

    def all(self) -> List[Pago]:
        productos = db.session.query(Pago).all()
        return productos
