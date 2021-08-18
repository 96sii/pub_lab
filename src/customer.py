from src.person import Person

class Customer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.drunk = 0

    def add_money(self, money):
        self.wallet += money

    def buy_drink(self, drink):
        self.wallet -= drink.price
        self.drunk += drink.alcohol_level

    def buy_food(self, food):
        self.wallet -= food.price
        self.drunk -= food.rejuvination_level
        

    