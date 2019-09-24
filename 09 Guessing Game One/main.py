import random

playAgain = True

while playAgain:
    guesses = 3
    correctAnswer = random.randint(1, 9)

    print("Welcome to the World's Best Guessing Game (WBGG).")
    print("The computer has already generated a random number between (and including) 1 and 9.")
    print("Please enter your guess below!")

    while guesses != 0:
        userGuess = int(input(""))
        if userGuess == correctAnswer:
            print("The correct answer is {}".format(correctAnswer))
            print("You guessed {}".format(userGuess))
            break
        if userGuess < correctAnswer:
            print("You guessed {}".format(userGuess))
            print("Sorry, you guessed too low. Try again.")
            guesses -= 1
            print("You have {} guesses remaining!".format(guesses))
        if userGuess > correctAnswer:
            print("You guessed {}".format(userGuess))
            print("Sorry, you guessed too high. Try again.")
            guesses -= 1
            print("You have {} guesses remaining!".format(guesses))

    if guesses > 0:
        print("Congratulations! You've won!")
        print("Do you want to play again? (y/n)")
    else:
        print("The correct answer was {}".format(correctAnswer))
        print("Sorry, you've lost. Do you want to play again? (y/n)")


    yesno = input("").lower()
    if yesno == 'n':
        playAgain = False
        print("Thank you for playing!")
