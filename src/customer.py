class Customer:
    def __init__(self, name, age):
        self.name = name
        self.wallet = 0 
        self.age = age
        self.drunk = 0

    def add_money(self, money):
        self.wallet += money

    def buy_drink(self, drink, pub):
        if pub.check_age(self) == True and self.drunk < 100:
            self.wallet -= drink.price
            pub.till += drink.price
            self.drunk += drink.alcohol_level
        

        
