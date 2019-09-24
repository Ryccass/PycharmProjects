# Random generate a number and asks user to guess
import random


def guess_number(digits=4):
    list1 = []
    isContinue = True
    for i in range(1, digits + 1):
        num = random.randint(1, 9)
        list1.append(num)
    #        print(str(list1))

    while isContinue:
        input_str = input("Please enter a " + str(digits) + "-digit number ")
        input_list = []
        input_list = [int(x) for x in input_str]
        isMatch = compare_lists(list1, input_list)
        if isMatch == digits:
            print("Congratulations! You guessed the right number")
            break
        again = str(input("There are " + str(isMatch) + " matches. Do you want to continue? y or n"))
        if again == "y":
            isContinue = True
        else:
            isContinue = False
            break


# compare 2 lists
def compare_lists(list1, input_list):
    isMatch = 0
    if len(list1) != len(input_list):
        # print(str(len(list1)),str(len(input_list)))
        return
    for i in range(0, len(list1)):
        if list1[i] == input_list[i]:
            isMatch += 1
            # print(isMatch) #
    return isMatch


digits = int(input("Please enter the number of digits you want to guess  "))
guess_number(digits)
# compare_lists([1,5,9],[1,5,9])