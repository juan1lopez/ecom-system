from typing import List
from app.models import Stock
from app import db

class StockRepository:

    def save(self, stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock

    def all(self) -> List[Stock]:
        productos = db.session.query(Stock).all()
        return productos
