from src.product import Product


class LawnGrass(Product):
    """Класс предоставляющий информацию о товаре, описании, цене и количестве в категории Smartphone"""

    def __init__(self, name, description, price, quantity, country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.__price * self.quantity + other.__price * other.quantity

        raise TypeError
