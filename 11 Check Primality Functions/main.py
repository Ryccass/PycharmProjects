import sys


def checkPrime(playAgain: bool):
    while playAgain:
        x = int(input("Please enter your number: \n"))
        if x == 1:
            print("1 is a prime number.")
            sys.exit()
        elif x == 2:
            print("2 is a prime number.")
            sys.exit()
        for i in range(2, x - 1):
            if x % i == 0:
                print("The number {} is not prime. It is divisible by {}".format(x, i))
                break
            else:
                print("The number {} is prime. It is only divisible by itself.".format(x))
                break

        print("Do you want to try another number? (y/n)")
        yesno = input("").lower()
        if yesno == 'n':
            print("Thank you for trusting the WBGG!")
            playAgain = False


checkPrime(True)
