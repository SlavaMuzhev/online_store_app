from typing import List, Optional


class Product:
    name: str
    description: str
    quantity: int
    __price: float

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер с проверкой на отрицательную цену и подтверждением снижения"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            user_answer = input(
                f"Цена товара {self.name} снижается с {self.__price} до {new_price} руб. Подтвердить? (y/n): "
            )
            if user_answer.lower() == "y":
                self.__price = new_price
                print("Цена успешно снижена")
            else:
                print("Действие отменено")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, current_products: Optional[List["Product"]] = None) -> "Product":
        """Создает новый товар или обновляет существующий в списке при совпадении имен"""
        name = product_data["name"]
        price = product_data["price"]
        quantity = product_data["quantity"]
        description = product_data["description"]

        if current_products:
            for product in current_products:
                if product.name == name:
                    product.quantity += quantity
                    product.price = max(product.price, price)
                    return product

        return cls(name, description, price, quantity)
