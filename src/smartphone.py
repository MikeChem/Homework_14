from src.product import Product


class Smartphone(Product):
    """Класс предоставляющий информацию о товаре, описании, цене и количестве в категории Smartphone"""

    def __init__(self, name, description, price, quantity, efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.__price * self.quantity + other.__price * other.quantity

        raise TypeError
