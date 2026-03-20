import pytest
from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


def test_product_iterator_init(category_smartphones: Category) -> None:
    """Тест инициализации итератора"""
    iterator = ProductIterator(category_smartphones)
    assert len(iterator.products) == 2
    assert iterator.index == 0


def test_product_iterator_next(category_smartphones: Category) -> None:
    """Тест перебора элементов через next()"""
    iterator = ProductIterator(category_smartphones)

    product1 = next(iterator)
    assert product1.name == "Samsung Galaxy C23 Ultra"

    product2 = next(iterator)
    assert product2.name == "Iphone 15"

    with pytest.raises(StopIteration):
        next(iterator)


def test_product_iterator_for_loop(category_smartphones: Category) -> None:
    """Тест работы итератора в цикле for"""
    iterator = ProductIterator(category_smartphones)
    products_list = []

    for product in iterator:
        products_list.append(product)

    assert len(products_list) == 2
    assert isinstance(products_list[0], Product)
    assert products_list[0].name == "Samsung Galaxy C23 Ultra"