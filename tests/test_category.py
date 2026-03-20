from src.category import Category
from src.product import Product


def test_category_init(category_smartphones: Category) -> None:
    """Тест корректности инициализации объекта Category"""
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Описание категории"
    assert len(category_smartphones.products_list) == 2
    assert category_smartphones.products.count("\n") == 1


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


def test_category_products_property(category_smartphones: Category) -> None:
    """Тест геттера products, который возвращает строку"""
    output = category_smartphones.products
    assert "руб. Остаток:" in output
    assert "шт." in output
    assert len(output.strip().split("\n")) == 2


def test_add_product_no_duplicates() -> None:
    """Тест, что add_product не добавляет один и тот же объект дважды"""
    Category.category_count = 0
    Category.product_count = 0

    cat = Category("Electronics", "Desc")
    p1 = Product("Nokia", "Old", 1000.0, 10)

    cat.add_product(p1)
    cat.add_product(p1)

    assert len(cat.products_list) == 1
    assert Category.product_count == 1


def test_products_list_getter(category_smartphones: Category) -> None:
    """Тест геттера products_list, возвращающего список объектов"""
    raw_list = category_smartphones.products_list
    assert isinstance(raw_list, list)
    assert isinstance(raw_list[0], Product)


def test_category_init_with_products() -> None:
    """Тест инициализации категории со списком и корректность счетчика"""
    Category.product_count = 0
    p1 = Product("p1", "d", 10.0, 1)
    p2 = Product("p2", "d", 20.0, 2)

    cat = Category("C", "D", [p1, p2])

    assert Category.product_count == 2
    assert len(cat.products_list) == 2


def test_category_str(category_smartphones: Category) -> None:
    """Проверка строкового отображения категории"""
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 13 шт."


def test_category_products_output(category_smartphones: Category) -> None:
    """Проверка, что геттер products использует строковое представление продуктов"""
    output = category_smartphones.products
    expected_samsung = "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    expected_iphone = "Iphone 15, 210000.0 руб. Остаток: 8 шт."

    assert expected_samsung in output
    assert expected_iphone in output
    assert output.strip() == f"{expected_samsung}\n{expected_iphone}"
