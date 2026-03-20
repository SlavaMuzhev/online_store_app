from src.category import Category
from src.product import Product


class ProductIterator:
    """Итератор для перебора продуктов в конкретной категории"""

    def __init__(self, category_obj: Category) -> None:
        self.products = category_obj.products_list
        self.index = 0

    def __iter__(self) -> ProductIterator:
        return self

    def __next__(self) -> Product:
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
