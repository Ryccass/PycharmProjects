def removeChars(string, n):
    return string[n:]


print(removeChars(input("Please enter a word: \n"),
                  int(input("Please enter the amount of letters you want deleted\n"))))
