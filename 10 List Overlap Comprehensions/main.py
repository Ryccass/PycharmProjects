import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

randomA = random.sample(range(1, 100), random.randint(1, 50))
randomB = random.sample(range(1, 100), random.randint(1, 50))


def main(listA, listB):
    listA = list(listA)
    listB = list(listB)
    listA.sort()
    listB.sort()
    print(listA)
    print(listB)

    newList = []

    for i in listA:
        if i in listB and i not in newList:
            newList.append(i)

    print(newList)


main(randomA, randomB)
