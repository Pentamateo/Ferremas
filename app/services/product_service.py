from sqlalchemy.orm import Session
from app.db.postgresql_manager import PostgreConnectionManager
from app.schemas.product import Product as ProductSchema
from app.models.product import Product
from app.repositories.product_repository import ProductRepository

class ProductService(ProductRepository):

    def __init__(
        self,
        db: PostgreConnectionManager
    ):
        self.db = db        
        super().__init__()

    def get_all(self) -> list[Product]:
        stmnt = self.db.session.query(ProductSchema).all()
        products = list(map(lambda row: Product(row.id, row.name,row. description, row.price, row.quantity), stmnt))
        print(products)
        return products 

    def get_by_id(self, product_id: str) -> Product:
        row = self.db.session.query(ProductSchema).filter(ProductSchema.id == product_id).first()
        if row is None:
         return None
        return Product(
        row.id,
        row.name,
        row.description,
        row.price,
        row.quantity
    )
    def delete(self, product_id: str) -> bool:
        existing = self.db.session.query(ProductSchema).filter(ProductSchema.id == product_id).first()
        if existing is None:
            return False
        self.db.session.delete(existing)
        self.db.session.commit()
        return True

    def update(self, product_data: dict) -> Product | None:
        existing = self.db.session.query(ProductSchema).filter(ProductSchema.id == product_data["id"]).first()

        if existing is None:
            print("Producto no encontrado con ID:", product_data["id"])
            return None

        existing.name = product_data["name"]
        existing.description = product_data.get("description")
        existing.price = product_data["price"]
        existing.quantity = product_data["quantity"]

        self.db.session.commit()
        self.db.session.refresh(existing)

        return Product(
        existing.id,
        existing.name,
        existing.description,
        existing.price,
        existing.quantity
    )
    
    def create(self, product_data = dict) -> None:
        product_schema = ProductSchema(**product_data)
        self.db.session.add(product_schema)
        self.db.session.commit()
        self.db.session.refresh(product_schema)
       
        return Product(
            product_schema.id,
            product_schema.name,
            product_schema.description,
            product_schema.price,
            product_schema.quantity
    )