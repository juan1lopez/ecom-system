from app.models import Producto
from app.repository import ProductoRepository
from app import cache
from flask import abort

repository = ProductoRepository()

class ProductoService:

    def find(self, id: int) -> Producto:
        """
        Busca un producto por su ID, utilizando cache para mejorar la eficiencia.
        
        - Si el producto está en el caché, se devuelve directamente.
        - Si no está en el caché, se consulta en el repositorio y se almacena en el caché.
        - Si el producto no existe en el repositorio, devuelve un error 404.
        """
        if id is not None: # valido si el id consultado 
            # Intentar obtener el producto del caché
            result = cache.get(f"producto_{id}") #busco si el producto esta en cache
            if result is not None:
                print(f"Producto {id} obtenido del caché")  # Producto encontrado en cache
            else:
                print(f"Producto {id} no está en el caché. Consultando el repositorio...")
            
                result = repository.find(id) # Buscar el producto en el repositorio

                if result is None: # Manejar el caso en que el producto no exista
                    abort(404, description="Product not found")
                
                cache.set(f"producto_{id}", result, timeout=30) # Guardar el resultado en el caché con un tiempo de expiración
                
        return result

    def guardar(self, producto: Producto) -> Producto:
        # Guardar el producto en el repositorio
        producto = repository.save(producto)
        cache.set(f"producto_{producto.id}", producto, timeout=30)
        return producto