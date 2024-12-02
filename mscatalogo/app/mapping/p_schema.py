from app.models import Producto
from marshmallow import validate, fields, Schema, post_load

class ProductoSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True)
    precio = fields.Float(required=True, validate=validate.Range(min=0))
    activado = fields.Boolean(required=True)

    @post_load
    def make_producto(self, data, **kwargs):
        return Producto(**data)