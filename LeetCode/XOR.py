def computeXOR(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0


def sub_lists(list1):
    sublist = [[]]
    for i in range(len(list1) + 1):
        for j in range(i + 1, len(list1) + 1):
            sub = list1[i:j]
            sublist.append(sub)

    return sublist


def fun(A, K):
    # Your code goes here
    c1 = 0;
    c2 = 0;
    c3 = 0;
    xor_result = computeXOR(K)
    #subsets = sub_lists(A)
    for s in list(A):
        if ((s) < xor_result):
            c1 += 1
        elif ((s) == xor_result):
            c2 += 1
        elif ((s) > xor_result):
            c3 += 1

    result = (((c1 + c2) ** 2) + ((c2 + c3) ** 2) + ((c3 + c1) ** 2)) - (c1 * c1 + c2 * c2 + c3 * c3)
    return(result % ((10 ** 9) + 7))


T = int(input())
for _ in range(T):
    N = int(input())
    K = int(input())
    A = map(int, input().split(' '))

    out_ = fun(A, K)
    print(out_)
