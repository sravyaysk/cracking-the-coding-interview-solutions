def checkIfPalindrome(tempstr):
    if (tempstr == tempstr[::-1]):
        return 1
    else:
        return 0


n = int(input())
for testcase in range(0, n):
    inputstr = input()
    palindromes = []
    for i in range(0, len(inputstr)):
        for j in range(i, len(inputstr)):
            tempstr = inputstr[i:j + 1]
            if (checkIfPalindrome(tempstr) and tempstr not in palindromes):
                palindromes.append(tempstr)
    print([x for x in palindromes if len(x) == max(len(x) for x in palindromes)][0])