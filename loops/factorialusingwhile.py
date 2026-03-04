'''
2.Write a Program to find the Mul of N numbers of a given numbers(Factorial)
input:5		Ans: 1*2*3*4*5 =>120
input :4	Ans : 1*2*3*4=>24
'''
start  = 1
end = 5
fact = 1
while start<=end: # 1<=5-T
    print(start,end=" ")#1
    fact = fact*start #1*1 1*2
    start = start + 1
print(f'factorial of the above numbers : {fact}')
    
    