from app.repository import ProductoRepository

producto_repository = ProductoRepository()

class ProductoService:

    def obtener_todos(self):
        return producto_repository.all()

    def guardar(self, producto):
        return producto_repository.save(producto)
    
    def modificar_cantidad(self, producto_id, nueva_cantidad):
        # Aquí puedes agregar más lógica de validación
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        
        # Intentar actualizar la cantidad en el repositorio
        producto_actualizado = producto_repository.update_cantidad(producto_id, nueva_cantidad)
        
        if not producto_actualizado:
            raise Exception("El producto con el ID especificado no existe.")
        
        return producto_actualizado
