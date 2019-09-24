def main():
    x = int(input("Enter a number: \n"))
    i = 1
    fib = []
    if x == 0:
        fib = [0]
    elif x == 1:
        fib = [1]
    elif x == 2:
        fib = [1, 1]
    elif x > 2:
        fib = [1, 1]
        while i < (x - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1

    return fib


print(main())
