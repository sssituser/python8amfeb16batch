'''
Write a program to find the revere of given number ?
	num = 123	reverse=321
	num = 567	reverse=765
	num = 439	reverse =934
'''

num =int(input('Enter a number '))
rev = 0
while (num>0): #123>0-T 12>0-T 1>0-T 0>0-F
    digit =  num%10 # digit = 3 digit = 2 digit = 1
    rev = rev*10+digit # rev = 3 rev = 32 rev = 321
    num=num//10 # num = 12 num = 1 num = 0
print(f'Reverse Number is :{rev}')
    