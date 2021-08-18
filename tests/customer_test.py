import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Clive")

    def test_customer_has_name(self):
        self.assertEqual("Clive", self.customer.name)

    
