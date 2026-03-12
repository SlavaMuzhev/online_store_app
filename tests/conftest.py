import json
from pathlib import Path

import pytest

from src.category import Category
from src.product import Product


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
