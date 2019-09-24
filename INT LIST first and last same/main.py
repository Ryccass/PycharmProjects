def isSame(lst):
    if lst[0] == lst[len(lst) - 1]:
        return True
    else:
        return False


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 15, 1]
print(isSame(myList))
