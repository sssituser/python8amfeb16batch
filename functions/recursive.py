'''
function is calling its own function is called recursive function.


Write a program to find the sum of n numbers
num = 5 sum = 1+2+3+4+5 => sum = 15


function:sumnnums
parameters : int
'''
def sumnnums(num): # num = 2
    if num==0:
        return 0
    return num+sumnnums(num-1)
num = 10
print(f' sum of {num} numbers is {sumnnums(num)}')




