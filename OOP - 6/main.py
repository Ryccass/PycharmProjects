class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp1 = Employee('John', 'Smith')

emp1.fullName = 'Corey Schafer'

print(emp1.first)
print(emp1.email)
print(emp1.fullName)

print("")
del emp1.fullName
print("")

print(emp1.first)
print(emp1.email)
print(emp1.fullName)
