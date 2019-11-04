def maxArea(height):
    i = 0
    j = len(height) - 1
    diff = [];
    length = [];
    breadth = []
    while (i <= j):
        if (height[i] <= height[j]):
            diff.append(height[j] - height[i])
            length.append(j - i)
            breadth.append(min(height[i], height[j]))
            i += 1
        else:
            diff.append(height[i] - height[j])
            length.append(j - i)
            breadth.append(min(height[j], height[i]))
            j -= 1
    maxarr = []
    for elem in range(0, len(length)):
        maxarr.append(length[elem] * breadth[elem])
    return max(maxarr)

arr=[1,8,6,2,5,4,8,3,7]
maxArea(arr)