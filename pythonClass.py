class Employee:
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Hari', 'Haran', 89000)
emp_2 = Employee('Nitish', 'Kumar', 88000)

print(emp_1.fullname())