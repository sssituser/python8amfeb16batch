'''
Write program to display  1.Display Duplicate Numbers in the  list
2.Display the Unique Numbers in the list
'''
li =[12,34,56,78,12,45,56,34,78,90,43,54,32]
di={}
for element in li:
    if di.__contains__(element):
        value = di.get(element)
        di[element]=value+1
    else:
        di[element]=1
dup=[];un =[]
print(di)  #{12: 2, 34: 2, 56: 2, 78: 2, 45: 1, 90: 1, 43: 1, 54: 1, 32: 1}
# current logic is the separation duplicates and uniques
for i in di.keys():#[12,34,56,78,45,90,43,54,32]
    if di.get(i)>=2:
        dup.append(i)
    else:
        un.append(i)
print(f"Duplicates {dup}\tunique elements  {un}")
