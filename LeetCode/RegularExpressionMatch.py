def checkInStr(str,char,index):
    for i in range(index,len(str)):
        if(str[i]!=char):
            return i

def isMatch(str,pattern):
    if(len(str)==0 and len(pattern)==0):
        return 1
    elif(len(str)>0 and len(pattern)==0):
        return 1
    elif(len(str)==0 and len(pattern)>0):
        if(pattern=='*'):
            return 1
        else:
            return 0
    else:
        if('*' not in pattern and '.' not in pattern):
            if(len(pattern)==len(str)):
                return 1
            else:
                return 0
        if(pattern == ".*"):
            return 1

        ind = 0
        for i in range(1,len(pattern)):
            if(pattern[i]!=str[i]):
                if(pattern[i]=='*'):
                    if(pattern[i-1].isalpha()):
                        ind = checkInStr(str,pattern[i-1],ind)


myinputs = [("aa","a"),("aa","a*"),("ab",".*"),("aab","c*a*b"),("mississippi","mis*is*p*.")]
for input in myinputs:
    isMatch(input[0],input[1])
