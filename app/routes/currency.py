from fastapi import APIRouter, Query, HTTPException
from app.services.currency_service import CurrencyService

currency_router = APIRouter()
currency_service = CurrencyService()

@currency_router.get("/convert")
def convert_currency(amount: float = Query(...), to: str = Query(...)):
    try:
        result = currency_service.convert(amount, to.upper())
        return {"original_amount": amount, "converted_amount": result, "to": to.upper()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
