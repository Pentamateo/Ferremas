from sqlalchemy.orm import Session
from app.models.order import Order
from app.repositories.order_repository import OrderRepository
from app.repositories.product_repository import ProductRepository

class OrderService:
    def __init__(self, db: Session):
        self.repo = OrderRepository(db)
        self.product_repo = ProductRepository(db)

    def create_order(self, order_data: Order):
        # product = self.product_repo.db.query(self.product_repo.db.query(self.product_repo.db.mapper.class_, self.product_repo.db.bind).mapper.class_).filter_by(id=order_data.product_id).first()
        # product = self.product_repo.db.query(self.product_repo.db.query(ProductRepository.__annotations__.get('db', None)).mapper.class_).filter_by(id=order_data.product_id).first()
        # product = self.product_repo.db.query(self.product_repo.db.query(ProductRepository.__annotations__.get('db', None)).mapper.class_).filter_by(id=order_data.product_id).first()
        # products = self.product_repo.get_all()
        # product = next((p for p in products if p.id == order_data.product_id), None)
        # if not product:
        #     raise Exception("Producto no encontrado")
        # total_price = product.price * order_data.quantity
        # return self.repo.create(order_data, total_price)
        pass

    def get_order(self, order_id: int):
        # return self.repo.get_by_id(order_id)
        pass
