import pytest


def test_init_smartphone_1(smartphone_1):
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_init_smartphone_2(smartphone_2):
    assert smartphone_2.efficiency == 98.2
    assert smartphone_2.model == "15"
    assert smartphone_2.memory == 512
    assert smartphone_2.color == "Gray space"


def test_init_smartphone_3(smartphone_3):
    assert smartphone_3.efficiency == 90.3
    assert smartphone_3.model == "Note 11"
    assert smartphone_3.memory == 1024
    assert smartphone_3.color == "Синий"


def test_add_smartphone(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 2580000


def test_add_smartphone_lawn_grass(smartphone_1, lawn_grass_1):
    with pytest.raises(TypeError):
        smartphone_1 + lawn_grass_1
