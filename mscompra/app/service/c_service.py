from app.repository import CompraRepository

compra_repository = CompraRepository()

class CompraService:

    def obtener_todos(self):
        return CompraRepository.all()

    def guardar(self, producto):
        return CompraRepository.save(producto)
