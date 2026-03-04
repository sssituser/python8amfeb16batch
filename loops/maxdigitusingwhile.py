'''
4.Write a program to find the  max digit of given number
	num = 321	output : 3 
	num = 456	output : 6 
    num = 897   output : 9
    num = 342   output : 4
'''
num = 897
max = num%10  # max = 1
while num>0: #321>0 32>0-T 3>0-T 0>0-F
    digit = num%10 # digit = 1 digit = 2 digit = 3
    if max<digit:  # 1<1-F 1<2-T 2<3-T
        max = digit  # max = 2 max = 3
    num = num//10 # num = 321//10 num = 32//10 num = 3//10 num = 0
print('max digit is ',max)

