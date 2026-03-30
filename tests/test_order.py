from src.base_category import BaseCategory
from src.order import Order
from src.product import Product


def test_order_init(product_iphone: Product) -> None:
    """Тест инициализации заказа и наследования от BaseCategory"""
    order = Order(product_iphone, 2)

    assert order.product.name == "Iphone 15"
    assert order.quantity == 2
    assert order.total_cost == 420000.0  # 210000 * 2
    assert isinstance(order, BaseCategory)


def test_order_str(product_samsung: Product) -> None:
    """Тест строкового представления заказа"""
    order = Order(product_samsung, 1)
    assert str(order) == "Заказ: Samsung Galaxy C23 Ultra, 1 шт. Итого: 180000.0 руб."
