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
searchInRotatedArray(arr,h,l,mid)




