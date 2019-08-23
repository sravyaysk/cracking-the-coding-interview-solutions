'''compute the number of elements that two arrays (of length A and B) have in common. and
problem :Given two sorted arrays, find the number of elements in common. The arrays are the same length and
each has all distinct elements.'''
from collections import OrderedDict

class SortedArrayIntersection:
    def method1(self,arr1,arr2):
        #a bad implementation
        result = []
        for elem in arr1:
            if(elem in arr2):           #binary search -> O(nlogn)
                result.append(elem)
        print(result)

    def method2(self,arr1,arr2):
        #as arrays are sorted, if we can find last element in array1(large element) in array2, we can search to the left of it
        result = []
        if(arr1[-1] in arr2):
            req_index = arr2.index(arr1[-1])
            result.append(arr1[-1])
            for i in arr2[0:req_index]:
                if(i in arr1):
                    result.append(i)

    def method3(self,arr1,arr2):
        #using a hash table, then for lookup -> O(1)
        keys = {0,1,2,3,4,5,6,7,8,9}
        result = []
        dic = OrderedDict()
        for i in arr1:
            key = i % 10
            dic.setdefault(key, []).append(i)
        print(dic)
        for i in arr2:
            key = i %10
            if(key in dic.keys()):
                if(i in dic[key]):
                    result.append(i)
        print(result)
        # for key, value in dic.items():
        #     print(key, value)

if __name__ == "__main__":
    arr1 = [13,27,35,40,49,55,59]
    arr2 = [17,35,39,40,55,58,60]    #sorted arrays, lengths are same, all has distinct elements
    SortedArrayIntersection().method3(arr1,arr2)
