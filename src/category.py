from typing import List, Optional

from src.product import Product


class Category:
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

    def add_product(self, product: Product) -> None:
        """Добавляет продукт, только если его еще нет в списке"""
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает список товаров в формате: Продукт, цена руб. Остаток: n шт."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    @property
    def products_list(self) -> List[Product]:
        """Геттер для получения самого списка объектов (для метода new_product)"""
        return self.__products
