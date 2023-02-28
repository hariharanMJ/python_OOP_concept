class Employee:

    raise_amount = 1.04 #class Variable
    no_of_emps = 0

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # applying self for raise amount can affect only the variable that has specified amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(my_date):
        if my_date.weekday() == 5 or my_date.weekday() == 6:
            return False
        return True

emp_1 = Employee('Hari', 'Haran', 89000)
emp_2 = Employee('Nitish', 'Kumar', 88000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'Joe-Root-70000'
emp_str_2 = 'Fred-TheRed-60000'
emp_str_3 = 'Mark-Rud-65000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_2.email)
print(new_emp_3.email)


import datetime

my_date = datetime.date(2023, 2, 28)
print(Employee.is_workday(my_date))

