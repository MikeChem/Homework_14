class Product:
    """Класс предоставляющий информацию о товаре, описании, цене и количестве"""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product):
        return cls(dict_product['name'], dict_product['description'], dict_product['price'], dict_product['quantity'])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        if new_price < self.__price:
            answer = input('Введите "y", если согласны понизить цену, если не согласны введите "n"\n')
            if answer == 'y':
                self.__price = new_price


