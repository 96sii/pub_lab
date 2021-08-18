import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink 
from src.employee import Employee

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Queen's left arm")
        self.customer = Customer("Clive", 45)
        self.customer2 = Customer("Bobby", 6)
        self.customer3 = Customer("Karen", 27)
        self.drink = Drink("Bacardi", 4, 20)
        self.drink_2 = Drink("Beer", 5, 15)
        self.employee = Employee ("Sarah", 20, 9.50)
        self.employee2 = Employee ("Robert", 26, 9.50)
        self.employee3 = Employee ("Chloe", 27, 12.50)

        

    def test_pub_has_name(self):
        self.assertEqual("The Queen's left arm", self.pub.name)

    def test_customer_buy_drink(self):
        
        self.customer.add_money(10)
        self.pub.serve_drink(self.customer, self.drink)
        self.assertEqual(4, self.pub.till)
        self.assertEqual(6, self.customer.wallet)

    def test_customer_buy_drink_fails(self):
        
        self.customer2.add_money(10)
        self.pub.serve_drink(self.customer2, self.drink)
        self.assertEqual(0, self.pub.till)
        self.assertEqual(10, self.customer2.wallet)

    def test_customer_buy_drink_too_drunk(self):
        
        self.customer.add_money(30)
        self.pub.serve_drink(self.customer, self.drink)
        self.pub.serve_drink(self.customer,self.drink)
        self.pub.serve_drink(self.customer,self.drink)
        self.pub.serve_drink(self.customer,self.drink)
        self.pub.serve_drink(self.customer,self.drink)
        self.pub.serve_drink(self.customer,self.drink)
        self.assertEqual(20, self.pub.till)
        self.assertEqual(10, self.customer.wallet)

    
    def test_pub_id(self):
        self.assertTrue(self.pub.check_age(self.customer))
    
    def test_pub_id_fails(self):
        self.assertFalse(self.pub.check_age(self.customer2))

    def test_pub_stock(self):
        self.pub.add_drink(self.drink)
        self.pub.add_drink(self.drink_2)
        self.assertEqual(2, len(self.pub.drinks))

    def test_stock_value(self):
        self.pub.add_drink(self.drink)
        self.pub.add_drink(self.drink_2)
        self.assertEqual(9, self.pub.stock_value())
    
    def test_wage_pay(self):
        self.pub.add_employee(self.employee)
        self.pub.add_employee(self.employee2)
        self.pub.add_employee(self.employee3)

        self.pub.pay_employees()
        self.assertEqual(9.50, self.employee.wallet)
        self.assertEqual(9.50, self.employee2.wallet)
        self.assertEqual(12.50, self.employee3.wallet)
