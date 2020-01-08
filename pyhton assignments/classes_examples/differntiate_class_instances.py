# 1- the target of this example to differentiate the method applied to the general glass and specific instance from it by showing how the method is applied to the whole class and how selectively change an instance of it
# 2- to understand the mechanism of working every time we call an instance of a class

class employee:
    raise_salary = 1.5
    num_ofemployee = 0
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + 'gmail.com'
        self.salary = salary
        employee.num_ofemployee += 1
    def employee_details(self):
        return 'the employee is {} {},his email is {} and get paid a salary of {}'.format(self.first, self.last, self.email, self.salary)
    def salary_after_raise(self):
        self.salary = int(self.salary * self.raise_salary)
    
    
print('********number of employees before calling is {} '.format(employee.num_ofemployee))

first_employee = employee('ahmed', 'mostafa', 2000)
second_employee = employee('mahmoud', 'hassan', 2200)
third_employee = employee('hosaam', 'ali', 2400)
first_employee.raise_salary = 1.1

print('********number of employees before calling is {}'.format(employee.num_ofemployee))
print('********', first_employee.employee_details())
print('*********************************')
print(employee.raise_salary)
print(first_employee.raise_salary)
print(second_employee.raise_salary)
print(third_employee.raise_salary)

print('*********************************show the attributes of instance classes')
print(first_employee.__dict__)  # this command to show the attributes of this instance class
print(second_employee.__dict__)  # this command to show the attributes of this instance class
print(third_employee.__dict__)  # this command to show the attributes of this instance class

print('********************************* to show the difference in the salary after applying the method')
print('the first employee salary is {}'.format(first_employee.salary))
first_employee.salary_after_raise()
print('the first employee salary after raise is {}'.format(first_employee.salary))
print('the second employee salary is {}'.format(second_employee.salary))
second_employee.salary_after_raise()
print('the second employee salary after raise is {}'.format(second_employee.salary))




