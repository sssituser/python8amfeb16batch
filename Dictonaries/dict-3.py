d = {10:"raj",11:"kiran",12:"pavan",14:"venki",13:"Arun",9:"vijay"}
print(d)
print(d.get(9))
d.pop(10) # this will delete by providing key
print(d)
d.setdefault(15,"Ram")
print(d)
print("deleted element is : ",d.popitem())
print("Dictonary : ",d)
d1 = {45:"aaa",55:"pppp"}
d.update(d1) # update funtion can update the d (dictonary)
print(d)