import pytest

from src.product import Product
from src.smartphone import Smartphone


def test_smartphone_init(smartphone_iphone: Smartphone) -> None:
    """Проверка инициализации специфических атрибутов смартфона"""
    assert smartphone_iphone.name == "iPhone 15"
    assert smartphone_iphone.efficiency == 15.0
    assert smartphone_iphone.model == "15"
    assert smartphone_iphone.memory == 512
    assert smartphone_iphone.color == "Gray"


def test_smartphone_add(smartphone_iphone: Product, smartphone_samsung: Product) -> None:
    """Проверка сложения двух смартфонов (одинаковый класс)"""
    assert smartphone_iphone + smartphone_samsung == 2580000.0


def test_smartphone_add_error(smartphone_iphone: Product) -> None:
    """Проверка ошибки при сложении смартфона с базовым продуктом"""
    other_product = Product("Table", "Furniture", 1000.0, 2)
    with pytest.raises(TypeError):
        _ = smartphone_iphone + other_product
