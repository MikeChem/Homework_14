import json
from typing import Any

from config import DATA_DIR
from src.category import Category
from src.product import Product

path_products_json = DATA_DIR / "products.json"


def get_products_json(file_path: Any) -> list:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о категории товаров,
    описании и списке товаров
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


def create_objects_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


# if __name__ == '__main__':
#     raw_data = get_products_json(path_products_json)
#     categories_data = create_objects_from_json(raw_data)
#
#     print(categories_data[0].name)
#     print(categories_data[0].description)
#     print(categories_data[0].products)
#
#     print(categories_data[1].name)
#     print(categories_data[1].description)
#     print(categories_data[1].products)
