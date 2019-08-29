'''Design an algorithm to print all permutations of a string. For simplicity, assume all characters are unique.'''
class Permutations:
    def factorial(self,n):
        if(n == 1):
            return n
        else:
            return n*(self.factorial(n-1))

    def swap(self,c, i, j):
        c = list(c)
        c[i], c[j] = c[j], c[i]
        return ''.join(c)

    def swap_chars_str(self,str,k):
        #print("input arr: ",str)
        #print("level :", k)
        str_gen = []
        for i in range(k,len(str)):
            temp_str = str
            result = self.swap(temp_str,i,k)
            str_gen.append(result)
        #print("permutations: ",str_gen)
        return str_gen

    def computeFactorial(self,num):
        res = [1]
        while(num > 1):
            res.append(num*res[-1])
            num -= 1
        #print(res)
        new_res = []
        for i in range(0,len(res)):
            new_res.append(sum(res[:i+1]))
        #print(new_res)
        return new_res

    def stringPermutations(self,str,l,k):
        facts = self.computeFactorial(l)
        count = 0
        for ind in str:
            if(count in facts):
                k = k+1
                if(k==facts[-1]):
                    break
            res = self.swap_chars_str(ind,l-(l-k))
            for i in res:
                str.append(i)
            count += 1
        strlist = sorted(list(set(str)))
        print("String Permutations are: ",(",".join(s for s in strlist)))
        print("No of permutations are :",len(strlist))


if __name__ == "__main__":
    str = 'abcd'
    Permutations().stringPermutations([str],len(str),0)
