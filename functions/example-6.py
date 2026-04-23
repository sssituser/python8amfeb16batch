
def reverse(num):
    if isinstance(num,int):
        num=str(num)
        return int(num[::-1])
    return num[::-1]

print(reverse(123))
print(reverse('abc'))