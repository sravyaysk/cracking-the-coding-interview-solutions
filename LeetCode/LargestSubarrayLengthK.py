def largestSubarray(arr,k):
    subarrays = []
    if(k<len(arr)):
        i=0
        while(i<=len(arr)-k):
            subarrays.append(arr[i:i+k])
            i += 1
        while(len(subarrays)>1):
            for i in range(0,len(subarrays)):
                for j in range(i+1,len(subarrays)):
                    for l in range(0,k):
                        if(subarrays[i][l] > subarrays[j][l]):
                            subarrays.pop(j)
                            break
                        elif(subarrays[i][l] < subarrays[j][l]):
                            subarrays.pop(i)
                            break
        return subarrays[0]
    else:
        return arr

arr = [1,4,3,2,5]
k=4
print(largestSubarray(arr,k))