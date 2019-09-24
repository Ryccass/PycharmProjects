

def wLoop(alist):
    newList = []
    for i in alist:
        if i not in newList:
            newList.append(i)
    return newList


def wSet(alist):
    newList = list(set(alist))
    newList.sort()
    return newList


myList = [1, 1, 5, 5, 20, 20, 46, 46]

print(wLoop(myList))
print(wSet(myList))