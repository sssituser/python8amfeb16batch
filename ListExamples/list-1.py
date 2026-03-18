li =[1,2,3,3,
     'abc','abc','def',
     8.9,7.8,7.8,
     True,False,
     8+5j,9+10j,
     [8,9],
     (7,8),
     {3,4,5},
     {"id":111,"name":'Arun'}]
print(li)
print(dir([])) 
li.append(1000)   #append can add the element directly and stores defalut end location
li.insert(0,8000) # insert can  the element at given index we need to pass two parameters , fisrt paramter is index,second parameter is Value.
print(li)
li.pop()
print(li)