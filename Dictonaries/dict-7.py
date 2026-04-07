'''
Write program to find the frequncy of the given name 
name = "arunkumar"         a-2  r-2 u - 2 n - 1 k - 1 m - 1
'''
name = input("Enter Name : ")# name = "arunkumar"
di ={}
for element in name: ##"abaac"
    if di.__contains__(element):
        value = di.get(element)
        di[element]=value+1
    else:
        di[element]=1     # di = {a:3,b:1,c:1}
print(di)    




