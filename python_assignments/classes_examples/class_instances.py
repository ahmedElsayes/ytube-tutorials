# in this tutorial we are just learning how to build the class and to call some instances of it
# first building a class for an employee has first and last name + his salary
class employee:
    def __init__(self, first, last, salary):     # the idea of this step to define the class attributes
        self.first = first
        self.last = last
        self.email = first + '.' + last + 'gmail.com'
        self.salary = salary

    # now to define a method to get the full name of the employee
    def employee_details(self):
        return 'the employee is {} {},his email is {} and get paid a salary of {}'.format(self.first, self.last, self.email, self.salary)

first_employee = employee('ahmed', 'mostafa', 2000)
second_employee = employee('mahmoud', 'hassan', 2200)
third_employee = employee('hosaam', 'ali', 2400)

# print(first_employee.employee_details())
print(employee.employee_details(first_employee))
