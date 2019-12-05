def romanToInt(s):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    stack = []
    stack.append(romans[s[0]])
    for i in range(1, len(s)):
        if (romans[s[i]] <= romans[s[i - 1]]):
            stack.append(romans[s[i]])
        else:
            prev = stack.pop()
            curr = romans[s[i]]
            stack.append(curr - prev)
    return sum(stack)

inputs = ['III','IV','IX','LVIII','MCMXCIV']
for i in inputs:
    print(romanToInt(i))