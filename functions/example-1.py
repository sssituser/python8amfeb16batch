'''
function : defining a function with out class can be called function
method : Defining function in side the class can be methods
write a program to find the sum of two numbers.

1. function name sum
2. two integer

'''
# defining funtion is done
def sum(num1,num2):
    print(f'sum of two numbers : {num1+num2}')
    
def sub(num1,num2):
    print(f'sub of two numbers : {num1-num2}')

def mul(num1,num2):
    print(f'mul of two numbers : {num1*num2}')
    
def div(num1,num2):
    print(f'quo of two numbers : {num1/num2}')

def fdiv(num1,num2):
    print(f'Quo of two numbers : {num1//num2}')
    
def exponen(num1,num2):
    print(f'{num1} to the power of {num2} : {num1**num2}')
    
    
    
# calling the function or consuming the function

sum(4,3)
sum(5,4)


sub(4,3)
sub(5,4)
    
mul(4,3)
mul(5,4)


div(4,3)
div(5,4)
    
    
    
fdiv(4,3)
fdiv(5,4)


exponen(4,3)
exponen(5,3)
    
    