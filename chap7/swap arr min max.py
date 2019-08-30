'''swap the minimum and maximum element in an integer array'''
class SwapMinMax:
    def solution1(self,arr):
        print("array before swap: ",arr)
        i,j= arr.index(min(arr)),arr.index(max(arr))
        arr[i],arr[j]=arr[j],arr[i]
        print("array after swap: ", arr)

if __name__ == "__main__":
    arr = [5,3,4,1,-2]
    SwapMinMax().solution1(arr)
