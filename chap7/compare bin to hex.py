'''write a function to check if the value of a binary number (passed as a string) equals the hexadecimal representation of a string.'''
class BintoHex():
    def convertBinToHex(self,binary,hexa):
        num1 = self.convertToDecimal(binary,2)
        print(num1)
        num2 = self.convertToDecimal(hexa,16)
        print(num2)
        if(num1 == num2):
            print("matched")
        elif((num1 == -1) or (num2 == -1)):
            print("Invalid format")
        else:
            print("Not matched")

    def convertToDecimal(self,representation,base):
        if(base < 2 or (base>10 and base != 16)):
            return -1
        strlen = len(representation)-1
        hexdecmap = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        sum = 0
        for char in representation:
            try:
                if (int(char) < base and int(char) >= 0):
                    sum += int(char)*pow(base,strlen)
                else:
                    return -1
            except:
                if(char.upper() in hexdecmap.keys()):
                    sum += hexdecmap[char]*pow(base,strlen)
                else:
                    print("invalid hexadecimal number")
                    return -1
            strlen -= 1

        return(sum)


if __name__ == '__main__':
    bin_num = '1010'
    hex_num = 'A'
    BintoHex().convertBinToHex(bin_num,hex_num)