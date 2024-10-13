class Product:
    """Класс предоставляющий информацию о товаре, описании, цене и количестве"""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
