import json
from pathlib import Path

import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product_samsung() -> Product:
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет", 180000.0, 5)


@pytest.fixture
def product_iphone() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_smartphones(product_samsung: Product, product_iphone: Product) -> Category:
    Category.category_count = 0
    Category.product_count = 0
    return Category("Смартфоны", "Описание категории", [product_samsung, product_iphone])


@pytest.fixture
def temp_json_file(tmp_path: Path) -> str:
    data = [
        {
            "name": "Смартфоны",
            "description": "Тест описание",
            "products": [{"name": "Samsung", "description": "256GB", "price": 100.0, "quantity": 5}],
        }
    ]
    test_file = tmp_path / "test_products.json"
    test_file.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return str(test_file)


@pytest.fixture
def smartphone_iphone() -> Smartphone:
    return Smartphone("iPhone 15", "512GB, Gray space", 210000.0, 8, 15.0, "15", 512, "Gray")


@pytest.fixture
def smartphone_samsung() -> Smartphone:
    return Smartphone("Samsung Galaxy C23 Ultra", "256GB, Серый цвет", 180000.0, 5, 14.0, "C23 Ultra", 256, "Gray")


@pytest.fixture
def grass_green() -> LawnGrass:
    return LawnGrass("Газон", "Густая трава", 500.0, 20, "Россия", "10 дней", "Зеленый")


@pytest.fixture
def grass_sport() -> LawnGrass:
    return LawnGrass("Спорт-Газон", "Стойкий", 700.0, 10, "Германия", "5 дней", "Тёмно-зеленый")
