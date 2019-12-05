def findNumber(st):
    stack=[]
    result=""
    for i in range(len(st)+1):
        stack.append(str(i+1))
        if i==len(st) or st[i]=="I":
            while len(stack):
                result=result+stack[-1]
                stack.pop()
    print(result)

strs = ["D",'I','ID','DI','IID','DDI','DD','II','IIDDD','DDIDDIID']
for s in strs:
    findNumber(s)
