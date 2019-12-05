def compareStrings(a,b):
    a_strs = a.split()
    b_strs = b.split()
    result = []
    flag = 0

    if(len(a_strs)>=len(b_strs)):
        l1=len(b_strs)
        l2=len(a_strs)
        flag = 2
        #getCount(l1,l2,b_strs,a_strs)
    else:
        l1=len(a_strs)
        l2=len(b_strs)
        flag = 1
        #getCount(l1, l2, a_strs, b_strs)

    for i in range(0,l1):
        count = 0
        for j in range(0,l2):
            if(flag == 1):
                temp_str1= a_strs[i]
                temp_str2 = b_strs[j]
            elif(flag == 2):
                temp_str1 = b_strs[i]
                temp_str2 = a_strs[j]
            temp1 = ''.join(sorted(temp_str1))
            temp12 = "".join(sorted(list(set(temp1))))
            temp2 = ''.join(sorted(temp_str2))
            temp22 = "".join(sorted(list(set(temp2))))
            c1 = [temp1.count(k) for k in temp12]
            c2 = [temp2.count(k) for k in temp22]
            if(c1[0] > c2[0]):
                count += 1
        result.append(count)
    return(result)


A="abcd aabc bd"
B="aaa aa"
compareStrings(A,B)