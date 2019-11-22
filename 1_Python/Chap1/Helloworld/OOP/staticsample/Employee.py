class Employee:
    def employeeDetails(self):
        self.name = "Aviash"

    @staticmethod
    def welcomeMessage():
        print("Hello")

employee = Employee()
print(employee.employeeDetails())
print(employee.name)
print(employee.welcomeMessage())