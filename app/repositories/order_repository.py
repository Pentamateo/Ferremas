from abc import ABC
from sqlalchemy.orm import Session
from app.models.order import Order

class OrderRepository(ABC):

    def create(self, order: Order) -> None:
        pass

    def get_by_id(self, order_id) -> Order:
        pass

    # def create(self, order_data: OrderCreate, total_price: float):
    #     order = Order(**order_data.dict(), total_price=total_price)
    #     self.db.add(order)
    #     self.db.commit()
    #     self.db.refresh(order)
    #     return order

    # def get_by_id(self, order_id: int):
    #     return self.db.query(Order).filter(Order.id == order_id).first()
