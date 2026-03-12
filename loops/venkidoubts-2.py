'''
Write program to check given numbers is prime or not
'''
num = int(input('Enter a number : '))
fcount = 0
start = 1
end = num
while start<=end:
    if num%start == 0:
        fcount= fcount+1
    start = start+1
if fcount==2:
    print(f'{num} is prime')
else:
    print(f'{num} is not a Prime')
