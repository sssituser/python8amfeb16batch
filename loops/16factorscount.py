num = int(input('Enter a number : ')); # 6
fcount = 0;
start = 1;
end = num;
fsum = 0;
while(start<end):
    if(num%start==0):
        fcount = fcount+1;
        fsum = fsum+start;
        print(start,end=",");
    start = start+1;
if(fsum==num):
    print(f'\n{num} has {fcount} factors and their sum is :{fsum} and is a Perfect number');
else:
    print(f'\n{num} has {fcount} factors and their sum is :{fsum} and is not a Perfect number');
    
    
