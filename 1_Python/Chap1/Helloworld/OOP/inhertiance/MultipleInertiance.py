class OperatingSystem:
    multiTasking =  True

class Apple:
    website = "http://aa.com"

class Mackbook(OperatingSystem,Apple):
    def __init__(self):
        if self.multiTasking is True:
            print("This mustitasking visit {} ".format(self.website))


mack = Mackbook()
