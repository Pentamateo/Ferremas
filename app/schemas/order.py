from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = "order"

    id = Column(String, primary_key=True, index=True)
    product_id = Column(Integer)
    quantity = Column(Integer)
    total_price = Column(Float)
    branch = Column(String)
    paid = Column(Boolean, default=False)
