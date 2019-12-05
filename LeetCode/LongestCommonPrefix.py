def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)):
                    answer = match
                    match = ""
    return answer

def longestCommonPrefix(strs):
    result = []
    for i in range(0, len(strs)):
        for j in range(i+1, len(strs)):
            res = longestSubstringFinder(strs[i], strs[j])
            if(len(res)>0):
                result.append(res)
    print(result)
    if(len(result)>0):
        return min(result, key=len)
    else:
        return ''

strs=["dog","racecar","car"]
print(longestCommonPrefix(strs))