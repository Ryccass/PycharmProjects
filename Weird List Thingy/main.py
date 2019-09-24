import random


def mergeLists(a, b):
    thirdList = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            thirdList.append(a[i])
        else:
            continue

    for i in range(len(b)):
        if b[i] % 2 != 0:
            thirdList.append(b[i])
        else:
            continue

    return thirdList


def makeRandomList(n):
    randomList = []
    for i in range(n):
        randomList.append(random.randrange(1, 1000, 1))
    return randomList


listA = makeRandomList(15)
listB = makeRandomList(15)
print("This is list A: {}".format(listA))
print('')
print("This is list B: {}".format(listB))
print('')
print(mergeLists(listA, listB))
