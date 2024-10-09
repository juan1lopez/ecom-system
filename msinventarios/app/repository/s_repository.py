from typing import List
from app.models import Stock
from app import db

class StockRepository:
    @staticmethod
    def save(stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock
    
    @staticmethod
    def all() -> List[Stock]:
        productos = db.session.query(Stock).all()
        return productos
