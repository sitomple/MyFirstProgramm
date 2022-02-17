
class Employee(object):
    def __init__(self, sirname):
        self.sirname = sirname
        self.pay = 0

    def addSalary(self, value):
        self.pay += value