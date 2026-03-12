'''
    Write a program to check given number is perfect number
    num = 6     factors = 1,2,3  1+2+3=>6
'''
num = int(input('Enter a number : '))
start = 1
end = num
sum = 0
while start<end:
    if num%start == 0:
        sum = sum + start
    start = start+1
if num==sum:
    print(f'{num} is a Perfect number')
else:
     print(f'{num} is not a Perfect number')

