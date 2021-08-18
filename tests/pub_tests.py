import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink 

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Queen's left arm")
        self.customer = Customer("Clive")
        self.drink = Drink("Bacardi", 4)
        

    def test_pub_has_name(self):
        self.assertEqual("The Queen's left arm", self.pub.name)

    def test_customer_buy_drink(self):
        
        self.customer.add_money(10)
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(4, self.pub.till)
        self.assertEqual(6, self.customer.wallet)