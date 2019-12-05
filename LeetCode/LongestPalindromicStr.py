def longestPalindrome2(s):
    if s == "":
        return s
    length = []
    s1 = s[::-1]

    for c, i in enumerate(s):
        for m, j in enumerate(s1):
            if i == j:
                temp = s[c:len(s) - m]
                if temp == temp[::-1]:
                    length.append(temp)
                    break

    return max(length, key=len)

def longestPalindrome(s):
    results = []
    flag = 0
    if (len(s) > 1):
        for i in range(0,len(s)):
            f = i
            try:
                l = s.rindex(s[i])
            except:
                l = f
            temp = s[f:l + 1]
            rev_temp = temp[::-1]
            if (temp == rev_temp and len(temp) > 1):
                flag = 1
                results.append(temp)
            elif(l!=f):
                while(l > 0 and l>f):
                    l = l-1
                    l =s[f:l+1].rindex(s[i])
                    temp = s[f:f+l + 1]
                    rev_temp = temp[::-1]
                    if (temp == rev_temp and len(temp) > 1):
                        flag = 1
                        results.append(temp)

        if(flag == 0):
            results.append(s[0])
    else:
        results.append(s)
    print(results)
    return max(results,key=len)

#print(longestPalindrome("babadada"))
#print(longestPalindrome("aaabaaaa"))
print(longestPalindrome2("jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"))
#print(longestPalindrome("abcdbbfcba"))