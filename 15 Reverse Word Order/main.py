def main(w):
    return ' '.join(w.split()[::-1])


print(main(input("Please enter a sentence or word sequence below: \n")))