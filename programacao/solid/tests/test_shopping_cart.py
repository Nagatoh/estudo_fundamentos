import pytest
from solid.shopping_cart import (
    Product,
    ShoppingCart,
    CartCalculator,
    VipCartCalculator,
    AnotherVipCartCalculator
)


@pytest.fixture
def sample_products():
    return [
        Product("Product 1", 10),
        Product("Product 2", 20),
        Product("Product 3", 30),
    ]


@pytest.fixture
def sample_shopping_cart(sample_products):
    cart = ShoppingCart()
    cart.products = sample_products
    return cart


def test_product_creation():
    product = Product("Test Product", 50)
    assert product.name == "Test Product"
    assert product.price == 50


def test_shopping_cart_add_product():
    cart = ShoppingCart()
    product = Product("Test Product", 50)
    cart.add_product(product)
    assert len(cart.products) == 1
    assert cart.products[0] == product


def test_cart_calculator_total_price(sample_shopping_cart):
    calculator = CartCalculator()
    total_price = calculator.calculate_total_price(sample_shopping_cart)
    assert total_price == 60


def test_vip_cart_calculator_total_price(sample_shopping_cart):
    calculator = VipCartCalculator()
    total_price = calculator.calculate_total_price(sample_shopping_cart)
    assert total_price == 54


def test_another_vip_cart_calculator_total_price(sample_shopping_cart):
    calculator = AnotherVipCartCalculator()
    total_price = calculator.calculate_total_price(sample_shopping_cart)
    assert total_price == 48


def test_vip_cart_calculator_discount(sample_shopping_cart):
    calculator = VipCartCalculator()
    total_price_with_discount = calculator.calculate_total_price_with_vip_discount(
        sample_shopping_cart)
    assert total_price_with_discount == 54


def test_another_vip_cart_calculator_discount(sample_shopping_cart):
    calculator = AnotherVipCartCalculator()
    total_price_with_discount = calculator.calculate_total_price_with_vip_discount(
        sample_shopping_cart)
    assert total_price_with_discount == 48
