'''
        indexing
        In order get the elements from the list we usig indexing
'''
li = [495,666,"abbb",7.8,True]
print(li[0],li[1],li[2],li[3],li[4])
print(li[-5],li[-4],li[-3],li[-2],li[-1])
# displaying the element using for loop
print('Displaying the element using for loop')
for element in li:
    print(element,end="\t")
print("\nDisplaying the elements of list using for loop +ve index")

for i in range(0,len(li)):
    print(f'index : {i}---->{li[i]}')
print("\nDisplaying the elemetns of list using for loop -ve index")

for i in range(-5,0,1):
    print(f'index {i}----->{li[i]}')