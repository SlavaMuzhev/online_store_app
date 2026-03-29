from abc import ABC, abstractmethod

class BaseCategory(ABC):
    """Абстрактный класс для категорий товаров и заказов"""

    @abstractmethod
    def __str__(self) -> str:
        """Обязательное строковое представление"""
        pass

    @property
    @abstractmethod
    def total_cost(self) -> float:
        """Обязательный расчет итоговой стоимости"""
        pass