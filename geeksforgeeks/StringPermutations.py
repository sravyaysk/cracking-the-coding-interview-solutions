def permuteUtil(mystr, count, result, level):
    if (level == len(result)):
        print(result)
        return
    for i in range(0, len(mystr)):
        if (count[i] == 0):
            continue
        newresult = list(result)
        newresult[level]=mystr[i]
        myresult = ''.join(newresult)
        count[i] -= 1
        permuteUtil(mystr, count, myresult, level + 1)
        count[i] += 1


n = int(input())
for testcase in range(0, n):
    str = input()
    charcount = {}
    for char in str:
        if (char not in charcount.keys()):
            charcount[char] = 1
        else:
            charcount[char] += 1

    mystr = "";
    count = []
    for key, value in charcount.items():
        mystr += key
        count.append(value)
    result = ' ' * (len(str))
    permuteUtil(mystr, count, result, 0)