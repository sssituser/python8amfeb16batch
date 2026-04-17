class Demo:
    def readnums(self):
        self.a = int(input('Enter a number : '))
        self.b = int(input('Enter b number : '))
    def shownums(self):
        print(f'a = {self.a}')
        print(f'b = {self.b}')
    def __add__(self,object):
        result = Demo()
        result.a = self.a + object.a
        result.b = self.b + object.b
        return result
  
print("===============Object - 1 =======================")
ob1 = Demo()
ob1.readnums()
ob1.shownums()

print("===============Object - 2 =======================")
ob2 = Demo()
ob2.readnums()
ob2.shownums()
print("===============Object -1  3 =======================")
ob3 = Demo()
ob3 = ob1 + ob2
ob3.shownums()