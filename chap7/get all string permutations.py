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
        print("input arr: ",str)
        print("level :", k)
        str_gen = []
        for i in range(k,len(str)):
            temp_str = str
            result = self.swap(temp_str,i,0)
            str_gen.append(result)
        print("permutations: ",str_gen)
        return str_gen

    def stringPermutations(self,generator,l):
        #num_perm = self.factorial(l)
        #print("No of permutations possible assuming all chars are unique are ",num_perm)
        for i in generator:
            result = self.swap_chars_str(i,l-l)
        self.stringPermutations(result,l-1)

if __name__ == "__main__":
    str = ['abcd']
    l = len(str[0])
    Permutations().stringPermutations(str,l)
