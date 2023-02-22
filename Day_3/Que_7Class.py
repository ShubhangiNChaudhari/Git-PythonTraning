class Employee:
    # define an attribute
    employee_id = 0

employee1 = Employee()
employee2 = Employee()


employee1.employeeID = 68
print(f"Employee ID: {employee1.employeeID}")

# access attributes using employee2
employee2.employeeID = 70
print(f"Employee ID: {employee2.employeeID}")