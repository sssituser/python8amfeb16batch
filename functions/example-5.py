'''
write a program to find the reverse of given number

num = 123 res = 321

function name : reverse
paramters: 1 integer
'''
def reverse(num):
    rev = 0
    while num>0:
        digit = num%10
        rev = rev*10+digit
        num = num//10
    return rev

x = reverse(123)
print(x)

print(reverse(345))
print(reverse('abc'))