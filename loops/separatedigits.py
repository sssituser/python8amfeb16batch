'''
4.Write a program to separate the digits of given number
	num = 123	output : 3 2  1
	num = 456	output : 6 5 4
'''

num = 123
while num>0: # 123>0-T 12>0-T 1>0-T 0>0-F
    digit = num%10 # digit = 123%10 digit = 3 digit = 12%10 digit = 2 digit = 1%10 digit = 1
    print(digit) # 3  2  1
    num = num//10 # num = 123//10 num = 12//10 num = 1//10 num = 0
    
   