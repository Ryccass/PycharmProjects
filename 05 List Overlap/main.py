import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

randomA = random.sample(range(1, 100), random.randint(1, 50))
randomB = random.sample(range(1, 100), random.randint(1, 50))
print(randomA)
print(randomB)


def mainLoop(listA, listB):

    listA = list(listA)
    listB = list(listB)
    listA.sort()
    listB.sort()
    
    newList = []

    for i in listA:
        if i in listB and i not in newList:
            newList.append(i)

    return newList


print(mainLoop(randomA, randomB))
