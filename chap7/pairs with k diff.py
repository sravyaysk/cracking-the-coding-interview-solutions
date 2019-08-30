'''Given an array of distinct integer values, count the number of pairs of integers that
have difference k. For example, given the array { 1, 7, 5, 9, 2, 12, 3} and the difference
k = 2,there are four pairs with difference2: (1, 3), (3, 5), (5, 7), (7, 9).'''
from QuickSort import *

class KDiffPairs:
    def solution1(self,arr,k):
        count = 0
        for i in range(0,len(arr)):
            for j in range(1,len(arr)):
                if(abs(arr[i]-arr[j]) == k):
                    print(arr[i],arr[j])
                    count += 1
        print("total no of pairs with k diff are ",count)

    def solution2(self,arr,k):
        QuickSort().quickSort(arr,0,len(arr)-1)
        print(arr)
        

if __name__ == "__main__":
    arr = [1, 7, 5, 9, 2, 12, 3]
    k = 2
    KDiffPairs().solution2(arr,k)