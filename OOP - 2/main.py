class Employee:
    # CLASS VARIABLES
    raiseAmount = 1.04
    numOfEmps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

        Employee.numOfEmps += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount)


print(Employee.numOfEmps)  # => prints 0

emp1 = Employee('Corey', 'Schafer', 10000)
emp2 = Employee('Test', 'User', 25000)

print(Employee.numOfEmps)  # => prints 2

# print(emp1.__dict__)
# print(Employee.__dict__)
#
# emp1.raiseAmount = 1.05
#
# print(Employee.raiseAmount)
# print(emp1.raiseAmount)
# print(emp2.raiseAmount)
