class CurrencyService:
    def convert(self, amount: float, to: str):
        rates = {
            "USD": 0.0013,
            "CLP": 1.0
        }
        if to not in rates:
            raise ValueError("Moneda no soportada")
        return amount * rates[to]
