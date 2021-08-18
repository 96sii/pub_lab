import unittest
from src.customer import Customer
from src.food import Food
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Clive", 45)
        self.food = Food("Crisps", 0.5, 2)
        self.drink = Drink("Cocktail", 9, 15)


    def test_customer_has_name(self):
        self.assertEqual("Clive", self.customer.name)

    def test_customer_age(self):
        self.assertEqual(45, self.customer.age)
    
    def test_food(self):
        self.customer.add_money(10)
        self.customer.buy_drink(self.drink)
        self.customer.buy_food(self.food)
        self.assertEqual(13, self.customer.drunk)

    
