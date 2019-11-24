class Library:
    def __init__(self, listOfBooks):
        self.availabelbooks = listOfBooks


    def displayAvailableBooks(self):
        for book in self.availabelbooks:
            print(book)

    def lendaBook(self):
        pass

    def addabook(self):
        pass

class Customer:
    def requestabook(self):
        pass

    def returnBook(self):
        pass

library = Library(['A','B','C'])
customer = Customer()
