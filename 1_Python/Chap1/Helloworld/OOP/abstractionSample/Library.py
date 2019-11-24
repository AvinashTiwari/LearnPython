class Library:
    def __init__(self, listOfBooks):
        self.availabelbooks = listOfBooks


    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        for book in self.availabelbooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availabelbooks:
            print("You now borrowed book")
            self.availabelbooks.remove(requestedBook)
        else:
            print("Book not available")



    def addabook(self,returnedBook):
        self.availabelbooks.append(returnedBook)
        print("You have returned a book")


class Customer:
    def requestabook(self):
        print("Enter the name of book")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter a book you want to return")
        self.book  =  input()
        return self.book

library = Library(['A','B','C'])
customer = Customer()

while True:
    print("Enter 1 ro display book")
    print("Enter 2 borrow book")
    print("Enter 3 to return abook")
    print("Enter 4 to exit")
    userchoice = int(input())
    if userchoice is 1:
        library.displayAvailableBooks()
    elif    userchoice is 2:
        requestBook = customer.requestabook()
        library.lendBook(requestBook)
    elif userchoice is 3:
        returnbook = customer.returnBook();
        library.addabook(returnbook)
    elif userchoice is 4:
        quit()
