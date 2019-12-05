def add2BinaryStrings(a,b):
    if (len(a) > len(b)):
        for i in range(0, len(a) - len(b)):
            b = "0" + b
    elif (len(a) < len(b)):
        for i in range(0, len(b) - len(a)):
            a = "0" + a
    a_rev = a[::-1];
    b_rev = b[::-1]
    res = "";
    carry = "0"
    for i in range(0, len(a)):
        if (a_rev[i] == b_rev[i]):
            if (a_rev[i] == "1" and carry == "0"):
                res = res + "0"
                carry = "1"
            elif (a_rev[i] == "1" and carry == "1"):
                res = res + "1"
                carry = "1"
            else:
                if(carry == "0"):
                    res = res + "0"
                    carry = "0"
                else:
                    res = res + "1"
                    carry = "0"
        else:
            if(carry == "0"):
                res = res + "1"
                carry = "0"
            else:
                res = res + "0"
                carry = "1"
    if(carry == "1"):
        res = res + "1"
    print(res[::-1])
    #print(carry)

a="1010"
b="1011"
add2BinaryStrings(a,b)