# class Foo(object):
#     def __init__(self,l,b):
#         self.a = l
#         self.b1 = b
#
#     def area(self):
#         return self.a*self.b1
#
#     def __str__(self):
#         print("rect",self.a,self.b1)
#
# temp = Foo(4,5)
# print(temp)

def writer():
    title = "HackerEarth"
    name = (lambda x:title+" "+x)

    return name

who = writer()
print(who("Fremont"))