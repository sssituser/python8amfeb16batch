num = int(input('Enter number : '))
start = 1
sum = 0
while start<=num :
    print(start)
    sum += start
    start+=1
avg = sum//num
print(f'sum :{sum}  and its average :{avg}')
    
    