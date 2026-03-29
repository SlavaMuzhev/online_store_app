from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture

from src.base_product import BaseProduct
from src.product import Product


def test_product_init(product_samsung: Product) -> None:
    """Тест корректности инициализации объекта Product"""
    assert product_samsung.name == "Samsung Galaxy C23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_price_setter_increase(product_samsung: Product) -> None:
    """Тест повышения цены (проходит без подтверждения)"""
    product_samsung.price = 200000.0
    assert product_samsung.price == 200000.0


def test_price_setter_zero_or_negative(product_samsung: Product, capsys: CaptureFixture) -> None:
    """Тест некорректной цены (цена не должна измениться)"""
    product_samsung.price = -100
    assert product_samsung.price == 180000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_decrease_confirm(product_samsung: Product, capsys: CaptureFixture) -> None:
    """Тест снижения цены при согласии пользователя (ввод 'y')"""
    with patch("builtins.input", return_value="y"):
        product_samsung.price = 150000.0
    assert product_samsung.price == 150000.0


def test_price_setter_decrease_cancel(product_samsung: Product, capsys: CaptureFixture) -> None:
    """Тест отмены снижения цены (ввод 'n')"""
    with patch("builtins.input", return_value="n"):
        product_samsung.price = 150000.0
    assert product_samsung.price == 180000.0  # Цена осталась старой


def test_new_product_creation() -> None:
    """Тест создания абсолютно нового продукта через classmethod"""
    data = {"name": "iPhone 15", "description": "512GB", "price": 1000.0, "quantity": 10}
    new_obj = Product.new_product(data)
    assert new_obj.name == "iPhone 15"
    assert new_obj.quantity == 10


def test_new_product_update_existing(product_samsung: Product) -> None:
    """Тест обновления существующего продукта (сложение количества и выбор макс. цены)"""
    data = {"name": "Samsung Galaxy C23 Ultra", "description": "Other", "price": 200000.0, "quantity": 5}
    # Передаем текущий продукт в списке
    updated_product = Product.new_product(data, [product_samsung])

    assert updated_product.quantity == 10  # 5 + 5
    assert updated_product.price == 200000.0  # Выбрана максимальная из 180к и 200к


def test_product_str(product_samsung: Product) -> None:
    """Проверка строкового отображения продукта"""
    assert str(product_samsung) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_products_addition(product_samsung: Product, product_iphone: Product) -> None:
    """Проверка сложения двух продуктов (сумма стоимостей всех единиц на складе)"""
    assert product_samsung + product_iphone == 2580000.0


def test_product_add_invalid_type(product_samsung: Product) -> None:
    """Тест на ошибку при сложении продукта с объектом другого типа"""
    with pytest.raises(TypeError) as excinfo:
        _ = product_samsung + 10  # type: ignore

    assert str(excinfo.value) == "Складывать можно только объекты класса Product"


def test_product_inheritance(smartphone_iphone: Product, grass_green: Product) -> None:
    """Проверка наследования от базового абстрактного класса"""

    assert isinstance(smartphone_iphone, BaseProduct)
    assert isinstance(grass_green, BaseProduct)


def test_base_product_abstract_methods() -> None:
    """Тестируем вызов пустых методов в абстрактном классе BaseProduct"""

    class TestProduct(BaseProduct):
        def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
            super().__init__(name, description, price, quantity)  # type: ignore[safe-super]

        def __str__(self) -> str:
            return super().__str__()  # type: ignore[safe-super]

        @classmethod
        def new_product(cls, product_data: dict) -> BaseProduct:
            return super().new_product(product_data)

    test_obj = TestProduct("n", "d", 1.0, 1)
    test_obj.__str__()
    TestProduct.new_product({})
