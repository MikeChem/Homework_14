from src.product import Product

class Category:
    """Класс предоставляющий информацию о категории товара, количестве товаров в категории и количестве категорий"""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.product_count += len(products) if products else 0
        Category.category_count += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ''
        for product in self.__products:
            products_str += f'{product.name}, {product.price} руб., Остаток: {product.quantity} шт.\n'
        return products_str

    @property
    def list_product(self):
        return self.__products



