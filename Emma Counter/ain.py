def countEmma(lst):
    count = 0
    for i in lst:
        if i == 'Emma':
            count += 1
        else:
            continue
    return 'Emma appears {} times in this list.'.format(count)


myList = ["Emma", "poop", "Emma", "Emma", "Emma", "Emma", "poop", "Emma", "Emma", "Emma", "Emma", "Emma", "Emma",
          "Emma", "Emma", "Emma", "Emma", "Emma", "Emma", "poop", "Emma", ]
print(countEmma(myList))
