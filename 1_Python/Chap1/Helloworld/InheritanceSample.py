class parent:
    def __init__(self):
        print("this is parent class")

    def parentFunc(self):
        print("this is parent function")


class child(parent):
    def __init__(self):
        print("This child class")

    def childFunc(self):
        print("this is child function")


c = child()

print(c.parentFunc())
