'''
Write a program to check given number is Armstrong or not
153 = 1cube+5cube+3cube
function:isarmonstrong
parameter:int
'''
def getcount(num):
    count = 0
    while num>0:
        count = count+1
        num//=10
    return count
def isarmstrong(num):
    power = getcount(num)
    copy = num
    sum = 0
    while num>0:
        digit = num%10
        sum = sum+digit**power
        num//=10
    return copy==sum
   
print(isarmstrong(153))
print(isarmstrong(123))