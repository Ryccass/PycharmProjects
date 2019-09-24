from time import sleep


def main(playAgain: bool):
    while playAgain:
        print("Please enter a number. I will tell you whether it's ODD or EVEN.")
        x = input("")
        sleep(.5)
        print("You have entered " + str(x) + ". \n")
        sleep(1)
        if (int(x) % 2) == 0:
            print("Your number is EVEN.")
        else:
            print("Your number is ODD")

        print("Do you want to try another number? (y/n)")
        playAgainChar = input("").upper()
        if playAgainChar == 'N':
            playAgain = False
            print("Thank you for using my application!")


main(True)
