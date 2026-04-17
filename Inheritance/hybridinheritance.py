'''
It is the combination of two inheritances.
example : combination of multi level and multiple inheritance
'''

class A:
    def readnums(self,a,b):
        self.a = a
        self.b = b
    def shownums(self):
        print(f'a= {self.a}\t b = {self.b}')    
class B(A):
    def sum(self):
        print(f'sum of a and b is :{self.a+self.b}')
    def sub(self):
        print(f'sub of and b is : {self.a-self.b}')
class C:
    def rem(self):
        print(f'rem  : {self.a%self.b}')
class D(B,C):# this statement is responsible for Hybrid inheritance
    def mul(self):
        print(f'mul of a and b is :{self.a*self.b}')
    def div(self):
        print(f'div of a and b is : {self.a//self.b}')
        
p = D()
p.readnums(5,2)
p.shownums()
p.sum()
p.sub()
p.mul()
p.div()
p.rem()