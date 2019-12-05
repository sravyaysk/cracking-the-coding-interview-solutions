def decodeString(s):
    count = s.count("[")
    while (count > 0):
        num = ""
        flag = 0
        if (s.rindex("[") < s.index("]")):
            first_ind = s.rindex("[")
            last_ind = s.index("]")
        else:
            temp = s[s.rindex("["):]
            if(temp.index("[")< temp.index("]")):
                first_ind = s.rindex("[")
                last_ind = first_ind+temp.index("]")
            else:
                first_ind = s.index("[")
                last_ind = s.index("]")
        bw_str = s[first_ind + 1:last_ind]
        try:
            for i in range(first_ind - 1, -1, -1):
                if (isinstance(int(s[i]), int)):
                    flag = 1
                    num = num + (s[i])
                    num_ind = i
                else:
                    break
            else:
                if(i!=0):
                    num_ind = first_ind - 1
                    num = (s[first_ind - 1])
        except:
            if(flag!=1):
                num_ind = first_ind - 1
                num = (s[first_ind - 1])
            else:
                pass

        num = int(num[::-1])
        s = s.replace(s[num_ind:last_ind + 1], (bw_str * num))
        count -= 1
    return s


# res=(decodeString("3[a2[c]]"))
# print(res)
# res=(decodeString("3[a]2[bc]"))
# print(res)
# res=(decodeString("2[abc]3[cd]ef"))
# print(res)
# res=(decodeString("10[abc]"))
# print(res)
# res=(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
# print(res)
res=decodeString("3[a10[bc]]")
print(res)