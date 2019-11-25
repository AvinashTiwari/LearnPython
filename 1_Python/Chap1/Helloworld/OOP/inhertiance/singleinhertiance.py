class Apple:
    manufature = "Apple Inc"
    contactwebsite = "contact"

    def contactDetails(self):
        print("Apple contact ", self.contactwebsite )


class MacBook(Apple):
    def __init__(self):
        self.yearofmanufacture = 2017

    def manufatureDetails(self):
        print("This macbook manufature in year {} by {} ".format(self.yearofmanufacture, self.manufature) )


macbook = MacBook()
print(macbook.manufatureDetails())