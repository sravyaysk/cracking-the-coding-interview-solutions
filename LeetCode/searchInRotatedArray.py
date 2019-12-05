'''
She asked for binary search functionality which tells no exists in array or not. Generally we find mid element through (low+high)/ 2 so she asked to change that and use random function to decide mid. Binary search is performed on sorted array but here unsorted array is given.

Two modifications are performed on binary search logic.

1) instead of sorted array, unsorted array has been given

2) Mid element is decided based on random function. Now we have to find out numbers from given array for which this function gives true result.

Hint: Function will return true for value x, if all numbers on left side of x are small and all number on  the right side of x are greater.

Example: [ 4, 3, 1, 5, 7, 6, 10]

Ans: 5,10

Rotated Array : Given the array [1 2 3 4 5 6], a rotation of 2 to the left gives [3 4 5 6 1 2]
'''
def method2(nums,target):
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

    if (len(nums) > 1):
        for i in range(0, len(nums) - 1):
            if (nums[i] > nums[i + 1]):
                break
        left_arr = nums[0:i + 1]
        right_arr = nums[i + 1:]
        if (target >= left_arr[0] and target <= left_arr[-1]):
            index = binarySearch(left_arr, 0, len(left_arr), target)
        elif (target >= right_arr[0] and target <= right_arr[-1]):
            ind = binarySearch(right_arr, 0, len(right_arr), target)
            if (ind != -1):
                index = len(left_arr) + ind
            else:
                index = ind
        else:
            index = -1

        return index
    elif (len(nums) == 1 and target != nums[0]):
        return -1
    elif (len(nums) == 1 and target == nums[0]):
        return 0
    else:
        return -1

def searchInRotatedArray(arr,h,l,mid):
    if(all(arr[l:mid])< arr[mid] and all(arr[mid+1:h])> arr[mid]):
        print(arr[mid])
        return arr[mid]
    else:
        if not((all(arr[l:mid])<mid)):
            mid = mid -1
            return searchInRotatedArray(arr,h,l,mid)
        elif not(all(arr[mid+1:h])>mid):
            mid = mid + 1
            return searchInRotatedArray(arr,h,l,mid)

arr = [4, 3, 1, 5, 7, 6, 10]
h = len(arr)
l = 0
mid = int((h + l) / 2)
#searchInRotatedArray(arr,h,l,mid)
arr1=[4,5,6,7,0,1,2]
print(method2(arr1,0))




