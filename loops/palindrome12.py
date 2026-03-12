num = int(input('Enter a number : '))
copy = num
rev = 0
while(num>0):
    rev = rev*10+num%10;
    num=num//10
if(copy==rev):
    print(f'{copy} is a Palindrome number')
else:
    print(f'{copy} is not a Palindrome number')