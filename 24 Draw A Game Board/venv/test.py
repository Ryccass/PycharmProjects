def find_it(seq):
    for i in seq:
        count = 0
        countInd = 0
        if seq[countInd] == i:
            count += 1
            countInd += 1
        if count % 2 != 0:
            return i


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))