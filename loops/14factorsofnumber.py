num = int(input('Enter a number : ')) # 6
start = 1    # start = 1
end = num    # end = 6
       #1<=6-T  2<=6-T 3<=6-T 4<=6-T 5<=6-T 6<=6
while (start <= end):
    if(num%start==0): ## 6%1->0  6%2->0 6%3->0 6%4 => 2  6%5->1 6%6->0
        print(start) # 1 , 2,3,6
    start = start+1 # 2,3,4,5,6
    

