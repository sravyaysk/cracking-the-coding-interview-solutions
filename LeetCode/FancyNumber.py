def checkFancyNumber(num):
    rotated_map = {0:0,1:1,6:9,8:8,9:6}
    res = []
    num_arr = [int(i) for i in str(num)]
    for i in num_arr:
        res.append(rotated_map[i])
    rev = res[::-1]
    if(rev==num_arr):
        print("Fancy number")
    else:
        print("Not a fancy number")

checkFancyNumber(996)