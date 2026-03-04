'''
2.Write a Program to find the Sum of N numbers of a given number
input:5		Ans: 1+2+3+4+5 =>15
input :4	Ans : 1+2+3+4=>10
'''
start = 1
end = 5
sum = 0;
while start<=end:          
    print(start,end=" ") 
    sum = sum+start  
    start = start+1 
print(f'sum of the above the numbers  : {sum} ')