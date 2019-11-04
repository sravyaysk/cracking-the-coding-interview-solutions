from itertools import permutations
def method2(n):
    result = []

    def gen(p, q, s):
        if p < 0 or q < 0:
            return
        if p == 0 and q == 0:
            result.append(s)
            return
        if (p > q):
            return
        
        i = s + "("
        j = s + ")"
        gen(p - 1, q, i)
        gen(p, q - 1, j)

    gen(n, n, "")
    return result

def generateParenthese(n):
    s = ""
    for i in range(0,n):
        s += ("(")
    for j in range(n-1,-1,-1):
        s += (")")
    print(n)
    print(s)
    perms = []

    for i in range(1, len(s) + 1):
        for c in permutations(s, i):
            perms.append("".join(c))

    #print(len(set(perms)))
    req_combs = list(set(perms))
    result = []
    for str in req_combs:
        intermediate = []
        flag = 0
        if len(str)==n*2 and str not in result and str[0]!=')':
            s1=0
            while(s1<len(str)):
                if(str[s1]== '('):
                    intermediate.append('(')
                else:
                    try:
                        intermediate.pop()
                    except:
                        flag = 1
                        break
                s1 += 1
            if(len(intermediate)==0 and flag==0):
                result.append(str)
    print(len(result))
    print(result)
    print("******"*10)

for num in range(8):
    generateParenthese(num)