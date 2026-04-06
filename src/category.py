from typing import List, Optional

from src.base_category import BaseCategory
from src.product import Product


class Category(BaseCategory):
    name: str
    description: str
    __products: List[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List["Product"]] = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products) if products is not None else 0

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def total_cost(self) -> float:
        """Суммарная стоимость всех товаров в категории (цена * количество на складе)"""
        return sum(product.price * product.quantity for product in self.__products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию только если это объект Product или его наследник
        и с обработкой исключения нулевого количества
        """
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты класса Product или его наследников")

            if product.quantity <= 0:
                from src.exceptions import ZeroQuantityError
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")

            if product not in self.__products:
                self.__products.append(product)
                Category.product_count += 1

        except (ZeroQuantityError, ValueError) as e:
            print(f"Ошибка добавления товара: {e}")
        else:
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self) -> str:
        """Возвращает список товаров, используя строковое отображение каждого продукта"""
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[Product]:
        """Геттер для получения самого списка объектов (для метода new_product)"""
        return self.__products

    def middle_price(self) -> float:
        """
        Подсчитывает средний ценник всех товаров в категории.
        Возвращает 0, если товаров нет.
        """
        try:
            total_sum = sum(product.price for product in self.__products)
            average = total_sum / len(self.__products)
            return round(average, 2)
        except ZeroDivisionError:
            return 0

