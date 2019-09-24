def fibo(rang):
    nums = []
    for i in range(0, rang):
        nums.append(i)

    newNums = []
    for i in nums:
        if i == 0:
            newNums.append(0)
        elif i == 1:
            newNums.append(1)
        elif i == 2:
            newNums.append(1)
        else:
            newNums.append(newNums[i - 2] + newNums[i - 1])
    print(newNums)

fibo(int(input("Please enter the amount of Fibonacci numbers you want: \n")))
