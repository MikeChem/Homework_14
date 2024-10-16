from src.product import Product


def test_init_product_1(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_init_product_2(product_2):
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_init_product_3(product_3):
    assert product_3.name == "Xiaomi Redmi Note 11"
    assert product_3.description == "1024GB, Синий"
    assert product_3.price == 31000.0
    assert product_3.quantity == 14


def test_price_update(capsys, product_1):
    product_1.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == 'Цена не должна быть нулевая или отрицательная'

def test_product_add(product_1, product_2):
    assert product_1 + product_2 == 2580000

def test_product_str(product_1):
    assert str(product_1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'
