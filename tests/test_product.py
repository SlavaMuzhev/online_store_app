from src.product import Product


def test_product_init(product_samsung: Product) -> None:
    """Тест корректности инициализации объекта Product"""
    assert product_samsung.name == "Samsung Galaxy C23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5
