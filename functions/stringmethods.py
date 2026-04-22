s = "abc"
print(s) # abc
x = s.upper()
print(x)
print(s) #ABC


print(s.__contains__("ab"))
print(s.__contains__("fd"))
print(s.index('a'))
print(s.index('c'))

print(s.__getitem__(0))
print(s.__getitem__(2))

dob = "19-Sept-2020"
l = dob.split("-")
print(l)
print(l[0])
print(l[1])
print(l[2])


import math

print(math.sqrt(36))
print(math.factorial(5))
print(math.cos(0))