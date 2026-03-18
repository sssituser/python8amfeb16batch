li = [ [12,34,67], [10,20,40], [11,22,33]]

print('============Matrix element are ==============')
for i in range(0,len(li)):
    for j in range(0,len(li[i])):
        print(li[i][j],end="\t")
    print()
print('============  Matrix Diagonal elements element are ==============')
for i in range(0,len(li)):
    for j in range(0,len(li[i])):
        if i==j or i+j == 2:
            print(li[i][j],end="\t")
        else:
            print(end="\t")
    print()
print('============  Matrix other than Diagonal elements element are ==============')
for i in range(0,len(li)):
    for j in range(0,len(li[i])):
        if i==j or i+j == 2:
            print(end="\t")
        else:
            print(li[i][j],end="\t")
    print()