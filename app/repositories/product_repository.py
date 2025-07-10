from abc import ABC

from app.models.product import Product

class ProductRepository(ABC):

    def get_all(self) -> list[Product]:
        pass

    def get_by_id(self, product_id: str) -> Product:
        pass

    def delete(self, product: Product) -> None:
        pass

    def update(self, product: Product) -> None:
        pass

    def create(self, product: Product) -> None:
        pass