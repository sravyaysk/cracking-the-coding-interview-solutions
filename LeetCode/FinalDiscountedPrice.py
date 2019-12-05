def finalPrice(prices):
    # Write your code here
    index_arr=[]
    price = 0
    for i in range(0,len(prices)):
        flag = 0
        for j in range(i+1,len(prices)):
            if(prices[i]==prices[j] or prices[j]<prices[i]):
                flag = 1
                break
        if(flag==1):
            price += (prices[i]-prices[j])
        else:
            price += prices[i]
            index_arr.append(i)
    print(price)
    for ind in index_arr:
        print(ind,end=' ')

arr = [5,1,3,4,6,2]
finalPrice(arr)