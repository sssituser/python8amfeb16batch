'''
    Write a progrm to count the factors of a given number:
    num = 8             factors = 1,2,4,8
'''
num = int(input('Enter a number : '))
fcount = 0
start = 1
end = num
while start<=end:
    if num%start == 0:
        fcount= fcount+1
    start = start+1
print(f'{num} factors count is : {fcount}')