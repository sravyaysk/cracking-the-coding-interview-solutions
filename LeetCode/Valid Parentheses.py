def isValid(s):
    open_braces = ['(', '[', '{']
    close_braces = [')', ']', '}']
    if (len(s) == 0):
        return True
    stack = []
    for i in s:
        if (i in open_braces):
            stack.append(i)
        if (i in close_braces):
            last = stack.pop()
            if (open_braces.index(last) != close_braces.index(i)):
                return False

    if (len(stack) == 0):
        return True
    else:
        return False

strs = ["()","()[]{}","(]","([)]","{[]}"]
for i in strs:
    if(isValid(i)):
        print("Valid")
    else:
        print("Invalid")