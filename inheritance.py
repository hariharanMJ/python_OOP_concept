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

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            employees = []
        else:
            self.employees = employees

    def add_emps(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emps(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Fred', 'TheRed', 40000, 'Python')
dev_2 = Developer('Alex', 'Shaw', 50000, 'Java')

mgr_1 = Manager('Joe','Root',80000, [dev_1])

print(mgr_1.email)
mgr_1.add_emps(dev_2)
mgr_1.remove_emps(dev_1)
mgr_1.print_emps()


#print(dev_1.email)
#print(dev_1.prog_lang)