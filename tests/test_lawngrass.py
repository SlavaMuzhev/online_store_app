import pytest

from src.lawngrass import LawnGrass


def test_lawngrass_init(grass_green: LawnGrass) -> None:
    """Проверка инициализации специфических атрибутов травы"""
    assert grass_green.name == "Газон"
    assert grass_green.country == "Россия"
    assert grass_green.germination_period == "10 дней"
    assert grass_green.color == "Зеленый"


def test_lawngrass_add(grass_green: LawnGrass, grass_sport: LawnGrass) -> None:
    """Проверка сложения двух объектов травы"""
    assert grass_green + grass_sport == 17000.0


def test_lawngrass_type_error(grass_green: LawnGrass) -> None:
    """Проверка ошибки при сложении травы с чем-то другим"""
    with pytest.raises(TypeError):
        _ = grass_green + 100  # type: ignore[operator]
