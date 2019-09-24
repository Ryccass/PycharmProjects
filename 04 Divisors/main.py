
def main():
    print("Please enter a number.")
    x = int(input(""))
    y = range(1, x+ 1)

    for i in y:
        if x % i == 0:
            print(i)
        else:
            continue


main()
