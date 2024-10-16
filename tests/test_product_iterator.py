def test_product_iterator(product_iterator):
    assert product_iterator.index == -1
    assert next(product_iterator).name == 'Samsung Galaxy S23 Ultra'
    assert next(product_iterator).name == 'Iphone 15'
    assert next(product_iterator).name == 'Xiaomi Redmi Note 11'

