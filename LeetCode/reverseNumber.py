def reverse(x):
    r = 0
    flag = 0
    if(x<0):
        temp = x
        x = x*(-1)
        flag = 1
    while x > 0:
        r *= 10
        r += x % 10
        x //= 10

    if(flag ==0):
        return r
    else:
        return (r*-1)



print(reverse(-120))