from app.models import Compra
from marshmallow import fields, Schema, post_load

class CompraSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    fecha_compra = fields.String(required=True)
    direccion_envio = fields.String(required=True)

    @post_load
    def make_compra(self, data, **kwargs):
        return Compra(**data)