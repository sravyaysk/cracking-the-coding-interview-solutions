def method2(s):
    result = 0
    sub = ''
    for i in s:
        if i not in sub:
            sub += i
            if len(sub) > result:
                result = len(sub)
        else:
            sub += i
            sub = sub[sub.index(i) + 1:]

    return result

def lengthOfLongestSubstring(s):
    lens = [];
    indexes = [];
    strs = []
    for i in range(0, len(s)):
        count = 0
        str = s[i]
        for j in range(i + 1, len(s)):
            if(s[i]!=s[j] and (s[j] not in str)):
                count += 1
                str = str + s[j]
            # if (s[i] == s[j]):
            #     strs.append(s[i:j])
            #     lens.append(len(s[i:j]))
            #     indexes.append((i, j))
            else:
                break
        lens.append(count+1)
    if (len(lens) > 0):
        return max(lens)
    else:
        return len(s)
print(lengthOfLongestSubstring("abcabcbb"))
print(method2("abcabcbb"))