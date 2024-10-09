from app.repository import PagoRepository

pago_repository = PagoRepository()

class PagoService:

    def __init__(self):
        self.pago_repository = PagoRepository()  # Crea una instancia de PagoRepository

    def obtener_todos(self):
        return self.pago_repository.all()  # Llama al método de la instancia
    
    @staticmethod
    def guardar(pago):
        return PagoRepository.save(pago)
