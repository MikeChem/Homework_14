import pytest

from src.category import Category
from src.product import Product
from tests.conftest import category_1


def test_init_category(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    assert Category.category_count == 2
    assert Category.product_count == 4
    assert len(category_1.list_product) == 3
    assert len(category_2.list_product) == 1


def test_category_products_property(category_1):
    assert (
        category_1.products
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_add_product():
    product = Product("1", "2", 3.0, 4)
    product.name = "1"
    product.description = "2"
    product.price = 180000.0
    product.quantity = 5


def test_str_category(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 27 шт."


def test_add_smartphone_lawn_grass(smartphone_1, lawn_grass_2):
    with pytest.raises(TypeError):
        smartphone_1 + lawn_grass_2()
