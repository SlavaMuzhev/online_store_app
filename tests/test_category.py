from src.category import Category
from src.product import Product


def test_category_init(category_smartphones: Category) -> None:
    """Тест корректности инициализации объекта Category"""
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Описание категории"
    assert len(category_smartphones.products) == 2


def test_category_counts(category_smartphones: Category) -> None:
    """Тест подсчета количества категорий и продуктов"""
    Category("Телевизоры", "Описание", [])

    assert Category.category_count == 2
    assert Category.product_count == 2  # В первой категории 2 товара, во второй 0


def test_product_count_increment() -> None:
    """тест на проверку суммы товаров во всех категориях"""
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("p1", "d1", 10.0, 1)
    p2 = Product("p2", "d2", 20.0, 2)

    cat1 = Category("C1", "D1", [p1])
    cat2 = Category("C2", "D2", [p2])

    assert cat1.name == "C1"
    assert cat2.name == "C2"
    assert Category.product_count == 2
    assert Category.category_count == 2
