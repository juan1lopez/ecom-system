from datetime import datetime
from app.models import Compra
from app.repository import CompraRepository
from app import cache

repository = CompraRepository()

class CompraService:

    def save(self, compra: Compra) -> Compra:
        """
        Guarda una nueva compra, estableciendo la fecha actual y almacenándola en caché.
        """
        compra.fecha_compra = datetime.now()
        result = repository.save(compra)  # Llama al método save del repositorio
        
        if result:
            cache.set(f"compra_{result.id}", result, timeout=60)  # Guarda en caché con un timeout de 60 segundos
        
        return result

    def delete(self, id: int) -> Compra:
        """
        Elimina una compra por su ID y limpia la caché asociada a esa compra.
        """
        # Busca la compra antes de intentar eliminarla
        compra = repository.find(id)
        if not compra:
            return None  # Maneja el caso cuando no se encuentra la compra

        # Elimina la compra de la base de datos
        result = repository.delete(compra)

        # Si se eliminó correctamente, elimina también del caché
        if result:
            cache.delete(f"compra_{id}")
        
        return result

    def find(self, id: int) -> Compra:
        """
        Busca una compra específica por ID utilizando caché.
        """
        result = cache.get(f"compra_{id}")
        
        if result is None:
            # Si no está en caché, consulta la base de datos y actualiza el caché
            result = repository.find(id)
            if result:
                cache.set(f"compra_{id}", result, timeout=60)
        
        return result
