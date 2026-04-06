import pytest

from src.exceptions import ZeroQuantityError
from src.product import Product


def test_product_init_zero_quantity_error():
    """Тест: создание товара с нулевым количеством вызывает ZeroQuantityError"""
    with pytest.raises(ZeroQuantityError):
        Product("Бракованный товар", "Описание", 1000.0, 0)
