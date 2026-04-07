s ={45,67,56}
print(s)
s.add(True)
print(s) # {True,45,67,56}
li = [4,2,7]
s.update(li)
print(s)

s.remove(True)
print(s)
s.discard(2)
s.discard(67)
#s.remove(100) This will raise key error
print(s)
s.clear()
print(s)