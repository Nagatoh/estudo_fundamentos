from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)


class IBaseCartCalculator(ABC):
    @abstractmethod
    def calculate_total_price(self, shopping_cart):
        pass

class IVipCartCalculator(ABC):
    @abstractmethod
    def calculate_total_price_with_vip_discount(self, shopping_cart):
        pass

class CartCalculator(IBaseCartCalculator):
    def calculate_total_price(self, shopping_cart):
        total_price = 0
        for product in shopping_cart.products:
            total_price += product.price
        return total_price

class VipCartCalculator(IBaseCartCalculator, IVipCartCalculator):
    def calculate_total_price(self, shopping_cart):
        return self.calculate_total_price_with_vip_discount(shopping_cart)

    def calculate_total_price_with_vip_discount(self, shopping_cart):
        total_price = CartCalculator.calculate_total_price(self, shopping_cart)
        total_price *= 0.9
        return total_price

class AnotherVipCartCalculator(IBaseCartCalculator, IVipCartCalculator):
    def calculate_total_price(self, shopping_cart):
        return self.calculate_total_price_with_vip_discount(shopping_cart)

    def calculate_total_price_with_vip_discount(self, shopping_cart):
        total_price = CartCalculator.calculate_total_price(self, shopping_cart)
        total_price *= 0.8
        return total_price