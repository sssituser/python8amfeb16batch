'''
        num = 123   
        1.Count digits : 3
        2.Sum of the digit : 6
        3.Average : sum/count
        4.Separating the digit
        5.reverse
        6.Palindrome
'''
num = int(input('Enter a number : '))
count = 0
sum = 0
avg = 0
rev = 0
copy = num
while(num>0):
    digit = num%10;
    print(digit,end=",");
    count=count+1;
    sum = sum+digit;
    rev = rev*10+digit;
    num=num//10
    
num = copy;
amssum = 0;
while(num>0):
    digit = num%10
    amssum = amssum+(digit**count)
    num//=10
    
avg = sum//count
if(copy==rev ):
    print(f'\n{copy} digit count : {count}\nSum : {sum}\nAverage : {avg}\nReverse : {rev} and is Palindrome ')
else:
    print(f'\n{copy} digit count : {count}\nSum : {sum}\nAverage : {avg}\nReverse : {rev}\n{copy}  is not a Palindrome ')
if(copy==amssum):
    print(f'{copy}  is an Armstrong number');
else:
    print(f'{copy}  is not an Armstrong number');
