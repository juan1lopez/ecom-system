from sqlalchemy import Boolean, Column, Integer, String, DateTime, Float
from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Pago(db.Model):
    __tablename__ = 'pagos'
    id: int = db.Column(Integer, primary_key=True)
    producto_id: int = db.Column(Integer, nullable=False)
    precio: float = db.Column(Float, nullable=False)
    medio_pago: str = db.Column(String, nullable=False)