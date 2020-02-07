t = int(input())
while(t > 0):
    secondline = input().split()
    n, sum = int(secondline[0]), int(secondline[1])
    arr = [int(x) for x in input().split()]
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > sum and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum:
            #print("Sum found between indexes")
            print("%d %d" % (start+1, i - 1+1))
            break
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
    t -= 1
    #print("No subarray found")
