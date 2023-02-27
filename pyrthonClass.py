class Employee:
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


emp_1 = Employee('Hari', "Haran", 89000)
emp_2 = Employee('Nitish', 'Kumar', 88000)

print(Employee)