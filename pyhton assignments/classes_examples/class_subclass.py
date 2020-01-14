# Here is the Targets of this training
# 1- first we will differentiate between class and subclass by create subclass and see the results of printing and use of help function
# 2- see if an attribute is attached to the subclass, how this will differentiate when we print instance of class and subclass
# (raising salary example + programming language as an extra attribut)
# 3- creating subclasses of manager and developer and how the subcalss can contain extra attributes, showing how subclasses can overlabs through calling method
# 4- showing the use if isinstance() && issubclass() functions to identify the relations between objects

class employee:
    raise_amt = 1.5
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.salary = salary
 # an example of using instance method
    def employee_details(self):
        return 'the employee is {} {},his email is {} and get paid a salary of {}'.format(self.first, self.last, self.email, self.salary)
    # def fullname(self):
    #     return '{} {}'.format(self.first, self.last)
    # update the salary with instance method
    def update_salary(self):
        self.salary = int(self.salary * self.raise_amt)
#************************************************
# creating a Developer as a subclass from employee
# class Developer(employee):
#     raise_amt = 2
#***********************************************
# creating a Developer as a subclass from employee
class Developer(employee):
    raise_amt = 2
    def __init__(self, first, last, salary, prog_languages):
        super().__init__(first, last, salary)   # instead of writing all attributes, this command pass all class attributes to the subclass
        self.prog_languages = prog_languages
# Creating Manager as a subclass from employee
class manager(employee):
    def __init__(self, first, last, salary, Employees=None):
        super().__init__(first, last, salary)
        if Employees is None:
            self.Employees = []
        else:
            self.Employees = Employees
        
    def add_employee(self, emp):
        if emp not in self.Employees:
            self.Employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.Employees:
            self.Employees.remove(emp)
        
    def print_employees(self):
        for emps in self.Employees:
            print('>>>',emps.employee_details())

# *****The goal of this section is to test the subclass (Developer) inheritance from the parent class (employee)
# Dev_1 = Developer('ahmed', 'elsayes', 1000)
# Dev_2 = Developer('hazem', 'galal', 2000)
# emp_1 = employee('ahmed', 'elsayes', 1000)
# Dev_1.update_salary()
# emp_1.update_salary()
# print(Dev_1.email)
# print(Dev_2.email)
# # print(help(Developer))
# print('This is my details as normal employee: {}'.format(emp_1.employee_details()))
# print('This is my details as normal employee: {}'.format(Dev_1.employee_details()))
# ****************************************
# this section to print the attribute added to the developer
# Dev_1 = Developer('ahmed', 'elsayes', 1000, 'Python')
# print('the developer is: {} {} // the programming language is: {}  '.format(Dev_1.first, Dev_1.last, Dev_1.prog_languages))
# ****************************************
# This section to test the manager subclass and see how it append other employees under this subclass
# and how it can call methods from the parent class (employee) inside it
Dev_1 = Developer('ahmed', 'elsayes', 2000, 'Python')
Dev_2 = Developer('hazem', 'galal', 3000, 'JavaScript')
emp_1 = employee('ahmed', 'elsayes', 1000)
Mng_1 = manager('Hany', 'Gamal', 7000, [Dev_1])

print('the manager email address: {}'.format(Mng_1.email))
Mng_1.add_employee(Dev_2)
Mng_1.add_employee(emp_1)
Mng_1.remove_employee(Dev_1)

Mng_1.print_employees()