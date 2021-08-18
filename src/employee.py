from src.person import Person

class Employee(Person):
    def __init__(self, name, age, wage):
        super().__init__(name, age)
        self.wage = wage
        

