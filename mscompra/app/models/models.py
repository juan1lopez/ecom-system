from sqlalchemy import Boolean, Column, Integer, String, DateTime
from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Compra(db.Model):
    __tablename__ = 'compras'
    id: int = db.Column(Integer, primary_key=True)
    producto_id: int = db.Column(Integer, nullable=False)
    fecha_compra: int = db.Column(DateTime, nullable=False)
    direccion_envio: str = db.Column(String, nullable=False)