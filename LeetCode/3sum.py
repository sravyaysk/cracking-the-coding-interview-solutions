def binarySearch(arr, l, r, x):
    if r > l:
        mid = int((l + r) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

def threeSum1(array):
    if len(array) < 3:
        return []
    if (all(num == 0 for num in array)):
        return [[0, 0, 0]]
    size = len(array)
    found = {}
    array = sorted(array)
    for index, value in enumerate(array):
        left = index + 1
        right = size - 1
        while left < right:
            total = value + array[left] + array[right]
            if total == 0:
                current = (value, array[left], array[right])
                if current not in found:
                    found[current] = True
                right = right - 1
            elif total < 0:
                left = left + 1
            else:
                right = right - 1
    return list(found.keys())


def threeSum(nums):
    n = sorted(nums)
    if (len(n) >= 3):
        result = []
        for i in range(0, len(n)):
            for j in range(i + 1, len(n)):
                sum = n[i] + n[j]
                reqnum = 0 - (sum)
                tempn = [n[t] for t in range(0, len(n)) if t not in (i, j)]
                index = binarySearch(tempn, 0, len(tempn), reqnum)
                if (index != -1):
                    temp = sorted([n[i], n[j], tempn[index]])
                    if (temp not in result):
                        result.append(temp)
        return result
    else:
        return []

#arr=[-1, 0, 1, 2, -1, -4]
#arr=[-1,0,1,0]
#arr=[0,0,0]
arr=[3,0,-2,-1,1,2]
result = threeSum1(arr)
print(result)