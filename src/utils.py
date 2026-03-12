import json
import os

from src.category import Category
from src.product import Product


def load_data_from_json(file_path: str) -> list[Category]:
    """
    Загружает данные из JSON и возвращает список объектов Category с вложенными Product
    """
    current_dir = os.path.dirname(__file__)
    full_path = os.path.abspath(os.path.join(current_dir, "..", file_path))

    categories = []

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Файл не найден по пути: {full_path}")

    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        for category_dict in data:
            products_list = []
            for prod_dict in category_dict.get("products", []):
                product = Product(
                    name=prod_dict["name"],
                    description=prod_dict["description"],
                    price=prod_dict["price"],
                    quantity=prod_dict["quantity"],
                )
                products_list.append(product)

            category = Category(
                name=category_dict["name"], description=category_dict["description"], products=products_list
            )
            categories.append(category)

    return categories
