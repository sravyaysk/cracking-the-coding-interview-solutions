'''write a function to add two simple mathematical expressions which are of the form Ax^a + Bx^b + . . . (where the coefficients
and exponents can be any positive or negative or real number).'''
class Add_two_exp_exprsns:
    def method1(self,expr1,expr2,x):
        new_expr1 = sorted(expr1) #replace sorted() with merge sort
        new_expr2 = sorted(expr2)
        exp_coef = {}
        for exp1 in new_expr1:
            if(exp1 in new_expr2):
                exp_coef[exp1]=2*exp1
                new_expr2.pop(new_expr2.index(exp1))    #replace index with binary search
            else:
                exp_coef[exp1]=exp1
        if(len(new_expr2)>0):
            for exp2 in new_expr2:
                exp_coef[exp2]=exp2

        #print(exp_coef)
        sum = 0
        for exp,coeff in exp_coef.items():
            #print(exp,coeff)
            sum = sum + (pow(x,exp)*coeff)
        print(sum)

if __name__ == "__main__":
    coeff_expr1 = [1,2,0.5,4]
    coeff_expr2 = [-1,6,1,8]
    x = 10
    Add_two_exp_exprsns().method1(coeff_expr1, coeff_expr2,x)