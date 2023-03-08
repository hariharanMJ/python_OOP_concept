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
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self) -> str:
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self) -> str:
        return "{} - {}".format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Joe', 'Root', 40000)
emp_2 = Employee('Nitish', 'Kumar', 50000)


#print(emp_1)
#print(emp_1 + emp_2)
#print(len(emp_1))