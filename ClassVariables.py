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

print(Employee.no_of_emps)

emp_1 = Employee('Hari', 'Haran', 89000)
emp_2 = Employee('Nitish', 'Kumar', 88000)

print(Employee.no_of_emps)


emp_1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay) #After appplying apply_raise() function to emp_1
