def isPalindrome(n):
    num = str(n)
    numRev = num[::-1]
    print(num, numRev)
    if num == numRev:
        return True
    else:
        return False

print(isPalindrome(122))