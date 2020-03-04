import math


class Calculator:
    def __init__(self, cost):
        self.my_cost = cost

    def markup(self,rt):
        mark = math.sqrt(rt)
        return self.my_cost * mark

    def family(self):
        pass


mycost = sum([1.00*2,1.50,0.66])

menu = Calculator(mycost);
charge = menu.markup(4)
print('PBJ Cost ' + str(charge))

charge =  menu.family()