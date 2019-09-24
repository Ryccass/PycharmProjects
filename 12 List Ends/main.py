a = [1]


def firstAndLast(listA: list):
    if len(listA) == 0:
        return []
    elif len(listA) == 1:
        return [listA[0]]
    else:
        return [listA[0], listA[-1]]


print(firstAndLast(a))
