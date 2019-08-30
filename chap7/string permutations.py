'''Given a smaller string s and a bigger string b, design an algorithm to find all permutations
of the shorter string within the longer one. Print the location of each permutation.'''
from itertools import permutations
class FindPermutations:
    def stringPermutations(self,string):
        perm_gen = permutations(string)
        result = []
        for perm in list(perm_gen):
            result.append((''.join(perm)))
        result = sorted(list(set(result)))
        print(result)
        return result

    def solution1(self,small,big):
        result = self.stringPermutations(small)
        for i in range(0,len(big)-4):
            curr = big[i:i+4]
            if(curr in result):
                print(curr,i)

    def solution2(self,small,big):
        result = self.stringPermutations(small)
        for i in range(0,len(big)-4):
            if(i in small):
                curr = big[i:i+4]
                if(curr in result):
                    print(curr,i)


if __name__ == "__main__":
    smallstr = "abbc"
    bigstr = "cbabadcbbabbcbabaabccbabc"
    FindPermutations().solution1(smallstr,bigstr)