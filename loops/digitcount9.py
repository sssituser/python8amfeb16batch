#Write program to find the no of digits present in the given number.
num = int(input('Enter a number :')) # 6789
copy = num
count = 0
while (num>0): 
    count += 1 
    num//=10  
print(f"No of Digits present in the given number {copy} is  : {count}")