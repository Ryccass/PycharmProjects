class Employee:
    raiseAmt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmt)


class Developer(Employee):
    raiseAmt = 1.10

    def __init__(self, first, last, pay, progLang):
        super().__init__(first, last, pay)
        self.progLang = progLang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def removeEmp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmps(self):
        for emp in self.employees:
            print('==> ' + emp.fullName())


dev1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev2 = Developer('Test', 'Employee', 75000, 'Java')

mgr1 = Manager('Sue', 'Smith', 90000, [dev1])

# print(mgr1.email)
# mgr1.addEmp(dev2)
# mgr1.printEmps()
# mgr1.removeEmp(dev1)

# print(dev1.email)
# print(dev1.progLang)

# print(dev1.pay)
# dev1.applyRaise()
# print(dev1.pay)

# print(dev1.email)
# print(dev2.email)

# print(help(Developer))
