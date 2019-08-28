'''Numbers are randomly generated and stored into an (expanding) array. How would you keep track of the median?'''
from QuickSort import *
#import heapq

class FindMedian:
    def findMedian(self,arr):
        QuickSort().quickSort(arr,0,len(arr)-1)
        if(len(arr)%2 == 0):
            median = (arr[int(len(arr)/2)]+arr[int((len(arr)-1)/2)])/2
        else:
            median = arr[int(len(arr/2))]
        print(median)

    # def findMedianHeap(self,arr):
    #     #convert list into a heap
    #     hp = heapq.heapify(arr)
    #     self.findMedian(hp)


if __name__ == "__main__":
    arr = [1,0,3,4,5,2]
    FindMedian().findMedian(arr)