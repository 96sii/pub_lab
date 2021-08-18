class Customer:
    def __init__(self, name):
        self.name = name
        self.wallet = 0 

    def add_money(self, money):
        self.wallet += money

    def buy_drink(self, drink, pub):
        self.wallet -= drink.price
        pub.till += drink.price