from src.utils import get_products_json


def test_get_products_json(path, data):
    assert get_products_json(path) == data