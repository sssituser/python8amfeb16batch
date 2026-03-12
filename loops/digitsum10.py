# Write a program to find the digits sum of  a given number 
# num = 123  sum = 6(1+2+3)

num = int(input('Enter a number : '))
copy = num
sum = 0
while (num>0):
    digit = num%10;
    sum += digit;
    num //=10
print(f'sum of the digits of {copy} is {sum}')