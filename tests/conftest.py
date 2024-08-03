import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5)


@pytest.fixture
def product2():
    return Product("Iphone 15",
                   "512GB, Gray space",
                   210000.0,
                   8)


@pytest.fixture
def category1(product1, product2):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    [product1, product2])


@pytest.fixture
def new_test_product():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
            }


@pytest.fixture
def product_test_setter():
    return Product.new_product(
            {
                "name": "Samsung Galaxy S23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            }
            )
