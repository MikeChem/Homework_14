import pytest


def test_init_lawn_grass_1(lawn_grass_1):
    assert lawn_grass_1.name == "Газонная трава"
    assert lawn_grass_1.description == "Элитная трава для газона"
    assert lawn_grass_1.price == 500.0
    assert lawn_grass_1.quantity == 20
    assert lawn_grass_1.country == "Россия"
    assert lawn_grass_1.germination_period == "7 дней"
    assert lawn_grass_1.color == "Зеленый"


def test_init_lawn_grass_2(lawn_grass_2):
    assert lawn_grass_2.name == "Газонная трава 2"
    assert lawn_grass_2.description == "Выносливая трава"
    assert lawn_grass_2.price == 450.0
    assert lawn_grass_2.quantity == 15
    assert lawn_grass_2.country == "США"
    assert lawn_grass_2.germination_period == "5 дней"
    assert lawn_grass_2.color == "Темно-зеленый"


def test_add_smartphone(lawn_grass_1, lawn_grass_2):
    assert lawn_grass_1 + lawn_grass_2 == 16750.0


def test_add_smartphone_lawn_grass(smartphone_1, lawn_grass_1):
    with pytest.raises(TypeError):
        smartphone_1 + lawn_grass_1
