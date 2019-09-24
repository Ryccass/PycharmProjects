def main(playAgain):
    while playAgain:

        print("Welcome to Rock Paper Scissors!")
        print("Player 1, please enter either 'R', 'P' or 'S' and please make sure Player 2 isn't watching!")
        player1Guess = input("").lower()
        print("Player 2, please enter either 'R', 'P' or 'S' and please make sure Player 2 isn't watching!")
        player2Guess = input("").lower()

        if player1Guess == 'r' or player1Guess == 'p' or player1Guess == 's':
            if player1Guess == 'r':
                if player2Guess != 'r' and player2Guess != 'p' and player2Guess != 's':
                    print("Not a valid option. Automatic loss. Player 1 Wins!")
                if player2Guess == 'r':
                    print("TIE!")
                if player2Guess == 'p':
                    print("Player 2 Wins!")
                if player2Guess == 's':
                    print("Player 1 Wins!")

            if player1Guess == 'p':
                if player2Guess != 'r' and player2Guess != 'p' and player2Guess != 's':
                    print("Not a valid option. Automatic loss. Player 1 Wins!")
                if player2Guess == 'r':
                    print("Player 1 Wins!")
                if player2Guess == 'p':
                    print("TIE!")
                if player2Guess == 's':
                    print("Player 2 Wins!")

            if player1Guess == 's':
                if player2Guess != 'r' and player2Guess != 'p' and player2Guess != 's':
                    print("Not a valid option. Automatic loss. Player 1 Wins!")
                if player2Guess == 'r':
                    print("Player 2 Wins!")
                if player2Guess == 'p':
                    print("Player 1 Wins!")
                if player2Guess == 's':
                    print("TIE!")
        else:
            if player2Guess != 'r' and player2Guess != 'p' and player2Guess != 's':
                print("Both Players entered invalid characters. TIE!")
            else:
                print("Player 1 entered an invalid character. Automatic Loss. Player 2 Wins!")

        print("Do you want to play again? (y/n)")
        yesno = input("").lower()

        if yesno == 'n':
            print("Thank you for playing!")
            break



# playAgain = True
main(playAgain = True)
