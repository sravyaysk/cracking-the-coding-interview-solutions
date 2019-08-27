'''Numbers are randomly generated and stored into an (expanding) array. How would you keep track of the median?'''
from QuickSort import *

class FindMedian:
    def findMedian(self,arr):
        QuickSort().quickSort(arr,0,len(arr)-1)
        if(len(arr)%2 == 0):
            median = (arr[int(len(arr)/2)]+arr[int((len(arr)-1)/2)])/2
        else:
            median = arr[int(len(arr/2))]
        print(median)

if __name__ == "__main__":
    arr = [1,0,3,4,5,2]
    FindMedian().findMedian(arr)