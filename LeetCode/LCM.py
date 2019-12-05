import math
from math import gcd, sqrt
prime = [True] * 100001


def SieveOfEratosthenes():
    prime[0] = False
    prime[1] = False

    for p in range(2, int(sqrt(100001)) + 1):
        if prime[p] == True:
            for i in range(p ** 2, 100001, p):
                prime[i] = False


def common_prime(a, b):
    __gcd = gcd(a, b)
    res = []
    for i in range(2, __gcd + 1):
        if prime[i] and __gcd % i == 0:
            #print(i, end=" ")
            res.append(i)
    return res

def is_prime(n):

    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    # We store the number of factors in this variable
    factors = 0
    # This will loop from 1 to n
    for i in range(1, n+1):
        # Check if `i` divides `n`, if yes then we increment the factors
        if n % i == 0:
            factors += 1
    # If total factors are exactly 2
    if factors == 2:
        return True
    return False


def prime(n):
    # Print the number of two's that divide n
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if(is_prime(i)):
                factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)
    return list(set(factors))


if __name__ == "__main__":

    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])
    l1 = prime(a)
    l2 = prime(b)
    #print(l2,l2)
    res = list(set(l1) & set(l2))
    # SieveOfEratosthenes()
    # res = common_prime(a, b)
    #print(res)
    if(len(res)>= 1):
        print(min(res))
    else:
        print("-1")