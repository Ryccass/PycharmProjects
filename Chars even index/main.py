def index(string):
    indeces = []
    for i in range(0, len(string)):
        if i % 2 == 0 and i != 0:
            indeces.append(i)
        else:
            continue

    for i in indeces:
        print("Index [{}] {}".format(i, string[i]))


index(input("Please enter a random sequence of letters and/or words below: \n"))