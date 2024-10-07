from sqlalchemy import Boolean, Column, Integer, String
from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Producto(db.Model):
    __tablename__ = 'productos'
    id: int = db.Column(Integer, primary_key=True)
    nombre: str = db.Column(String, nullable=False)
    precio: int = db.Column(Integer, nullable=False)
    activado: bool = db.Column(Boolean, nullable=False, default=True)
