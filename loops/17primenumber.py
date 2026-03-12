'''
    Write a program to check given number is Prime or not.
'''
num = int(input('Enter  a number : ')) # num = 5
start = 1
end = num
count= 0
while start<=end:
    if num%start == 0:
        count = count+1 
    start=start+1
if count==2:
    print(f'{num} is a Prime number')
else:
     print(f'{num} is not a Prime number')
    
        
