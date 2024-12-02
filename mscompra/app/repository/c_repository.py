from app import db
from app.models import Compra

class CompraRepository:

    def save(self, compra: Compra) -> Compra:
        db.session.add(compra)
        db.session.commit()
        return compra

    def find(self, id: int) -> Compra:
        return Compra.query.get(id)

    def delete(self, compra: Compra) -> bool:
        db.session.delete(compra)
        db.session.commit()
        return True
