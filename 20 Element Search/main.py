def main1(a):
    number = int(input("Please enter a number:\n"))
    for i in a:
        if i == number:
            return True
    return False


def binary_search(lis, num):
    # While num is not equal to the value of the middle index of lis
    while num != lis[round(len(lis)/2)]:
        # if the list only has 2 values, no binary search possible, break
        if len(lis) < 2:
            break
        # elif num is bigger than the value of the middle index of lis
        elif num > lis[round(len(lis)/2)]:
            # lis is equal to the slice from the middle index until the end
            lis = lis[round(len(lis)/2):]
        # elif num is smaller than the value of the middle index of lis
        elif num < lis[round(len(lis)/2)]:
            # lis is equal to the slice from the start until the middle index
            lis = lis[:round(len(lis)/2)]

    if num == lis[round(len(lis)/2)]:
        return True
    else:
        return False


a = [71,
     9,
     35,
     30,
     68,
     2,
     1,
     7,
     76,
     99,
     19,
     3,
     92,
     66,
     22]

a = sorted(a)
print(len(a))

# print(main1(a))
# print(binary_search(a, 10)) # prints True
# print(binary_search(a, 9)) # prints False
# print(binary_search(a, 92)) # prints False
# print(binary_search(a, 2)) # prints True