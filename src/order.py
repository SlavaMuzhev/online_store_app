from src.product import Product
from src.base_category import BaseCategory

class Order(BaseCategory):
    """Класс для оформления заказа на один вид товара"""

    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.__total_cost = self.product.price * self.quantity

    @property
    def total_cost(self) -> float:
        """Возвращает итоговую стоимость заказа"""
        return self.__total_cost

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итого: {self.total_cost} руб."