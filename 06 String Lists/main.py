playAgain = True

while playAgain:

    word = input("PLease enter a word \n")
    word = str(word.lower())
    reverse = word[::-1]
    print(reverse)
    if word == reverse:
        print("This word is a palindrome!")
    else:
        print("This word is not a palindrome!")

    playAgainValue = input("Do you want to try another word? (y/n) \n").upper()
    if playAgainValue == 'N':
        playAgain = False
        print("Goodbye!")
