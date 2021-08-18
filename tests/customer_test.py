import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Clive", 45)

    def test_customer_has_name(self):
        self.assertEqual("Clive", self.customer.name)

    def test_customer_age(self):
        self.assertEqual(45, self.customer.age)

    
