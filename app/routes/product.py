from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse
from app.db.postgresql_manager import PostgreConnectionManager
from app.services.product_service import ProductService

product_router = APIRouter()
database = PostgreConnectionManager()
product_service = ProductService(database)

@product_router.get("/products")
def list_products():
    product_list = product_service.get_all()
    return JSONResponse(
        content = [product.__dict__ for product in product_list]
    )

@product_router.get("/products")
def get_product(product_id: str):
    product = product_service.get_by_id(product_id)
    if product is None:
        return JSONResponse(status_code=404, content={"message": "Producto no encontrado"})
    return JSONResponse(content=product.__dict__)
    

@product_router.post("/product")
def add_product(product_data: dict):
    post_product = product_service.create(product_data)
    return JSONResponse(content=post_product.__dict__)
    
@product_router.put("/product")
def update_product(product_data: dict):
    updated_product = product_service.update(product_data)
    if updated_product is None:
        return JSONResponse(status_code=404, content={"message": "Producto no encontrado"})
    return JSONResponse(content=updated_product.__dict__)


@product_router.delete("/product")
def delete_product(product_id: str):
    success = product_service.delete(product_id)
    if not success:
        return JSONResponse(status_code=404, content={"message": "Producto no encontrado"})
    return JSONResponse(content={"message": "Producto eliminado correctamente"})