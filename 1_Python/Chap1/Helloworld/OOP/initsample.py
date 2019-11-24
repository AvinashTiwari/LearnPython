class Employee:

    def __init__(self):
        self.name = "Avinash"

    def enterEmployeeDetails(self):
        self.name ="Avinash"

    def displayEmployeeDeatails(self):
        print(self.name)

employee = Employee()

print(employee.displayEmployeeDeatails())