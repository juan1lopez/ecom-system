from app.repository import StockRepository

stock_repository = StockRepository()

class StockService:

    def obtener_todos(self):
        return StockRepository.all()

    def guardar(self, pago):
        return StockRepository.save(pago)
