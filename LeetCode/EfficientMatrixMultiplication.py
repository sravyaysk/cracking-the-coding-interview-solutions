def getCombinations(str,l):
    start_char = "("
    end_char = ")"
    gen_strs = []
    for i in range(0,len(str)):
        temp = ""
        for j in range(0,len(str)+1):
            if((j-i)%l==0 and (j-i)>0):
                #print(i,j)
                gen_strs.append((str.replace(str[i],"("+str[i]).replace(str[j-1],str[j-1]+")")))
                #temp_str = start_char+str[i:j]+end_char+str[j:len(str)]
                #gen_strs.append(temp_str)
        if(i==len(str)-l):
            break
    return gen_strs

n = int(input())
while(n*2 > 0):
    arr_len = int(input())
    arr = list(map(int,input().split()))
    no_of_matrices = arr_len - 1
    matrices = [chr(j) for j in range(65,65+arr_len-1)]
    matrices_size = [(arr[i],arr[i+1]) for i in range(0,arr_len-1)]
    matrix = "".join(i for i in matrices)
    # print(matrices)
    # print(matrices_size)
    # print(matrix)
    k = len(matrix)
    result = []
    while(k>1):
        coms = getCombinations(matrix,k)
        for c in coms:
            mainstr = c
            result.append(c)
            matrix = (c[c.rindex("(")+1:c.index(")")])
            k -= 1
            coms = getCombinations(matrix, k)
            continue
    n -= 1