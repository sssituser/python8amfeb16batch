'''
function : defining a function with out class can be called function
method : Defining function in side the class can be methods
write a program to find the sum of two numbers.

1. function name sum
2. two integer

'''
# defining funtion is done
def sum(num1,num2):
     return num1+num2
    
def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2
    
def div(num1,num2):
    return num1/num2

def fdiv(num1,num2):
    return num1//num2
    
def exponen(num1,num2):
   return num1**num2
    
    
    
# calling the function or consuming the function

x = sum(4,3)
y = sum(5,4)
print(x,y)

p = sub(4,3)
q = sub(5,4)
print(p,q) 
r = mul(4,3)
s =mul(5,4)
print(r,s)

l = div(4,3)
m = div(5,4)
print(l,m)
    
    
    
i = fdiv(4,3)
j = fdiv(5,4)
print(i,j)

m = exponen(4,3)
n = exponen(5,3)
print(m,n) 
    