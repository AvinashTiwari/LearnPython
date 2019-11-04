class person:
    def getName(self):
        print("Avinash")

    def getAge(self):
        print(16)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getNameNew(self):
        print("your name is " + self.name)

    def getAgeNew(self):
        print("your age is " + self.age)


p = person("bob", "21")
print(p.getName())
print(p.getAge())
print(p.getNameNew())
print(p.getAgeNew())
