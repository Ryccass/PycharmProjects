def printHorizLine():
    print(" --- " * boardSize)

def printVertLine():
    print("|   " * (boardSize +1))

if __name__ == "__main__":
    boardSize = int(input("Please define the size of your game board below: \n"))

    for index in range(boardSize):
        printHorizLine()
        printVertLine()