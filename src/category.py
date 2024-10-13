class Category:
    """Класс предоставляющий информацию о категории товара, количестве товаров в категории и количестве категорий"""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.product_count += len(products) if products else 0
        Category.category_count += 1
