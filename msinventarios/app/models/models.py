from sqlalchemy import Boolean, Column, Integer, String, DateTime
from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Stock(db.Model):
    __tablename__ = 'transacciones'
    id: int = db.Column(Integer, primary_key=True)
    producto_id: int = db.Column(Integer, nullable=False)
    fecha_transaccion: int =db.column(DateTime, nullable=False)
    cantidad: float = db.Column(float, nullable=False)
    entrada_salida: int = db.Column(Integer, nullable=False) # 1:entrada o 2:salida