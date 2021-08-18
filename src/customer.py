class Customer:
    def __init__(self, name, age):
        self.name = name
        self.wallet = 0 
        self.age = age
        self.drunk = 0

    def add_money(self, money):
        self.wallet += money

    def buy_drink(self, drink):
        self.wallet -= drink.price
        self.drunk += drink.alcohol_level

    def buy_food(self, food):
        self.wallet -= food.price
        self.drunk -= food.rejuvination_level
        

    