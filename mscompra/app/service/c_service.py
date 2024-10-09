from app.repository import CompraRepository

compra_repository = CompraRepository()

class CompraService:

    def obtener_todos(self):
        # Llamar al método 'all' desde la instancia 'compra_repository'
        return CompraRepository.all()

    def guardar(self, producto):
        # Llamar al método 'save' desde la instancia 'compra_repository'    
        return CompraRepository.save(producto)