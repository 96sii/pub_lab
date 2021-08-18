class Pub:
    def __init__(self, name):
        self.name = name
        self.till = 0
        self.drinks = []
        self.employees = []

    def check_age(self, customer):
        if customer.age >= 18:
            return True

    def check_drunk(self, customer):
        return customer.drunk
        
    def serve_drink(self, customer, drink):
        if self.check_age(customer) == True and self.check_drunk(customer) < 100:
            self.till += drink.price
            customer.buy_drink(drink)
            
    def add_drink(self, drink):
        self.drinks.append(drink)

    def stock_value(self):
        total = 0
        for drink in self.drinks:
            total += drink.price
        return total
            
    def pay_employees(self):
        for employee in self.employees:
            employee.wallet += employee.wage
    
    def add_employee(self, employee):
        self.employees.append(employee)
