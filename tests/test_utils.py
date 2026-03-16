import pytest

from src.category import Category
from src.utils import load_data_from_json


def test_load_data_from_json(temp_json_file: str) -> None:
    """Тест успешной загрузки данных и создания объектов."""
    Category.category_count = 0
    Category.product_count = 0

    result = load_data_from_json(temp_json_file)

    assert len(result) == 1
    assert isinstance(result[0], Category)
    assert result[0].name == "Смартфоны"
    assert len(result[0].products_list) == 1
    assert result[0].products_list[0].name == "Samsung"

    assert Category.category_count == 1
    assert Category.product_count == 1


def test_load_data_file_not_found() -> None:
    """Тест генерации ошибки при отсутствии файла."""
    with pytest.raises(FileNotFoundError):
        load_data_from_json("non_existent_file.json")
