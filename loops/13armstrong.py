'''
Write a program to check given number is Armstrong or not
153=> 1cube+5cube+3cube => 153
1634=> 1pow4+6pow4+3pow4+4pow4 1634

'''
num = int(input('Enter a number : ')) 
copy = num   
pow = 0   
sum = 0 
#Counting Digit   
while (num>0): 
    pow=pow+1  
    num=num//10 
num=copy 

#Sum of the Power values
while (num>0): 
    digit = num%10 
    sum = sum+digit**pow 
    num=num//10 
    
#compring original number with Sum
if (copy==sum):
    print(f'{copy} is an Armstrong Number ')
else:
    print(f'{copy} is not an Armstrong Number')