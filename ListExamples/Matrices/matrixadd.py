a =[[10,20],[30,40]]
b =[[11,22],[33,44]]
print('===A matrix elements=========')
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        print(a[i][j],end="\t")
    print("\n")
print('===B matrix elements=========')
for i in range(0,len(b)):
    for j in range(0,len(b[i])):
        print(b[i][j],end="\t")
    print("\n")
    
print('===Sum of A and B matrix elements=========')
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        print(a[i][j]+b[i][j],end="\t")
    print("\n")
    
print('===Sub of A and B matrix elements=========')
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        print(a[i][j]-b[i][j],end="\t")
    print("\n")