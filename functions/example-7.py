'''
Write a program to check given number  / string is a palindrome or not
num = 123  123 is not a Palindnrome 
num = 121  121 is a  Palindrome 
num = 'eye' 'eye' is a Palindrome 

function name : ispalindrome
Parameters : str/int
'''
# def reverse(value): # 123,'eye'
#     if isinstance(value,int):
#         value = str(value)
#         return int(value[::-1])
#     return value[::-1]

def reverse(value):
    if isinstance(value,int):
        rev = 0
        while value>0:
            rev = rev*10+value%10
            value//=10
        return rev
    return value[::-1]
        
def ispalindrome(value):
    return value == reverse(value)

num = 123
x = ispalindrome(num)

print(num,x)

num = 121
print(num,ispalindrome(num))

num = 'leg'
x = ispalindrome(num)

print(num,x)

num = 'eye'
print(num,ispalindrome(num))