class Pub:
    def __init__(self, name):
        self.name = name
        self.till = 0
        self.drinks = []

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        
        