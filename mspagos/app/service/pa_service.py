from app.repository import PagoRepository

pago_repository = PagoRepository()

class PagoService:

    def obtener_todos(self):
        return PagoRepository.all()

    def guardar(self, pago):
        return PagoRepository.save(pago)
