class Product:

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        price: float,
        quantity: int
    ):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
