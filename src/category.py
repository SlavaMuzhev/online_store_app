from typing import List


from src.product import Product


class Category:
    name: str
    description: str
    products: List[Product]
    category_count = 0
    product_count = 0
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.products)
