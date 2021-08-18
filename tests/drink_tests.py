import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Bacardi", 4, 20)

    def test_drink_has_name(self):
        self.assertEqual("Bacardi", self.drink.name)
