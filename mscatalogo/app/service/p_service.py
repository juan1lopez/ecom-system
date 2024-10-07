from app.repository import ProductoRepository

producto_repository = ProductoRepository()

class ProductoService:

    def obtener_todos(self):
        return producto_repository.all()

    def guardar(self, producto):
        return producto_repository.save(producto)
