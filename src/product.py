class Product:
    """Класс предоставляющий информацию о товаре, описании, цене и количестве"""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, dict_product, products=None):
        if products:
            for product in products:
                if product.name == dict_product['name']:
                    product.quantity += dict_product['quantity']
                    product.price = max([product.price, dict_product['price']])
                    return product
        return cls(dict_product['name'], dict_product['description'], dict_product['price'], dict_product['quantity'])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        if new_price < self.__price:
            answer = input('Введите "y", если согласны понизить цену, если не согласны введите "n"\n')
            if answer != 'y':
                return
        self.__price = new_price

# emp_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
# print(emp_1)
