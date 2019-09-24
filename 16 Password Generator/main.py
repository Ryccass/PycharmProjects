from random import randint
from random import choice

# User picks a strength, appropriate function gets called
def main(strength):
    if strength == 1:
        print(weak())
    elif strength == 2:
        print(medium())
    elif strength == 3:
        print(strong())


# pre-made list of words. Simply chooses one of those
def weak():
    words = ['a',
             'ability',
             'able',
             'about',
             'above',
             'accept',
             'according',
             'account',
             'across',
             'act',
             'action',
             'activity',
             'actually',
             'add',
             'address',
             'administration']
    newPass = choice(words)
    return newPass

# Letters (lower and upper) + numbers.
def medium():
    abc = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Generate empty list
    newPass = []
    # Ask the user for Password length
    length = int(input("Please enter a number. This will determine the length of your password."))
    # loop from 1 to length, adding a random character to the newPass each time
    for i in range(1, length + 1):
        newPass.append(abc[randint(1, len(abc) - 1)])
        newPass1 = ''.join(newPass)
        i += 1
    return newPass1

# Letters (lower and upper) + numbers + symbols
def strong():
    abc = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_=+[]{}|;:',<.>/?`~ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Generate empty list
    newPass = []
    # Ask the user for Password length
    length = int(input("Please enter a number. This will determine the length of your password."))
    # loop from 1 to length, adding a random character to the newPass each time
    for i in range(1, length + 1):
        newPass.append(abc[randint(1, len(abc) - 1)])
        newPass1 = ''.join(newPass)
        i += 1
    return newPass1


main(int(input("How strong do you want your password to be? (1 = weak, 2 = medium, 3 = strong)")))
