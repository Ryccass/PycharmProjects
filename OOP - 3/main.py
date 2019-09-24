import datetime


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

    @classmethod
    def setRaiseAmt(cls, amount):
        cls.raiseAmount = amount

    @classmethod
    def fromString(cls, empStr):
        first, last, pay = empStr.split('-')
        return cls(first, last, pay)

    @staticmethod
    def isWorkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Corey', 'Schafer', 10000)
emp2 = Employee('Test', 'User', 25000)

myDate = datetime.date(2019, 9, 24)
print(Employee.isWorkday(myDate))  # => True

# empStr1 = 'John-Doe-70000'
# empStr2 = 'Steve-Smith-30000'
# empStr3 = 'Jane-Doe-90000'
#
# newEmp1 = Employee.fromString(empStr1)
#
# print(newEmp1.email)
# print(newEmp1.pay)
