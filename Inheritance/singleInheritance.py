class BasicCalcy:
    def readnums(self):
        self.a = int(input('Enter num1 : '))
        self.b =int(input('Enter num2  :'))
    def sum(self):
        print(f'sum is :{self.a+self.b}')
    def sub(self):
        print(f'sub is :{self.a-self.b}')
    def mul(self):
        print(f'mul is :{self.a*self.b}')
    def div(self):
        print(f'quo is :{self.a//self.b}') 
from math import  *
class ScientificCalcy(BasicCalcy):
    def sine(self):
        value = int(input('Enter Sine Values : '))
        print(f'sine{value} is {sin(value)}')
    def cosi(self):
        self.value = int(input('Enter Cosi Values : '))
        print(f'sine{self.value} is {cos(self.value)}') 
s = ScientificCalcy()
s.readnums()
s.sum()
s.sub()
s.mul()
s.div()
s.sine()
s.cosi()