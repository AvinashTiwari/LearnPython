class Employee:
    name="Ben"
    designation = "Sales Exe"
    salesMadeThisWeek = 12

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target had been achieved")
        else:
            print("Target had not been achieved")

employeeOne = Employee()
print(employeeOne.name)
print(employeeOne.hasAchievedTarget())
