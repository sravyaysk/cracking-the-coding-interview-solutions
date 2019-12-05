def removeDuplicates(nums):
    nums = sorted(list(set(nums)))
    print(nums,len(nums))
    return len(nums)

arr=[1,1,2]
removeDuplicates(arr)