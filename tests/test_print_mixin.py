import pytest

from src.product import Product


def test_mixin_log_output(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверка, что миксин печатает лог при создании объекта"""
    Product("Тест", "Опис", 100.0, 1)
    captured = capsys.readouterr()
    assert "Создан объект: Product" in captured.out
    assert "Тест" in captured.out
