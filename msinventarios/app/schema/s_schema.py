from app.models import Stock
from marshmallow import validate, fields, Schema, post_load

class StockSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    fecha_transaccion= fields.String(required=True)
    cantidad = fields.Float(required=True)
    entrada_salida = fields.Integer(required=True)

    @post_load
    def make_pago(self, data, **kwargs):
        return Stock(**data)