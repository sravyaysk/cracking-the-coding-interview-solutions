def myAtoi1(str):
    mystr = str.strip()
    result = ""
    num_flag = 0
    sym_flag = 0
    try:
        if (mystr[0] == "+" or mystr[0] == "-" or isinstance(int(mystr[0]), int)):
            for i in range(0, len(mystr)):
                if ((mystr[0] == "-" or mystr[0]=='+') and '-' not in result and sym_flag==0):
                    if(mystr[0]!='+'):
                        result += mystr[0]
                    sym_flag = 1
                elif (num_flag == 0):
                    try:
                        if (isinstance(int(mystr[i]), int)):
                            num_flag = 1
                            result += mystr[i]
                    except:
                        break
                else:
                    try:
                        if (num_flag == 1 and isinstance(int(mystr[i]), int)):
                            result += mystr[i]
                        else:
                            break
                    except:
                        break
            if (len(result) > 0):
                if (result[0] == "-"):
                    try:
                        num = int(result[1:])
                    except:
                        return 0
                    if ((-2 ** 31) <= num * -1):
                        return (num * -1)
                    else:
                        return (-2 ** 31)
                else:
                    num = int(result)
                    if (num <= (2 ** 31 - 1)):
                        return (num)
                    else:
                        return (2 ** 31 - 1)
            else:
                return 0
        else:
            return 0
    except:
        return 0

def myAtoi(str):
    mystr = str.strip()
    if ("+" in mystr and '-' in mystr and (mystr.index("+")==mystr.index("-")+1 or mystr.index("-")==mystr.index("+")+1)):
        return 0
    # elif ("+" in mystr and "-" not in mystr and mystr.index("+") > 0):
    #     return 0
    # elif("-" in mystr and "+" not in mystr and mystr.index("-") > 0):
    #     return 0

    res = ""
    for i in mystr:
        try:
            if ((i == "-" and "-" not in res) or i == "+" or isinstance(int(i), int)):
                if (i != "+"):
                    res += i
                if(i == "+" and "-" in res):
                    break
                if(i=="-" and "+" in res):
                    break
            else:
                break
        except:
            break
    if (len(res) > 0):
        if (res[0] == "-"):
            try:
                num = int(res[1:])
            except:
                return 0
            if ((-2 ** 31) <= num * -1):
                return (num * -1)
            else:
                return (-2 ** 31)
        else:
            num = int(res)
            if (num <= (2 ** 31 - 1)):
                return (num)
            else:
                return (2 ** 31 - 1)
    else:
        return 0

# print(myAtoi1("3.14159"))
# print(myAtoi1("     -42"))
# print(myAtoi1("-5-"))
# print(myAtoi1("-13+8"))
# print(myAtoi1("13-"))
# print(myAtoi1("words and 987"))
print(myAtoi1("+1"))