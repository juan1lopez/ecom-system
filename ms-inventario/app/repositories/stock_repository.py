from app import db
from typing import List
from app.models import Stock
import logging
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError 
from sqlalchemy import func, case
import threading

class StockRepository:
    _lock = threading.Lock()  # Lock para sincronizar los hilos

    def save(self, stock: Stock) -> Stock:
        # Adquirir el Lock para garantizar que solo un hilo ejecute esta parte
        with self._lock:
            try:
                # Operación crítica, guardando el stock en la base de datos
                db.session.add(stock)
                db.session.commit()
                return stock
            except Exception as e:
                # Deshacer la transacción en caso de error
                db.session.rollback()
                raise e
    
    def cuantity(self, producto_id: int) -> float:
        entradas = db.session.query(
            func.sum(case((Stock.entrada_salida == 1, Stock.cantidad), else_=0))
        ).filter(Stock.producto == producto_id).scalar() or 0

        salidas = db.session.query(
            func.sum(case((Stock.entrada_salida == 2, Stock.cantidad), else_=0))
        ).filter(Stock.producto == producto_id).scalar() or 0

        return entradas - salidas
                   






# 50 compras por segundo
#1)test de carga con k6 de servidor de desarrollo
# docker build -f ./Dockerfile.gunicorn -t app-commerce:gunicorn
# test de carga con k6 de servidor de gunicorn
# docker build -f ./Dockerfile -t app-commerce:uwsgi
# test de carga con k6 de servidor de uwsgi
# test de carga aplicando traefik  con balanceo de carga y escalado horizontal



#mkcert