from app.models import Pago
from marshmallow import validate, fields, Schema, post_load

class PagoSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    precio = fields.Float(required=True)
    medio_pago = fields.String(required=True)

    @post_load
    def make_pago(self, data, **kwargs):
        return Pago(**data)