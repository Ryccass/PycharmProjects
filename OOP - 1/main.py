from random import *


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Corey', 'Schafer', 6000)
emp2 = Employee('Test', 'User', 10000)

# print(emp1, emp2)
# print(emp1.email, emp2.email)
# print(emp1.fullName(), emp2.fullName())

# emp1.first = 'Corey'
# emp1.last = 'Schafer'
# emp1.email = 'corey.schafer@company.com'
# emp1.pay = 6000
#
# emp2.first = 'Test'
# emp2.last = 'User'
# emp2.email = 'test.user@company.com'
# emp2.pay = 10000