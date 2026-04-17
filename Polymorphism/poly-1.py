class PolyEx:
    def area(self,l=0,b=0):
        if type(l)==float:
             return f"Area of cirlcle : {3.14*l*l} msq"
        elif l!=0 and b ==0:
            return f"Area of Square : {l*l} msq"
        elif l!=0 and b !=0:
            return f"Area of Rectangle is : {l*b} msq"
        
        
p1 = PolyEx()
print(p1.area(5))   
print(p1.area(5,6))       
print(p1.area(6.7))   