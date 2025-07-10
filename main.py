from fastapi import FastAPI

from app.routes.currency import currency_router
from app.routes.product import product_router


app = FastAPI(title="API con 4 Integraciones")

app.include_router(product_router, prefix="/products", tags=["Productos"])
# app.include_router(order_routes.router, prefix="/orders", tags=["Pedidos"])
# app.include_router(webpay_routes.router, prefix="/webpay", tags=["WebPay"])
# app.include_router(currency_router, prefix="/currency", tags=["Cambio de Divisas"])
