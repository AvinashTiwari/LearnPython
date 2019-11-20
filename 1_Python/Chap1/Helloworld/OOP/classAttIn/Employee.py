class Employee:
    numberOfWorkingHours = 40

employeeOne = Employee()
employeeTwo =  Employee()

print(employeeOne.numberOfWorkingHours)

Employee.numberOfWorkingHours = 45

print(employeeOne.numberOfWorkingHours)

employeeOne.name = "Avinash"
print(employeeOne.name )