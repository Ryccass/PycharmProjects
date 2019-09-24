# from time import sleep


def main(listA: list):
    print("Please enter a number.")
    x = int(input(""))
    listB = []
    for i in listA:
        if i < x:
            listB.append(i)
        else:
            continue
    print(listB)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print([aa for aa in a if aa < 5])

main(a)
