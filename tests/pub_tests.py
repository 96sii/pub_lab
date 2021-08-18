import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink 

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Queen's left arm")
        self.customer = Customer("Clive", 45)
        self.customer2 = Customer("Bobby", 6)
        self.customer3 = Customer("Karen", 27)
        self.drink = Drink("Bacardi", 4, 20)
        

    def test_pub_has_name(self):
        self.assertEqual("The Queen's left arm", self.pub.name)

    def test_customer_buy_drink(self):
        
        self.customer.add_money(10)
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(4, self.pub.till)
        self.assertEqual(6, self.customer.wallet)

    def test_customer_buy_drink_fails(self):
        
        self.customer2.add_money(10)
        self.customer2.buy_drink(self.drink, self.pub)
        self.assertEqual(0, self.pub.till)
        self.assertEqual(10, self.customer2.wallet)

    def test_customer_buy_drink_too_drunk(self):
        
        self.customer.add_money(30)
        self.customer.buy_drink(self.drink, self.pub)
        self.customer.buy_drink(self.drink, self.pub)
        self.customer.buy_drink(self.drink, self.pub)
        self.customer.buy_drink(self.drink, self.pub)
        self.customer.buy_drink(self.drink, self.pub)
        self.customer.buy_drink(self.drink, self.pub)
        
        self.assertEqual(20, self.pub.till)
        self.assertEqual(10, self.customer.wallet)

    
    def test_pub_id(self):
        self.assertTrue(self.pub.check_age(self.customer))
    
    def test_pub_id_fails(self):
        self.assertFalse(self.pub.check_age(self.customer2))
    
   